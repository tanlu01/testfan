# 搜索主搜，筛选器+销量/价格/综合，组合筛选

tags: combination_search,p0

* 萌推APP登录,通过手机号="15021721257"和验证码

## 组合筛选：综合+筛选器（服务，类别）

tags: filter-1

* 搜索结果页接口, search_keyword="手机",sort="_default",min_price="",max_price="",expand_filters="{service_id:2}",cat="20041"
* 判断搜索结果按照排序为"_default",服务为萌推好店，类别为付费会员的结果

## 组合筛选：价格降序+筛选器（服务，类别）

tags: filter-2

* 搜索结果页接口, search_keyword="手机",sort="_price",min_price="",max_price="",expand_filters="{service_id:2}",cat="20041"
* 判断搜索结果按照排序为"_price",服务为萌推好店，类别为付费会员的结果

## 组合筛选：销量升序+筛选器（服务，类别）

tags: filter-3

* 搜索结果页接口, search_keyword="手机",sort="_sales",min_price="",max_price="",expand_filters="{service_id:2}",cat="20041"
* 判断搜索结果按照排序为"_sales",服务为萌推好店，类别为付费会员的结果