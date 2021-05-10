# 新报名系统

tags: act_seckill

## mms login并创建商品
* MMS商家登录,通过用户名="18017752229",密码="19660302,.cj"
* 创建待审核商品,商品价钱="10",mall_id="",goods_name=""
* 校验并更新商家资质参加活动


## oms login并审核商品
* OMS小二后台登录,通过手机号="wuyiqiang"和密码="1qaz2wsx!!"
* OMS审核商品


## act login并创建秒杀报名
* Act平台登录,注入token到ActApiHeaders
* ACT新报名系统创建秒杀报名,商品id=""


## oms_new login并创建秒杀活动
* 新OMS小二后台登录,通过用户名="wenjie"和密码="a1a1a1"
* 新OMS平台创建秒杀活动,参数:新报名系统秒杀报名id="",秒杀活动id="",档期id=""


## app login
* 萌推APP登录,通过手机号="15021721258"和验证码


## 获取活动的商品库存信息
* 获取秒杀活动详情,activity_id=""
* 直购下单,参数:商品id="",类目id="",支付方式="",店铺优惠券id="",平台优惠券id="",推币使用="",礼品卡使用=""
* 获取秒杀活动详情,activity_id=""