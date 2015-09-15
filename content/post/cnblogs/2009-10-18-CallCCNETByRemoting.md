---
categories:
- 技术文章
date: '2009-10-18'
title: 通过.NET Remoting调用CCNET接口的方法
url: /2009/10/18/CallCCNETByRemoting/

---


像我们用的cctray，可以设置.NET Remoting的方式添加一个主机，然后获取服务器编译的结果并提供手工触发编译的功能。因为工作需要，我需要通过代码查询编译服务器当前的编译状况，获取一些CCNET服务器端的信息。因此，我也通过.NET Remoting方式，轻松的取得了想要的一些信息。

首先，需要添加引用：ThoughtWorks.CruiseControl.Remote.dll，了解.NET Remoting的应该知道这个DLL定义的是远程封送的对象接口。

然后，调用也很简单：
<div class="cnblogs_code"><span style="color: #0000ff;">static</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;Main(</span><span style="color: #0000ff;">string</span><span style="color: #000000;">[]&nbsp;args)
{
&nbsp;&nbsp;&nbsp;&nbsp;ICruiseManager&nbsp;manger&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;(ICruiseManager)RemotingServices.Connect(</span><span style="color: #0000ff;">typeof</span><span style="color: #000000;">(ICruiseManager),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">tcp://xxx.xxx.xxx.xxx:21234/CruiseManager.rem</span><span style="color: #800000;">"</span><span style="color: #000000;">);
<br />
&nbsp;&nbsp;&nbsp;&nbsp;ProjectStatus[]&nbsp;status&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;manger.GetProjectStatus();
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">foreach</span><span style="color: #000000;">&nbsp;(var&nbsp;s&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;status)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;输出上次成功编译的标签号</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine(s.LastSuccessfulBuildLabel);
&nbsp;&nbsp;&nbsp;&nbsp;}
}</span></div>

&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/10/18/CallCCNETByRemoting.html](http://www.cnblogs.com/coderzh/archive/2009/10/18/CallCCNETByRemoting.html)**