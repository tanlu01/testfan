# 物流违规管理,违规数据申诉
tags:punish_joan,p0

* OMS小二后台登录,通过手机号="wenjie"和密码="a1a1a1"
* MMS商家登录,通过用户名="18017752229",密码="19660302,.cj"
* 新OMS小二后台登录,通过用户名="wenjie"和密码="a1a1a1"


## 物流违规-延迟发货不可申诉
tags:punish_delay

* 萌推APP登录,通过手机号="15021721258"和验证码
* 创建待审核商品,商品价钱="10",mall_id="",goods_name=""
* OMS审核商品
* 直购下单,参数:商品id="",类目id="",支付方式="",店铺优惠券id="IGNORE",平台优惠券id="IGNORE",推币使用="IGNORE",礼品卡使用="IGNORE"
* 生成预支付订单并mock支付,order_id="",payment_method="",platform=""
* MMS订单发货,goods_id="",order_id=""
* 小二添加延迟发货数据
* 小二确认扣款
* 商家端显示此条违规订单,value="3"