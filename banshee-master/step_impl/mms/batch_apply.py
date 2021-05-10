from getgauge.python import step, data_store
from api.mms.activity.batch_apply import Batch_apply 
{"request_type":2,"schedule_id":1150,"goods":[{"goods_id":37647160}]}
@step("提报商品,request_type=<request_type>,schedule_id=<schedule_id>,goods=<goods>")
def batch_apply(request_type,schedule_id,goods):
    batch_apply = Batch_apply() 
    
    batch_apply.data['request_type'] = request_type
    batch_apply.data['schedule_id'] = schedule_id

    goods_list = [{"goods_id":int(goods)} for goods in goods.split(',')]
    # goods_list = goods.split(',')
    # for goods in goods_list:
    #     batch_apply.data['goods'].append({"goods_id":int(goods)})
    batch_apply.data['goods'].extend(goods_list)

    resp = batch_apply.request()
    #print(resp)
    #assert resp['code'] == 0

