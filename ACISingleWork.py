import requests
import json
import threading
import os
import time


def writeData(format_data):
    fileName = "ACI单个作品实时数据.csv"
    if not os.path.exists(fileName):
        with open(fileName, 'a', newline='', encoding='utf-8') as f:
            f.writelines("%s,%s,%s,%s,%s,%s,%s,%s" % ('当地时间',
                                                      '发布时间',
                                                      '作品标题',
                                                      '作品分享链接',
                                                      '播放数',
                                                      '点赞数',
                                                      '评论数',
                                                      '分享数',
                                                      ))
            f.writelines('\n')
            f.close()
    with open(fileName, 'a', newline='', encoding='utf-8') as f:
        f.writelines("%s,%s,%s,%s,%s,%s,%s,%s" % (format_data['local_time'],
                                                  format_data['public_time'],
                                                  format_data['desc'],
                                                  format_data['share_url'],
                                                  format_data['play_count'],
                                                  format_data['digg_count'],
                                                  format_data['comment_count'],
                                                  format_data['share_count'],
                                                  ))
        f.writelines('\n')
        f.close()

def test_task(url,cookies):
    # cookies = "__guid=181552757.3199703258393263600.1600073066517.8777; ttcid=b2946df63d4d41e993a1abf0ba3e038a41; ttwid=1%7CaKFVq6CuVo9BFkc4fmkbvvVFXjW-Wuv-FR6cX3zKl5A%7C1600073070%7C46c1d7ccc227e952b87c823a28842282ba9ce245294cde549691255b52869bb5; oc_login_type=LOGIN_PERSON; toutiao_sso_user=d76178578ba0c52928ce51c926f643aa; toutiao_sso_user_ss=d76178578ba0c52928ce51c926f643aa; odin_tt=10b1ba84c2cca2ecdf95d52785fbc4b933a0b950b9fdf137f14b7103a2875b35844091e83e2ada4beebb1d45356471bf; sso_uid_tt=3f37cc1850a8a4d2d643cf149b93ceba; sso_uid_tt_ss=3f37cc1850a8a4d2d643cf149b93ceba; passport_auth_status=327c032ca1e0ba9a01834ff4f6d19daf%2C47ffc05a029389f2b795c5230b32b661; sid_guard=a6652d756a8c20209814f4a645b453e1%7C1601791893%7C5184000%7CThu%2C+03-Dec-2020+06%3A11%3A33+GMT; uid_tt=76033d1f34dc15fa11b35ab9a4b1004d; uid_tt_ss=76033d1f34dc15fa11b35ab9a4b1004d; sid_tt=a6652d756a8c20209814f4a645b453e1; sessionid=a6652d756a8c20209814f4a645b453e1; sessionid_ss=a6652d756a8c20209814f4a645b453e1; SLARDAR_WEB_ID=62317957531; csrf_token=sClWrNFsEUZrdOtqUtxERoqtxucQTdIa; MONITOR_WEB_ID=f12b40dd-7142-4b3a-b926-5f803e1abd28; s_v_web_id=kfyzedtd_Qlf0e6GT_vmRM_4Lj0_8hG9_eJ3wqXE7xL02; tt_scid=L6grPbJBqonW7v8ulnraH85RqNox0RZpFvcQ0Un2mYnAg.jD4kRbgY66BtkfWcn09a7a; passport_csrf_token=633ad482b8c2fa368eda6d3bb8384ce1; monitor_count=4"

    # 累计观看人数
    # getLiveRealTimeSummary
    # url = 'https://creator.douyin.com/web/api/media/aweme/post/?scene=star_atlas&status=0&count=12&max_cursor=0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F85.0.4183.121+Safari%2F537.36&browser_online=true&timezone_name=Asia%2FShanghai&aid=1128&_signature=mJqrKAAgEADtayB2A7vDApiaqzAAMf1'


    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': cookies,
    }
    # 获取实时观看人数
    Request_Work_info = requests.get(url=url, headers=header)
    AllInfo = json.loads(Request_Work_info.text)
    # 作品以列表存储
    Work_info = AllInfo['aweme_list']
    # print(Work_info)

    for i in range(len(Work_info)):
        # 获取作品时间戳
        # print(Work_info[0])
        work_time = time.localtime(Work_info[i]['create_time'])
        # print(work_time)
        # work_time = time.localtime(Work_info[i]['timer']['public_time'])
        # 时间戳格式化
        print('发布时间', end='')
        public_time = time.strftime("%Y/%m/%d %H:%M:%S", work_time)
        print(public_time)

        # 获取当地时间
        local_time = time.localtime()
        local_time = time.strftime("%Y/%m/%d %H:%M:%S", local_time)
        print('当地时间', end='')
        print(local_time)

        print('作品标题', end='')
        print(Work_info[i]['desc'])
        desc = Work_info[i]['desc']

        print('作品分享链接', end='')
        print(Work_info[i]['share_url'])
        share_url = Work_info[i]['share_url']

        # 'statistics'作品统计数据
        print('作品统计数据', end='')
        # print(Work_info[0]['statistics'])

        print('播放数', end='')
        print(Work_info[i]['statistics']['play_count'])
        play_count = Work_info[i]['statistics']['play_count']

        print('点赞数', end='')
        print(Work_info[i]['statistics']['digg_count'])
        digg_count = Work_info[i]['statistics']['digg_count']

        print('评论数', end='')
        print(Work_info[i]['statistics']['comment_count'])
        comment_count = Work_info[i]['statistics']['comment_count']

        print('分享数', end='')
        print(Work_info[i]['statistics']['share_count'])
        share_count = Work_info[i]['statistics']['share_count']

        format_data = {'local_time':local_time,
                       'public_time': public_time,
                       'desc': desc,
                       'share_url': share_url,
                       'play_count': play_count,
                       'digg_count': digg_count,
                       'comment_count': comment_count,
                       'share_count': share_count,
                       }

        writeData(format_data)

if __name__ == '__main__':
    # 请求作品页面链接
    url = "https://creator.douyin.com/web/api/media/aweme/post/?scene=star_atlas&status=0&count=12&max_cursor=0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F86.0.4240.75+Safari%2F537.36&browser_online=true&timezone_name=Asia%2FShanghai&aid=1128&_signature=fKqqFgAgEAMJWyFIHz-OpHyqqgAACMr"
    cookies = "ttcid=23307476ffe7422e97dac6d2a19a8e3025; ttwid=1%7CHq5wpJ-dPMd5q7D2RdGkTLlNhcrUGZeGGe_3C8t2h7g%7C1601275399%7C5765da1fc0b36447d5f6653875f07b1c82352088112df6095479ff927b4fbd5e; oc_login_type=LOGIN_PERSON; csrf_token=BscMYlxMAMFhvcmNyVgzUNgmaEhYXTZx; s_v_web_id=kg3037vw_f5gzG3CP_3gCq_4CEJ_BKs1_vDcJNu68zcM9; odin_tt=8546ddc57562c752922d5ee3d1426327b8599d55601fdb0a04f456a5b5e559daaeac91366a663b84c69f4d05b73bdf30; sso_uid_tt=2323ed073f777941d2155b99e42236e2; sso_uid_tt_ss=2323ed073f777941d2155b99e42236e2; toutiao_sso_user=53cf009519c2322a720d849520a54066; toutiao_sso_user_ss=53cf009519c2322a720d849520a54066; passport_auth_status=ea3048a4b002401934add882f80a4f22%2C41f7cf130e134f375eb632593d20a099; sid_guard=32037e3d5188ec14c03334bdf30f7d66%7C1602293409%7C5184000%7CWed%2C+09-Dec-2020+01%3A30%3A09+GMT; uid_tt=48192298ce67b165a96d2f308c9948c6; uid_tt_ss=48192298ce67b165a96d2f308c9948c6; sid_tt=32037e3d5188ec14c03334bdf30f7d66; sessionid=32037e3d5188ec14c03334bdf30f7d66; sessionid_ss=32037e3d5188ec14c03334bdf30f7d66; MONITOR_WEB_ID=73672661-162e-44dc-9aaa-5f871ebfedf3; tt_scid=AdLaTAbTfaLXU3IhZdI3gNPhpG2f-xRgAWVCSU55C52pChU22dljQgdNaIRZ8YxK0c55; SLARDAR_WEB_ID=62317957531"

    count = 0
    while True:
        try:
            count = count + 1
            print('开启第' + str(count) + '次任务')
            test_task(url=url, cookies=cookies)
            time.sleep(60)
        except Exception as e:
            print(e)
            continue