from django.http import HttpResponse, request
from django.shortcuts import render
from . import ReadFile
import jsonpatch
import json
import pandas as pd
import sys


def index(request):
    return render(request, 'app/index.html')




def checkfile(request):
    df = pd.read_excel(path_target_data)
    lable_event_name = df.ix[:, 0]
    for name in lable_event_name:
        get_data_diff(name)
    return render(request, "app/result.html")



"""log的地址与anyproxy中js方法地址一致"""
path_target_data = '/Users/beartwo/Desktop/广东电子合同埋点.xlsx'
path_log_data = '/Users/beartwo/Documents/lmh/anyproxy/anyproxy_data/data.json'


def excel_event_id(event_name):
    df = pd.read_excel(path_target_data)
    row = df[df['事件名'].isin([event_name])].index.values[0]
    event_id = df.ix[row, 1]
    return event_id



def get_target(event_name):
    """获取需求EXCEL中的属性字段"""
    df = pd.read_excel(path_target_data)
    row = df[df['事件名'].isin([event_name])].index.values[0]
    # #row = df[df['事件ID'].isin([event_id])].index.values[0]
    targrt_data = df.ix[row, 2]
    list1 = targrt_data.split('\n')
    list2 = []
    for l in list1:
        list2.append(l.split('='))
        # print(list2)
        dict_targrt_data = dict(list2)
    #print(dict_targrt_data)
    return dict_targrt_data



def get_log(event_name):
    """获取log中的属性字段"""
    fd = path_log_data
    event_id = excel_event_id(event_name)
    list_log =[]
    with open(fd, 'r') as a:
        log_data = a.readlines()
        # s1 = set()
        for test_dic in log_data:
            test_dic1 = eval(test_dic)
            reponsedata_event_id = get_target_value('event_id', test_dic1, [])
            reponsedata_bus_props = get_target_value('bus_props', test_dic1, [])
            reponsedata_usr_props = get_target_value('usr_props', test_dic1, [])
            reponsedata_event_type = get_target_value('event_type',test_dic1,[])
            list_1 = ['event_type']
            list_2 = dict(zip(list_1,reponsedata_event_type))
            list_event_type =[]
            list_event_type.append(list_2)
            #print(list_event_type)
            if event_id in reponsedata_event_id:
                log_total = reponsedata_bus_props+reponsedata_usr_props+list_event_type
                dictMerged = {}
                for x in log_total:
                    dictMerged.update(x)
                #print(dictMerged)
                list_log.append(dictMerged)
                #print(list_log)
    return list_log



def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list




    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


def _get_value(key, val, tmp_list):
    #print(val)
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身





#判断event_id 是否上报
def get_log_all_event_id():
    """获取log中的属性字段"""
    fd = path_log_data
    list_log =[]
    with open(fd, 'r') as a:
        log_data = a.readlines()
        # s1 = set()
        for test_dic in log_data:
            test_dic1 = eval(test_dic)
            reponsedata_event_id = get_target_value('event_id', test_dic1, [])
            list_log.append(reponsedata_event_id)
    b = str(list_log)
    b1 = b.replace('[', '')  # 删除"["
    b2 = b1.replace(']', '')  # 删除"]"
    return b2



#判断上报字段是否完整

def get_data_diff(event_name):

    all_event_id = get_log_all_event_id()

    event_id = excel_event_id(event_name)


    if event_id in all_event_id:
        global list_res
        dict_get_target = get_target(event_name)

        get_dictMerged = get_log(event_name)

        temp1, temp2 = "已匹配", "未匹配"

        list_result = []

        for log in get_dictMerged:
            list_temp = []
            list_res = []

            for i in dict_get_target.values():
                if i not in log.values():
                    temp = temp2
                else:
                    temp = temp1
                str = i + " " + temp
                list_res.append(str)
                list_temp.append(temp)
            list_temp_1 = set(list_temp)

            if len(list_temp_1) == 1 and temp1 in list_temp_1:
                list_result.append('pass')
            else:
                list_result.append(list_res)

        if "pass" in list_result:
            print ("%s 上报正常" % event_id)
        else:
            print('%s ' % event_id + '上报字段异常：%s' % list_res)
    else:
        print ('%s 未上报该事件' % event_id)






