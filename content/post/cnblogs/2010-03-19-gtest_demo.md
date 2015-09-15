---
categories:
- 技术文章
date: '2010-03-19'
title: gtest参数化测试代码示例
url: /2010/03/19/gtest_demo/

---


在[玩转 Google开源C++单元测试框架Google Test系列(gtest)之四 - 参数化](http://www.cnblogs.com/coderzh/archive/2009/04/08/1431297.html)中已经介绍过了如何使用gtest进行参数化测试。在twitter上应 @xlinker 的要求，我在这里提供一个参数化的完整例子。这个例子也是我当初了解gtest时写的，同时这个例子也在《玩转》系列中出现过。最后，我再附上整个demo工程，里面有一些其他的示例，刚开始上手的同学可以直接拿我的demo工程去试，有任何疑问都欢迎提出。以下是使用TEST_P宏进行参数化测试的示例：

<div class="cnblogs_code">
<div><span style="color: #000000">#include&nbsp;</span><span style="color: #800000">"</span><span style="color: #800000">stdafx.h</span><span style="color: #800000">"</span><span style="color: #000000">
#include&nbsp;</span><span style="color: #800000">"</span><span style="color: #800000">foo.h</span><span style="color: #800000">"</span><span style="color: #000000">
#include&nbsp;</span><span style="color: #000000">&lt;</span><span style="color: #000000">gtest</span><span style="color: #000000">/</span><span style="color: #000000">gtest.h</span><span style="color: #000000">&gt;</span><span style="color: #000000">
<br />
</span><span style="color: #0000ff">class</span><span style="color: #000000">&nbsp;IsPrimeParamTest&nbsp;:&nbsp;</span><span style="color: #0000ff">public</span><span style="color: #000000">::testing::TestWithParam</span><span style="color: #000000">&lt;</span><span style="color: #0000ff">int</span><span style="color: #000000">&gt;</span><span style="color: #000000">
{
<br />
};
<br />
</span><span style="color: #008000">//</span><span style="color: #008000">&nbsp;不使用参数化测试，就需要像这样写五次</span><span style="color: #008000">
</span><span style="color: #000000">TEST(IsPrimeTest,&nbsp;HandleTrueReturn)
{
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(</span><span style="color: #800080">3</span><span style="color: #000000">));
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(</span><span style="color: #800080">5</span><span style="color: #000000">));
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(</span><span style="color: #800080">11</span><span style="color: #000000">));
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(</span><span style="color: #800080">23</span><span style="color: #000000">));
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(</span><span style="color: #800080">17</span><span style="color: #000000">));
}
<br />
</span><span style="color: #008000">//</span><span style="color: #008000">&nbsp;使用参数化测试，只需要：</span><span style="color: #008000">
</span><span style="color: #000000">TEST_P(IsPrimeParamTest,&nbsp;HandleTrueReturn)
{
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff">int</span><span style="color: #000000">&nbsp;n&nbsp;</span><span style="color: #000000">=</span><span style="color: #000000">&nbsp;&nbsp;GetParam();
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_TRUE(IsPrime(n));
}
<br />
<span style="color: #008000">//</span><span style="color: #008000"> 定义参数</span>
INSTANTIATE_TEST_CASE_P(TrueReturn,&nbsp;IsPrimeParamTest,&nbsp;testing::Values(</span><span style="color: #800080">3</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">5</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">11</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">23</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">17</span><span style="color: #000000">));
<br />
</span><span style="color: #008000">//</span><span style="color: #008000">&nbsp;-----------------------
</span><span style="color: #008000">//</span><span style="color: #008000">&nbsp;更复杂一点的参数结构</span><span style="color: #008000">
</span><span style="color: #000000">
</span><span style="color: #0000ff">struct</span><span style="color: #000000">&nbsp;NumberPair
{
&nbsp;&nbsp;&nbsp;&nbsp;NumberPair(</span><span style="color: #0000ff">int</span><span style="color: #000000">&nbsp;_a,&nbsp;</span><span style="color: #0000ff">int</span><span style="color: #000000">&nbsp;_b)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a&nbsp;</span><span style="color: #000000">=</span><span style="color: #000000">&nbsp;_a;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;</span><span style="color: #000000">=</span><span style="color: #000000">&nbsp;_b;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff">int</span><span style="color: #000000">&nbsp;a;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff">int</span><span style="color: #000000">&nbsp;b;
};
<br />
</span><span style="color: #0000ff">class</span><span style="color: #000000">&nbsp;FooParamTest&nbsp;:&nbsp;</span><span style="color: #0000ff">public</span><span style="color: #000000">&nbsp;::testing::TestWithParam</span><span style="color: #000000">&lt;</span><span style="color: #000000">NumberPair</span><span style="color: #000000">&gt;</span><span style="color: #000000">
{
<br />
};
<br />
TEST_P(FooParamTest,&nbsp;HandleThreeReturn)
{
&nbsp;&nbsp;&nbsp;&nbsp;FooCalc&nbsp;foo;
&nbsp;&nbsp;&nbsp;&nbsp;NumberPair&nbsp;pair&nbsp;</span><span style="color: #000000">=</span><span style="color: #000000">&nbsp;GetParam();
&nbsp;&nbsp;&nbsp;&nbsp;EXPECT_EQ(</span><span style="color: #800080">3</span><span style="color: #000000">,&nbsp;foo.Calc(pair.a,&nbsp;pair.b));
}
<br />
INSTANTIATE_TEST_CASE_P(ThreeReturn,&nbsp;FooParamTest,&nbsp;testing::Values(NumberPair(</span><span style="color: #800080">12</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">15</span><span style="color: #000000">),&nbsp;NumberPair(</span><span style="color: #800080">18</span><span style="color: #000000">,&nbsp;</span><span style="color: #800080">21</span><span style="color: #000000">)));</span></div></div>

完整示例工程：
  
[/Files/coderzh/Code/gtest_demo.rar](http://files.cnblogs.com/coderzh/Code/gtest_demo.rar)&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/03/19/gtest_demo.html](http://www.cnblogs.com/coderzh/archive/2010/03/19/gtest_demo.html)**