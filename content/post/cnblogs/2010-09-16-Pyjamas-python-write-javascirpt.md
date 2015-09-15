---
categories:
- 技术文章
date: '2010-09-16'
title: Pyjamas - 用python代替javascript编写基于浏览器的应用
url: /2010/09/16/Pyjamas-python-write-javascirpt/

---


如果能用python代替Javascript编写基于浏览器的应用，该有多好啊。但是，Javascript是唯一一种能在浏览器里执行的语言（Flash或Silverlight除外）。换个思路，先用Python编写代码，然后在通过编译器转为为Javascript脚本，这样确实是可行的。嗯，已经有人这么干了，就是这个：[Pyjamas
](http://pyjs.org/)

#### Pyjamas的介绍：

Google 的 Web Toolkit (GWT) 让我们能够完全用 Java&#8482; 代码开发具有 Ajax 功能的 Rich Internet  Application (RIA)。可以使用丰富的 Java 工具集（IDE、重构、代码补全、调试器等等）开发出可以部署在所有主流 Web  浏览器中的应用程序。在 GWT 的帮助下，可以编写出在浏览器中运行但是表现与桌面应用程序相似的应用程序。 

和GWT类似，Pyjamas是一个跨浏览器API，有了它，你可以使用Python编写客户端功能。  使用Pyjamas的优点是你可以用 Python代替HTML和JavaScript编写网络程序，你可以重复使用和导入类和模块。 此外AJAX库还可以解决互用性问题，不用担心程序在IE6, IE7, Firefox, Safari, Opera等浏览器上的兼容问题。 

![](http://pyjs.org/img/overview.png)&nbsp;

&nbsp;

是不是觉得很酷呢？pyjamas有一个演示页面，里面有多个的效果。 

比如：

火星登陆游戏：[http://pyjs.org/examples/asteroids/output/Space.html](http://pyjs.org/examples/asteroids/output/Space.html)

邮件客户端：[http://pyjs.org/examples/mail/output/Mail.html ](http://pyjs.org/examples/mail/output/Mail.html)

GWTCanvas：[http://pyjs.org/examples/gwtcanvas/output/GWTCanvasDemo.html ](http://pyjs.org/examples/gwtcanvas/output/GWTCanvasDemo.html)

(HTML5 Canvas?? 有人讨论这个问题在[这里](http://osdir.com/ml/pyjamas-dev/2010-06/msg00600.html)) 

&nbsp;

更多内容直接浏览pyjamas的主页了：[http://pyjs.org ](http://pyjs.org/)

最近打算学习HTML5，但是HTML5说到底，还是在那摆弄着一堆的Javascript。所以，先玩玩pyjamas也无妨啊！~&nbsp; 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/09/16/Pyjamas-python-write-javascirpt.html](http://www.cnblogs.com/coderzh/archive/2010/09/16/Pyjamas-python-write-javascirpt.html)**