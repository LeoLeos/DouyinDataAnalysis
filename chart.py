from pyecharts.charts import Line
from pyecharts import options as opts
import pandas as pd
import time

def charthtml(FileName):
    data = pd.read_csv(FileName)
    line = (
        Line()
        .add_xaxis(data['时间'].tolist())
        .add_yaxis('近5分钟流量速度', data[' 近5分钟流量速度'].tolist())
        .add_yaxis('近30分钟流量速度', data[' 近30分钟流量速度'].tolist())
        .add_yaxis('近一小时流量速度', data[' 近一小时流量速度'].tolist())
        .add_yaxis('近六小时流量速度', data[' 近六小时流量速度'].tolist())
        .add_yaxis('近十二小时流量速度', data[' 近十二小时流量速度'].tolist())
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    line.render(FileName + '.html')

if __name__ == '__main__':
    FileName = ['ACI人工软骨号直播间流量速度.csv', 'ACI直播间流量速度.csv']
    # FileName = ['ACI直播间流量速度.csv']

    # FileName = 'ACI直播间流量速度.csv'
    # FileName = '誉马线直播间流量速度.csv'
    while True:
        for i in FileName:
            charthtml(i)
        time.sleep(60)
