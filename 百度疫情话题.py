import requests
import time
from lxml import etree



session = requests.session()

#反爬虫的方式headers的伪造
headers = {
    #指定客户端能够接受的内容类型
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #请求头允许客户端声明它可以理解的自然语言，以及优先选择的区域方言 最佳语言为中文-中国（默认权重为1），其次为中文，权重为0.9
    'Accept-Language':'zh-CN,zh;q=0.9',
    #连接状态
    'Connection':'keep-alive',
    #当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的
    'Referer':'https://www.baidu.com',
    #表示请求的目的地，即以document方式获取的数据
    'Sec-Fetch-Dest':'document',
    #表示这是一个浏览器的页面切换请求(request)，navigate请求仅在浏览器切换页面时创建，该请求应该返回HTML
    'Sec-Fetch-Mode':'navigate',
    #表示一个请求发起者的来源与目标资源来源之间的关系，此处表示，发起和目标站点源完全一致
    'Sec-Fetch-Site':'same-origin',
    #导航请求由用户激活以外的原因触发
    'Sec-Fetch-User':'?1',
    #可以把所属本站的所有 http 连接升级为 https 连接
    'Upgrade-Insecure-Requests':'1',
    #最重要的请求头信息之一；一般可以直接复制，对于一些变化的可以选择构造
    'cookie':'BAIDUID=1683EDF66AE0E28A51DBEB4EB5D063DC:FG=1; BIDUPSID=1683EDF66AE0E28A51DBEB4EB5D063DC; PSTM=1661661840; BD_UPN=123253; newlogin=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=VpnckYzN0tTVDY1NWxUZ28tM2laRGJqRDY2MkVJM0ZEakhtQ3VFVzFTS3I4RXRqRVFBQUFBJCQAAAAAAAAAAAEAAABpMxBUx-~S4sWoMTg1NjYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKtjJGOrYyRjU; BDUSS_BFESS=VpnckYzN0tTVDY1NWxUZ28tM2laRGJqRDY2MkVJM0ZEakhtQ3VFVzFTS3I4RXRqRVFBQUFBJCQAAAAAAAAAAAEAAABpMxBUx-~S4sWoMTg1NjYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKtjJGOrYyRjU; MCITY=-257:; BDSFRCVID=gZkOJeC629VsKMnj5ooqM6tDMJN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbk8oKP2fC03HRjvMn__DT5QqxbXqhcbHmOZ0l8KtDQ6hpPw04ChhPbbXHjJ0Ur-MGvILDQmWIQHDUbb5M7DKpK-DhQOqUc0fCr4KKJxtfKWeIJo5fcI-TLOhUJiB5JMBan7_pbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_xjjLWD53XepJf-K6WbC600njVanI_Hn7zePJAMU4pbt-qJjcp-23uWJFaab7a8DQmQMckX6_7XHjnBT5Ka2vB_xo10h0Keh8mjKcmh50kQN3TqPKO5bRiLRoFtq6CDn3oyTbJXp0nj-Oly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfD7H3KC2JC8KhMK; ab_sr=1.0.1_YmIwMGZiNzRmZWE2MjhjY2UxODQ2ZDgyMDA5OTE1YzYxNWEwMzE0MDQxOGM1ZjA5YTliMDFiOTgzMGM5NTM3NmZlYjU2OThhNjA1MjNmODlmNDk0N2Y3ODA4NGFjZDliZDRiNzMxMjM4NWRlMDRlM2E0N2NiNWFkM2Q4YjBkNmRkMTgzNWI0ZWM0YmQwMmMyMTBhODUxOTU3OWJhZTgwNw==; delPer=0; BD_CK_SAM=1; BDSFRCVID_BFESS=gZkOJeC629VsKMnj5ooqM6tDMJN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbk8oKP2fC03HRjvMn__DT5QqxbXqhcbHmOZ0l8KtDQ6hpPw04ChhPbbXHjJ0Ur-MGvILDQmWIQHDUbb5M7DKpK-DhQOqUc0fCr4KKJxtfKWeIJo5fcI-TLOhUJiB5JMBan7_pbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_xjjLWD53XepJf-K6WbC600njVanI_Hn7zePJAMU4pbt-qJjcp-23uWJFaab7a8DQmQMckX6_7XHjnBT5Ka2vB_xo10h0Keh8mjKcmh50kQN3TqPKO5bRiLRoFtq6CDn3oyTbJXp0nj-Oly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfD7H3KC2JC8KhMK; BAIDUID_BFESS=1683EDF66AE0E28A51DBEB4EB5D063DC:FG=1; H_PS_645EC=0500QSX0UcJNU9dtrCsVNG8o8xJhDwE/dEkH/lMN9DhiOYFDzSt1WbLMxBYK37GGAddv; BA_HECTOR=2k2g2k2l208k2gal20245kkh1hid43t19; ZFY=3mFHp:AK5cLIvGCI3p4RP:AjdV49evmpiBofln9lGUqa0:C; BDRCVFR[C0p6oIjvx-c]=ddONZc2bo5mfAF9pywdpAqVuNqsus; PSINO=1; H_PS_PSSID=37378_36547_36466_37352_36885_34813_36802_36786_37260_37343_37363; BDSVRTM=1235',
    #向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    #防止泄露浏览器详细信息
    'sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    #是否移动端用户
    'sec-ch-ua-mobile':'?0',
    #操作系统名称
    'sec-ch-ua-platform':'"macOS"',

}


def get_url(url):
    #反爬进行4次重试
    max_number = 4
    while True:
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            req.encoding = 'utf-8'
            return req.text
        else:
            print('\n error \n', req.text)
            time.sleep(100)
        max_number += 1
        if max_number == 4:
            break

def get_baidu_spider(html):
    response = etree.HTML(html)
    item_link = response.xpath('//a[@class="news-title-font_1xS-F"]/@href')
    item_name = response.xpath('//a[@class="news-title-font_1xS-F"]/@aria-label')
    #保存
    for item_links, item_names in zip(item_link, item_name):
        print(item_names)
        with open('疫情.txt', mode='a+', encoding='utf-8') as f:
            f.write(item_names.replace('标题：', ''))
            f.write('\n')


def start():
    #开始爬取
    while True:
        for number in range(0, 360, 10):
            time.sleep(3)
            url = 'https://www.baidu.com/s?ie=utf-8&medium=0&rtt=1&bsst=1&rsv_dl=news_b_pn&cl=2&wd=%E7%96%AB%E6%83%85%E8%AF%9D%E9%A2%98&tn=news&rsv_bp=1&rsv_sug3=2&oq=&rsv_btype=t&f=8&inputT=1287&rsv_sug4=1638&x_bfe_rqs=032000000000000000004400000000000000000000000008&x_bfe_tjscore=0.080000&tngroupname=organic_news&newVideo=12&goods_entry_switch=1&pn={}'.format(number)
            html = get_url(url)
            get_baidu_spider(html)
            time.sleep(10)


start()