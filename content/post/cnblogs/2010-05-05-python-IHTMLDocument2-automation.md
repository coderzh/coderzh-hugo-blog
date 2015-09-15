---
categories:
- 技术文章
date: '2010-05-05'
title: Python操作IHTMLDocument2用于自动化测试
url: /2010/05/05/python-IHTMLDocument2-automation/

---


<div>有些软件的界面采用Win32窗口嵌套一个IE控件，用Spy++只能识别出一个Internet  Explorer_Server控件。常用的几个API函数无法取到IE控件里面的内容，更无法对里面的控件进行操作，所以这给自动化带来了麻烦。本文将讲述如何使用Python获取IHTMLDocument2接口，用于自动化测试。

#### 获取IHTMLDocument2接口
参考：[http://support.microsoft.com/kb/249232](http://support.microsoft.com/kb/249232 "http://support.microsoft.com/kb/249232")
相应的Python实现代码如下：
</div><div class="cnblogs_code"><div><span style="color: #008000;">#</span><span style="color: #008000;">!/usr/bin/env&nbsp;python</span><span style="color: #008000;">
#</span><span style="color: #008000;">coding:utf-8</span><span style="color: #008000;">
</span><span style="color: #000000;">
</span><span style="color: #800080;">__author__</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">CoderZh</span><span style="color: #800000;">'</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;sys
<br />
</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Important&nbsp;for&nbsp;multithreading</span><span style="color: #008000;">
</span><span style="color: #000000;">sys.coinit_flags&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;0&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;pythoncom.COINIT_MULTITHREADED</span><span style="color: #008000;">
</span><span style="color: #000000;">
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;win32com
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;win32com.client
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;win32gui
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;win32con
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;pythoncom
<br />
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;getIEServer(hwnd,&nbsp;ieServer):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;win32gui.GetClassName(hwnd)&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">Internet&nbsp;Explorer_Server</span><span style="color: #800000;">'</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ieServer.append(hwnd)
<br />
</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__name__</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">__main__</span><span style="color: #800000;">'</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">pythoncom.CoInitializeEx(0)&nbsp;#&nbsp;not&nbsp;use&nbsp;this&nbsp;for&nbsp;multithreading</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;mainHwnd&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.FindWindow(</span><span style="color: #800000;">'</span><span style="color: #800000;">windowclass</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">windowtitle</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;mainHwnd:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ieServers&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.EnumChildWindows(mainHwnd,&nbsp;getIEServer,&nbsp;ieServers)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;len(ieServers)&nbsp;</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">&nbsp;0:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ieServer&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;ieServers[0]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.RegisterWindowMessage(</span><span style="color: #800000;">'</span><span style="color: #800000;">WM_HTML_GETOBJECT</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ret,&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.SendMessageTimeout(ieServer,&nbsp;msg,&nbsp;0,&nbsp;0,&nbsp;win32con.SMTO_ABORTIFHUNG,&nbsp;</span><span style="color: #000000;">1000</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ob&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;pythoncom.ObjectFromLresult(result,&nbsp;pythoncom.IID_IDispatch,&nbsp;0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doc&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32com.client.dynamic.Dispatch(ob)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;doc.url
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doc.all[</span><span style="color: #800000;">'</span><span style="color: #800000;">id</span><span style="color: #800000;">'</span><span style="color: #000000;">].click()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">pythoncom.CoUninitialize()</span></div></div>

#### 多线程操作
IHTMLDocument2是线程安全的，默认情况下不能在多线程中使用，否则会抛异常。但是在具体使用过程中，又必须使用多线程。解决办法就是上面的代码中的：
<div class="cnblogs_code"><div><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Important&nbsp;for&nbsp;multithreading</span><span style="color: #008000;">
</span><span style="color: #000000;">sys.coinit_flags&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;0&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;pythoncom.COINIT_MULTITHREADED</span></div></div>

这句必须在开头的时候设定，同时，不要再显示调用pythoncom.CoInitializeEx(0)和 pythoncom.CoUninitialize()。

参考：[http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem](http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem "http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem")

&nbsp;

#### IHTMLDocument2 接口

IHTMLDocument2接口有哪些方法，可以查询[http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx](http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx "http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx")

基本能够满足自动化测试的需要，可以在此基础上封装出更易使用的自动化UI测试框架。 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/05/05/python-IHTMLDocument2-automation.html](http://www.cnblogs.com/coderzh/archive/2010/05/05/python-IHTMLDocument2-automation.html)**