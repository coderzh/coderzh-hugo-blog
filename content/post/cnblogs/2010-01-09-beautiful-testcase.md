---
categories:
- 技术文章
date: '2010-01-09'
title: 编写优美的GTest测试案例
url: /2010/01/09/beautiful-testcase/

---


使用gtest也有很长一段时间了，这期间也积累了一些经验，所以分享一下。GTest为我们提供了便捷的测试框架，让我们只需要关注案例本身。如何在GTest框架下写出优美的测试案例，我觉得必须要做到：

1.  案例的层次结构一定要清晰2.  案例的检查点一定要明确3.  案例失败时一定要能精确的定位问题4.  案例执行结果一定要稳定5.  案例执行的时间一定不能太长6.  案例一定不能对测试环境造成破坏7.  案例一定独立，不能与其他案例有先后关系的依赖8.  案例的命名一定清晰，容易理解  

案例的可维护性也是非常重要，如果做到上面的8点，自然也就做到了可维护性。下面来分享一下我对于上面8点的经验：

#### 1. 案例的层次结构一定要清晰

所谓层次结构，至少要让人一眼就能分辨出被测代码和测试代码。简单的说，就是知道你在测什么。由于是进行接口测试，我已经习惯了如下的案例层次：
  
[![gtestproject](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/GTest_999B/gtestproject_thumb_2.jpg "gtestproject")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/GTest_999B/gtestproject_3.jpg) 

**DataDefine**

我会将测试案例所需要的数据，以及数据之间的联系全部在预先定义好。测试数据与案例逻辑的分离，有利于维护和扩展测试案例。同时，GTest先天就支持测试数据参数化，为测试数据的分离提供了进一步的便捷。什么是测试数据参数化？就是你可以预先定义好一批各种各样的数据，而你只需要编写一个测试案例的逻辑代码，gtest会将定义好的数据逐个套入测试案例中进行执行。具体的做法请见：[玩转Google开源C++单元测试框架Google Test系列(gtest)之四 - 参数化](http://www.cnblogs.com/coderzh/archive/2009/04/08/1431297.html)

**SUT**

SUT，即system under test，表明你的测试对象是什么，它可以是一个类(CUT)，对象(OUT)，函数(MUT)，甚至可以是整个应用程序(AUT)。我单独将这个层次划分出来，主要有两个目的：

*   明确的表示出你的测试对象是什么*   为复杂调用对象包装简单调用接口  

明确表示测试对象是什么，便于之后对测试案例的维护和对测试案例的理解。同时，对于一些被测对象，你想要调用它需要经过一系列烦琐的过程，这时，就需要将这一烦琐的调用过程隐藏起来，而只关注被测对象的输入和输出。

**TestCase**

测试工程中，必须非常明确的表示出哪些是测试案例，哪些是其他的辅助文件。通常，我们会在测试案例的文件名加上Test前缀(或者后缀)。我建议，将所有的测试案例文件或代码放在最显眼的地方，让所有看到你的测试工程的人，第一眼看到的就是测试案例，这很重要。

**Checker**

对于一个复杂系统的接口测试，仅仅坚持输入和输出是远远不够的。比如测试一个写数据库的函数，函数的返回值告诉你数据已经成功写入是远远不够的，你必须亲身去数据库中查个究竟才行。因此，对于某一类的测试案例，我们可以抽象出一些通用的检查点代码。

如果做到上面的分层，那么一个测试案例写出来的结构应该会是这个样子：
<div class="cnblogs_code"><div><span style="color: #000000;">TEST(TestFoo,&nbsp;JustDemo)
{
&nbsp;&nbsp;&nbsp;&nbsp;GetTestData();&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;获取测试数据</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;CallSUT();&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;调用被测方法</span><span style="color: #008000;">
</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;CheckSomething();&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;检查点验证</span><span style="color: #008000;">
</span><span style="color: #000000;">}</span></div></div>

这样的测试案例，一目了然。

#### 2. 案例的检查点一定要明确

一定要明确案例的检查点是什么，并且让检查点尽量集中。有一个不好的习惯就是核心的检查点在分布在多个函数中，需要不断的跳转才能了解到这个案例检查了些什么。好的做法应该是尽量让检查点集中，能够非常清晰的分辨出案例对被测代码做了哪些检查。所以，尽量让Gtest的ASSERT_和EXPECT_系列的宏放在明显和正确的地方。

#### 3. 案例失败时一定要能精确的定位问题

测试案例失败时，我们通常手忙脚乱。如果一个测试案例Failed，却不能立即推断是被测代码的Bug的话，这个测试案例也有待改进。我们可以在一些复杂的检查点断言中加入一些辅助信息，方便我们定位问题。比如下面这个测试案例：
<div class="cnblogs_code"><div><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;n&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #800080;">1</span><span style="color: #000000;">;
</span><span style="color: #0000ff;">bool</span><span style="color: #000000;">&nbsp;actualResult&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Foo::Dosometing(n);
ASSERT_TRUE(actualResult)</span></div></div>

如果测试案例失败了，会得到下面的信息：

<div class="cnblogs_code"><div><span style="color: #000000;">Value&nbsp;of:&nbsp;actualResult
Actual:&nbsp;</span><span style="color: #0000ff;">false</span><span style="color: #000000;">
Expected:</span><span style="color: #0000ff;">true</span></div></div>

这样的结果对于我们来说，几乎没有什么用。因为我们根本不知道actualResult是什么，以及在什么情况下才会出现非预期值。因此，在断言处多加入一些信息，将有助于定位问题：
<div class="cnblogs_code"><div><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;n&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #800080;">1</span><span style="color: #000000;">;
</span><span style="color: #0000ff;">bool</span><span style="color: #000000;">&nbsp;actualResult&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Foo::Dosometing(n);
ASSERT_TRUE(actualResult)&nbsp;</span><span style="color: #000000;">&lt;&lt;</span><span style="color: #000000;">&nbsp;L</span><span style="color: #800000;">"</span><span style="color: #800000;">Call&nbsp;Foo::Dosometing(n)&nbsp;when&nbsp;n&nbsp;=&nbsp;</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">&lt;&lt;</span><span style="color: #000000;">&nbsp;n;</span></div></div>

#### 
4. 案例执行结果一定要稳定

要保证测试案例在什么时候、什么情况下执行的结果都是一样的。一个一会成功一会失败的案例是没有意义的。要保证案例稳定性的方法有很多，比如杜绝案例之间的影响，有时候，由于前一个案例执行完后，将一些系统的环境破坏了，导致后面的案例执行失败。在测试某些本身就存在一定几率或延时的系统时，使用超时机制是比较简单的办法。比如，你需要测试一个启动Windows服务的方法，如果我们在调用了该方法后立即进行检查，很可能检查点会失败，有时候也许又是通过的。这是因为Windows服务由Stop状态到Running状态，中间还要经过一个Padding状态。所以，简单的做法是使用超时机制，隔断时间检查一次，直到超过某个最大忍受时间。
<div class="cnblogs_code" onclick="cnblogs_code_show('bf476fb7-90bf-42ca-a114-4ab3fb2e1bc2')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_bf476fb7-90bf-42ca-a114-4ab3fb2e1bc2"><div><span style="color: #000000;">ASSERT_TRUE(StartService(</span><span style="color: #800000;">'</span><span style="color: #800000;">xxx</span><span style="color: #800000;">'</span><span style="color: #000000;">));
</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;tryTimes&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">0</span><span style="color: #000000;">;
</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;status&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;GetServiceStatus(</span><span style="color: #800000;">'</span><span style="color: #800000;">xxx</span><span style="color: #800000;">'</span><span style="color: #000000;">);
</span><span style="color: #0000ff;">while</span><span style="color: #000000;">&nbsp;(status&nbsp;</span><span style="color: #000000;">!=</span><span style="color: #000000;">&nbsp;Running)
{
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;(tryTimes&nbsp;</span><span style="color: #000000;">&gt;=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">10</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">break</span><span style="color: #000000;">;
&nbsp;&nbsp;&nbsp;&nbsp;::Sleep(</span><span style="color: #800080;">200</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;tryTimes</span><span style="color: #000000;">++</span><span style="color: #000000;">;
&nbsp;&nbsp;&nbsp;&nbsp;status&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;GetServiceStatus(</span><span style="color: #800000;">'</span><span style="color: #800000;">xxx</span><span style="color: #800000;">'</span><span style="color: #000000;">);
}
ASSERT_EQ(Running,&nbsp;status)&nbsp;</span><span style="color: #000000;">&lt;&lt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">Check&nbsp;the&nbsp;status&nbsp;after&nbsp;StartService('xxx')</span><span style="color: #800000;">"</span><span style="color: #000000;">;</span></div></div></div>

&nbsp;

#### 5. 案例执行的时间一定不能太长

我们应该尽量让案例能够快速的执行，一方面，我们可以通过优化我们的代码来减少运行时间，比如，减少对重复内容的读取。一方面，对于一些比较耗时的操作，比如文件系统，网络操作，我们可以使用Mock对象来替代真实的对象。使用GMock是一个不错的选择。

#### 6. 案例一定不能对测试环境造成破坏

有的案例需要在特定的环境下来能执行，因此会在案例的初始化时对环境进行一些修改。注意，不管对什么东西进行了修改，一定要保证在案例执行完成的TearDown中将这些环境都还原回来。否则有可能对后面的案例造成影响，或者出现一些莫名其妙的错误。

#### 7. 案例一定独立，不能与其他案例有先后关系的依赖

任何一个案例都不依赖于其他测试案例，任何一个案例的执行结果都不应该影响到别的案例。任何一个案例都可以单独拿出去正确的执行。所以，不能寄希望于前一个案例所做的环境准备，因为这是不对的。

#### 8. 案例的命名一定清晰，容易理解

案例的名字要规范，长不要紧，一定要清晰的表达测试案例的用途。比如，下面的测试案例名称都是不好的：
<div class="cnblogs_code"><div><span style="color: #000000;">TEST(TestFoo,&nbsp;Test)
TEST(TestFoo,&nbsp;Normal)
TEST(TestFoo,&nbsp;Alright)</span></div></div>

比如像下面的案例名称就会好一点：

<div class="cnblogs_code"><div><span style="color: #000000;">TEST(TestFoo,&nbsp;Return_True_When_ParameterN_Larger_Then_Zero)
TEST(TestFoo,&nbsp;Return_False_When_ParameterN_Is_Zero)</span></div></div>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/09/beautiful-testcase.html](http://www.cnblogs.com/coderzh/archive/2010/01/09/beautiful-testcase.html)**