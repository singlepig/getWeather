#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib2, httplib
from BeautifulSoup import BeautifulSoup

def getIpAddr():
    '''从http://www.ip.cn网站获取外网ip和地理位置'''
    url = 'http://www.ip.cn'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    # 通过<div class="well">标签找到位置信息
    find_div = soup.find('div',{'class':'well'})
    ip = find_div.code.next
    # 定位地理位置信息
    # <p>GeoIP: Nanjing, Jiangsu, China</p>
    addr = find_div.contents[1].next
    # 得到拼音字符串，然后进行分割,得到addr列表
    addr = addr.split(':')
    # addr取原列表中的最后一个元素
    addr = addr[-1]
    # 将包含位置信息的字符串用','再次分割，得到城市、省份
    addr = addr.split(',')
    # 去除字符串两边多余的空格
    print ip
    for n in range(len(addr)):
        addr[n] = addr[n].strip()
        print addr[n]
    return [ip, addr]

if __name__ == '__main__':
    getIpAddr()

