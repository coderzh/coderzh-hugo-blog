---
categories:
- 技术文章
date: '2010-04-27'
title: Python天天美味(34) - Decorators详解
url: /2010/04/27/python-cookbook33-Decorators/

---


Python中的Decorators表面看起来很像C#的Attribute，其实不然，Python的Decorators和C#的Attribute完全是两个东西。Python的Decorators让我想到了设计模式中的装饰者模式（Decorator Pattern）。

### Decorator Pattern

  <div class="cnblogs_code"><div><span style="color: #000000;">Attach&nbsp;additional&nbsp;responsibilities&nbsp;to&nbsp;an&nbsp;object&nbsp;dynamically. 
Decorators&nbsp;provide&nbsp;a&nbsp;flexible&nbsp;alternative&nbsp;to&nbsp;subclassing&nbsp;for&nbsp;extending&nbsp;functionnality.</span></div></div>  

Python中的通过Decorators对函数、方法或类进行装饰，从而达到增加对象的职责，或控制对象调用的作用。而C#的Attribute仅仅是起到元数据标识作用，最终通过反射获取这些特定信息。

先来个简单的示例，先定义一个Coffee类，
<div class="cnblogs_code"><div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Coffee(object):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1.0</span><span style="color: #000000;">
<br />
coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Coffee()
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;coffee.get_cost()&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;1.0</span></div></div>

这时，我想通过装饰者模式计算Milk的价格，通常这样实现：
<div class="cnblogs_code" onclick="cnblogs_code_show('5edef3d0-bb20-42e6-9e25-83c5948aa064')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_5edef3d0-bb20-42e6-9e25-83c5948aa064"><div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Milk(Coffee):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;coffee):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;coffee
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;self.coffee.get_cost()&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0.5</span><span style="color: #000000;">

coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Coffee()
coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Milk(coffee)
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;coffee.get_cost()&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;1.5</span></div></div></div>

上面是经典的装饰者模式的实现，Python中通过Decorators可以实现成这样：
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;milk_decorator(get_cost):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_milk_cost(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;get_cost(self)&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0.5</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;get_milk_cost
<br />
</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Coffee(object):
&nbsp;&nbsp;&nbsp;&nbsp;@milk_decorator
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1.0</span><span style="color: #000000;">
<br />
coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Coffee()
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;coffee.get_cost()&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">1.5</span></div></div>

假设一下，如果有更多的，比如：Whip, Sprinkles, Tee, 必须为每个装饰者都实现一个函数，将会出现函数爆炸，我们可以只实现一个通用的Decorator函数，通过在get_cost函数添加多个@Decorator，这很符合Decorator Pattern的思想。
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost_decorator(additional_cost):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;wrapper1(func):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;wrapper2(instance):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;func(instance)&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;additional_cost
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;wrapper2
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;wrapper1
<br />
</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Coffee(object):
&nbsp;&nbsp;&nbsp;&nbsp;@get_cost_decorator(</span><span style="color: #000000;">0.5</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;@get_cost_decorator(</span><span style="color: #000000;">0.7</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;@get_cost_decorator(</span><span style="color: #000000;">0.2</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1.0</span><span style="color: #000000;">
<br />
coffee&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Coffee()
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;coffee.get_cost()&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">2.4</span></div></div>

上面的get_cost_decorator类看上去比较复杂，不要紧，一会再回头看这个函数。

### Decorators基础

闲话不多说，先看下面的简单例子：

<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;myDecorator(func):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;newFunction():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">inside&nbsp;newFunction</span><span style="color: #800000;">"</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;func()
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;newFunction
<br />
@myDecorator
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;aFunction():
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">inside&nbsp;aFunction()</span><span style="color: #800000;">"</span><span style="color: #000000;">
<br />
aFunction()</span></div></div>

最终输出：

<div class="cnblogs_code"><div><span style="color: #000000;">inside&nbsp;newFunction
inside&nbsp;aFunction()</span></div></div>

我们看到，myDecorator函数的参数其实是aFunction的函数地址，并且返回一个函数地址，返回的函数才是最终真正调用的地址。最终的调用，等价于：
<div class="cnblogs_code"><div><span style="color: #000000;">aFunction&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;myDecorator(aFunction)
aFunction()</span></div></div>

其中，myDecorator也可以使用class来实现，比如：
<div class="cnblogs_code"><div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;myDecorator(object):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;func):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.func&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;func
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__call__</span><span style="color: #000000;">(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">inside&nbsp;myDecorator</span><span style="color: #800000;">"</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.func()
@myDecorator
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;aFunction():
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">inside&nbsp;aFunction()</span><span style="color: #800000;">"</span></div></div> 

最终，

<div class="cnblogs_code"><div><span style="color: #000000;">aFunction()</span></div></div>
<br />
相对于
<div class="cnblogs_code"><div><span style="color: #000000;">aFunction&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;myDecorator(aFunction)
aFunction()&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;__call__</span></div></div>

### Decorators调用规律

上面的例子，我们可以很容易的得到这样一个规律：

<div class="cnblogs_code"><div><span style="color: #000000;">@A
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;f&nbsp;():
&nbsp;&nbsp;&nbsp;&nbsp;&#8230;</span></div></div>

最终等价于：

<div class="cnblogs_code"><div><span style="color: #000000;">f&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;A(f)</span></div></div>
<br />
如果更复杂一些：
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">@A
@B
@C
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;f&nbsp;():
&nbsp;&nbsp;&nbsp;&nbsp;&#8230;</span></div></div>

则相对于：

<div class="cnblogs_code"><div><span style="color: #000000;">f&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;A(B(C(f)))</span></div></div>
<br />
再看看有参数的例子，
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">@A(args)
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;f&nbsp;():
&nbsp;&nbsp;&nbsp;&nbsp;&#8230;</span></div></div>

这时，f相当于：

<div class="cnblogs_code"><div><span style="color: #000000;">_deco&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;A(args)
f&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;_deco(f)</span></div></div>

因此，A的实现也会相对复杂一些：

<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;A(args):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;wrapper1(f):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;wrapper2():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;&#8220;before&nbsp;call&nbsp;f()&#8221;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;wrapper2
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;wrapper1</span></div></div>

有点绕吧，嗯，还算简单，我们回头看最开头那个例子，

<div class="cnblogs_code"><div><span style="color: #000000;">@get_cost_decorator(</span><span style="color: #000000;">0.5</span><span style="color: #000000;">)
@get_cost_decorator(</span><span style="color: #000000;">0.7</span><span style="color: #000000;">)
@get_cost_decorator(</span><span style="color: #000000;">0.2</span><span style="color: #000000;">)
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_cost(self):&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1.0</span></div></div>

相当于：

<div class="cnblogs_code"><div><span style="color: #000000;">get_cost&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;&nbsp;get_cost_decorator(</span><span style="color: #000000;">0.5</span><span style="color: #000000;">)(get_cost_decorator(</span><span style="color: #000000;">0.7</span><span style="color: #000000;">)(get_cost_decorator(</span><span style="color: #000000;">0.2</span><span style="color: #000000;">)(get_cost)))&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;绕晕了~~</span></div></div>
<br />
### Decorators典型应用 &#8211; singleton class
<br />
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;singleton(cls):
&nbsp;&nbsp;&nbsp;&nbsp;instances&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;{}
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;getinstance():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;cls&nbsp;</span><span style="color: #0000ff;">not</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;instances:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;instances[cls]&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;cls()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;instances[cls]
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;getinstance
<br />
@singleton
</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;MyClass:
&nbsp;&nbsp;&nbsp;&nbsp;...</span></div></div>

参考文章：
  
[Decorators for Functions and Methods](http://www.python.org/dev/peps/pep-0318/)
  
[Introduction to Python Decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240808)&nbsp;
  
[Decorator pattern](http://en.wikipedia.org/wiki/Decorator_pattern)&nbsp;
  
[[Python学习]decorator的使用&nbsp; - limodou](http://blog.donews.com/limodou/archive/2004/12/19/207521.aspx)

&nbsp;
  
[](http://www.cnblogs.com/coderzh/tag/PythonCookBook/)

#### [Python    天天美味系列（总）](http://www.cnblogs.com/coderzh/archive/2008/07/08/pythoncookbook.html)  

[Python      天天美味(30) - python数据结构与算法之快速排序](http://www.cnblogs.com/coderzh/archive/2008/09/20/1294947.html)&nbsp;       
  
[Python      天天美味(31) - python数据结构与算法之插入排序](http://www.cnblogs.com/coderzh/archive/2008/09/21/1295434.html)&nbsp;
  
[Python      天天美味(32) - python数据结构与算法之堆排序](http://www.cnblogs.com/coderzh/archive/2008/09/22/1296195.html)&nbsp;
  
[Python      天天美味(33) - 五分钟理解元类（Metaclasses）[转]](http://www.cnblogs.com/coderzh/archive/2008/12/07/1349735.html)

[Python      天天美味(34) - Decorators详解](http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html) 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html](http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html)**