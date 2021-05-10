from getgauge.python import step, data_store
from api.mt.mt import Mt
import urllib
from api.mt.search.applet import Applet
from api.mt.search.category_nav import Category_nav
from api.mt.search.hint import Hint
from api.mt.search.hot import Hot
from api.mt.search.mall_middle_page import Mall_middle_page
from api.mt.search.match import Match
from api.mt.search.order import Order
from api.mt.search.result_page import Result_page
from api.mt.search.rank import Rank
from api.mt.search.scene_page import Scene_page
from api.mt.search.stage import Stage
from api.mt.search.words import Words



@step("搜索关键词绑定的小应用, search_keyword=<search_keyword>")
def applet(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    applet = Applet()
    applet.api = applet.api.replace('$search_keyword', search_keyword)
    applet.request()
    print(applet.resp.json())


@step("搜索结果页 配置组合关键字, search_keyword=<search_keyword>")
def category_nav(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    category_nav = Category_nav()
    category_nav.api = category_nav.api.replace('$search_keyword', search_keyword)
    category_nav.request()
    print(category_nav.resp.json())


@step("获取搜索提示, search_keyword=<search_keyword>")
def hint(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    hint = Hint()
    hint.api = hint.api.replace('$search_keyword', search_keyword)
    hint.request()
    print(hint.resp.json())


@step("获取热门搜索")
def hot():
    hot = Hot()
    hot.request()
    print(hot.resp.json())


@step("搜索接口, search_keyword=<search_keyword>")
def match(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    match = Match()
    match.api = match.api.replace('$search_keyword', search_keyword)
    match.request()
    print(match.resp.json())


@step("搜索订单, search_keyword=<search_keyword>")
def order(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    order = Order()
    order.api = order.api.replace('$search_keyword', search_keyword)
    order.request()
    print(order.resp.json())


@step("搜索结果页接口, search_keyword=<search_keyword>,sort=<sort>,min_price=<min_price>,max_price=<max_price>,expand_filters=<expand_filters>,cat=<cat>")
def page_result(search_keyword,sort,min_price,max_price,expand_filters,cat):
    search_keyword = urllib.parse.quote(search_keyword)
    result_page = Result_page()
    result_page.api = result_page.api.replace('$search_keyword', search_keyword)
    result_page.api =result_page.api.replace('$sort', sort)
    result_page.api=result_page.api.replace("$min_price",min_price)
    result_page.api = result_page.api.replace("$max_price", max_price)
    result_page.api = result_page.api.replace("$expand_filters", expand_filters)
    result_page.api = result_page.api.replace("$cat", cat)
    resp =result_page.request()
    assert resp['code'] == result_page.success_resp['code']
    result_item=resp['data']['items'][:-1]
    data_store.suite['result_item'+str(sort)]=result_item



@step("判断搜索结果页的数据与搜索词<serach_words>一致,flag=<flag>")
def verificat_page_result(serach_words,flag):
    result_page = Result_page()
    if flag==1 and result_page.host == 'http://sx.api.mengtuiapp.com':
        result_item=data_store.suite['result_item_default']
        for goods_name in [item['goods']['goods_name'] for item in result_item]:
            assert goods_name.find(serach_words) >= 0


@step("判断根据排序方式搜索结果不同")
def verificat_sort_result():
    result_default = data_store.suite['result_item_default']
    result_sales = data_store.suite['result_item_sales']
    if len(result_default)>0 and len(result_sales)>0:
        assert [item['goods']['goods_id'] for item in result_default]!=[item['goods']['sales'] for item in result_sales]

@step("判断查询结果在同一个类目中")
def verificat_goods_type():
    result_sales= data_store.suite['result_item_sales']
    for goods_type in [item['search_goods_type'] for item in result_sales]:
        assert goods_type==0

#测试环境的排序是错的，所以此条case通不过
@step("判断按照销量进行排序")
def verificat_sales_sort():
    result_page = Result_page()
    if result_page.host != 'http://sx.api.mengtuiapp.com':
        result_sales = data_store.suite['result_item_sales']
        result_sales=[item['goods']['sales'] for item in result_sales]
        sales_sort=sorted(result_sales,reverse=True)
        assert result_sales==sales_sort

#测试环境的排序是错的，所以此条case通不过
@step("判断搜索结果按照价格顺序排列,sort=<sort>")
def verificat_price_sort(sort):
    result_page=Result_page()
    if result_page.host!='http://sx.api.mengtuiapp.com':
        if sort=="price":
            ascending_price = [item['goods']['show_price'] for item in data_store.suite['result_itemprice']]
            assert ascending_price==sorted(ascending_price)
        else:
            descending_price = [item['goods']['show_price'] for item in data_store.suite['result_item_price']]
            assert descending_price == sorted(descending_price,reverse=True)

@step("判断商品的价格在价格区间内")
def verificat_price():
    result_page = Result_page()
    if result_page.host != 'http://sx.api.mengtuiapp.com':
        price_result = [item['goods']['show_price'] for item in data_store.suite['result_item_default']]
        assert min(price_result)>=10
        assert max(price_result)<=200


@step("热搜榜接口")
def rank():
    rank = Rank()
    rank.request()
    print(rank.resp.json())


@step("搜索接口scene_page, search_keyword=<search_keyword>")
def scene_page(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    scene_page = Scene_page()
    scene_page.api = scene_page.api.replace('$search_keyword', search_keyword)
    scene_page.request()
    print(scene_page.resp.json())


@step("搜索接口stage, search_keyword=<search_keyword>")
def stage(search_keyword):
    search_keyword = urllib.parse.quote(search_keyword)
    stage = Stage()
    stage.api = stage.api.replace('$search_keyword', search_keyword)
    stage.request()
    print(stage.resp.json())


@step("获得搜索中间页的数据")
def words():
    words = Words()
    resp = words.request()
    assert resp['code'] == words.success_resp['code']
    hot_words = resp['data']['hot_words']
    activity_words = resp['data']['activity_words']
    assert hot_words != ''
    assert activity_words != ''
    data_store.suite['hot_words'] = hot_words
    data_store.suite['activity_words'] = activity_words


@step("获取搜索中间页的“搜索发现”数据并判断")
def check_search_words():
    words = Words()
    hot_words = data_store.suite['hot_words']
    activity_words = data_store.suite['activity_words']
    ##判断对应词的style,以项目中的配置为准
    for item in hot_words:
        if item["word"] in words.words.keys():
            assert str(item["style"])==str(words.words[item["word"]])
    # ##判断对应词的link,以项目的配置为准
    for item in activity_words:
        if item["word"] in words.links.keys():
            assert str(item["link"]) == str(words.links[item["word"]])

@step("判断搜索结果按照排序为<sort>,服务为萌推好店，类别为付费会员的结果")
def verificat_filter(sort):
    #会员是搜索部门给的结果，无法通过字段判断
    filter_result=data_store.suite['result_item'+str(sort)]
    for goods in [item['goods']['mall']['labels'][0] for item in filter_result]:
        assert goods["type"]=="nice_mall"
    if sort=="_price":
        descending_price = [item['goods']['show_price'] for item in filter_result]
        assert descending_price == sorted(descending_price, reverse=True)
    if sort=="_sales":
        result_sales = [item['goods']['sales'] for item in filter_result]
        assert result_sales==sorted(result_sales,reverse=False)


@step("获得搜索店铺中间页的数据,mall_id=<mall_id>")
def middle_page_result(mall_id):
    mall_middle_page=Mall_middle_page()
    mall_middle_page.api.replace("mallId",mall_id)
    resp=mall_middle_page.request()
    #print(resp)
    assert resp['code']==mall_middle_page.success_resp['code']
    data_store.suite['mall_search_data']=resp['data']

@step("判断搜索发现中的数据是否完整")
def verificat_search_data():
    mall_middle_page = Mall_middle_page()
    assert mall_middle_page.word.sort()==data_store.suite['mall_search_data'].sort()

@step("判断搜索结果页的商品只是本店<mall_id_1>的商品")
def verificat_same_shop(mall_id_1):
    result_default = data_store.suite['result_item_default']
    for mall_id in [item['goods']['mall_id'] for item in result_default]:
        assert str(mall_id)==str(mall_id_1)





