from datetime import datetime
import datetime
import time
from getgauge.python import step, data_store
from api.comment.comment import Mms_comment
from api.comment.comment_audit import Comment_audit
from api.comment.review_add import Review_add
from api.comment.review_report import Review_report


@step("获得评价内容并做校验")
def getComment():
    time.sleep(10)
    mms_comment=Mms_comment()
    mms_comment.data["order_id"]=data_store.suite['order_id']
    mms_comment.data["from_review_time"] = str(datetime.date.today())+" 00:00:00"
    mms_comment.data["to_review_time"] = str(datetime.date.today())+" 24:00:00"
    resp=mms_comment.request()
    resp_data = resp["payload"]["list"][0]
    data_store.suite['review_id']=resp_data["id"]
    assert resp["code"] == mms_comment.success_resp["code"]
    #assert resp_data["buyer_name"] == mms_comment.message["buyer_name"]
    assert resp_data["review_text"] == mms_comment.message["review_text"]
    assert resp_data["description_rating"] == mms_comment.message["description_rating"]
    #assert review_time == str(time.strptime(review_time, "%Y-%m-%d %H:%M:%S"))
    #assert resp_data["response"]["response_text"] == mms_comment.message["response_text"]


@step("回复操作校验")
def reply():
    review_add=Review_add()
    review_add.data["review_id"]=data_store.suite['review_id']
    review_add.data["merchant_views"]="谢谢买家"
    resp=review_add.request()
    assert resp["code"]==review_add.success_resp["code"]


@step("举报操作校验")
def report():
    review_report=Review_report()
    review_report.data["id"]=data_store.suite['review_id']
    review_report.data["reason_id"] = 1
    resp=review_report.request()
    assert resp["code"]==review_report.success_resp["code"]


@step("萌推小二后台审核举报成功")
def examine():
    comment_audit=Comment_audit()
    comment_audit.data['id']=data_store.suite['review_id']
    comment_audit.data['audit_status']=2
    comment_audit.data['reason_id']=1
    resp=comment_audit.request()
    assert resp["code"]==comment_audit.success_resp["code"]


