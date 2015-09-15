---
categories:
- 技术文章
date: '2010-07-18'
title: Chrome默认字体太小解决办法
url: /2010/07/18/chrome-minimum-font-size/

---


当网站的字体为12px时，在Chrome里显示的非常小，看起来非常的吃力。修改的方法：

1. 务必先关闭你的Chrome浏览器。（不先关闭的话，修改可能会被覆盖掉）

2. 最好再备份一下配置文件，如果配置文件搞坏了会很惨：
<div class="cnblogs_code"><div><span style="color: #000000;">cd&nbsp;.config</span><span style="color: #000000;">/</span><span style="color: #000000;">google</span><span style="color: #000000;">-</span><span style="color: #000000;">chrome</span><span style="color: #000000;">/</span><span style="color: #000000;">Default
cp&nbsp;Preferences&nbsp;Preferences.bak</span><span class="Apple-style-span" style="font-family: verdana,'courier new';">&nbsp;</span></div></div>

3. 修改Preferences文件
<div class="cnblogs_code"><div><span style="color: #000000;">gedit&nbsp;Preferences</span></div></div>
<br />
&nbsp;&nbsp; &nbsp;找到:
<div class="cnblogs_code"><div><span>"</span><span>webkit</span><span>"</span><span>:&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>webprefs</span><span>"</span><span>:&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>default_fixed_font_size</span><span>"</span><span>:&nbsp;</span><span>16</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>default_font_size</span><span>"</span><span>:&nbsp;</span><span>17</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>fixed_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u7B49.5BBD\u5FAE\u7C73.9ED1</span><span>"</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>sansserif_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u5FAE\u7C73.9ED1</span><span>"</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>serif_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u5FAE\u7C73.9ED1</span><span>"</span><span style="color: #000000;">
</span><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
</span><span>}</span></div></div>

&nbsp;&nbsp; &nbsp;加上<span style="color: #ff0000;">"minimum_font_size": 15,</span>
<div class="cnblogs_code"><div><span>"</span><span>webkit</span><span>"</span><span>:&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>webprefs</span><span>"</span><span>:&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>default_fixed_font_size</span><span>"</span><span>:&nbsp;</span><span>16</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>default_font_size</span><span>"</span><span>:&nbsp;</span><span>17</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>fixed_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u7B49.5BBD\u5FAE\u7C73.9ED1</span><span>"</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #ff0000;">**"**</span><span style="color: #ff0000;">**minimum_font_size**</span><span style="color: #ff0000;">**"**</span><span style="color: #ff0000;">**:&nbsp;**</span><span style="color: #ff0000;">**15**</span><span style="color: #ff0000;">**,**</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>sansserif_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u5FAE\u7C73.9ED1</span><span>"</span><span>,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>"</span><span>serif_font_family</span><span>"</span><span>:&nbsp;</span><span>"</span><span>\u6587.6CC9.9A7F\u5FAE\u7C73.9ED1</span><span>"</span><span style="color: #000000;">
</span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">&nbsp;&nbsp;}
}</span></div></div>

4. 保存退出。启动Chrome，字体变大了。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/07/18/chrome-minimum-font-size.html](http://www.cnblogs.com/coderzh/archive/2010/07/18/chrome-minimum-font-size.html)**