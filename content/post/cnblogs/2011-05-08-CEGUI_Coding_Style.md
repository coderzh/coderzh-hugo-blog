---
categories:
- 技术文章
date: '2011-05-08'
title: 从CEGUI源码看代码规范
url: /2011/05/08/CEGUI_Coding_Style/

---

  
[CEGUI](http://www.cegui.org.uk/)（Crazy Eddie&#8217;s GUI）是一个使用C++实现的基于LGPL协议的的开源GUI库，主要应用于游戏界面。连著名的开源游戏引擎Orge3D也放弃了自己的界面引擎而使用第三方的开源界面引擎CEGUI。

对于开源的代码工程，我首先会观察它的代码规范。比如，使用什么命名法，是否使用异常等等，这很有用。看不同的开源工程，可以看到各种不同的代码规范，其中有很多是值得借鉴的。

代码规范本身并没有绝对的对错之分，但我们往往为了某一个代码规范争论的面红耳赤。比如，是否使用匈牙利命名法，使用BOOL还是bool等等。这时，就必须综合考虑团队现有的使用习惯和既有代码的风格，制定出一套适合自己的统一的规范。所以，规范除了对与错，最关键的地方还是要统一。存在即合理，我们不要一味去排斥其他人的使用习惯和规范，而应该多读读别人的代码，看看著名的开源代码，了解别人的做法，然后对自己的做法进行一些反思。这才是面对代码规范正确的心态。

CEGUI是一套不错的界面库，界面布局使用XML来描述，提供了专用的界面编辑器，让界面制作变得更简单。CEGUI作为一个成熟的开源产品，代码已经经历了无数的千锤百炼，整体风格比较统一，是一个很好的学习范本。接下来，我粗浅的分析一下CEGUI一些值得学习的地方。

**1. Camel命名法**

CEGUI完全摈弃了匈牙利命名法，而使用更贴近语义的不使用变量类型前缀的Camel(骆驼)命名法，这也是现今代码通用的做法。匈牙利命名法在较老的工程中比较常见。无数使用Camel的著名开源工程，很好的告诉了匈牙利命名法的支持者，不使用匈牙利命名法，代码依然清晰可读，甚至会更好。

**2. 成员变量前缀**

CEGUI中无论是class还是struct，成员变量都统一加d_前缀。通常的两种做法是不加前缀和加m_前缀。

**3. struct**

CEGUI中，struct的命名没有使用全大写，而是和class的大小写命名一样。在struct中，只可能出现数据成员，操作符重载函数，构造函数等。struct只用来数据结构存储使用，不使用任何其他的成员函数。

**4. 字符串处理**

CEGUI中的字符串处理没有使用char, wchar_t, TCHAR，std:string，ATL::CString，而是自己实现了一套String类（CEGUIString.h）。自己实现的String类优势非常明显，可以让程序员从繁琐的字符指针操作中解脱出来，将更多的精力放在功能的实现上。自定义的String可以实现更多方便、切合实际使用的函数。（比如CEGUI中的find_first_not_of，replace等函数。）如果要实现一个String类，CEGUI中的CEGUIString是一个很好的范本。

**5. 使用bool**

使用bool和BOOL都有各自的理由，CEGUI中全部使用bool，是现在流行，最常见的，也是我喜欢的做法。

**6. 异常机制**

CEGUI中完全使用异常机制，通过重载std::exception定义了一套完整的异常机制。通过异常的处理，使得程序员从繁琐的错误检查和错误返回值中解放出来。如果想了解C++中如何能够很好的使用异常，看看CEGUI中异常的实现吧（CEGUIExceptions.h）。

**7. 不用goto**

几乎每一本教材都会告诫用户，不要使用goto，这会让你的代码变得凌乱不堪。然而当真正成为一个程序员，加入一个公司甚至大型公司，里面的代码照样充斥了无数的goto语句。goto的滥用是绝对不允许的，goto在某些情况下的确有它的合理之处（比如保证函数单一出口，释放资源）。还是那句话，存在即合理。CEGUI中完全不使用goto，有了错误，立即抛异常，或者直接返回。我本人也是比较喜欢这种提前返回的方式。

**8. 简单易用的Log系统**

如果想实现一个既简单，又易用的Log系统，就看看CEGUI中的实现吧（CEGUILogger）。支持Log等级（Error，Warning等），输出日期、当前代码行等功能。

**9. Singleton的实现**

CEGUI中使用了一个通用的Singleton&lt;T&gt;模板基类，这个技巧非常好使。实现也非常简单：

<div class="cnblogs_code">
<div><span style="color: #000000;">template&nbsp;</span><span style="color: #000000;">&lt;</span><span style="color: #000000;">typename&nbsp;T</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000FF;">class</span><span style="color: #000000;">&nbsp;CEGUIEXPORT&nbsp;Singleton
<br />
{
<br />
</span><span style="color: #0000FF;">protected</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000FF;">static</span><span style="color: #000000;">
<br />
#ifdef&nbsp;__MINGW32__
<br />
&nbsp;&nbsp;&nbsp;&nbsp;CEGUIEXPORT
<br />
</span><span style="color: #0000FF;">#endif</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;T</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;ms_Singleton;
<br />
</span><span style="color: #0000FF;">public</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;Singleton(&nbsp;</span><span style="color: #0000FF;">void</span><span style="color: #000000;">&nbsp;)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;{
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assert(&nbsp;</span><span style="color: #000000;">!</span><span style="color: #000000;">ms_Singleton&nbsp;);
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ms_Singleton&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;static_cast</span><span style="color: #000000;">&lt;</span><span style="color: #000000;">T</span><span style="color: #000000;">*&gt;</span><span style="color: #000000;">(</span><span style="color: #0000FF;">this</span><span style="color: #000000;">);
<br />
&nbsp;&nbsp;&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">~</span><span style="color: #000000;">Singleton(&nbsp;</span><span style="color: #0000FF;">void</span><span style="color: #000000;">&nbsp;)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;&nbsp;assert(&nbsp;ms_Singleton&nbsp;);&nbsp;&nbsp;ms_Singleton&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">0</span><span style="color: #000000;">;&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000FF;">static</span><span style="color: #000000;">&nbsp;T</span><span style="color: #000000;">&amp;</span><span style="color: #000000;">&nbsp;getSingleton(&nbsp;</span><span style="color: #0000FF;">void</span><span style="color: #000000;">&nbsp;)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;&nbsp;assert(&nbsp;ms_Singleton&nbsp;);&nbsp;&nbsp;</span><span style="color: #0000FF;">return</span><span style="color: #000000;">&nbsp;(&nbsp;</span><span style="color: #000000;">*</span><span style="color: #000000;">ms_Singleton&nbsp;);&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000FF;">static</span><span style="color: #000000;">&nbsp;T</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;getSingletonPtr(&nbsp;</span><span style="color: #0000FF;">void</span><span style="color: #000000;">&nbsp;)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;&nbsp;</span><span style="color: #0000FF;">return</span><span style="color: #000000;">&nbsp;(&nbsp;ms_Singleton&nbsp;);&nbsp;&nbsp;}
<br />
</span><span style="color: #0000FF;">private</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;Singleton</span><span style="color: #000000;">&amp;</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000FF;">operator</span><span style="color: #000000;">=</span><span style="color: #000000;">(</span><span style="color: #0000FF;">const</span><span style="color: #000000;">&nbsp;Singleton</span><span style="color: #000000;">&amp;</span><span style="color: #000000;">)&nbsp;{&nbsp;</span><span style="color: #0000FF;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000FF;">this</span><span style="color: #000000;">;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;Singleton(</span><span style="color: #0000FF;">const</span><span style="color: #000000;">&nbsp;Singleton</span><span style="color: #000000;">&amp;</span><span style="color: #000000;">)&nbsp;{}
<br />
};</span></div>
</div>

如上面的Logger类，要使用Singleton，则这样定义：

<div class="cnblogs_code">
<div><span style="color: #0000FF;">class</span><span style="color: #000000;">&nbsp;CEGUIEXPORT&nbsp;Logger&nbsp;:&nbsp;</span><span style="color: #0000FF;">public</span><span style="color: #000000;">&nbsp;Singleton&nbsp;</span><span style="color: #000000;">&lt;</span><span style="color: #000000;">Logger</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">
<br />
{
<br />
}</span></div>
</div>

这样做最大的一个好处是统一，不会在代码中出现各种稀奇古怪不同的Singleton实现。同时哪个class是Singleton也一目了然。

**总结 &nbsp;&nbsp;**

本文仅仅讨论CEGUI中的代码规范，而且也只是其中很小的一部分，如有疏漏欢迎一起讨论。之后我会更加关注CEGUI现细节，如有收获将与大家分享。
最后，我还是那句话：<span style="color: red; ">不要完全排斥任何一种规范，将每种规范了解和使用过后，再来思考自己应该怎样做。</span>

<span style="color: red; ">
</span>

CEGUI主页：[http://www.cegui.org.uk](http://www.cegui.org.uk/wiki/index.php/Downloads)

源码下载 ：[http://www.cegui.org.uk/wiki/index.php/Downloads](http://www.cegui.org.uk/wiki/index.php/Downloads)

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2011/05/08/CEGUI_Coding_Style.html](http://www.cnblogs.com/coderzh/archive/2011/05/08/CEGUI_Coding_Style.html)**