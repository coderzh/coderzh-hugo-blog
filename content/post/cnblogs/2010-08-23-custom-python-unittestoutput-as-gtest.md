---
categories:
- 技术文章
date: '2010-08-23'
title: Python 天天美味(37) - 让python的unittest像gtest一样输出
url: /2010/08/23/custom-python-unittestoutput-as-gtest/

---


Python自带的unittest已经很简单易用了，不过我一直不喜欢的是它的命令行输出，格式显得有点乱。而我比较喜欢的是gtest的命令行输出格式，用不同的颜色进行标识，整齐划一，非常明了。于是，我扩展一下Python的unittest模块，让它也能输出和gtest一样好看的命令行结果。

首先，我们先来看看unittest默认的命令行输出结果。这里，我先随便写两个测试案例，让其中一个通过，另外一个不通过，然后查看一下测试结果。

<div class="cnblogs_code" onclick="cnblogs_code_show('cff78c40-6d56-46dc-ae5c-a0ce21bd7c19')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)
<div id="cnblogs_code_open_cff78c40-6d56-46dc-ae5c-a0ce21bd7c19">
<div><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;unitest

</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;FooTest(unittest.TestCase):

&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;setUp(self):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.a&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">

&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;testPass(self):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.a&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;self.a&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.assertEqual(</span><span style="color: #000000;">2</span><span style="color: #000000;">,&nbsp;self.a)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;testFail(self):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.a&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;self.a&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.assertEqual(</span><span style="color: #000000;">3</span><span style="color: #000000;">,&nbsp;self.a)</span></div>
</div>
</div>

main函数，调用unittest自己的TextTestRunner：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__name__</span><span style="color: #000000;">==</span><span style="color: #800000;">'</span><span style="color: #800000;">__main__</span><span style="color: #800000;">'</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;unittest.main()</span></div>
</div>

输出的结果：

![](http://images.cnblogs.com/cnblogs_com/coderzh/unittestoutput.jpg)

&nbsp;

有点凌乱（当然，可能你并不觉得），好的，接下来开始实现一个自定义的TestRunner，让unittest输出和gtest一样，使用不同的颜色。

&nbsp;

这个过程其实很简单，主要分为两个步骤：

1. 编写自定义的TestRunner类，执行其中的run方法，控制整个测试的过程和输出。参照unitest自己的TextTestRunner方法就好了。只是把输出部分做一些修改。

2. 编写自定义的TestResult类，继承自unittest中的TestResult类。重写其中几个方法，也都是修改输出内容的部分。

&nbsp;

当然，我们还需要在命令行中输出不同的颜色。

如果你不是使用的Windows，可以参照：[http://code.activestate.com/recipes/475116-using-terminfo-for-portable-color-output-cursor-co/](http://code.activestate.com/recipes/475116-using-terminfo-for-portable-color-output-cursor-co/) 

<span>如果你使用的是Windows，其实只要调用一个Windows API就好了。这个API就是</span>**<span>SetConsoleTextAttribute</span>**<span>。见下面的代码：</span>

<div class="cnblogs_code">
<div><span style="color: #008000;">#</span><span style="color: #008000;">#&nbsp;&nbsp;http://code.activestate.com/recipes/496901/&nbsp;(r3)</span><span style="color: #008000;">
<br />
#</span><span style="color: #008000;">&nbsp;See&nbsp;http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp</span><span style="color: #008000;">
<br />
#</span><span style="color: #008000;">&nbsp;for&nbsp;information&nbsp;on&nbsp;Windows&nbsp;APIs.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">STD_INPUT_HANDLE&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">10</span><span style="color: #000000;">
<br />
STD_OUTPUT_HANDLE</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">11</span><span style="color: #000000;">
<br />
STD_ERROR_HANDLE&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">12</span><span style="color: #000000;">
<br />
FOREGROUND_WHITE&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x0007</span><span style="color: #000000;">
<br />
FOREGROUND_BLUE&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x01</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;text&nbsp;color&nbsp;contains&nbsp;blue.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">FOREGROUND_GREEN</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x02</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;text&nbsp;color&nbsp;contains&nbsp;green.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">FOREGROUND_RED&nbsp;&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x04</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;text&nbsp;color&nbsp;contains&nbsp;red.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">FOREGROUND_INTENSITY&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x08</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;text&nbsp;color&nbsp;is&nbsp;intensified.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">FOREGROUND_YELLOW&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;FOREGROUND_RED&nbsp;</span><span style="color: #000000;">|</span><span style="color: #000000;">&nbsp;FOREGROUND_GREEN
<br />
BACKGROUND_BLUE&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x10</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;background&nbsp;color&nbsp;contains&nbsp;blue.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">BACKGROUND_GREEN</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x20</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;background&nbsp;color&nbsp;contains&nbsp;green.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">BACKGROUND_RED&nbsp;&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x40</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;background&nbsp;color&nbsp;contains&nbsp;red.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">BACKGROUND_INTENSITY&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">0x80</span><span style="color: #000000;">&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;background&nbsp;color&nbsp;is&nbsp;intensified.</span><span style="color: #008000;">
<br />
</span><span style="color: #000000;">
<br />
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;ctypes
<br />
std_out_handle&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
<br />
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;set_color(color,&nbsp;handle</span><span style="color: #000000;">=</span><span style="color: #000000;">std_out_handle):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #800000;">(color)&nbsp;-&gt;&nbsp;BOOL&nbsp;&nbsp;&nbsp;&nbsp;
<br />
&nbsp;&nbsp;&nbsp;&nbsp;Example:&nbsp;set_color(FOREGROUND_GREEN&nbsp;|&nbsp;FOREGROUND_INTENSITY)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;bool&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;ctypes.windll.kernel32.SetConsoleTextAttribute(handle,&nbsp;color)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;bool</span></div>
</div>

#### TestRunner类

<div class="cnblogs_code">
<div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;MyTestRunner:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;stream</span><span style="color: #000000;">=</span><span style="color: #000000;">sys.stderr,&nbsp;descriptions</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">,&nbsp;verbosity</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;_ColorWritelnDecorator(stream)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.descriptions&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;descriptions
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.verbosity&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;verbosity
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;run(self,&nbsp;test):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;MyTestResult(self.stream,&nbsp;self.descriptions,&nbsp;self.verbosity)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.yellow(</span><span style="color: #800000;">'</span><span style="color: #800000;">Note:&nbsp;Your&nbsp;Unit&nbsp;Tests&nbsp;Starts</span><span style="color: #800000;">'</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;time.time()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test(result)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stopTime&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;time.time()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeTaken&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;stopTime&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">&nbsp;startTime
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.green(result.separator2)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;result.testsRun
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(</span><span style="color: #800000;">"</span><span style="color: #800000;">Ran&nbsp;%d&nbsp;test%s&nbsp;in&nbsp;%.3fs</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(run,&nbsp;run&nbsp;</span><span style="color: #000000;">!=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">and</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">s</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">or</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">""</span><span style="color: #000000;">,&nbsp;timeTaken))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failed,&nbsp;errored&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;map(len,&nbsp;(result.failures,&nbsp;result.errors))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.green(</span><span style="color: #800000;">"</span><span style="color: #800000;">[&nbsp;&nbsp;PASSED&nbsp;&nbsp;]&nbsp;%d&nbsp;tests</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;(run&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">&nbsp;failed&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">&nbsp;errored))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">not</span><span style="color: #000000;">&nbsp;result.wasSuccessful():
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;errorsummary&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">""</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;failed:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.red(</span><span style="color: #800000;">"</span><span style="color: #800000;">[&nbsp;&nbsp;FAILED&nbsp;&nbsp;]&nbsp;%d&nbsp;tests,&nbsp;listed&nbsp;below:</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;failed)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;failedtest,&nbsp;failederorr&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;result.failures:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.red(</span><span style="color: #800000;">"</span><span style="color: #800000;">[&nbsp;&nbsp;FAILED&nbsp;&nbsp;]&nbsp;%s</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;failedtest)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;errored:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.red(</span><span style="color: #800000;">"</span><span style="color: #800000;">[&nbsp;&nbsp;ERRORED&nbsp;]&nbsp;%d&nbsp;tests</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;errored)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;erroredtest,&nbsp;erorrmsg&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;result.errors:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.red(</span><span style="color: #800000;">"</span><span style="color: #800000;">[&nbsp;&nbsp;ERRORED&nbsp;]&nbsp;%s</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;erroredtest)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;failed:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(</span><span style="color: #800000;">"</span><span style="color: #800000;">%d&nbsp;ERRORED&nbsp;TEST</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;failed)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;errored:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(</span><span style="color: #800000;">"</span><span style="color: #800000;">%d&nbsp;ERRORED&nbsp;TEST</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;errored)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;result</span></div>
</div>

#### TestResult类

<div class="cnblogs_code">
<div><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;MyTestResult(unittest.TestResult):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;separator1&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">[----------]&nbsp;</span><span style="color: #800000;">'</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;separator2&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">[==========]&nbsp;</span><span style="color: #800000;">'</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;stream</span><span style="color: #000000;">=</span><span style="color: #000000;">sys.stderr,&nbsp;descriptions</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">,&nbsp;verbosity</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest.TestResult.</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;stream
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.showAll&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;verbosity&nbsp;</span><span style="color: #000000;">&gt;</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.dots&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;verbosity&nbsp;</span><span style="color: #000000;">==</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">1</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.descriptions&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;descriptions
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;getDescription(self,&nbsp;test):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.descriptions:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;test.shortDescription()&nbsp;</span><span style="color: #0000ff;">or</span><span style="color: #000000;">&nbsp;str(test)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">else</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;str(test)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;startTest(self,&nbsp;test):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.green(</span><span style="color: #800000;">'</span><span style="color: #800000;">[&nbsp;Run&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]&nbsp;</span><span style="color: #800000;">'</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(self.getDescription(test))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest.TestResult.startTest(self,&nbsp;test)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.showAll:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(self.getDescription(test))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(</span><span style="color: #800000;">"</span><span style="color: #800000;">&nbsp;...&nbsp;</span><span style="color: #800000;">"</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;addSuccess(self,&nbsp;test):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest.TestResult.addSuccess(self,&nbsp;test)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.showAll:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(</span><span style="color: #800000;">"</span><span style="color: #800000;">ok</span><span style="color: #800000;">"</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">elif</span><span style="color: #000000;">&nbsp;self.dots:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.green(</span><span style="color: #800000;">'</span><span style="color: #800000;">[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OK&nbsp;]&nbsp;</span><span style="color: #800000;">'</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(self.getDescription(test))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;addError(self,&nbsp;test,&nbsp;err):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest.TestResult.addError(self,&nbsp;test,&nbsp;err)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.showAll:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(</span><span style="color: #800000;">"</span><span style="color: #800000;">ERROR</span><span style="color: #800000;">"</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">elif</span><span style="color: #000000;">&nbsp;self.dots:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(</span><span style="color: #800000;">'</span><span style="color: #800000;">E</span><span style="color: #800000;">'</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;addFailure(self,&nbsp;test,&nbsp;err):
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unittest.TestResult.addFailure(self,&nbsp;test,&nbsp;err)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;self.showAll:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(</span><span style="color: #800000;">"</span><span style="color: #800000;">FAIL</span><span style="color: #800000;">"</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">elif</span><span style="color: #000000;">&nbsp;self.dots:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.red(</span><span style="color: #800000;">'</span><span style="color: #800000;">[&nbsp;&nbsp;FAILED&nbsp;&nbsp;]&nbsp;</span><span style="color: #800000;">'</span><span style="color: #000000;">)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.writeln(self.getDescription(test))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.stream.write(self._exc_info_to_string(err,&nbsp;test))</span></div>
</div>

#### 执行

<div class="cnblogs_code">
<div><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__name__</span><span style="color: #000000;">==</span><span style="color: #800000;">'</span><span style="color: #800000;">__main__</span><span style="color: #800000;">'</span><span style="color: #000000;">:
<br />
&nbsp;&nbsp;&nbsp;&nbsp;unittest.main(testRunner</span><span style="color: #000000;">=</span><span style="color: #000000;">MyTestRunner())</span></div>
</div>

&nbsp;

#### 效果

![](http://images.cnblogs.com/cnblogs_com/coderzh/myunittestoutput.jpg)

&nbsp;

(哈哈，简直一山寨版gtest的输出啊！~)

&nbsp;

代码下载： [http://coderzh.googlecode.com/svn/trunk/CodeSnippet/myunittest.py](http://coderzh.googlecode.com/svn/trunk/CodeSnippet/myunittest.py)
  
[Python 天天美味(32) - python数据结构与算法之堆排序](http://www.cnblogs.com/coderzh/archive/2008/09/22/1296195.html)&nbsp;
  
[Python 天天美味(33) - 五分钟理解元类（Metaclasses）[转]](http://www.cnblogs.com/coderzh/archive/2008/12/07/1349735.html)
  
[Python 天天美味(34) - Decorators详解](http://www.cnblogs.com/coderzh/archive/2010/04/27/python-cookbook33-Decorators.html)
  
[Python 天天美味(35) - 细品lambda](http://www.cnblogs.com/coderzh/archive/2010/04/30/python-cookbook-lambda.html) 
  
[Python 天天美味(36) - 用Python实现Spy++](http://www.cnblogs.com/coderzh/archive/2010/05/02/python-cookbook-pyspy.html)&nbsp;


**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/08/23/custom-python-unittestoutput-as-gtest.html](http://www.cnblogs.com/coderzh/archive/2010/08/23/custom-python-unittestoutput-as-gtest.html)**