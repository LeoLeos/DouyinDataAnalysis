#coding:utf-8
import pandas as pd
import numpy as np
from sklearn import linear_model
import time
import os

def prerate(fileName):
    # 获取当地时间
    local_time = time.localtime()
    local_time = time.strftime("%Y/%m/%d %H:%M:%S", local_time)
    print('当地时间', end='')
    print(local_time)

    PF = pd.read_csv('D:\Smile\DataAnalysisProject\DouyinBuyinLiveDate\ACI号\ACI直播间实时数据.csv', encoding="utf-8")
    x = PF.index.values.tolist()
    # y= PF.columns.values
    y = PF['累计观看次数'].tolist()
    x = [[i] for i in x]

    print('近5分钟直播间流量速度：', end='')
    five_min_reg = linear_model.LinearRegression()
    five_min_reg.fit(x[-15:], y[-15:])
    print(five_min_reg.coef_[0])
    print('近30分钟直播间流量速度：', end='')
    thirty_min_reg = linear_model.LinearRegression()
    thirty_min_reg.fit(x[-30:], y[-30:])
    print(thirty_min_reg.coef_[0])
    print('近一小时直播间流量速度：', end='')
    sixty_min_reg = linear_model.LinearRegression()
    sixty_min_reg.fit(x[-60:], y[-60:])
    print(sixty_min_reg.coef_[0])
    print('近六小时直播间流量速度：', end='')
    six_hour_reg = linear_model.LinearRegression()
    six_hour_reg.fit(x[-360:], y[-360:])
    print(six_hour_reg.coef_[0])
    print('近十二小时直播间流量速度：', end='')
    twelve_hour_reg = linear_model.LinearRegression()
    twelve_hour_reg.fit(x[-720:], y[-720:])
    print(twelve_hour_reg.coef_[0])

    format_data = {'RealTime': local_time, 'five_min_speed': five_min_reg.coef_[0], 'thirty_min_speed': thirty_min_reg.coef_[0], 'sixty_min_speed': sixty_min_reg.coef_[0],
                   'six_hour_speed': six_hour_reg.coef_[0], 'twelve_hour_speed': twelve_hour_reg.coef_[0]}

    if not os.path.exists(fileName):
        with open(fileName, 'a', newline='', encoding='utf-8') as f:
            f.write('%s, %s, %s, %s, %s, %s' % ('时间', '近5分钟流量速度', '近30分钟流量速度', '近一小时流量速度', '近六小时流量速度', '近十二小时流量速度'))
            f.writelines('\n')
            f.close()
    with open(fileName, 'a', newline='', encoding='utf-8') as f:
        f.write('%s, %s, %s, %s, %s, %s' % (format_data['RealTime'], format_data['five_min_speed'], format_data['thirty_min_speed'], format_data['sixty_min_speed'],
                                            format_data['six_hour_speed'], format_data['twelve_hour_speed']))
        f.writelines('\n')
        f.close()

if __name__ == '__main__':
    count = 0
    while True:
        count = count + 1
        print('开启第' + str(count) + '次任务:ACI直播间流量速度')
        fileName = 'ACI'+'直播间流量速度.csv'
        prerate(fileName)
        time.sleep(60)
