---
categories:
- 技术文章
date: '2010-02-28'
title: 通过NBehave了解BDD(Behavior Driven Development)
url: /2010/02/28/BDD-By-NBehave/

---


之前写过一篇介绍BDD的文章([优美的测试代码 - 行为驱动开发(BDD)](http://www.cnblogs.com/coderzh/archive/2009/07/26/1531633.html))，很多同学都表示很感兴趣，但感觉过于抽象。因此，本文通过使用NBehave框架，通过非常简单而又具体的例子，加深对BDD的认识。

#### BDD简介

WikiPedia中的说明：

_<span style="color: #000000;">Behavior&nbsp;Driven&nbsp;Development&nbsp;(or&nbsp;BDD)&nbsp;is&nbsp;an&nbsp;Agile&nbsp;software&nbsp;development&nbsp;technique  </span><span style="color: #000000;">that&nbsp;encourages&nbsp;collaboration&nbsp;between&nbsp;developers</span><span style="color: #000000;">,  QA&nbsp;and&nbsp;non-technical&nbsp;or&nbsp;business&nbsp;participants&nbsp;in&nbsp;a&nbsp;software&nbsp;project.</span>_
**

<span class="Apple-style-span" style="font-weight: normal;">BDD通过故事模板和场景，描述产品在用户操作时的具体功能表现，有点类似传统的Use Case。<span style="color: red;">BDD的故事模板和场景，更加贴近用户的行为，BDD的测试案例，更加注重从用户的角度进行测试。</span></span>

**

通常，故事模板类似：

**
**

**
<div class="cnblogs_code">
<div><span style="color: #0000ff;">As</span><span style="color: #000000;">&nbsp;a&nbsp;[X]&nbsp;
<br />
</span><span style="color: #0000ff;">I</span><span style="color: #000000;">&nbsp;want&nbsp;[Y]&nbsp;
<br />
</span><span style="color: #0000ff;">so</span><span style="color: #000000;">&nbsp;that&nbsp;[Z]</span></div>
</div>

<span class="Apple-style-span" style="font-weight: normal;">场景模板类似：</span>

**

**
**

**
<div class="cnblogs_code">
<div><span style="color: #0000ff;">Given</span><span style="color: #000000;">&nbsp;some&nbsp;initial&nbsp;context&nbsp;(the&nbsp;givens),&nbsp;
<br />
</span><span style="color: #0000ff;">When</span><span style="color: #000000;">&nbsp;an&nbsp;</span>event<span style="color: #000000;">&nbsp;occurs,&nbsp;
<br />
</span><span style="color: #0000ff;">then</span><span style="color: #000000;">&nbsp;ensure&nbsp;some&nbsp;outcomes.</span></div>
</div>
**

#### NBehave简介

NBehave是.NET版本的BDD框架，通过NBehave，能够方便的进行行为驱动开发。NBehave负责将场景模板映射到案例代码，内置NUnit，XUnit，MbTest，或者MSTest等单元测试框架，同时负责执行并生成测试报告。因此，通过NBehave，我们只需要：

1.  编写场景模板2.  编写对应的场景类，映射模板中的具体行为和表现。3.  通过NBehave-Console.exe执行案例。或者集成到（MSBuild，NAnt中）

#### 

简单实例

比如，我们编写如下场景：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">Given</span><span style="color: #000000;">&nbsp;I&nbsp;am&nbsp;not&nbsp;logged&nbsp;in
<br />
</span><span style="color: #0000ff;">When</span><span style="color: #000000;">&nbsp;I&nbsp;log&nbsp;in&nbsp;as&nbsp;Morgan&nbsp;with&nbsp;a&nbsp;password&nbsp;SecretPassw0rd
<br />
</span><span style="color: #0000ff;">Then</span><span style="color: #000000;">&nbsp;I&nbsp;should&nbsp;see&nbsp;a&nbsp;message</span><span style="color: #000000;">,</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">"</span><span style="color: #000000;">Welcome,&nbsp;Morgan!</span><span style="color: #000000;">"</span></div>
</div>

我们把上面的内容保存到一个文件中，命名为：_**user_logs_in_successfully.feature**_

接下来，编写对应的场景类：

<pre><div class="cnblogs_code"><div><span style="color: #0000ff;">using</span><span style="color: #000000;">&nbsp;NBehave.Narrator.Framework;
</span><span style="color: #0000ff;">using</span><span style="color: #000000;">&nbsp;NBehave.Spec.NUnit;
</span><span style="color: #000000;">  
[ActionSteps]
</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;UserLogsInSuccessfully
</span><span style="color: #000000;">{
 &nbsp;&nbsp; </span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;some&nbsp;code&nbsp;to&nbsp;setup&nbsp;_currentPage
&nbsp;&nbsp;&nbsp; </span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;...</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; [Given(</span><span style="color: #800000;">"</span><span style="color: #800000;">I&nbsp;am&nbsp;not&nbsp;logged&nbsp;in</span><span style="color: #800000;">"</span><span style="color: #000000;">)]
&nbsp;&nbsp;&nbsp; </span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;LogOut()
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; {
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _currentPage.click(</span><span style="color: #800000;">"</span><span style="color: #800000;">logout</span><span style="color: #800000;">"</span><span style="color: #000000;">);
</span><span style="color: #000000;"></span><span style="color: #000000;"></span></div>

<span style="color: #000000;">&nbsp;&nbsp;&nbsp; }
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; [When(</span><span style="color: #800000;">"</span><span style="color: #800000;">I&nbsp;log&nbsp;in&nbsp;as&nbsp;$username&nbsp;with&nbsp;a&nbsp;password&nbsp;$password</span><span style="color: #800000;">"</span><span style="color: #000000;">)]
&nbsp;&nbsp;&nbsp; </span><span style="color: #0000ff;">public</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;LogIn(</span><span style="color: #0000ff;">string</span><span style="color: #000000;">&nbsp;username,&nbsp;</span><span style="color: #0000ff;">string</span><span style="color: #000000;">&nbsp;password)
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; {
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _currentPage.click(</span><span style="color: #800000;">"</span><span style="color: #800000;">login</span><span style="color: #800000;">"</span><span style="color: #000000;">);
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; }
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; [Then(</span><span style="color: #800000;">"</span><span style="color: #800000;">I&nbsp;should&nbsp;see&nbsp;a&nbsp;message,&nbsp;\</span><span style="color: #800000;">"</span><span style="color: #000000;">$message\</span><span style="color: #800000;">""</span><span style="color: #000000;">)]
&nbsp;&nbsp;&nbsp; </span><span style="color: #0000ff;">public</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;CheckMessage(</span><span style="color: #0000ff;">string</span><span style="color: #000000;">&nbsp;message)
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; {
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _currentPage.ToString().ShouldContain(message);
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp; }
</span><span style="color: #000000;">}</span>
</div>

<span class="Apple-style-span" style="font-family: verdana,'courier new'; white-space: normal;">上面的代码简单明了，通过Given, When, Then等.NET Attribute，建立了场景类中的方法与场景模板之间的联系。我们还看到，这几个Attribute还支持参数匹配，比如，通过$username匹配到Login函数的username参数，非常的方便使用。实际上参数还支持正则表达式以及数组参数，详细参考文本最后的链接：[Steps](http://nbehave.codeplex.com/wikipage?title=ActionSteps&amp;referringTitle=latest%20release "ActionSteps&amp;referringTitle=latest%20release")</span>

</pre>

接下来，就是执行了，通过：

<pre><div class="cnblogs_code"><span style="color: #000000;">&gt;NBehave-Console.exe&nbsp;NameOfDll.dll&nbsp;/sf</span><span style="color: #000000;">=</span><span style="color: #000000;">user_logs_in_successfully.feature</span>
</div>
</pre>

执行后如果全部通过，会有通过的通过的信息输出，如果案例失败了，会有详细的错误输出。

#### 

NBehave文档

通过上面简单的示例，是不是对BDD有了更加直观的了解了呢。如果想了解更多关于NBehave框架的内容，请参考NBehave主页：[http://nbehave.codeplex.com/](http://nbehave.codeplex.com/)

其中，本文的例子也是NBehave主页中的Documents中来的。

参考链接：

*   [Getting started](http://nbehave.codeplex.com/wikipage?title=Getting%20started&amp;referringTitle=latest%20release "Getting%20started&amp;referringTitle=latest%20release") （简单入门，本文的例子也是从这里来的）*   [Steps](http://nbehave.codeplex.com/wikipage?title=ActionSteps&amp;referringTitle=latest%20release "ActionSteps&amp;referringTitle=latest%20release") （场景类中，Given, When, Then等Attribute使用的详细规则）*   [Integrate into build process](http://nbehave.codeplex.com/wikipage?title=IntegrateBuild&amp;referringTitle=latest%20release "IntegrateBuild&amp;referringTitle=latest%20release") （介绍如何集成Nbehave到持续构建中，比如，MSBuild，NAnt）*   [scenario files](http://nbehave.codeplex.com/wikipage?title=scenario%20files&amp;referringTitle=Getting%20started "scenario%20files&amp;referringTitle=Getting%20started") （场景文件(本文中的user_logs_in_successfully.feature)的一些编写规则）

#### 

BDD与TDD

我认为，BDD和TDD是相辅相成的。我可以想象这样一个开发过程：

<span style="color: red;">产品人员或QA人员根据产品需求设计好各种场景文件（Scenario files） -&gt; 开发人员编写对应的场景类（Scenario class）-&gt; 执行场景 &#8211;&gt; 执行结果失败 &#8211;&gt; 编写相应的产品代码（Product code） &#8211;&gt; 再次执行场景 &#8211;&gt; 重复执行这个过程，直到所有场景通过</span>

这就是我所理解的行为<span style="color: red;">驱动</span>开发，我就不画图了，大家有什么看法呢？

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/02/28/BDD-By-NBehave.html](http://www.cnblogs.com/coderzh/archive/2010/02/28/BDD-By-NBehave.html)**