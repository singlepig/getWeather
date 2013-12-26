#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib2, httplib
from BeautifulSoup import BeautifulSoup

def getIpAddr():
    '''从http://www.ip.cn网站获取外网ip和地理位置'''
    url = 'http://www.ip.cn'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    # 分析http://www.ip.cn的源码，发现ip被<code>唯一包含，
    # 所以通过find('code')进行解析，如果不唯一，可以找出所有，然后筛选
    ip = soup.find('code').next #next用于去掉标签<code>
    # 通过<p>标签找到位置信息
    find_p = soup.find('p')
    # 将beautifulsoup对象转换成字符串
    str_find_p = str(find_p)
    # 定位地理位置信息
    position = str_find_p.find(';')
    # uft-8里中文占3字节，str()之后的结果一个字节是一个下标
    # <p>当前 IP：<code>218.94.124.47</code>&nbsp;来自：江苏省南京市 电信</p>
    # 来自： 各占3个下表，从江字开始，所以是position + 10
    addr = str_find_p[position + 10:-4]
    print ip
    print addr
    return [ip, addr]

if __name__ == '__main__':
    getIpAddr()

