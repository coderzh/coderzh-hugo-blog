---
categories:
- 技术文章
date: '2010-11-30'
title: Google App Engine的14宗罪
url: /2010/11/30/goodby-google-app-engine/

---


最近一位老外朋友很郁闷，使用Google App Engine平台，花了15000欧(![](http://www.cnblogs.com/Emoticons/QQ/01.gif)), 却用的很不爽。于是耐心的写了一篇《[Goodbye Google App Engine](http://www.carlosble.com/?p=719)》，引来众人围观，其中还包括Google的工程师亲临指导。我也是Google App Engine的使用者，不过我基本上是属于个人开发，从来没有超过标，不需要给美刀，用的也挺爽。不过这位老兄是正儿八经的使用GAE进行企业级工程的开发，确实把他郁闷坏了。老外说话都比较啰嗦，我帮他总结了一下他提到的GAE14宗罪，同时也加上自己的一点注释。

&nbsp;

![image](http://images.cnblogs.com/cnblogs_com/coderzh/Windows-Live-Writer/a06c36f0ed3d_930/image_thumb.png "image")

&nbsp;

#### 1. 需要Python2.5版本

Ubuntu中早已经默认不是2.5版本了，现在主流版本已经进入到2.6甚至2.7了，所以用个GAE还要再装个2.5版本，让人很不爽。

#### 2. 不支持Https

#### 3.&nbsp; 请求超过30秒将会返回失败

对于上传大数据到数据库来说，简直不可想象。迫不得已的做法是将数据分割成多个小块进行上传。多痛苦。

#### 4. 每个GET或POST请求从Server到别的地址，如果没有在5秒内完成，将会自动停止

#### 5. 不能使用基于C的Python模块

#### 6. 不支持LIKE操作

虽然有通过starts with的hack方法实现，但是和全文检索还有很大差距。可以想象，数据库中的数据不能执行条件搜索，多么不可思议。所以很多GAE站点的站内搜索都直接交给了Google Search。

#### 7. 不支持数据库表的Join操作

一般的一个小型网站，多表查询也是很常用的，GAE告诉你，俺就是不支持！

#### 8. 数据库实在太慢

所谓的BigTable到底是坑爹呢还是咋的，速度确实不敢恭维。

#### 9. 本地调试时的数据库行为和上传后不一致

本地调试指的是用dev_appserver.py在本地调试，每次本地执行好好的，单元测试也都通过的，一上传，就嗝屁了~~

#### 10. 数据库太多的索引(index)

写一个Hello World还可以，如果真的要写一个企业级应用，数据库表的字段多的很给力，基于多个字段查询时，GAE也很给力的自动给你加上很多indexs。

#### 11. 一次查询不能返回超过1000条的记录

过去我也为这个懊恼，其实现在的GAE版本已经将这个限制去掉了，为此我还和一位同学打过赌，最后我输的很惨。

#### 12. 不支持文件系统

想要操作服务器的文件系统，写个配置文件，或上传个文件？还是不要想了。

#### 13. 数据库和Memcache操作经常失败

每做一次数据库或Memcache操作，都要担心一把是否操作失败，确实闹心。

#### 14. 每个Memcache值最大为1M，Google是否想让我们把所有东西都放人Memcache？

似乎这个大哥犯了个错，Memcache通常大小限制也是1M。不过，我确实怀疑，Google的Memcache，是我们所认识的那个Memcache吗？

&nbsp;

<span style="color: red;">上面的14宗罪主要代表这个国外老兄自己的意见，同时加上了一点本人的看法，欢迎大家反驳。</span>

虽然GAE有很多限制和缺陷，但是我对GAE还是喜爱有加的。GAE是免费的，任何人都可以很轻松的通过GAE实现自己的Web应用。比如，做一些实用的小工具，实现一个博客程序来练手。通过GAE，我们可以轻松的搭建属于自己的Blog([micolog](http://micolog.xuming.net/zh-cn))，搭建属于自己的Wiki系统([NancyWiki](http://code.google.com/p/nancywiki/))。

没有GAE，就不会有大家都懂的[gappproxy](http://www.cnblogs.com/coderzh/admin/www.williamlong.info/archives/1697.html)，[gtap](http://code.google.com/p/gtap/)，[twiter-feed](http://code.google.com/p/twitter-feed/)。是的，你懂的。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/11/30/goodby-google-app-engine.html](http://www.cnblogs.com/coderzh/archive/2010/11/30/goodby-google-app-engine.html)**