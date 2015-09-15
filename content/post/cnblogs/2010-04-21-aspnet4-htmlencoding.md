---
categories:
- 技术文章
date: '2010-04-21'
title: ASP.NET4.0新的语法用于HTML Encoding
url: /2010/04/21/aspnet4-htmlencoding/

---


从ScottGu大神那里看到的，ASP.NET4.0启用新的<span style="color: #0000ff;">&lt;%: %&gt;</span>语法用于HTML编码。Html Encoding的一般用于防止跨站攻击(XSS)，详情可以参考我之前写过的一篇文章：[http://www.cnblogs.com/coderzh/archive/2008/09/06/1285500.html](http://www.cnblogs.com/coderzh/archive/2008/09/06/1285500.html)。

之前的做法是：
  <div class="cnblogs_code"><div><span style="color: #000000; background-color: yellow;">&lt;%=</span><span style="color: #000000;">&nbsp;Server.HtmlEncode(value)&nbsp;</span><span style="color: #000000; background-color: yellow;">%&gt;</span></div></div>  
<br />
如果value已经被Html Encode过一次的话，再调用Server.HtmlEncode会得到非预期的值。
<br />
新的&lt;%: %&gt;语法解决了这个问题，使用起来也非常的简单。
  <div class="cnblogs_code"><div><span style="color: #000000; background-color: yellow;">&lt;%</span><span style="color: #000000; background-color: yellow;">:</span><span style="color: #000000;">&nbsp;value&nbsp;</span><span style="color: #000000; background-color: yellow;">%&gt;</span></div></div>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/04/21/aspnet4-htmlencoding.html](http://www.cnblogs.com/coderzh/archive/2010/04/21/aspnet4-htmlencoding.html)**