---
categories:
- 技术文章
date: '2010-09-12'
title: 发布基于GAE的个人Wiki系统 - NancyWiki
url: /2010/09/12/nancywiki/

---


#### 介绍

一个周末的时间，我写了这个Wiki系统。[](http://wiki.coderzh.com/)[NancyWiki](http://wiki.coderzh.com/)是基于[](http://appengine.google.com/)[](http://appengine.google.com/)[Google App Engine](http://appengine.google.com/)开发的，使用的语言是Python。Wiki标记语言采用的是Markdown，因为它简单，易用。

<div class="important">NancyWiki致力于打造用户真正想要的个人Wiki系统。多看书，多学习，多记笔记，就用NancyWiki！ </div>

NancyWiki尊崇的原则：尽量保持简单，实用。NancyWiki保持了代码的精简，一共3个python文件：main.py, models.py, views.py。同时，提供了完善的换肤功能，让用户更加简单的DIY自己的Wiki皮肤，现themes目录提供了simple和plain两套皮肤，可以在设置页面随时进行切换。

#### 试用

NancyWiki提供了一个[](http://wiki.coderzh.com/demo)[](http://wiki.coderzh.com/demo)[Demo](http://wiki.coderzh.com/demo)页面，任何人都可以对这个页面进行编辑。心动不如行动，赶紧[体验](http://wiki.coderzh.com/demo)一下吧。

#### 下载

NancyWiki是开放所有源代码的，任何人下载源码，申请一个[Google App Engine](http://appengine.google.com/)账号，就可以部署完全属于自己的Wiki系统。

Google Code主页: [http://code.google.com/p/nancywiki/](http://code.google.com/p/nancywiki/)

下载1.0.1稳定版本：[http://nancywiki.googlecode.com/files/nancywiki1.0.1.zip](http://nancywiki.googlecode.com/files/nancywiki1.0.1.zip)

获取最新代码：

<div class="cnblogs_code">
<div><span style="color: #000000;">hg&nbsp;clone&nbsp;https:</span><span style="color: #000000;">//</span><span style="color: #000000;">nancywiki.googlecode.com</span><span style="color: #000000;">/</span><span style="color: #000000;">hg</span><span style="color: #000000;">/</span><span style="color: #000000;">&nbsp;nancywiki</span></div></div>

#### 
安装
  
[](http://disqus.com/)[](http://disqus.com/)

下载了源码后，打开app.yaml文件，修改application字段为你的GAE应用的名称：&nbsp; 

<div class="cnblogs_code"><div><span style="color: #000000;">application:&nbsp;yourappname</span></div></div>
<br />
然后，由于NancyWiki本身不提供评论系统（简单原则），而是在模板里挂接[Disqus](http://disqus.com/)的评论系统。因此，如果想使用Disqus评论系统，请先注册一个[Disqus](http://disqus.com/)账号，然后学习一下用法。待你了解差不多之后，回过头来，修改一下wiki.html模板中的评论部分的代码为你自己的Disqus代码。 
<br />
<div class="cnblogs_code">
<div><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">div&nbsp;</span><span style="color: #ff0000;">id</span><span style="color: #0000ff;">="comments"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">div&nbsp;</span><span style="color: #ff0000;">id</span><span style="color: #0000ff;">="disqus_thread"</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">div</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">script&nbsp;</span><span style="color: #ff0000;">type</span><span style="color: #0000ff;">="text/javascript"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000; background-color: #f5f5f5;">
</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disqus_developer&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">=</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">1</span><span style="color: #000000; background-color: #f5f5f5;">;
</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(</span><span style="color: #0000ff; background-color: #f5f5f5;">function</span><span style="color: #000000; background-color: #f5f5f5;">()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff; background-color: #f5f5f5;">var</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;dsq&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">=</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;document.createElement(</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">script</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">);&nbsp;dsq.type&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">=</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">text/javascript</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">;&nbsp;dsq.async&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">=</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;</span><span style="color: #0000ff; background-color: #f5f5f5;">true</span><span style="color: #000000; background-color: #f5f5f5;">;
</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dsq.src&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">=</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">http://nancywiki.disqus.com/embed.js</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">;
</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(document.getElementsByTagName(</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">head</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">)[</span><span style="color: #000000; background-color: #f5f5f5;">0</span><span style="color: #000000; background-color: #f5f5f5;">]&nbsp;</span><span style="color: #000000; background-color: #f5f5f5;">||</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;document.getElementsByTagName(</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">body</span><span style="color: #000000; background-color: #f5f5f5;">'</span><span style="color: #000000; background-color: #f5f5f5;">)[</span><span style="color: #000000; background-color: #f5f5f5;">0</span><span style="color: #000000; background-color: #f5f5f5;">]).appendChild(dsq);
</span><span style="color: #000000; background-color: #f5f5f5;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;})();
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">noscript</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">Please&nbsp;enable&nbsp;JavaScript&nbsp;to&nbsp;view&nbsp;the&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">a&nbsp;</span><span style="color: #ff0000;">href</span><span style="color: #0000ff;">="http://disqus.com/?ref_noscript=nancywiki"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">comments&nbsp;powered&nbsp;by&nbsp;Disqus.</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">a</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">noscript</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">div</span><span style="color: #0000ff;">&gt;</span></div></div>

&nbsp;配置完了，上传： 

<div class="cnblogs_code">
<div><span style="color: #000000;">python&nbsp;appcfg.py&nbsp;update&nbsp;yourappname</span></div></div>

太棒了，赶紧体验一下吧，访问：http://yourappname.appspot.com/

#### 
使用

<div>

*   新建页面

在浏览器的地址栏里输入任意不存在的地址，将会创建一个默认的页面（实际并未写入数据库），点击**编辑**按钮，进入页面的编辑页面。或者，先编辑页面内容中的地址超链接，通过点击超链接创建新页面。 `[New Page](link)` 效果：[New Page](http://wiki.coderzh.com/link)

*   编辑页面

点击**编辑**按钮，进入传说中的_所想即所得_编辑界面。为了方便编写Markdown内容，我使用了[wmd](http://www.wmd-editor.com/)（The Wysiwym Markdown Editor）编辑器。可以用鼠标，正所谓：所点即所想，所想即所得。你在编辑的任何时候，都可以即时的查看到预览的效果。（就在编辑页面的下方）。更多Markdown语法，详见：[http://en.wikipedia.org/wiki/Markdown](http://en.wikipedia.org/wiki/Markdown)

*   删除页面

我不提供删除页面功能，如果这个页面当初不需要，为什么创建出来呢？既然已经来到了人世，何不改头换面呢？

*   设置

设置页面，可以设置网站的标题，谷歌搜索的域名（由于GAE拒不提供like语法，只能借助Google搜索），Wiki皮肤。</div>

#### 
截图

### ![](http://images.cnblogs.com/cnblogs_com/coderzh/nancywiki/nancywiki.jpg)

&nbsp;

 我的个人Wiki：[http://wiki.coderzh.com](http://wiki.coderzh.com/)

体验地址：[http://wiki.coderzh.com/demo](http://wiki.coderzh.com/demo)

&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/09/12/nancywiki.html](http://www.cnblogs.com/coderzh/archive/2010/09/12/nancywiki.html)**