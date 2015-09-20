---
categories:
- 技术文章
date: '2015-03-29'
description: ''
keywords:
- Augmented Traffic Control 网络模拟 工具
tags: []
title: Facebook网络模拟测试工具ATC使用
url: /2015/03/29/AugmentedTrafficControl/

---


就在上周，Facebook在其工程博客（[原文](https://code.facebook.com/posts/1561127100804165/augmented-traffic-control-a-tool-to-simulate-network-conditions/)）上宣布开源移动网络测试工具Augmented Traffic Control（[ATC](https://github.com/facebook/augmented-traffic-control)），我迅速试用了一番，非常不错，对手游或者其他APP的调试和测试都非常有帮助，介绍给大家。

<!--more-->

![ATC](http://7xlx3k.com1.z0.glb.clouddn.com/ATC.jpg-w)

现在已经是APP时代了，由于手机网络的特殊性，移动APP需要面临更加复杂的网络环境。在设计之初就要考虑如何应对各种网络环境，比如很高的延迟，经常丢包，频繁的断线。特别是手游，断线重连机制设计的好坏直接影响到游戏的体验。

所以，在开发过程中模拟各种网络环境进行测试变得越来越重要。在ATC出来之前，微软曾经有一个网络模拟工具NEWT（Network Emulator for Windows Toolkit），使用起来也是方便。（NEWT的诞生也蛮有意思，见：[NEWT的前世今生](http://blog.sina.com.cn/s/blog_4caedc7a0100g9y6.html)）

![NEWT](http://7xlx3k.com1.z0.glb.clouddn.com/NEWT.jpg-w)

那么，对比NEWT，ATC有些什么特点呢？

ATC有两个最吸引人的特点：

1. **在手机上通过Web界面就可以随时切换不同的网络环境。**
1. **多个手机可以连接到同一个WIFI下，相互之间模拟的网络环境各不影响。**

可以想象一下这个场景：一群程序猿和测试猴子热火朝天的在办公室忙活着，这时有一个叫ATC WiFi的热点，任何人都可以将手机连接上去，通过Web界面随意切换到各种不同的网络环境下进行调试和测试……

想想都有点小激动呢，接下来就来试用一把，感受一下ATC的威力。

ATC只能运行在Linux上，所以搭建部署稍显麻烦一些。本文将介绍在虚拟机里如何搭建ATC环境。大致有以下几个步骤：

1. VMWare装个Ubuntu系统吧（以前我常用VirtualBox，各种兼容性问题被坑惨了不敢用了）。
1. 除非你的机器有无线网卡，不然找一个USB无线网卡，用来设置WIFI热点。
1. 部署ATC

Ubuntu中设置WiFi热点功能，在系统自带的工具里可以直接开启。但是，由于是Ad-hoc模式，Android手机根本搜不到信号。所以必须设置AP模式才能让Android手机搜到。我折腾了好一阵，最后发现这篇文章最靠谱：[http://my.oschina.net/eechen/blog/227230](http://my.oschina.net/eechen/blog/227230)，照着设置一般就OK了。

接下来是部署ATC，其实也很简单，官方文档上写的也很清楚：[https://github.com/facebook/augmented-traffic-control](https://github.com/facebook/augmented-traffic-control)

首先，必须安装Python2.7以上版本，然后安装pip：

```
sudo apt-get install python-pip python-dev build-essential）
sudo pip install --upgrade pip 
```

然后，使用pip直接安装好ATC所有组件：

```
pip install atc_thrift atcd django-atc-api django-atc-demo-ui django-atc-profile-storage
```

接下来部署Django的web工程，提供手机访问并用来配置和切换网络用的。

1.使用django-admin生成一个新的django工程：

```
django-admin startproject atcui
cd atcui
```

2.修改atcui/settings.py，加入ATC相关的内容：

``` python 
INSTALLED_APPS = (
    ...
    # Django ATC API
    'rest_framework',
    'atc_api',
    # Django ATC Demo UI
    'bootstrap_themes',
    'django_static_jquery',
    'atc_demo_ui',
    # Django ATC Profile Storage
    'atc_profile_storage',
)
```

3.修改atcui/urls.py，urlpatterns 中加入atc的url页面：

``` python
...
...
from django.views.generic.base import RedirectView
 
urlpatterns = patterns('',
    ...
    # Django ATC API
    url(r'^api/v1/', include('atc_api.urls')),
    # Django ATC Demo UI
    url(r'^atc_demo_ui/', include('atc_demo_ui.urls')),
    # Django ATC profile storage
    url(r'^api/v1/profiles/', include('atc_profile_storage.urls')),
    url(r'^$', RedirectView.as_view(url='/atc_demo_ui/', permanent=False)),
)
```

4.更新一下数据库：

```
python manage.py migrate
```

**万事俱备，就差启动了……**

前面设置WiFI热点时，你还记得设置的无线网卡的名字吗？嗯，就是wlan0，这个很重要。接下来要启动网络控制的核心组件atcd，需要通过参数指定提供Wifi热点的内网用的网卡名字，外网访问的网卡名默认是eth0（如果不是也需要通过--atcd-wan指定）

```
sudo atcd --atcd-lan wlan0
```

然后，启动Django的工程：

```
sudo python manage.py runserver 0.0.0.0:8000
```

用手机连接上去试试吧。看看虚拟机的IP，比如我设置的是192.168.6.1，手机浏览器里访问：http://192.168.6.1:8000

![ATCWeb](http://7xlx3k.com1.z0.glb.clouddn.com/ATCWeb.jpg-w)

在手机的界面里，你可以分别对网络上行下行进行设置，主要设置的参数有：

1. 网络带宽（bandwidth）
1. 延迟（latency）
1. 丢包率（packet loss）
1. 错包率（corrupted packets）
1. 乱序率（packets ordering）

通过设置上面的参数，可以模拟出各种常用的网络环境，比如：2G，3G，4G，WiFi等等，同时也可以模拟一些异常情况，比如信号很差，延迟很大，丢包率高的情况。具体有哪些场景和参数设置，欢迎大家一起交流交流，下面是[Comcast](https://github.com/tylertreat/Comcast)提供的一份参数配置（国外的网络和国内的很不一样吧，仅供参考，欢迎大家修正和补充）

<table>
<thead>
<tr>
<th align="center">Name</th>
<th align="right">Latency</th>
<th align="right">Bandwidth</th>
<th align="right">Packet-loss</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">GPRS (good)</td>
<td align="right">500</td>
<td align="right">50</td>
<td align="right">2</td>
</tr>
<tr>
<td align="center">EDGE (good)</td>
<td align="right">300</td>
<td align="right">250</td>
<td align="right">1.5</td>
</tr>
<tr>
<td align="center">3G/HSDPA (good)</td>
<td align="right">250</td>
<td align="right">750</td>
<td align="right">1.5</td>
</tr>
<tr>
<td align="center">DIAL-UP (good)</td>
<td align="right">185</td>
<td align="right">40</td>
<td align="right">2</td>
</tr>
<tr>
<td align="center">DSL (poor)</td>
<td align="right">70</td>
<td align="right">2000</td>
<td align="right">2</td>
</tr>
<tr>
<td align="center">DSL (good)</td>
<td align="right">40</td>
<td align="right">8000</td>
<td align="right">0.5</td>
</tr>
<tr>
<td align="center">WIFI (good)</td>
<td align="right">40</td>
<td align="right">30000</td>
<td align="right">0.2</td>
</tr>
<tr>
<td align="center">Satellite</td>
<td align="right">1500</td>
<td align="right">-</td>
<td align="right">0.2</td>
</tr>
</tbody>
</table>
