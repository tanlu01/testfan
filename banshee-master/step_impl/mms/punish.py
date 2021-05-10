import urllib

from api.mms.punish.punishment import Punishment
from api.oms.punish.add_punish import Add_punish
from getgauge.python import step, data_store
import time
from api.oms.punish.handlepunishment import Handlepunishmenth
from api.oms.punish.mall_punishment import Mall_punishment
from api.oms.punish.mallpunishmentrecord import Mallpunishmentrecord
from api.oms.punish.mallpunishmentrule import Mallpunishmentrule
from api.oms.punish.punish_add_delay import Punishment_add_delay
from api.oms.punish.punish_confirm import Punishment_confirm
from api.oms.punish.punishment_appeal import Punish_appeal
from api.oms.punish.punishmentrule_search import  Punishmentrule_search


@step("新建店铺违规配置<config><detail>扣分<score>罚款<money>限制<days>天,违规类型<title>,违规详情<punish_detail>")
def add_punish_config(config,detail,score,money,days,title,punish_detail):
    mallpunishmentrule=Mallpunishmentrule()
    if config=="可申诉":
        mallpunishmentrule.data["type"]=0
        mallpunishmentrule.data["appeal_status"]=1
    if config=="不可申诉":
        mallpunishmentrule.data["type"] = 1
        mallpunishmentrule.data["appeal_status"] = 0
    mallpunishmentrule.data["title"] = title
    mallpunishmentrule.data["detail"] = punish_detail
    mallpunishmentrule.data["rule"]='{"related_order":1,"related_goods":1,"score":{"number":'+str(score)+',"max":"100","is_show":1},"money":{"number":'+str(money)+',"is_show":1},"limit":{"scene_type":0,"days":'+str(days)+',"is_show":1}}'
    mallpunishmentrule.data["status"]=1
    resp=mallpunishmentrule.request()
    data_store.suite["punish_score"] = score
    data_store.suite["punish_money"] = money
    data_store.suite["title"] = title
    data_store.suite["punish_days"] = days
    data_store.suite["punish_details"] = punish_detail
    assert resp["code"] == mallpunishmentrule.success_resp['code']
    punishmentrule_search = Punishmentrule_search()
    resp = punishmentrule_search.request()
    data_store.suite["punishmentrule_id"] = resp["payload"]["data"][0]["id"]


@step("新建店铺违规")
def add_punish():
    add_punish=Add_punish()
    add_punish.data['mall_id']=100241
    add_punish.data['rule_id'] = data_store.suite["punishmentrule_id"]
    add_punish.data['score']=data_store.suite["punish_score"]
    add_punish.data['detail'] = data_store.suite["punish_details"]
    add_punish.data['money'] = data_store.suite["punish_money"]
    punish_creat_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    add_punish.data['open_time']= punish_creat_time
    add_punish.data['update_at'] = punish_creat_time
    add_punish.data['limit_days']= data_store.suite["punish_days"]
    add_punish.data['related_order']= "1688340242146312246"
    add_punish.data['related_sku'] = "109531"
    resp=add_punish.request()
    assert resp["code"]==add_punish.success_resp['code']
    mallpunishmentrecord = Mallpunishmentrecord()
    today = time.strftime("%Y-%m-%d", time.localtime())
    time_c = "%5B%22" + str(today) + "T07%3A03%3A14.295Z%22%2C%22" + str(today) + "T07%3A03%3A14.295Z%22%5D"
    mallpunishmentrecord.api = mallpunishmentrecord.api.replace("$create_at", time_c)
    resp = mallpunishmentrecord.request()
    assert resp["code"] == mallpunishmentrecord.success_resp['code']
    data_store.suite["punish_id"]=resp['payload']["data"][0]['id']


@step("小二处理<detail>")
def operation_punish(detail):
    handlepunishmenth=Handlepunishmenth()
    handlepunishmenth.data['record_id']=data_store.suite["punish_id"]
    if detail=="违规记录":
        handlepunishmenth.data['status']="待确认"
    if detail == "申诉":
        handlepunishmenth.data['status']="申诉中"
        handlepunishmenth.data['info'] = "同意"
    resp=handlepunishmenth.request()
    assert resp["code"] == handlepunishmenth.success_resp['code']


@step("商家端显示此条违规订单,value=<value>")
def punish_order(value):
    punishment=Punishment()
    punishment.api = punishment.api.replace("$type", value)
    resp=punishment.request()
    if value==0:
        assert resp["payload"]['list'][0]["id"]==data_store.suite["punish_id"]
    if value ==3:
        assert resp["payload"]['list'][0]["id"] == data_store.suite["delay_punish_id"]

@step("商家对违规订单进行申诉")
def oder_appeal():
    punish_appeal=Punish_appeal()
    punish_appeal.data["appeal_reason"]="hh"
    punish_id=data_store.suite["punish_id"]
    punish_appeal.data['id']=int(punish_id)
    resp=punish_appeal.request()
    assert resp["code"] == punish_appeal.success_resp['code']

@step("小二添加延迟发货数据")
def punish_delay():
    punishment_delay=Punishment_add_delay()
    punishment_delay.data['buyer_id']=36051410
    punishment_delay.data['goods_id'] = data_store.suite['goods_id_punish']
    punishment_delay.data['mall_id'] = 100241 #111家居生活官方旗舰店
    punishment_delay.data['number']="100"
    punishment_delay.data['order_id'] = data_store.suite['order_id']
    resp=punishment_delay.request()
    assert resp["code"] == punishment_delay.success_resp['code']

@step("小二确认扣款")
def punishment_confirm():
    mall_punishment=Mall_punishment()
    resp=mall_punishment.request()
    assert resp["code"] == mall_punishment.success_resp['code']
    confirm_data=resp["payload"]["list"][0]
    data_store.suite['delay_punish_id']=confirm_data["id"]
    punishment_confirm=Punishment_confirm()
    punishment_confirm.data["selected"][0]=confirm_data
    resp=punishment_confirm.request()
    if resp["code"]==0:
        assert resp["code"] == punishment_confirm.success_resp['code0']
    if resp["code"]==1:
        assert resp["code"] == punishment_confirm.success_resp['code1']
