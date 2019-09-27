#!usr/bin/python
# -*- coding: utf-8 -*-
# author: 李爽
# description：
import uuid
from flask import Flask, Blueprint, render_template, request
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


login_bp = Blueprint('login', __name__)
register_bp = Blueprint('register', __name__)
send_sms_bp = Blueprint('send_sms', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    return 'login'


@register_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        telephone = request.form['telephone']
        password = request.form['password']
    return 'sd'


@send_sms_bp.route('/send', methods=['POST'])
def send_sms_code():
    '''
    发送短信验证码，待完成
    :return:
    '''
    # client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')
    #
    # request = CommonRequest()
    # request.set_accept_format('json')
    # request.set_domain('dysmsapi.aliyuncs.com')
    # request.set_method('POST')
    # request.set_protocol_type('https')  # https | http
    # request.set_version('2017-05-25')
    # request.set_action_name('SendSms')
    #
    # request.add_query_param('RegionId', "cn-hangzhou")
    # request.add_query_param('PhoneNumbers', "18645402819")
    # request.add_query_param('SignName', "黑龙江第一火腿")
    # request.add_query_param('TemplateCode', "SMS_164470164")
    # request.add_query_param('TemplateParam', "{\"code\":\"1111\"}")
    #
    # response = client.do_action(request)
    # # python2:  print(response)
    # print(str(response, encoding='utf-8'))
