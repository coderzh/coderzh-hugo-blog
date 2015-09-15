---
categories:
- 技术文章
date: '2010-05-05'
title: Get IHTMLDocument2 for UI Automation in Python
url: /2010/05/05/Get-IHTMLDocument2-UIAutomation-Python/

---


<div>Some software embed ie control in win32 window as the User Interface, such as Internet   Explorer_Server. We can hardly identify the html control inner Internet   Explorer_Server through Spy++. So it takes a great pain to ui automation. This post, I will introduce a way for Internet   Explorer_Server automation. 

</div>

#### Get IHTMLDocument2 interface

Also see：[http://support.microsoft.com/kb/249232](http://support.microsoft.com/kb/249232)

Here is my python implentment：
<div><div><div class="cnblogs_code"><div><span style="color: #008000;">#</span><span style="color: #008000;">!/usr/bin/env&nbsp;python</span><span style="color: #008000;">
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
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">pythoncom.CoUninitialize()</span></div></div><span style="color: #008000;"></span></div></div>

#### Multithreading

IHTMLDocument2 is thread safe, we can not use it in any other thread except the main thread by default. If you want to use it in multi threads, write these code at the top of your file, and remenber do not explicit call pythoncom.CoInitializeEx(0) and pythoncom.CoUninitialize() :
<div><div><div class="cnblogs_code"><div><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Important&nbsp;for&nbsp;multithreading</span><span style="color: #008000;">
</span><span style="color: #000000;">sys.coinit_flags&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;0&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;pythoncom.COINIT_MULTITHREADED</span></div></div><span style="color: #008000;"></span></div></div>

Also see：[http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem](http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem "http://bytes.com/topic/python/answers/26897-multithreaded-com-server-problem")

&nbsp;

#### IHTMLDocument2 for UI Automation

Also see : [http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx](http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx "http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx")

Now, you can write your own UI Automation framework by IHTMLDocument2.

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/05/05/Get-IHTMLDocument2-UIAutomation-Python.html](http://www.cnblogs.com/coderzh/archive/2010/05/05/Get-IHTMLDocument2-UIAutomation-Python.html)**