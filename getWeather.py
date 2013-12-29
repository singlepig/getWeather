#!/usr/binenv python
# -*- coding: UTF-8 -*-

import json
import urllib2
from BeautifulSoup import BeautifulStoneSoup

import getIpAddr


def getJsonUrlNo(province, city):
    '''解析xml信息，提取city的json数据对于的url号,返回一个uncode字
符串'''
    baseUrl = 'http://flash.weather.com.cn/wmaps/xml/'
    url = baseUrl + province + '.xml'
    xml = urllib2.urlopen(url).read()
    soup = BeautifulStoneSoup(xml)
    cityList = soup.findAll('city',{'pyname':city})
    cityUrl = cityList[0]['url']
    return cityUrl  

def getJsonInfo(province, city):
    '''根据province，city参数查找city的json格式的天气信息,返回一个dict'''
    baseUrl = 'http://m.weather.com.cn/data/'
    jsonUrlNo = getJsonUrlNo(province, city)
    jsonUrl = baseUrl + jsonUrlNo + '.html'
    weatherHtml = urllib2.urlopen(jsonUrl).read()  
    weatherJSON = json.JSONDecoder().decode(weatherHtml)  
    weatherInfo = weatherJSON['weatherinfo']  
    return weatherInfo


def printDayWeather(weatherInfo):
    '''格式化输出今明后三天的天气信息'''
    print '城市：', weatherInfo['city']
    print '日期：', weatherInfo['date_y']
    print '1.今天天气:'
    print '  温度：', weatherInfo['temp1']
    print '  天气：', weatherInfo['weather1']
    print '  风速：', weatherInfo['wind1']  
    print '  紫外线：', weatherInfo['index_uv']  
    print '  穿衣指数：', weatherInfo['index_d']  
    print '2.明天天气：'  
    print '  温度：', weatherInfo['temp2']  
    print '  天气：', weatherInfo['weather2']  
    print '  风速：', weatherInfo['wind2']  
    print '  紫外线：', weatherInfo['index48_uv']  
    print '  穿衣指数：', weatherInfo['index48_d']  
    print '3.后天天气：'  
    print '  温度：', weatherInfo['temp3']  
    print '  天气：', weatherInfo['weather3']  
    print '  风速：', weatherInfo['wind3']  

if __name__ == '__main__':
    # 获取基于ip的地理位置
    location = getIpAddr.getIpAddr()
    city, province = location[0].lower(), location[1].lower()
    dayInfo = getJsonInfo(province, city)
    # 输出全天天气
    printDayWeather(dayInfo)
    
