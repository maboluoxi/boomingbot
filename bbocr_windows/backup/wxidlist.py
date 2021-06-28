#!/usr/bin/env python2
#-*- coding:utf-8 -*-
if __name__ == '__main__':
    with open('wxidlist.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            wx_id = l.split(' ')[8][1:-2]
            print wx_id
