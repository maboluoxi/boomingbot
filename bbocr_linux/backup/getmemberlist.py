#!/usr/bin/env python2
#-*- coding:utf-8 -*-
#import pdb
#pdb.set_trace()

import itchat
from itchat.content import *

itchat.auto_login(hotReload='True')

# 找到目标群组
roomslist = itchat.get_chatrooms(update=True)
for r in roomslist:
    # print r['NickName']
    if r['NickName'] == u'软件学院2020级非全日制': # 找到目标群
        chatGtoupName = r['UserName'] # 系统的群id
        # itchat.send_msg(u'hello', chatGtoupName)
        memberlist = r['MemberList']
        print r
        for m in memberlist:
            if m['DisplayName'] != null:
                print m['DisplayName']
            elif m['NickName'] != null:
                print m['NickName']
