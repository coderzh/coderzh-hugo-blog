---
categories:
- 技术文章
date: 2015-11-14T19:36:38+08:00
keywords:
- http 劫持
title: "网站被随机挂广告，疑似被 HTTP 劫持"
url: "/2015/11/14/http-dns-hijack/"

---

最近发现我的博客网站随机的会在右下角出现一个 google 的广告，郁闷至极，我的博客网站根本没有任何广告。于是今天特意去查了查，这广告到底从何而来。

<!--more-->

## 现象

首先，广告长这样：

![blogads](http://7xlx3k.com1.z0.glb.clouddn.com/blogads.jpg)

太可恨了！我的网站是 [http://blog.coderzh.com/](http://blog.coderzh.com/)， 检查了网站的源文件，没有被修改的痕迹，也根本不会有什么广告代码。所以怀疑是被运营商劫持了！

我使用的是广州电信100M光纤，被挂广告只有在家里上电信光纤时会出现，连手机里访问也会有广告：

![phoneads](http://7xlx3k.com1.z0.glb.clouddn.com/phoneads.jpg)

但是如果手机连的是联通4G，就没有一点问题！

后来在追查过程中，发现遇到这个问题的不止我一个人，比如，云风在他的新浪微博里说到：

[http://weibo.com/2388714105/D2013qUSo?type=comment#_rnd1447506909896](http://weibo.com/2388714105/D2013qUSo?type=comment#_rnd1447506909896)

![yunfengads](http://7xlx3k.com1.z0.glb.clouddn.com/yunfengads.jpg-ws)

另一个博主也遇到这个问题：[网站被黑了随机挂ca-pub-8129816473729933的google广告，怎么办？](http://www.lovefcwr.com/20151110-google-ca-pub-8129816473729933)

还有一个用户在 Google Adsens 也举报了这个广告主：[Please help us to stop this Google Adsense user ](https://productforums.google.com/forum/#!topic/adsense/qeeYrD7kvUA;context-place=forum/adsense)

## 初步分析

这个问题出现在最近1，2个月，被插入广告的都属于同一个广告主：ca-pub-8129816473729933 。

很多网站广告插入的方式和表现是完全一致的。广告隔断时间会出现一次，刷新网页后就消失了。

我和云风使用的宽带都是广州电信！（我手机换成联通移动 4G 就没问题。）

所以，不得不怀疑是电信做了手脚，对访问的网站进行了劫持！电信也不是第一次做 **HTTP 劫持** 这种事。

于是，我捕捉了一些现场证据，分析了劫持的脚本和基本原理，然后拨通了中国电信 10000 号。

## 10000 号
电信工作人员矢口否认进行了 HTTP 劫持，把原因归咎到电脑是否中毒了，WIFI 路由器被做了手脚等等。我说我的电脑杀过毒并没有问题，不仅电脑，iPhone 手机访问网页也会被嵌入广告，你是说我的 iPhone 也中毒了吗？而且切换成联通 4G 就没有问题，你说和你们没关系？ WIFI 路由器我也试了把 DNS 设置成各种不同的，包括默认的，甚至把路由器恢复出厂设置，通通没用！

最后他说可能和我拨号分配到的 IP 是内网 IP有关，帮我恢复到公网 IP 试试。 What ! 难道我的网络之前一直属于你们的局域网？？不应该默认就是公网 IP 吗？？

然而，切换公网 IP 后也并没有什么用！（中间还出现切换出错，导致我几个小时拨号不成功上不了网，哭了~~）

打 10000 号目前还未解决问题，解决不了去工信部投诉去。

## 深入分析

访问一个网站，网站的内容都是被恶意篡改过的，这多么可怕。

于是在 Chrome 里 “审查元素”里跟踪了一下，看看到底是如何篡改的。通过查看 Elements ，发现 html 里被嵌入了以下代码：

![adjs2](http://7xlx3k.com1.z0.glb.clouddn.com/adsjs2.jpg-w)

picturefill.min.js 是我网站使用的一个正常的 js 文件，查看网页源码发现，出现了两条关于 picturefill.min.js 的代码：

```javascript
<script type="text/javascript" src="assets/picturefill/picturefill.min.js"></script>
<script src="http://blog.coderzh.com/assets/picturefill/picturefill.min.js?_Ax144746802655173=xxA.baidu.com"></script>
```

然后再查看请求 picturefill.min.js 时返回了什么：

![fakejs](http://7xlx3k.com1.z0.glb.clouddn.com/fakejs.jpg-w)

![rightjs](http://7xlx3k.com1.z0.glb.clouddn.com/rightjs.jpg-w)

上面显示，请求 picturefill.min.js 时，返回的竟然是被篡改的内容，被篡改的内容里，先是再次请求了一次原版的 picturefill.min.js ，然后就是插入 google 的广告代码。

从 google 的广告代码看出，广告主的 ID 是：ca-pub-8129816473729933 ， 正是和云风及之前一位博主说到的广告主是同一个！ Google 你还不赶紧查查他！

最后这段恶意篡改的 js 代码生成出来的嵌入广告是这样的：

![adjs](http://7xlx3k.com1.z0.glb.clouddn.com/adsjs.jpg-w)

之后又试验了多次，总结了进行 HTTP 劫持的基本套路：

 1. 劫持任一 js 的请求，返回包含原 js 及恶意代码的假的 js 内容。
 1. 假的 js 通过 DOM 操作，强行在原来的网页内植入广告。

这种恶意修改 DOM 的方式，和之前常见的把原网站套入一个 iframe 的方式有所不同。基本很难防范。

## 解决方法

打 10000 号，投诉，投诉，再投诉。

工信部投诉地址：[http://www.chinatcc.gov.cn:8080/cms/shensus/](http://www.chinatcc.gov.cn:8080/cms/shensus/)

为了找出哪一层路由做了手脚，大家通过 traceroute ( Windows 里是 tracert ) 看看访问被植入广告的网站到底经过哪些路由。下面是我的 tracert 结果：

```bash
D:\Code\Go\coderzh-hugo-blog>tracert blog.coderzh.com

通过最多 30 个跃点跟踪
到 github.map.fastly.net [103.245.222.133] 的路由:

  1    <1 毫秒   <1 毫秒   <1 毫秒 192.168.0.1
  2    12 ms     2 ms     1 ms  113.109.112.1
  3     3 ms     3 ms     3 ms  183.56.38.209
  4     5 ms     3 ms     3 ms  183.56.30.21
  5     9 ms     8 ms     8 ms  202.97.34.114
  6     9 ms     8 ms     7 ms  202.97.34.74
  7   156 ms   158 ms   156 ms  202.97.60.214
  8   158 ms   168 ms   166 ms  ae-1.r30.tokyjp05.jp.bb.gin.ntt.net [129.250.2.157]
  9   164 ms   176 ms   175 ms  ae-17.r01.tokyjp03.jp.bb.gin.ntt.net [129.250.6.117]
 10     *        *        *     请求超时。
 11   164 ms   164 ms   163 ms  103.245.222.133

跟踪完成。
```

假如你不是对一个网站很熟悉，你压根发现不了这广告根本不是网站主投放的。

这种强行修改你访问网页的内容来植入广告的方式，非常可怕。使得我们在上网的时候没有一点安全感。如果你访问一个网站，都不能保证获取到的内容是该网站原版的内容，而是被肆意的插入广告，被修改的内容。那么之后他很可能会骗取你的账号密码，偷走你的隐私，拿走你的存款，这是多么可怕和不可接受的事。