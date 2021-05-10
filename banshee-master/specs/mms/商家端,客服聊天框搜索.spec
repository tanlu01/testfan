# 商家端搜索，客服聊天框搜索页，对搜索结果进行筛选

tags: seller_search, p0

## mms login并获取店铺基本信息

* MMS商家登录,通过用户名="17621250031",密码="123456"

## 进入客服聊天页面，在“商品推荐”页面的搜索框中进行搜索，并对结果进行判断(测试环境此条case不通)

* 搜索结果页接口, search_keyword="衬衫",sort="_default",min_price="",max_price="",expand_filters="{mall_id:100003}",cat=""
* 判断搜索结果页的数据与搜索词"衬衫"一致,flag="1"
* 判断搜索结果页的商品只是本店"100003"的商品


