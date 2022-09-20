import csv
import re



#将原始的文件清洗换行符等
# cd = csv.reader(open('疫情数据2.csv', 'r', encoding='utf-8'))
# for item in cd:
#     txt_list = [items.replace('\n','').replace('\t','').replace('\r','').replace('\u3000','').replace('\u2002', '') for items in item]
#     print(txt_list)
#     with open('清洗后疫情数据.csv', 'a+', encoding='utf-8-sig', newline='') as f:
#         f = csv.writer(f)
#         f.writerow(txt_list)





#表头
with open('data22.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = [
        '时间',
        '新增确诊人数',
        '无症状感染',
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
        '上海新增',
        '北京新增',
        '天津新增',
        '重庆新增',
        '广西新增',
        '宁夏新增',
        '内蒙古新增',
        '西藏新增',
        '新疆新增',
        '云南新增',
        '四川新增',
        '海南新增',
        '广东新增',
        '台湾新增',
        '贵州新增',
        '湖南新增',
        '福建新增',
        '江西新增',
        '浙江新增',
        '湖北新增',
        '陕西新增',
        '安徽新增',
        '江苏新增',
        '河南新增',
        '甘肃新增',
        '青海新增',
        '山东新增',
        '山西新增',
        '河北新增',
        '辽宁新增',
        '吉林新增',
        '黑龙江新增',
        '香港新增',
        '澳门新增'

    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

dict = {
    '时间':0,
    '新增确诊人数':0,
    '无症状感染':0,
    '上海':0,
    '北京':0,
    '天津':0,
    '重庆':0,
    '广西':0,
    '内蒙古':0,
    '西藏':0,
    '新疆':0,
    '宁夏':0,
    '云南':0,
    '四川':0,
    '海南':0,
    '广东':0,
    '台湾':0,
    '贵州':0,
    '湖南':0,
    '福建':0,
    '江西':0,
    '浙江':0,
    '湖北':0,
    '陕西':0,
    '安徽':0,
    '江苏':0,
    '河南':0,
    '甘肃':0,
    '青海':0,
    '山东':0,
    '山西':0,
    '河北':0,
    '辽宁':0,
    '吉林':0,
    '黑龙江':0,
    '香港':0,
    '澳门':0,

    '上海新增': 0,
    '北京新增': 0,
    '天津新增': 0,
    '重庆新增': 0,
    '广西新增': 0,
    '内蒙古新增': 0,
    '西藏新增': 0,
    '新疆新增': 0,
    '宁夏新增': 0,

    '云南新增':0,
    '四川新增':0,
    '海南新增':0,
    '广东新增':0,
    '台湾新增':0,
    '贵州新增':0,
    '湖南新增':0,
    '福建新增':0,
    '江西新增':0,
    '浙江新增':0,
    '湖北新增':0,
    '陕西新增':0,
    '安徽新增':0,
    '江苏新增':0,
    '河南新增':0,
    '甘肃新增':0,
    '青海新增':0,
    '山东新增':0,
    '山西新增':0,
    '河北新增':0,
    '辽宁新增':0,
    '吉林新增':0,
    '黑龙江新增':0,
    '香港新增':0,
    '澳门新增':0,



    }

#统计数据
cd = csv.reader(open('清洗后疫情数据.csv', 'r', encoding='utf-8'))
for item in cd:
    txt_time = item[1]
    txt = ''.join(item)
    #每天本土新增
    dict['时间'] = item[1]
    # 新增确诊病例
    newConfirmed = re.search('\u65b0\u589e\u786e\u8bca.*?\u4f8b(\d*)\u4f8b', txt, re.S)
    #无症状感染
    Confirmed = re.search('31个省（自治区、直辖市）和新疆生产建设兵团报告新增无症状感染者(\d*)例', txt, re.S)
    #省份无症状
    wuzhengzhuang_s = ''.join(re.findall('报告新增无症状感染者.*）。当', txt))
    #省份新增
    new_data = ''.join(re.findall('本土病例\d*例（(.*?)）', item[2]))
    try:
        dict['新增确诊人数'] = newConfirmed.group(1)
    except AttributeError:
        dict['新增确诊人数'] = 0
    try:
        dict['无症状感染'] = Confirmed.group(1)
    except AttributeError:
        dict['无症状感染'] = 0

    try:
        sh = re.search('上海(\d*)', wuzhengzhuang_s, re.S)
        dict['上海'] = sh.group(1)

    except:
        dict['上海'] = '0'

    try:
        bj = re.search('北京(\d*)', wuzhengzhuang_s, re.S)
        dict['北京'] = bj.group(1)

    except:
        dict['北京'] = '0'

    try:
        cq = re.search('重庆(\d*)', wuzhengzhuang_s, re.S)
        dict['重庆'] = cq.group(1)

    except:
        dict['重庆'] = '0'

    try:
        gx = re.search('广西(\d*)', wuzhengzhuang_s, re.S)
        dict['广西'] = gx.group(1)
    except:
        dict['广西'] = '0'

    try:
        nmg = re.search('内蒙古(\d*)', wuzhengzhuang_s, re.S)
        dict['内蒙古'] = nmg.group(1)

    except:
        dict['内蒙古'] = '0'

    try:
        xz = re.search('西藏(\d*)', wuzhengzhuang_s, re.S)
        dict['西藏'] = xz.group(1)
    except:
        dict['西藏'] = '0'

    try:
        xj = re.search('新疆(\d*)', wuzhengzhuang_s, re.S)
        dict['新疆'] = xj.group(1)
    except:
        dict['新疆'] = '0'

    try:
        nx = re.search('宁夏(\d*)', wuzhengzhuang_s, re.S)
        dict['宁夏'] = nx.group(1)
    except:
        dict['宁夏'] = '0'

    try:
        yn = re.search('\u4e91\u5357(\d*)', wuzhengzhuang_s, re.S)
        dict['云南'] = yn.group(1)
    except AttributeError:
        dict['云南'] = 0
    try:
        sc = re.search('四川(\d*)', wuzhengzhuang_s, re.S)
        dict['四川'] = sc.group(1)
    except:
        dict['四川'] = 0
    try:
        hn = re.search('海南(\d*)', wuzhengzhuang_s, re.S)
        dict['海南'] = hn.group(1)
    except:
        dict['海南'] = 0
    try:
        gd = re.search('广东(\d*)', wuzhengzhuang_s, re.S)
        dict['广东'] = gd.group(1)
    except:
        dict['广东'] = 0
    try:
        tw = re.search('台湾(\d*)', wuzhengzhuang_s, re.S)
        dict['台湾'] = tw.group(1)
    except:
        dict['台湾'] = 0
    try:
        gz = re.search('贵州(\d*)', wuzhengzhuang_s, re.S)
        dict['贵州'] = gz.group(1)
    except:
        dict['贵州'] = 0
    try:
        hn = re.search('湖南(\d*)', wuzhengzhuang_s, re.S)
        dict['湖南'] = hn.group(1)
    except:
        dict['湖南'] = 0
    try:
        fj = re.search('福建(\d*)', wuzhengzhuang_s, re.S)
        dict['福建'] = fj.group(1)
    except:
        dict['福建'] = 0
    try:
        jx = re.search('江西(\d*)', wuzhengzhuang_s, re.S)
        dict['江西'] = jx.group(1)
    except:
        dict['江西'] = 0
    try:
        zj = re.search('浙江(\d*)', wuzhengzhuang_s, re.S)
        dict['浙江'] = zj.group(1)
    except:
        dict['浙江'] = 0
    try:
        hb = re.search('湖北(\d*)', wuzhengzhuang_s, re.S)
        dict['湖北'] = hb.group(1)
    except:
        dict['湖北'] = 0
    try:
        sx = re.search('陕西(\d*)', wuzhengzhuang_s, re.S)
        dict['陕西'] = sx.group(1)
    except:
        dict['陕西'] = 0
    try:
        ah = re.search('安徽(\d*)', wuzhengzhuang_s, re.S)
        dict['安徽'] = ah.group(1)
    except:
        dict['安徽'] = 0
    try:
        js = re.search('江苏(\d*)', wuzhengzhuang_s, re.S)
        dict['江苏'] = js.group(1)
    except:
        dict['江苏'] = 0
    try:
        hn = re.search('河南(\d*)', wuzhengzhuang_s, re.S)
        dict['河南'] = hn.group(1)
    except:
        dict['河南'] = 0
    try:
        gs = re.search('甘肃(\d*)', wuzhengzhuang_s, re.S)
        dict['甘肃'] = gs.group(1)
    except:
        dict['甘肃'] = 0
    try:
        qh = re.search('青海(\d*)', wuzhengzhuang_s, re.S)
        dict['青海'] = qh.group(1)
    except:
        dict['青海'] = 0
    try:
        sd = re.search('山东(\d*)', wuzhengzhuang_s, re.S)
        dict['山东'] = sd.group(1)
    except:
        dict['山东'] = 0
    try:
        sx = re.search('山西(\d*)', wuzhengzhuang_s, re.S)
        dict['山西'] = sx.group(1)
    except:
        dict['山西'] = 0
    try:
        hb = re.search('河北(\d*)', wuzhengzhuang_s, re.S)
        dict['河北'] = hb.group(1)
    except:
        dict['河北'] = 0
    try:
        ln = re.search('辽宁(\d*)', wuzhengzhuang_s, re.S)
        dict['辽宁'] = ln.group(1)
    except:
        dict['辽宁'] = 0
    try:
        jl = re.search('吉林(\d*)', wuzhengzhuang_s, re.S)
        dict['吉林'] = jl.group(1)
    except:
        dict['吉林'] = 0
    try:
        hlj = re.search('黑龙江(\d*)', wuzhengzhuang_s, re.S)
        dict['黑龙江'] = hlj.group(1)
    except:
        dict['黑龙江'] = 0
    try:
        xg = re.search('香港(\d*)', wuzhengzhuang_s, re.S)
        dict['香港'] = xg.group(1)
    except:
        dict['香港'] = 0
    try:
        am = re.search('澳门(\d*)', wuzhengzhuang_s, re.S)
        dict['澳门'] = am.group(1)
    except:
        dict['澳门'] = 0

    ##########

    try:
        sh_s = re.search('上海(\d*)', new_data, re.S)
        dict['上海新增'] = sh_s.group(1)
    except AttributeError:
        dict['上海新增'] = 0


    try:
        bj_s = re.search('北京(\d*)', new_data, re.S)
        dict['北京新增'] = bj_s.group(1)
    except AttributeError:
        dict['北京新增'] = 0


    try:
        tj_s = re.search('天津(\d*)', new_data, re.S)
        dict['天津新增'] = tj_s.group(1)
    except AttributeError:
        dict['天津新增'] = 0

    try:
        cq_s = re.search('重庆(\d*)', new_data, re.S)
        dict['重庆新增'] = cq_s.group(1)
    except AttributeError:
        dict['重庆新增'] = 0

    try:
        gx_s = re.search('广西(\d*)', new_data, re.S)
        dict['广西新增'] = gx_s.group(1)
    except AttributeError:
        dict['广西新增'] = 0

    try:
        nx_s = re.search('宁夏(\d*)', new_data, re.S)
        dict['宁夏新增'] = nx_s.group(1)
    except AttributeError:
        dict['宁夏新增'] = 0

    try:
        nmg_s = re.search('内蒙古(\d*)', new_data, re.S)
        dict['内蒙古新增'] = nmg_s.group(1)
    except AttributeError:
        dict['内蒙古新增'] = 0



    try:
        xz_s = re.search('西藏(\d*)', new_data, re.S)
        dict['西藏新增'] = xz_s.group(1)
    except AttributeError:
        dict['西藏新增'] = 0

    try:
        xj_s = re.search('新疆(\d*)', new_data, re.S)
        dict['新疆新增'] = xj_s.group(1)
    except AttributeError:
        dict['新疆新增'] = 0

    try:
        yn_s = re.search('云南(\d*)', new_data, re.S)
        dict['云南新增'] = yn_s.group(1)
    except AttributeError:
        dict['云南新增'] = 0

    try:
        sc_s = re.search('四川(\d*)', new_data, re.S)
        dict['四川新增'] = sc_s.group(1)
    except:
        dict['四川新增'] = 0

    try:
        hn_s = re.search('海南(\d*)', new_data, re.S)
        dict['海南新增'] = hn_s.group(1)

    except:
        dict['海南新增'] = 0

    try:
        gd_s = re.search('广东(\d*)', new_data, re.S)
        dict['广东新增'] = gd_s.group(1)

    except:
        dict['广东新增'] = 0

    try:
        tw_s = re.search('台湾(\d*)', new_data, re.S)
        dict['台湾新增'] = tw_s.group(1)
    except:
        dict['台湾新增'] = 0

    try:
        gz_s = re.search('贵州(\d*)', new_data, re.S)
        dict['贵州新增'] = gz_s.group(1)
    except:
        dict['贵州新增'] = 0

    try:
        hn_s = re.search('湖南(\d*)', new_data, re.S)
        dict['湖南新增'] = hn_s.group(1)

    except:
        dict['湖南新增'] = 0

    try:
        fj_s = re.search('福建(\d*)', new_data, re.S)
        dict['福建新增'] = fj_s.group(1)
    except:
        dict['福建新增'] = 0

    try:
        jx_s = re.search('江西(\d*)', new_data, re.S)
        dict['江西新增'] = jx_s.group(1)

    except:
        dict['江西新增'] = 0

    try:
        zj_s = re.search('浙江(\d*)', new_data, re.S)
        dict['浙江新增'] = zj_s.group(1)

    except:
        dict['浙江新增'] = 0

    try:
        hb_s_s = re.search('湖北(\d*)', new_data, re.S)
        dict['湖北新增'] = hb_s_s.group(1)

    except:
        dict['湖北新增'] = 0

    try:
        sx_s = re.search('陕西(\d*)', new_data, re.S)
        dict['陕西新增'] = sx_s.group(1)

    except:
        dict['陕西新增'] = 0

    try:
        ah_s = re.search('安徽(\d*)', new_data, re.S)
        dict['安徽新增'] = ah_s.group(1)
    except:
        dict['安徽新增'] = 0

    try:
        js_s = re.search('江苏(\d*)', new_data, re.S)
        dict['江苏新增'] = js_s.group(1)

    except:
        dict['江苏新增'] = 0

    try:
        hn_s = re.search('河南(\d*)', new_data, re.S)
        dict['河南新增'] = hn_s.group(1)
    except:
        dict['河南新增'] = 0

    try:
        gs_s = re.search('甘肃(\d*)', new_data, re.S)
        dict['甘肃新增'] = gs_s.group(1)

    except:
        dict['甘肃新增'] = 0

    try:
        qh_s = re.search('青海(\d*)', new_data, re.S)
        dict['青海新增'] = qh_s.group(1)
    except:
        dict['青海新增'] = 0

    try:
        sd_s = re.search('山东(\d*)', new_data, re.S)
        dict['山东新增'] = sd_s.group(1)

    except:
        dict['山东新增'] = 0

    try:
        sx_s = re.search('山西(\d*)', new_data, re.S)
        dict['山西新增'] = sx_s.group(1)

    except:
        dict['山西新增'] = 0

    try:
        hb_s = re.search('河北(\d*)', new_data, re.S)
        dict['河北新增'] = hb_s.group(1)

    except:
        dict['河北新增'] = 0

    try:
        ln_s = re.search('辽宁(\d*)', new_data, re.S)
        dict['辽宁新增'] = ln_s.group(1)

    except:
        dict['辽宁新增'] = 0

    try:
        jl_s_s = re.search('吉林(\d*)', new_data, re.S)
        dict['吉林新增'] = jl_s_s.group(1)

    except:
        dict['吉林新增'] = 0

    try:
        hlj_s = re.search('黑龙江(\d*)', new_data, re.S)
        dict['黑龙江新增'] = hlj_s.group(1)


    except:
        dict['黑龙江新增'] = 0

    try:
        xg_s = re.search('香港(\d*)', new_data, re.S)
        dict['香港新增'] = xg_s.group(1)

    except:
        dict['香港新增'] = 0

    try:
        am_s = re.search('澳门(\d*)', new_data, re.S)
        dict['澳门新增'] = am_s.group(1)
    except:
        dict['澳门新增'] = 0

    #保存
    with open('data22.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = [
            '时间',
            '新增确诊人数',
            '无症状感染',
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
            '上海新增',
            '北京新增',
            '天津新增',
            '重庆新增',
            '广西新增',
            '宁夏新增',
            '内蒙古新增',
            '西藏新增',
            '新疆新增',
            '云南新增',
            '四川新增',
            '海南新增',
            '广东新增',
            '台湾新增',
            '贵州新增',
            '湖南新增',
            '福建新增',
            '江西新增',
            '浙江新增',
            '湖北新增',
            '陕西新增',
            '安徽新增',
            '江苏新增',
            '河南新增',
            '甘肃新增',
            '青海新增',
            '山东新增',
            '山西新增',
            '河北新增',
            '辽宁新增',
            '吉林新增',
            '黑龙江新增',
            '香港新增',
            '澳门新增'

        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow(dict)










