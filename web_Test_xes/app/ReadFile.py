#!/usr/bin/python
# -*- coding : UTF-8 -*-
from typing import TextIO

import xmltodict
import json


class ReadFile(object):

    def __init__(self):
        pass

    """获取xml文件并将内容转化为json并将其转换成字典"""

    def load_json(self,xml_path):
        # 获取xml文件
        xml_file = open(xml_path, 'r')
        # 读取xml文件内容
        xml_str = xml_file.read()
        # 将读取的xml内容转为json
        xmlparse = xmltodict.parse(xml_str)
        jsonstr = json.dumps(xmlparse)
        jsondocs = json.loads(jsonstr)
        xml_file.close()
        return jsondocs

    """读取json文件并将返回值转换成字典"""
    def json_file(self,json_path):
        #获取json文件
        myJsonfile = open(json_path,'r')
        #将返回值转换成字典
        Dictionaries = json.load(myJsonfile)
        # #将Dictionaries字段转换成json串
        # JsonString = json.dumps(Dictionaries)
        myJsonfile.close()
        return Dictionaries

    def strings_file( self, strings_path ):
        #获取strings文件
        strings_file = open(strings_path,'r')
        # 使用readlines读取
        lines = strings_file.readlines()
        #临时存储到一个list中
        list = {}
        for line in lines:
            #将读取的每行内容过滤掉换行符和；，如果不加这个条件，输入的内容将会有换行符和；
            line = line.strip('\n')
            line = line.strip(';')
            ss = line.split('=')  #将每行内容根据=分割
            if len(ss) > 1:
                a = eval(ss[1])  #去除字符串前后引号
                b = eval(ss[0])
                list[a] = b
        strings_file.close()
        return list
