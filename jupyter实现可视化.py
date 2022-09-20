#!/usr/bin/env python
# coding: utf-8

# In[34]:

#本文件在jupyter下运行才会出现可视化

# 导入模块
import pandas as pd

df = pd.read_csv(
    'data.csv')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。

df.head()[:0]

x = list(df['时间'][0:30].values)

# In[ ]:


# In[36]:


from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie, Grid, Map, Page

bar = (
    Bar(init_opts=opts.InitOpts(width="980px", height="500px", bg_color='pink'))
    .add_xaxis([
        '上海',
        '北京',
        '天津',
        '重庆',
        '广西',
        '宁夏',
        '内蒙古',
        '西藏',
        '新疆',
        '云南',
        '四川',
        '海南',
        '广东',
        '台湾',
        '贵州',
        '湖南',
        '福建',
        '江西',
        '浙江',
        '湖北',
        '陕西',
        '安徽',
        '江苏',
        '河南',
        '甘肃',
        '青海',
        '山东',
        '山西',
        '河北',
        '辽宁',
        '吉林',
        '黑龙江',
        '香港',
        '澳门',
    ])  # 添加x轴数据各省份名
    .add_yaxis("新增确诊人数", df['新增确诊人数'][0:30].values.tolist())  # 添加y轴数据死亡人数
    .add_yaxis("无症状感染", df['无症状感染'][0:30].values.tolist())  # 添加y轴数据累计确诊人数
    .set_global_opts(  # 设置标题
        title_opts=opts.TitleOpts(title='各省当天新增确诊人数与无症状感染情况'),
        datazoom_opts=[opts.DataZoomOpts(type_="slider")],
        yaxis_opts=opts.AxisOpts(name="人数"),
        xaxis_opts=opts.AxisOpts(name="省份")
    )

)
bar.render_notebook()

# In[38]:


from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result;


with open(r"./疫情.txt", encoding='utf-8') as fp:
    text = fp.read()
    print(text)
    text = trans_CN(text)
    # print(text)
    mask = np.array(image.open(r"./1.jpeg"))
    wordcloud = WordCloud(
        mask=mask,
        font_path=r"./wqy-microhei.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()

# In[ ]:


# In[40]:


china_map = (
    Map(init_opts=opts.InitOpts(width="980px", height="500px", bg_color='pink'))
    .add("现有确诊", [list(i) for i in zip([

        '上海',
        '北京',
        '天津',
        '重庆',
        '广西',
        '宁夏',
        '内蒙古',
        '西藏',
        '新疆',
        '云南',
        '四川',
        '海南',
        '广东',
        '台湾',
        '贵州',
        '湖南',
        '福建',
        '江西',
        '浙江',
        '湖北',
        '陕西',
        '安徽',
        '江苏',
        '河南',
        '甘肃',
        '青海',
        '山东',
        '山西',
        '河北',
        '辽宁',
        '吉林',
        '黑龙江',
        '香港',
        '澳门',
    ], df['新增确诊人数'].values.tolist())], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各地区现有确诊人数"),
        visualmap_opts=opts.VisualMapOpts(max_=300, is_piecewise=False, is_show=True),
        legend_opts=opts.LegendOpts(pos_left="90%", pos_top="60%"),
    )
)
china_map.render_notebook()

# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:



