---
categories:
- 技术文章
date: '2010-05-02'
title: Python天天美味(36) - 用Python实现Spy++
url: /2010/05/02/python-cookbook-pyspy/

---


Spy++是微软出品的用来获取Window窗口信息的一个小工具。实现的原理其实不难，通过调用某些特定的Windows API即可。于是，我打算用Python也实现一个功能简化版本的小工具，取名叫PySpy++。Python中调用Windows API一般使用pywin32这套库，界面库我使用PyQT4。

### 
Spy++原理

Spy++中，最常用的一个功能，就是识别窗口。其中主要需要用到的Windows API有：

**获取当前鼠标位置**：
  <div class="cnblogs_code"><div><span style="color: #000000;">BOOL&nbsp;GetCursorPos(&nbsp;LPPOINT&nbsp;lpPoint&nbsp;);</span></div></div>
<br />
**获取位于指定位置的窗口句柄**：
  <div class="cnblogs_code"><div><span style="color: #000000;">HWND&nbsp;WindowFromPoint(&nbsp;POINT&nbsp;Point&nbsp;);</span></div></div>
<br />
**获取窗口类别**：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;GetClassName(&nbsp;HWND&nbsp;hWnd,&nbsp;LPTSTR&nbsp;lpClassName,&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nMaxCount&nbsp;);</span></div></div>
<br />
**获取窗口内容或标题**：
<br />
方法一：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;GetWindowText(&nbsp;HWND&nbsp;hWnd,&nbsp;LPTSTR&nbsp;lpString,&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nMaxCount&nbsp;);</span></div></div>
<br />
这个API有时候不能取到某些控件的值，因此，使用方法二。
<br />
方法二：
<br />
给窗口发送WM_GETTEXT消息：
  <div class="cnblogs_code"><div><span style="color: #000000;">LRESULT&nbsp;SendMessage(&nbsp;HWND&nbsp;hWnd,&nbsp;UINT&nbsp;Msg,&nbsp;WPARAM&nbsp;&nbsp;wParam,&nbsp;LPARAM&nbsp;lParam&nbsp;);</span></div></div>
<br />
**高亮选中的窗口**：
<br />
先获取当前窗口的大小，然后画一个矩形框。
<div class="cnblogs_code" onclick="cnblogs_code_show('b406a3cc-6fd5-4155-b3c5-661aeedad0eb')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_b406a3cc-6fd5-4155-b3c5-661aeedad0eb"><div><span style="color: #000000;">BOOL&nbsp;GetWindowRect(&nbsp;HWND&nbsp;hWnd,&nbsp;LPRECT&nbsp;lpRect&nbsp;);
<br />
BOOL&nbsp;Rectangle(
&nbsp;&nbsp;&nbsp;&nbsp;HDC&nbsp;hdc,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;handle&nbsp;to&nbsp;DC</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nLeftRect,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;x-coord&nbsp;of&nbsp;upper-left&nbsp;corner&nbsp;of&nbsp;rectangle</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nTopRect,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;y-coord&nbsp;of&nbsp;upper-left&nbsp;corner&nbsp;of&nbsp;rectangle</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nRightRect,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;x-coord&nbsp;of&nbsp;lower-right&nbsp;corner&nbsp;of&nbsp;rectangle</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;nBottomRect&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;y-coord&nbsp;of&nbsp;lower-right&nbsp;corner&nbsp;of&nbsp;rectangle</span><span style="color: #008000;">
</span><span style="color: #000000;">);</span></div></div></div>

鼠标移开窗口后，窗口需要恢复原状，需要重新刷新：
<div class="cnblogs_code"><div><span style="color: #000000;">BOOL&nbsp;InvalidateRect(
&nbsp;&nbsp;&nbsp;&nbsp;HWND&nbsp;hWnd,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;handle&nbsp;to&nbsp;window</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;CONST&nbsp;RECT</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;lpRect,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;rectangle&nbsp;coordinates</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;BOOL&nbsp;bErase&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;erase&nbsp;state</span><span style="color: #008000;">
</span><span style="color: #000000;">);
<br />
BOOL&nbsp;UpdateWindow(
&nbsp;&nbsp;&nbsp;&nbsp;HWND&nbsp;hWnd&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;handle&nbsp;to&nbsp;window</span><span style="color: #008000;">
</span><span style="color: #000000;">);
<br />
BOOL&nbsp;RedrawWindow(
&nbsp;&nbsp;&nbsp;&nbsp;HWND&nbsp;hWnd,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;handle&nbsp;to&nbsp;window</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;CONST&nbsp;RECT&nbsp;</span><span style="color: #000000;">*</span><span style="color: #000000;">lprcUpdate,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;update&nbsp;rectangle</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;HRGN&nbsp;hrgnUpdate,&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;handle&nbsp;to&nbsp;update&nbsp;region</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;UINT&nbsp;flags&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;array&nbsp;of&nbsp;redraw&nbsp;flags</span><span style="color: #008000;">
</span><span style="color: #000000;">);</span></div></div>

### PyWin32对应的函数

在Python中调用Windows API，首先下载PyWin32，地址：[http://pywin32.sourceforge.net/](http://pywin32.sourceforge.net/ "http://pywin32.sourceforge.net/")

安装完成后，打开帮助文档Python for Windows Documentation，里面有所有需要的东西，随时用来查看。

常用的API在win32api模块里，界面相关的API在win32gui模块里，API参数中定义的一些常量在win32con模块中。上面的Windows API对应PyWin32中的函数为：
<div class="cnblogs_code" onclick="cnblogs_code_show('0bb3057d-fe77-413c-862e-d5513ed8c35e')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_0bb3057d-fe77-413c-862e-d5513ed8c35e"><div><span style="color: #000000;">(int,&nbsp;int)&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**GetCursorPos**</span><span style="color: #000000;">()
int&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**WindowFromPoint**</span><span style="color: #000000;">(point)
string&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**GetClassName**</span><span style="color: #000000;">(hwnd)</span><span style="color: #000000;">
string&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**GetWindowText**</span><span style="color: #000000;">(hwnd)
int&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**SendMessage**</span><span style="color: #000000;">(hwnd,&nbsp;message&nbsp;,&nbsp;wparam&nbsp;,&nbsp;lparam&nbsp;)
(left,&nbsp;top,&nbsp;right,&nbsp;bottom)&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span><span style="color: #0000ff;">**GetWindowRect**</span><span style="color: #000000;">(hwnd)
win32gui.</span><span style="color: #0000ff;">**Rectangle**</span><span style="color: #000000;">(hdc,&nbsp;LeftRect,&nbsp;TopRect,&nbsp;RightRect,&nbsp;BottomRect)
win32gui.</span><span style="color: #0000ff;">**InvalidateRect**</span><span style="color: #000000;">(hWnd,&nbsp;Rect,&nbsp;Erase)
win32gui.</span><span style="color: #0000ff;">**UpdateWindow**</span><span style="color: #000000;">(hwnd)</span><span style="color: #000000;">
win32gui.</span><span style="color: #0000ff;">**RedrawWindow**</span><span style="color: #000000;">(hWnd,&nbsp;rcUpdate,&nbsp;hrgnUpdate,&nbsp;flags)</span></div></div></div>

### 代码实现

界面库使用PyQT4，参考资料可以从我之前的一篇博客里了解：[PyQt4 学习资料汇总](http://www.cnblogs.com/coderzh/archive/2009/06/28/1512654.html)

工具对话框窗口有两个控件，一个是QLabel控件，一个是QTextEdit控件。QLabel控件就是那个用来鼠标按下去后去捕捉窗口，QTextEdit控件用来显示窗口的信息。为了让QTextEdit响应自定义的鼠标事件，我创建了一个自定义QLabel控件SpyLabel，继承自QLabel。
  <div class="cnblogs_code" onclick="cnblogs_code_show('6f02d0d9-05ac-42f9-976b-64d94619fb30')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_6f02d0d9-05ac-42f9-976b-64d94619fb30"><div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;SpyLabel(QtGui.QLabel):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;parent&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;None):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QtGui.QLabel.</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;parent)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.parent&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;parent
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.spying&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;False
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.rectanglePen&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.CreatePen(win32con.PS_SOLID,&nbsp;</span><span style="color: #000000;">3</span><span style="color: #000000;">,&nbsp;win32api.RGB(</span><span style="color: #000000;">255</span><span style="color: #000000;">,&nbsp;0,&nbsp;0))
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.prevWindow&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;None
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.**setCursor**(QtCore.Qt.SizeAllCursor)</span></div></div></div>  

SpyLabel中处理鼠标移动事件：
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;mouseMoveEvent(self,&nbsp;event):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.spying:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;curX,&nbsp;curY&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.GetCursorPos()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hwnd&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.</span>**<span style="color: #0000ff;">WindowFromPoint</span>**<span style="color: #000000;">((curX,&nbsp;curY))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.checkWindowValidity(hwnd):&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.prevWindow:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.refreshWindow(self.prevWindow)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.prevWindow&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;hwnd
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.highlightWindow(hwnd)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.displayWindowInformation(hwnd)</span></div></div>

鼠标松开事件：
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;mouseReleaseEvent(self,&nbsp;event):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.spying:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.prevWindow:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.refreshWindow(self.prevWindow)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.ReleaseCapture()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.spying&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;False</span></div></div>

高亮窗口的函数：
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;highlightWindow(self,&nbsp;hwnd):
&nbsp;&nbsp;&nbsp;&nbsp;left,&nbsp;top,&nbsp;right,&nbsp;bottom&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.GetWindowRect(hwnd)
&nbsp;&nbsp;&nbsp;&nbsp;windowDc&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.GetWindowDC(hwnd)
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;windowDc:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prevPen&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.SelectObject(windowDc,&nbsp;self.rectanglePen)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prevBrush&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.SelectObject(windowDc,&nbsp;win32gui.GetStockObject(win32con.HOLLOW_BRUSH))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.</span>**<span style="color: #0000ff;">Rectangle</span>**<span style="color: #000000;">(windowDc,&nbsp;0,&nbsp;0,&nbsp;right&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">&nbsp;left,&nbsp;bottom&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">&nbsp;top)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.SelectObject(windowDc,&nbsp;prevPen)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.SelectObject(windowDc,&nbsp;prevBrush)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32gui.ReleaseDC(hwnd,&nbsp;windowDc)</span></div></div>

刷新窗口的函数：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;refreshWindow(self,&nbsp;hwnd):
&nbsp;&nbsp;&nbsp;&nbsp;win32gui.</span>**<span style="color: #0000ff;">InvalidateRect</span>**<span style="color: #000000;">(hwnd,&nbsp;None,&nbsp;True)
&nbsp;&nbsp;&nbsp;&nbsp;win32gui.</span>**<span style="color: #0000ff;">UpdateWindow</span>**<span style="color: #000000;">(hwnd)
&nbsp;&nbsp;&nbsp;&nbsp;win32gui.</span>**<span style="color: #0000ff;">RedrawWindow</span>**<span style="color: #000000;">(hwnd,&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None,&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None,&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32con.RDW_FRAME</span><span style="color: #000000;">|</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32con.RDW_INVALIDATE</span><span style="color: #000000;">|</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32con.RDW_UPDATENOW</span><span style="color: #000000;">|</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;win32con.RDW_ALLCHILDREN)</span></div></div>  

显示窗口信息：

<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;displayWindowInformation(self,&nbsp;hwnd):
&nbsp;&nbsp;&nbsp;&nbsp;className&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.GetClassName(hwnd)
&nbsp;&nbsp;&nbsp;&nbsp;buf_size&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;win32gui.</span>**<span style="color: #0000ff;">SendMessage</span>**<span style="color: #000000;">(hwnd,&nbsp;win32con.WM_GETTEXTLENGTH,&nbsp;0,&nbsp;0)
&nbsp;&nbsp;&nbsp;&nbsp;buffer&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.PyMakeBuffer(buf_size)
&nbsp;&nbsp;&nbsp;&nbsp;win32gui.</span>**<span style="color: #0000ff;">SendMessage</span>**<span style="color: #000000;">(hwnd,&nbsp;win32con.WM_GETTEXT,&nbsp;buf_size,&nbsp;buffer)
&nbsp;&nbsp;&nbsp;&nbsp;windowText&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;buffer[:buf_size]
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">try</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;windowText&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;unicode(windowText,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">gbk</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">pass</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;message&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[</span><span style="color: #800000;">'</span><span style="color: #800000;">Handle:\t</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;str(hwnd),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">Class&nbsp;Name:\t</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;className,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">Window&nbsp;Text:\t</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;windowText]
&nbsp;&nbsp;&nbsp;&nbsp;self.output(</span><span style="color: #800000;">'</span><span style="color: #800000;">\r\n</span><span style="color: #800000;">'</span><span style="color: #000000;">.join(message))</span></div></div>

注意到上面SendMessage函数，需要传入一个分配的缓冲区，用于获取返回的内容。这里使用了：
<div class="cnblogs_code"><div><span style="color: #000000;">buffer&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;win32gui.PyMakeBuffer(buf_size)</span></div></div>  
<br />
由于返回的内容中可能有中文，因此使用unicode(windowText, 'gbk')进行一下转换。   
<br />
### 
演示
<br />
![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/Python36PythonSpy_B49/image_thumb_1.png "image") 
<br />
![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/Python36PythonSpy_B49/image_thumb.png "image") 
<br />
&nbsp;
<br />
二进制下载：
  
[http://pyspyplusplus.googlecode.com/files/pyspy++.exe](http://pyspyplusplus.googlecode.com/files/pyspy%2B%2B.exe)&nbsp;
<br />
源代码：
  
[http://code.google.com/p/pyspyplusplus/](http://code.google.com/p/pyspyplusplus/)&nbsp;
<br />
&nbsp;
<br />
&nbsp;
<br />
#### [Python  天天美味系列（总）](http://www.cnblogs.com/coderzh/archive/2008/07/08/pythoncookbook.html)  
<br />
[Python  天天美味(31) - python数据结构与算法之插入排序](http://www.cnblogs.com/coderzh/archive/2008/09/21/1295434.html)&nbsp; 
  
[Python  天天美味(32) - python数据结构与算法之堆排序](http://www.cnblogs.com/coderzh/archive/2008/09/22/1296195.html)&nbsp;
  
[Python  天天美味(33) - 五分钟理解元类（Metaclasses）[转]](http://www.cnblogs.com/coderzh/archive/2008/12/07/1349735.html)
<br />
[Python  天天美味(34) - Decorators详解](http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html) 
  
[Python  天天美味(35) - 细品lambda](http://www.cnblogs.com/coderzh/archive/2010/04/30/python-cookbook-lambda.html)&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/05/02/python-cookbook-pyspy.html](http://www.cnblogs.com/coderzh/archive/2010/05/02/python-cookbook-pyspy.html)**