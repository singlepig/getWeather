# xml接口

1. 全国 xml 接口  
    http://flash.weather.com.cn/wmaps/xml/china.xml
    
2. 省级 xml 接口：包含省内各市的相关信息  
    http://flash.weather.com.cn/wmaps/xml/省拼音.xml  
    以江苏省为例：
```
<jiangsu dn="nay">
<city cityX="119.25" cityY="139.85" cityname="徐州" centername="徐州" fontColor="FFFFFF" pyName="xuzhou" state1="0" state2="0" stateDetailed="晴" tem1="-4" tem2="8" temNow="-1" windState="西风3-4级" windDir="北风" windPower="0级" humidity="42%" time="19:10" url="101190801"/>
<city cityX="267" cityY="90" cityname="连云港" centername="连云港" fontColor="FFFFFF" pyName="lianyungang" state1="0" state2="1" stateDetailed="晴转多云" tem1="-4" tem2="8" temNow="2" windState="西南风转西风3-4级" windDir="西南风" windPower="2级" humidity="30%" time="19:10" url="101191001"/>
<city cityX="227" cityY="175" cityname="宿迁" centername="宿迁" fontColor="FFFFFF" pyName="suqian" state1="0" state2="0" stateDetailed="晴" tem1="-2" tem2="8" temNow="2" windState="西风转西北风3-4级" windDir="西南风" windPower="1级" humidity="39%" time="19:10" url="101191301"/>
<city cityX="279" cityY="190" cityname="淮安" centername="淮安" fontColor="FFFFFF" pyName="huaian" state1="0" state2="0" stateDetailed="晴" tem1="-3" tem2="9" temNow="1" windState="西南风3-4级" windDir="南风" windPower="2级" humidity="45%" time="19:10" url="101190901"/>
<city cityX="360" cityY="169" cityname="盐城" centername="盐城" fontColor="FFFFFF" pyName="yancheng" state1="0" state2="0" stateDetailed="晴" tem1="-2" tem2="8" temNow="1" windState="西风3-4级" windDir="南风" windPower="2级" humidity="48%" time="19:10" url="101190701"/>
<city cityX="318.7" cityY="294.85" cityname="扬州" centername="扬州" fontColor="FFFFFF" pyName="yangzhou" state1="0" state2="0" stateDetailed="晴" tem1="-3" tem2="11" temNow="4" windState="西南风转西风3-4级" windDir="西南风" windPower="1级" humidity="25%" time="19:00" url="101190601"/>
<city cityX="366" cityY="269" cityname="泰州" centername="泰州" fontColor="FFFFFF" pyName="taizhou" state1="0" state2="1" stateDetailed="晴转多云" tem1="-3" tem2="8" temNow="1" windState="西风3-4级" windDir="南风" windPower="2级" humidity="59%" time="19:00" url="101191201"/>
<city cityX="278" cityY="343" cityname="南京" centername="南京" fontColor="FFFF00" pyName="nanjing" state1="0" state2="0" stateDetailed="晴" tem1="-2" tem2="11" temNow="3" windState="西南风转西风3-4级" windDir="西风" windPower="2级" humidity="32%" time="19:10" url="101190101"/>
<city cityX="328" cityY="339" cityname="镇江" centername="镇江" fontColor="FFFFFF" pyName="zhenjiang" state1="0" state2="0" stateDetailed="晴" tem1="-2" tem2="10" temNow="3" windState="西风3-4级" windDir="西南风" windPower="2级" humidity="38%" time="19:10" url="101190301"/>
<city cityX="450" cityY="297" cityname="南通" centername="南通" fontColor="FFFFFF" pyName="nantong" state1="0" state2="1" stateDetailed="晴转多云" tem1="-2" tem2="9" temNow="3" windState="西风3-4级" windDir="西南风" windPower="1级" humidity="39%" time="19:00" url="101190501"/>
<city cityX="338" cityY="380" cityname="常州" centername="常州" fontColor="FFFFFF" pyName="changzhou" state1="0" state2="0" stateDetailed="晴" tem1="-2" tem2="10" temNow="3" windState="西风3-4级" windDir="西南风" windPower="2级" humidity="34%" time="19:10" url="101191101"/>
<city cityX="400" cityY="386" cityname="无锡" centername="无锡" fontColor="FFFFFF" pyName="wuxi" state1="1" state2="1" stateDetailed="多云" tem1="-2" tem2="9" temNow="1" windState="西南风3-4级" windDir="北风" windPower="0级" humidity="42%" time="19:10" url="101190201"/>
<city cityX="450" cityY="388" cityname="苏州" centername="苏州" fontColor="FFFFFF" pyName="suzhou" state1="0" state2="0" stateDetailed="晴" tem1="0" tem2="9" temNow="1" windState="西南风转西风3-4级" windDir="南风" windPower="1级" humidity="48%" time="19:00" url="101190401"/>
</jiangsu>
```
3. 县级市 xml 接口：包含市内各区的相关信息  
    http://flash.weather.com.cn/wmaps/xml/市拼音.xml  
    县级市中每个市有url号码  
    以南京市为例：
```
<nanjing dn="day">
<city cityX="299" cityY="86" cityname="六合" centername="六合" fontColor="FFFFFF" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="6" tem2="-4" temNow="-1" windState="西风转西南风3-4级" windDir="西风" windPower="1级" humidity="59%" time="09:20" url="101190105"/>
<city cityX="241" cityY="224" cityname="浦口" centername="浦口" fontColor="FFFFFF" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="7" tem2="-3" temNow="1" windState="西风转西南风3-4级" windDir="南风" windPower="1级" humidity="47%" time="09:20" url="101190107"/>
<city cityX="303" cityY="190" cityname="南京市" centername="南京市" fontColor="FFFF00" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="7" tem2="-3" temNow="1" windState="西风转西南风3-4级" windDir="北风" windPower="1级" humidity="53%" time="09:20" url="101190101"/>
<city cityX="316" cityY="274" cityname="江宁" centername="江宁" fontColor="FFFFFF" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="7" tem2="-3" temNow="1" windState="西风转西南风3-4级" windDir="北风" windPower="1级" humidity="53%" time="09:20" url="101190104"/>
<city cityX="380" cityY="341" cityname="溧水" centername="溧水" fontColor="FFFFFF" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="7" tem2="-2" temNow="1" windState="西风转西南风3-4级" windDir="西南风" windPower="1级" humidity="55%" time="09:20" url="101190102"/>
<city cityX="371" cityY="419" cityname="高淳" centername="高淳" fontColor="FFFFFF" pyName="" state1="0" state2="0" stateDetailed="晴" tem1="7" tem2="-2" temNow="1" windState="西风转西南风3-4级" windDir="西南风" windPower="1级" humidity="49%" time="09:20" url="101190103"/>
</nanjing>
```


# json接口
1. 详细天气 json 接口  
    'http://m.weather.com.cn/data/' + url号码 + '.html'  
    以南京为例：
```
{"weatherinfo":{"city":"南京","city_en":"nanjing","date_y":"2013年12月29日","date":"","week":"星期日","fchh":"11","cityid":"101190101","temp1":"7℃~-4℃","temp2":"11℃~-1℃","temp3":"13℃~1℃","temp4":"14℃~2℃","temp5":"15℃~3℃","temp6":"14℃~2℃","tempF1":"44.6℉~24.8℉","tempF2":"51.8℉~30.2℉","tempF3":"55.4℉~33.8℉","tempF4":"57.2℉~35.6℉","tempF5":"59℉~37.4℉","tempF6":"57.2℉~35.6℉","weather1":"晴","weather2":"晴","weather3":"晴","weather4":"多云","weather5":"多云转阴","weather6":"阴转多云","img1":"0","img2":"99","img3":"0","img4":"99","img5":"0","img6":"99","img7":"1","img8":"99","img9":"1","img10":"2","img11":"2","img12":"1","img_single":"0","img_title1":"晴","img_title2":"晴","img_title3":"晴","img_title4":"晴","img_title5":"晴","img_title6":"晴","img_title7":"多云","img_title8":"多云","img_title9":"多云","img_title10":"阴","img_title11":"阴","img_title12":"多云","img_title_single":"晴","wind1":"西风转西南风3-4级","wind2":"西风4-5级转3-4级","wind3":"西风4-5级转3-4级","wind4":"西南风转南风3-4级","wind5":"西风转西北风3-4级","wind6":"北风转西北风3-4级","fx1":"西风","fx2":"西南风","fl1":"3-4级","fl2":"4-5级转3-4级","fl3":"4-5级转3-4级","fl4":"3-4级","fl5":"3-4级","fl6":"3-4级","index":"冷","index_d":"天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。","index48":"冷","index48_d":"天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。","index_uv":"中等","index48_uv":"中等","index_xc":"适宜","index_tr":"一般","index_co":"较舒适","st1":"6","st2":"-3","st3":"9","st4":"0","st5":"12","st6":"0","index_cl":"较不宜","index_ls":"基本适宜","index_ag":"极不易发"}}
```


2. 实况天气 json 接口  
    'http://www.weather.com.cn/data/sk/' + url号码 + '.html'  
    以南京为例：
```
{"weatherinfo":{"city":"南京","cityid":"101190101","temp":"4","WD":"西南风","WS":"2级","SD":"30%","WSE":"2","time":"17:45","isRadar":"1","Radar":"JC_RADAR_AZ9250_JB"}}
```
