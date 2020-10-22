from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd
import time

def charthtml(FileName):
    data = pd.read_csv(FileName)
    # 发布时间类别
    category = list(set(data["发布时间"].values.tolist()))
    line = Line()
    # line.add_xaxis(data['当地时间'].tolist())
    for i in category:
        line.add_xaxis(data[data["发布时间"] == i]['当地时间'].to_list())
        line.add_yaxis(i, data[data["发布时间"] == i]['播放数'].to_list())

    line.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    line.render('ACI单个作品实时数据.csv.html')

if __name__ == '__main__':
    FileName = ['D:\Smile\DataAnalysisProject\DouyinBuyinLiveDate\ACI号\ACI单个作品实时数据.csv', ]
    # FileName = ['ACI直播间流量速度.csv']

    # FileName = 'ACI直播间流量速度.csv'
    # FileName = '誉马线直播间流量速度.csv'
    while True:
        for i in FileName:
            charthtml(i)
        time.sleep(60)
