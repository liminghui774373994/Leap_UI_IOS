from django.http import HttpResponse
from django.shortcuts import render
from dingtalkchatbot.chatbot import DingtalkChatbot
from monitor import dbconn
import time
from datetime import datetime, date, timedelta
from monitor.dbconn import dbconn


# 执行检查数据的SQL
def create_sql(sql_anme, content_sql_name):
    conn = dbconn()
    sql = test_sql(sql_anme)
    a = conn.execute(sql, content_sql_name)
    b = [str(i) for i in a]
    result = "\n".join(b)
    return result


# 获取时间函数
def getNowtime(time_type):
    if time_type == 'nowtime':
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    elif time_type == 'yesterday':
        # print((date.today() + timedelta(hours=-24)).strftime("%Y-%m-%d %H:%M:%S"))
        return (date.today() + timedelta(hours=-24)).strftime("%Y-%m-%d %H:%M:%S")


# SQL语句
def test_sql(sql_name):
    if sql_name == 'article表content_url为空':
        return "SELECT id,content_url FROM `article` WHERE content_url = ''"
    elif sql_name == 'material表duration为空':
        return "SELECT id,duration FROM `material` WHERE duration = ''"
    elif sql_name == 'article表content_url带空格':
        yesterday = getNowtime('yesterday')
        nowtime = getNowtime('nowtime')
        return "SELECT id,content_url FROM `article` WHERE  content_url like '% %' AND update_time BETWEEN '" + yesterday + "'AND'" + nowtime + "'"
    elif sql_name == 'material表url带空格':
        yesterday = getNowtime('yesterday')
        nowtime = getNowtime('nowtime')
        return " SELECT id,url FROM `material` WHERE  url like '% %' AND update_time BETWEEN '" + yesterday + "'AND'" + nowtime + "'"
    elif sql_name == 'check_invetee':
        return "SELECT puid,invitee_puid FROM activity_user_invite WHERE puid = invitee_puid ;;"
    elif sql_name == 'check_repetitioncoupon':
        return "select * from (select puid,count(puid)as cnt from activity_user_coupon_record where `from`=1 and start_timeBETWEEN '" + lastyear + "'AND'" + nowtime + "' group by puid order by count(puid) desc)as temp where cnt > 1;"
    elif sql_name == 'check_limit':
        return "select * from (select puid,count(puid)as cnt from activity_user_coupon_record where `state` in(0,1,2,3) group by puid order by count(puid) desc) as temp where cnt > 30;"
    elif sql_name == 'check_cancelnotify':
        return "SELECT event_data FROM `activity_coupon_error_record` WHERE state = 2 AND event_type = 1;"
    elif sql_name == 'check_exchangenotify':
        return "SELECT event_data FROM `activity_coupon_error_record` WHERE state = 2 AND event_type = 2;"
    elif sql_name == 'check_notify_record':
        return "SELECT notify_id FROM activity_coupon_notify_record WHERE msg_state=0 AND create_time BETWEEN '" + yesterday + "'AND'" + nowtime + "';"


def warning(result, sql_name):
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=7937f9a0421492670da93a58085dc418d149672462113fbab3a65c24fa6e927c'
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)
    # Text消息@所有人
    xiaoding.send_text(msg='●【内容中心】线下监控\n' + sql_name + ',异常数据如下：\nid=' + result + '\n请检查！', is_at_all=True)
    if sql_name == 'check_invetee':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：邀请者和被邀请者为同一学员；\n(puid,invetee)=\n' + result + '\n请检查！',
                                   is_at_all=True))
    elif sql_name == 'check_repetitioncoupon':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：该学员领取到多张新生优惠券；\n(puid,number)=\n' + result + '\n请检查！',
                                   is_at_all=True))
    elif sql_name == 'check_limit':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：该学员当前可用优惠券已超30张上限；\n(puid,number)=' + result + '\n请检查！',
                                   is_at_all=True))
    elif sql_name == 'check_cancelnotify':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：作废真实优惠券失败超过3次；\n(event_data)=' + result + '\n请检查！',
                                   is_at_all=True))
    elif sql_name == 'check_exchangenotify':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：虚拟优惠券变动通知失败超过3次；\n(event_data)=' + result + '\n请检查！',
                                   is_at_all=True))
    elif sql_name == 'check_notify_record':
        return (xiaoding.send_text(msg='●【老带新】线下监控\n异常情况：业务方通知状态和业务方接口返回的状态不一致；\n(event_data)=' + result + '\n请检查！',
                                   is_at_all=True))
    else:
        return (
            xiaoding.send_text(msg='●【内容中心】线下监控\n' + sql_name + ',异常数据如下：\nid=' + result + '\n请检查！', is_at_all=True))


def index(request):
    return render(request, 'monitor/index.html')


def content_center_monitor(request):
    sql_list = ['article表content_url为空', 'material表duration为空', 'article表content_url带空格', 'material表url带空格']
    for sql_name in sql_list:
        result = create_sql(sql_name, 'mysql_content_center')
        if len(result) == 0:
            print(True)
        else:
            warning(result, sql_name)
            return HttpResponse('提交成功，请查看钉钉报警！')


def activity_monitor(request):
    sql_list = ['check_invetee', 'check_repetitioncoupon', 'check_limit', 'check_cancelnotify', 'check_exchangenotify',
                'check_notify_record']
    for sql_name in sql_list:
        result = create_sql(sql_name, 'mysql_activity')
        if len(result) == 0:
            print(True)
        else:
            warning(result, sql_name)
            return HttpResponse('提交成功，请查看钉钉报警！')

#
# def get_log_data(request):
#     return HttpResponse('获取成功')

#! /usr/bin/python
# coding:utf-8



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

# def get_log_data(request):
#     fd = '/Users/beartwo/Documents/lmh/anyproxy/anyproxy_data/data.json'
#     with open(fd, 'r') as a:
#         log_data = a.readlines()
#         for test_dic in log_data:
#             test_dic1 = eval(test_dic)
#             reponsedata_event_id = get_target_value('event_id', test_dic1, [])
#             reponsedata_content_type = get_target_value('content_type', test_dic1, [])
#             reponsedata_teacher_id = get_target_value('teacher_id', test_dic1, [])
#             reponsedata_search_type = get_target_value('search_type', test_dic1, [])
#             reponsedata_content = get_target_value('content', test_dic1, [])
#             reponsedata_query = get_target_value('query', test_dic1, [])
#             reponsedata_location_id = get_target_value('location_id', test_dic1, [])
#             reponsedata_page = get_target_value('page', test_dic1, [])
#             reponsedata_sug = get_target_value('sug', test_dic1, [])
#             reponsedata_word = get_target_value('word', test_dic1, [])
#             reponsedata_package_id = get_target_value('package_id', test_dic1, [])
#
#             dict = {'event_id': reponsedata_event_id[0], 'content_type': reponsedata_content_type,
#                     'teacher_id': reponsedata_teacher_id,
#                     'search_type': reponsedata_search_type, 'content': reponsedata_content, 'query': reponsedata_query,
#                     'location_id': reponsedata_location_id, 'page': reponsedata_page, 'sug': reponsedata_sug,
#                     'word': reponsedata_word,
#                     'package_id': reponsedata_package_id}
#
#             if '11-002-026' in dict.values() or '11-002-027' in dict.values() or '11-002-028' in dict.values() or '11-002-024' \
#                     in dict.values() or '11-041-010' in dict.values() or '11-045-001' in dict.values():
#                 print(dict)
#                 #return render(request, 'log_index.html', {'dict': dict})
#
#             else:
#                 pass
#         return HttpResponse(str(dict))

def get_log_data(request):
    return render(request, 'monitor/log_index.html')

