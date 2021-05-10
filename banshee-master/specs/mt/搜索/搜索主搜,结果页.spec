# 搜索主搜，输入关键字“手机”，进入搜索结果页，对搜结果进行排序和筛选

tags: search_result_page,p0

* 萌推APP登录,通过手机号="15021721257"和验证码

## 进入搜索中间页，输入"手机"，进入搜索结果页

tags: page_result

* 搜索结果页接口, search_keyword="手机",sort="_default",min_price="",max_price="",expand_filters="",cat=""
* 判断搜索结果页的数据与搜索词"手机"一致,flag="1"

## 点击销量排序再切回综合排序，判断根据排序方式搜索结果不同

tags: sort_p0

* 搜索结果页接口, search_keyword="手机",sort="_sales",min_price="",max_price="",expand_filters="",cat=""
* 搜索结果页接口, search_keyword="手机",sort="_default",min_price="",max_price="",expand_filters="",cat=""
* 判断根据排序方式搜索结果不同

## 点击销量，查询结果在同一个类目中，按照销量排序（测试环境此功能有问题，所以这条case通不过）

tags: sort_sales

* 搜索结果页接口, search_keyword="手机",sort="_sales",min_price="",max_price="",expand_filters="",cat=""
* 判断查询结果在同一个类目中
* 判断按照销量进行排序

## 点击价格升降序，查询结果按照升、降序排列（price升序_price降序,测试环境不执行此case）

tags: sort_price

* 搜索结果页接口, search_keyword="手机",sort="price",min_price="",max_price="",expand_filters="",cat=""
* 判断搜索结果按照价格顺序排列,sort="price"
* 搜索结果页接口, search_keyword="手机",sort="_price",min_price="",max_price="",expand_filters="",cat=""
* 判断搜索结果按照价格顺序排列,sort="_price"

## 点击“价格”，修改价格区间，搜索结果中商品为价格区间的商品(测试环境不执行此case)

tags: update_price

* 搜索结果页接口, search_keyword="手机",sort="_default",min_price="10",max_price="200",expand_filters="",cat=""
* 判断商品的价格在价格区间内

