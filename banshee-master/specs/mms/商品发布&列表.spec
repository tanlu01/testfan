# 前置条件：商家登陆发布商品，小二审核商品，app端购买商品，最后商家校验商品

tags: mms_check,p0


## mms login并获取店铺基本信息
* MMS商家登录,通过用户名="18017752229",密码="19660302,.cj"

## 获取店铺上架/下架状态的商品数量,商品状态:['上架':2, '下架':4]
* 获取上架状态商品数量
* 获取下架状态商品数量

## 创建待审核商品
* 创建待审核商品,商品价钱="10",mall_id="",goods_name=""

## oms login
* OMS小二后台登录,通过手机号="wuyiqiang"和密码="1qaz2wsx!!"

## oms审核商品
* OMS审核商品


##再次获取店铺已上架状态的商品数量
* 获取上架状态商品数量
* 查询商品,goods_id="",goods_status="2"


## app login
* 萌推APP登录,通过手机号="15021721258"和验证码

## 直购下单
* 直购下单,参数:商品id="",类目id="",支付方式="",店铺优惠券id="",平台优惠券id="",推币使用="",礼品卡使用=""

## mock支付订单
* 生成预支付订单并mock支付,order_id="",payment_method="",platform=""


##第三次获取店铺已上架状态的商品数量
* 查询商品,goods_id="",goods_status="2"
