import requests
import csv
from playwright_stealth import stealth_sync
import time
import re
from playwright.sync_api import sync_playwright
from lxml import etree




def get_html(html):
    '''解析html得到每天的链接'''
    response = etree.HTML(html)
    '''选择"zxxx_list"的ul下的li'''
    tr = ('//ul[@class="zxxx_list"]/li')
    '''item依次表示tr中的一个元素，遍历'''
    for item in tr:
        '''网址拼接，xpath定位a标签中指定超链接目标的URL'''
        item_url = 'http://www.nhc.gov.cn' + item.xpath('./a/@href')[0]
        '''打印'''
        print(item_url)
        '''xpath定位元素,在当前节点下面进行选择'''
        data_time = item.xpath('./span/text()')
        with open('链接.csv', 'a+', encoding='utf-8-sig', newline='') as f:
            f = csv.writer(f)
            '''单行写入，将一个列表全部写入csv的同一行'''
            f.writerow([item_url] + [data_time])


def get_item_url():
    '''打开提取到的链接进行爬取'''
    cd = csv.reader(open('链接.csv', 'r', encoding='utf-8'))
    for item in cd:
        '''将文本中的去除零宽字符替换成空格'''
        item_url = item[0].replace('﻿', '')
        '''打印出item_url内容'''
        print(item_url)
        '''获取页面源代码'''
        html = get_urls(item_url)
        '''解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象,以便使用xpath函数'''
        item_response = etree.HTML(html)
        '''从任意层级开始查找div,若满足id具有xw_box属性，再查找其子节点，并赋予格式'''
        p = item_response.xpath('//div[@id="xw_box"]/p[@style="text-align: justify; line-height: 1.5; text-indent: 2em; font-family: 仿宋,仿宋_GB2312; font-size: 16pt; -ms-text-justify: inter-ideograph;"]')
        if p == []:
            p = item_response.xpath('//div[@id="xw_box"]/p')
        txt_list = []
        for p_s in p:
            '''该标签下（包括其中包含的子标签）的所有文本'''
            txt = p_s.xpath('.//text()')
            if txt != [] and txt != ['\n']:
                '''保存'''
                txt_list.append(''.join(txt))
                print(txt)
        '''导入爬取数据，输出文件对象'''
        with open('疫情数据xin.csv', 'a+', encoding='utf-8-sig', newline='') as f:
            f = csv.writer(f)
            f.writerow(item + txt_list)


def get_urls(url):
    '''爬取url'''
    '''导入了sync_playwright方法,返回的是一个PlaywrightContextManager对象,将其赋值为变量 p'''
    with sync_playwright() as p:
        '''launch 方法返回的是一个 Browser 对象，我们将其赋值为 browser 变量'''
        browser = p.chromium.launch()
        '''调用 browser 的 new_page 方法，相当于新建了一个选项卡，返回的是一个 Page 对象，将其赋值为 page'''
        page = browser.new_page()
        stealth_sync(page)
        '''goto加载某个页面'''
        page.goto(url)
        '''挂起(等待)当前线程的执行'''
        time.sleep(10)
        '''页面内容'''
        html = page.content()
        '''关闭当前窗口'''
        browser.close()
        return html

get_item_url()