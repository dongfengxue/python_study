#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 13:47
# @Author  : Lhj
# @Site    : 
# @File    : send_message.py
# @Software: PyCharm

import requests
from fake_useragent import UserAgent
import time
import schedule
import json
import logging

logging.basicConfig(level=logging.INFO,
                    filename='mess.log',
                    filemode = 'a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
logger = logging.getLogger(__name__)

SCKEY = 'SCU141247Te3764693a97d7a2b9bd9e082825902cb5feb44636fbf9'
url = 'https://sc.ftqq.com/{}.send'.format(SCKEY)



class Send_message(object):
    def __init__(self,url,data):
        self.url = url
        self.data = data

    def job(self):
        headers = {
            'User-Agent': UserAgent().chrome
        }
        response = requests.get(url= self.url,headers=headers,params=self.data)

        logger.debug(response.text)
        message = json.loads(response.text)   #字符串转化为字典格式输出
        logger.info(message)
        print(message)



if __name__ == '__main__':
    # schedule.every(2).minutes.do(job)
    #设置运行时间
    run_time = "09:55"
    print("定时任务启动，每天{}运行提醒".format(run_time))

    data = {
        'text': 'jd',
        'desp': '无详细内容记得操作{}'.format(time.time()*1000)

    }


    list = Send_message(url,data)
    # schedule.every(70).seconds.do(list.job)
    schedule.every().day.at(run_time).do(list.job)

    while True:
        schedule.run_pending()

    # mes = '{"errno":1024,"errmsg":"\u4e0d\u8981\u91cd\u590d\u53d1\u9001\u540c\u6837\u7684\u5185\u5bb9"}'
    # print( json.loads(mes))
