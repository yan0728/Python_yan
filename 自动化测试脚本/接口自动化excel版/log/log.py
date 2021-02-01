#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: log.py
@time:2021/2/1 0001
"""

import logging
from 自动化测试脚本.接口自动化excel版.setting import config

def log():
    #创建logger，如果参数为空则返回root logger
    # logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。
    logger = logging.getLogger("nick")
    #设置logger日志等级
    logger.setLevel(logging.INFO)

    #这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        #创建handler
        fh = logging.FileHandler(config.TEST_LOG,encoding="utf-8")
        ch = logging.StreamHandler()

        #设置输出日志格式,
        # fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        # datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
        # style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'
        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(filename)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
            )

        #为handler指定输出格式，注意大小写
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger  # 直接返回logger

logger = log()