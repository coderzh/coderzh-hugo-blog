---
categories:
- 技术文章
date: '2010-04-30'
title: Python天天美味(35) - 细品lambda
url: /2010/04/30/python-cookbook-lambda/

---


lambda函数也叫匿名函数，即，函数没有具体的名称。先来看一个最简单例子：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;f(x):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;x</span><span style="color: #000000;">**</span><span style="color: #000000;">2</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;f(</span><span style="color: #000000;">4</span><span style="color: #000000;">)</span></div>
</div>

Python中使用lambda的话，写成这样

<div class="cnblogs_code">
<div><span style="color: #000000;">g&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;x&nbsp;:&nbsp;x</span><span style="color: #000000;">**</span><span style="color: #000000;">2</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;g(</span><span style="color: #000000;">4</span><span style="color: #000000;">)</span></div>
</div>

lambda表达式在很多编程语言都有对应的实现。比如C#：

<div class="cnblogs_code">
<div><span style="color: #000000;">var&nbsp;g&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;x&nbsp;</span><span style="color: #000000;">=&gt;</span><span style="color: #000000;">&nbsp;x</span><span style="color: #000000;">**</span><span style="color: #000000;">2</span><span style="color: #000000;">
<br />
Console.WriteLine(g(</span><span style="color: #000000;">4</span><span style="color: #000000;">))</span></div>
</div>

那么，lambda表达式有什么用处呢？很多人提出了质疑，lambda和普通的函数相比，就是省去了函数名称而已，同时这样的匿名函数，又不能共享在别的地方调用。其实说的没错，lambda在Python这种动态的语言中确实没有起到什么惊天动地的作用，因为有很多别的方法能够代替lambda。同时，使用lambda的写法有时显得并没有那么pythonic。甚至有人提出之后的Python版本要取消lambda。

回过头来想想，Python中的lambda真的没有用武之地吗？其实不是的，至少我能想到的点，主要有：

1. 使用Python写一些执行脚本时，使用lambda可以省去定义函数的过程，让代码更加精简。

2. 对于一些抽象的，不会别的地方再复用的函数，有时候给函数起个名字也是个难题，使用lambda不需要考虑命名的问题。

3. 使用lambda在某些时候让代码更容易理解。

### lambda基础

lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象，见证一下：

<div class="cnblogs_code">
<div><span style="color: #000000;">g&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;x&nbsp;:&nbsp;x</span><span style="color: #000000;">**</span><span style="color: #000000;">2</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;g
<br />
</span><span style="color: #000000;">&lt;</span><span style="color: #000000;">function&nbsp;</span><span style="color: #000000;">&lt;</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">&nbsp;at&nbsp;</span><span style="color: #000000;">0x00AFAAF0</span><span style="color: #000000;">&gt;</span></div>
</div>

C#3.0开始，也有了lambda表达式，省去了使用delegate的麻烦写法。C#中的lambda表达式关键字是=&gt;，看下面的一个例子：

<div class="cnblogs_code">
<div><span style="color: #000000;">var&nbsp;array&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">[]&nbsp;{</span><span style="color: #800080;">2</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800080;">3</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800080;">5</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800080;">7</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800080;">9</span><span style="color: #000000;">};
<br />
var&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;array.Where(n&nbsp;</span><span style="color: #000000;">=&gt;</span><span style="color: #000000;">&nbsp;n&nbsp;</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">3</span><span style="color: #000000;">);&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;[5,&nbsp;6,&nbsp;9]</span></div>
</div>

C#使用了扩展方法，才使得数组对象拥有了像Where,Sum之类方便的方法。Python中，也有几个定义好的全局函数方便使用的，他们就是<span style="color: #0000ff;">filter</span>, <span style="color: #0000ff;">map</span>, <span style="color: #0000ff;">reduce。</span>

<div class="cnblogs_code" onclick="cnblogs_code_show('47fa6edc-8d9f-4da0-9a7d-a477697f4781')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)
<div id="cnblogs_code_open_47fa6edc-8d9f-4da0-9a7d-a477697f4781">
<div><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;foo&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[</span><span style="color: #000000;">2</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">18</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">9</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">22</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">17</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">24</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">8</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">12</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">27</span><span style="color: #000000;">]

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;filter(</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;x:&nbsp;x&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">3</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;0,&nbsp;foo)
  
[</span><span style="color: #000000;">18</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">9</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">24</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">12</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">27</span><span style="color: #000000;">]

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;map(</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;x:&nbsp;x&nbsp;</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">2</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">10</span><span style="color: #000000;">,&nbsp;foo)
  
[</span><span style="color: #000000;">14</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">46</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">28</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">54</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">44</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">58</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">26</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">34</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">64</span><span style="color: #000000;">]

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">

</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;reduce(</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;x,&nbsp;y:&nbsp;x&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;y,&nbsp;foo)

</span><span style="color: #000000;">139</span></div>
</div>
</div>

### 非lambda不可？

上面例子中的map的作用，和C#的Where扩展方法一样，非常简单方便。但是，Python是否非要使用lambda才能做到这样的简洁程度呢？在对象遍历处理方面，其实Python的<span style="color: #0000ff;">for..in..if</span>语法已经很强大，并且在易读上胜过了lambda。比如上面map的例子，可以写成：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;[x&nbsp;</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">2</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">10</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;x&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;foo]</span></div>
</div>

非常的简洁，易懂。filter的例子可以写成：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;[x&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;x&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;foo&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;x&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">3</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;0]</span></div>
</div>

同样也是比lambda的方式更容易理解。

所以，什么时候使用lambda，什么时候不用，需要具体情况具体分析，只要表达的意图清晰就好。一般情况下，如果for..in..if能做的，我都不会选择lambda。 

### lambda broken?

在数学教学中，经常会使用到lambda，比如有一位老兄就遇到这样一个问题。他想创建一个函数数组fs=[f0,...,f9] where fi(n)=i+n. 于是乎，就定义了这么一个lambda函数：

<div class="cnblogs_code">
<div><span style="color: #000000;">fs&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[(</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;n:&nbsp;i&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;n)&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;i&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;range(</span><span style="color: #000000;">10</span><span style="color: #000000;">)]</span></div>
</div>

但是，奇怪的是，

<div class="cnblogs_code">
<div><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">3</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">13</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">4</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">13</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">5</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">13</span></div>
</div>

结果并没有达到这位老兄的预期，预期的结果应该是：

<div class="cnblogs_code">
<div><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">3</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">7</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">4</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">8</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">5</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">9</span></div>
</div>

问题其实出在变量i上。上面的代码换个简单的不使用lambda的缩减版本：

<div class="cnblogs_code">
<div><span style="color: #000000;">i&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;fs(n):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;n&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;i
<br />
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;fs(</span><span style="color: #000000;">1</span><span style="color: #000000;">)&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;2</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">
<br />
i&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">2</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;fs(</span><span style="color: #000000;">1</span><span style="color: #000000;">)&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;3</span></div>
</div>

可见，上面没有达到预期的原因是lambda中的i使用的是匿名函数外的全局变量。修改一下：

<div class="cnblogs_code">
<div><span style="color: #000000;">fs&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[(</span><span style="color: #0000ff;">lambda</span><span style="color: #000000;">&nbsp;n,&nbsp;i</span><span style="color: #000000;">=</span><span style="color: #000000;">i&nbsp;:&nbsp;i&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;n)&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;i&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;range(</span><span style="color: #000000;">10</span><span style="color: #000000;">)]
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">3</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">7</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">4</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">8</span><span style="color: #000000;">
<br />
</span><span style="color: #000000;">&gt;&gt;&gt;</span><span style="color: #000000;">&nbsp;fs[</span><span style="color: #000000;">5</span><span style="color: #000000;">](</span><span style="color: #000000;">4</span><span style="color: #000000;">)
<br />
</span><span style="color: #000000;">9</span></div>
</div>

参考资料
  
[Python: Lambda Functions](http://www.secnetix.de/olli/Python/lambda_functions.hawk)&nbsp;
  
[Python&#8217;s lambda is broken!](http://math.andrej.com/2009/04/09/pythons-lambda-is-broken/)
  
[Using lambda Functions - Dive Into Python](http://diveintopython.org/power_of_introspection/lambda_functions.html)

&nbsp;

#### [Python 天天美味系列（总）](http://www.cnblogs.com/coderzh/archive/2008/07/08/pythoncookbook.html)
  
[Python 天天美味(30) - python数据结构与算法之快速排序](http://www.cnblogs.com/coderzh/archive/2008/09/20/1294947.html)&nbsp;
  
[Python 天天美味(31) - python数据结构与算法之插入排序](http://www.cnblogs.com/coderzh/archive/2008/09/21/1295434.html)&nbsp;
  
[Python 天天美味(32) - python数据结构与算法之堆排序](http://www.cnblogs.com/coderzh/archive/2008/09/22/1296195.html)&nbsp;
  
[Python 天天美味(33) - 五分钟理解元类（Metaclasses）[转]](http://www.cnblogs.com/coderzh/archive/2008/12/07/1349735.html)
  
[Python 天天美味(34) - Decorators详解](http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html) 


**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/04/30/python-cookbook-lambda.html](http://www.cnblogs.com/coderzh/archive/2010/04/30/python-cookbook-lambda.html)**