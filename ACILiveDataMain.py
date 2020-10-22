import requests
import json
import threading
import os
import time

def test_task(room_id, cookies):

    # cookies = ""
    # 直播房间id
    # room_id

    # 累计观看人数
    # getLiveRealTimeSummary
    url = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeSummary?room_id='+room_id+'&app_id=&user_id='
    # 实时观看人数
    # getLiveRealTimeLineChart
    getLiveRealTimeLineChart1 = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeLineChart?room_id='+room_id+'&app_id=&user_id=&line_chart_type=1'
    # 实时购物袋点击
    #
    getLiveRealTimeLineChart2 = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeLineChart?room_id='+room_id+'&app_id=&user_id=&line_chart_type=2'
    # 实时商品点击
    getLiveRealTimeLineChart3 = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeLineChart?room_id='+room_id+'&app_id=&user_id=&line_chart_type=3'
    # 实时支付GMV（小店）
    getLiveRealTimeLineChart4 = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeLineChart?room_id='+room_id+'&app_id=&user_id=&line_chart_type=4'
    # 观看男女比例、年龄段
    age_range = 'https://buyin.jinritemai.com/api/liveData/getLiveRealTimeUserPortrait?room_id='+room_id+'&app_id=&user_id='

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': cookies,
    }
    all_url = [url, getLiveRealTimeLineChart1, getLiveRealTimeLineChart2, getLiveRealTimeLineChart3,
               getLiveRealTimeLineChart4]
    # 获取实时观看人数
    info_getLiveRealTimeLineChart1 = requests.get(url=getLiveRealTimeLineChart1, headers=header)
    text_info_getLiveRealTimeLineChart1 = json.loads(info_getLiveRealTimeLineChart1.text)
    real_watch_times = text_info_getLiveRealTimeLineChart1['data']['real_watch_times']['line_chart_list']
    print('实时时间点:' + str(real_watch_times[0]['time']))
    real_watch_time = str(real_watch_times[0]['time'])
    print('实时观看人数:' + str(real_watch_times[0]['value']))
    real_watch = str(real_watch_times[0]['value'])

    # 获取累计浏览人数
    info_url = requests.get(url=url, headers=header)
    text_info_url = json.loads(info_url.text)
    sumary = text_info_url['data']
    print('累计观看次数:' + str(sumary['accumulative_watch_times']))
    accumulative_watch_times = str(sumary['accumulative_watch_times'])
    print('创建订单量:' + str(sumary['created_order_num']))
    created_order_num = str(sumary['created_order_num'])
    print('创建GMV:' + str(sumary['created_gmv']))
    created_gmv = str(sumary['created_gmv'])
    print('支付订单量:' + str(sumary['pay_order_num']))
    pay_order_num = str(sumary['pay_order_num'])
    print('支付GMV:' + str(sumary['pay_gmv']))
    pay_gmv = str(sumary['pay_gmv'])
    print('订单付款率:' + str(sumary['order_pay_ratio']))
    order_pay_ratio = str(sumary['order_pay_ratio'])

    # 获取年龄段信息
    info_url = requests.get(url=age_range, headers=header)
    text_info_age_range = json.loads(info_url.text)
    age_distribution = text_info_age_range['data']['age_distribution']
    age_distributionList = []
    for i in age_distribution:
        print('年龄段：'+str(i['age_range'])+'  比例：'+str(i['distribution'])+'%')
        age_distributionList.append(str(i['distribution']))
    gender_distribution = text_info_age_range['data']['gender_distribution']
    print('男:'+str(gender_distribution['male_distribution'])+'%')
    male_distribution = str(gender_distribution['male_distribution'])
    print('女:'+str(gender_distribution['female_distribution'])+'%')
    female_distribution = str(gender_distribution['female_distribution'])

    format_data = {'real_watch_time': real_watch_time,
                   'real_watch': real_watch,
                   'accumulative_watch_times': accumulative_watch_times,
                   'created_order_num': created_order_num,
                   'created_gmv': created_gmv,
                   'pay_order_num': pay_order_num,
                   'pay_gmv': pay_gmv,
                   'order_pay_ratio': order_pay_ratio,

                   'age_distribution18-23':age_distributionList[0],
                   'age_distribution24-30': age_distributionList[1],
                   'age_distribution31-40': age_distributionList[2],
                   'age_distribution41-50': age_distributionList[3],
                   'age_distribution50+': age_distributionList[4],
                   'male_distribution': male_distribution,
                   'female_distribution': female_distribution,
                   }

    def writeData(format_data):
        fileName = "ACI直播间实时数据.csv"
        if not os.path.exists(fileName):
            with open(fileName, 'a', newline='', encoding='utf-8') as f:
                f.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % ('实时时间点',
                                                                              '实时观看人数',
                                                                              '累计观看次数',
                                                                              '创建订单量',
                                                                              '创建GMV',
                                                                              '支付订单量',
                                                                              '支付GMV',
                                                                              '订单付款率',
                                                                               '18-23',
                                                                               '24-30',
                                                                               '31-40',
                                                                               '41-50',
                                                                               '50+',
                                                                               '男',
                                                                               '女',


                                                          ))
                f.writelines('\n')
                f.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (format_data['real_watch_time'],
                                                                              format_data['real_watch'],
                                                                              format_data['accumulative_watch_times'],
                                                                              format_data['created_order_num'],
                                                                              format_data['created_gmv'],
                                                                              format_data['pay_order_num'],
                                                                              format_data['pay_gmv'],
                                                                              format_data['order_pay_ratio'],

                                                                               format_data['age_distribution18-23'],
                                                                               format_data['age_distribution24-30'],
                                                                               format_data['age_distribution31-40'],
                                                                               format_data['age_distribution41-50'],
                                                                               format_data['age_distribution50+'],
                                                                               format_data['male_distribution'],
                                                                               format_data['female_distribution'],
                                                          ))
                f.writelines('\n')
                f.close()
        else:
            with open(fileName, 'a', newline='', encoding='utf-8') as f:
                f.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (format_data['real_watch_time'],
                                                                              format_data['real_watch'],
                                                                              format_data['accumulative_watch_times'],
                                                                              format_data['created_order_num'],
                                                                              format_data['created_gmv'],
                                                                              format_data['pay_order_num'],
                                                                              format_data['pay_gmv'],
                                                                              format_data['order_pay_ratio'],

                                                                               format_data['age_distribution18-23'],
                                                                               format_data['age_distribution24-30'],
                                                                               format_data['age_distribution31-40'],
                                                                               format_data['age_distribution41-50'],
                                                                               format_data['age_distribution50+'],
                                                                               format_data['male_distribution'],
                                                                               format_data['female_distribution'],
                                                          ))
                f.writelines('\n')
                f.close()

    writeData(format_data)

if __name__ == '__main__':
    # 直播间id
    room_id = "6886012931289385743"
    # 浏览器信息包
    cookies = "ttcid=f56af9976ac64bd395d683b4578beb0e37; gfpart_1.0.0.1546_8991=1; gfsitesid=YTRmNGQ2NGVhNXwxNjAyMTQyOTgxNzF8fDAGBgYGBgY; sessionid_ss=8185892738844b29b825488e4553e553; buyin_shop_type=24; MONITOR_WEB_ID=f01fc370-b331-4866-8262-1bff3f9818c2; buyin_app_id=1128; sid_tt=8185892738844b29b825488e4553e553; sessionid=8185892738844b29b825488e4553e553; uid_tt=d14fdefb0e6f8a20d3095cbbde35a63a; uid_tt_ss=d14fdefb0e6f8a20d3095cbbde35a63a; gftoken=ODE4NTg5MjczOHwxNjAyMzc5MjY2NjJ8fDAGBgYGBgY; tt_scid=yAeml4CbAM0T6I9mByIT6xNyNPDaysrSGvZR477MpE2hjefpGNXeTRpBtvjBaE4F703c; passport_auth_status=93032caf2d3abf65e255523611d00d1b%2C1aedd6d7178f2617bfa8ef1302f5eb5c; sid_guard=8185892738844b29b825488e4553e553%7C1602383880%7C5184000%7CThu%2C+10-Dec-2020+02%3A38%3A00+GMT; PHPSESSID=edb8b83f7fe9cb331f3d16ee71f2427f; PHPSESSID_SS=edb8b83f7fe9cb331f3d16ee71f2427f; SASID=SID2_3441309816927198867"

    count = 0
    while True:
        try:
            count = count + 1
            print('开启第' + str(count) + '次任务')
            test_task(room_id, cookies)
            time.sleep(60)
        except Exception as e:
            print(e)
            continue
