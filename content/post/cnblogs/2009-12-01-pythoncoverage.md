---
categories:
- 技术文章
date: '2009-12-01'
title: Python 代码覆盖率统计工具 coverage.py
url: /2009/12/01/pythoncoverage/

---


coverage.py是一个用来统计python程序代码覆盖率的工具。它使用起来非常简单，并且支持最终生成界面友好的html报告。在最新版本中，还提供了分支覆盖的功能。

官方网站：
  
[http://nedbatchelder.com/code/coverage/](http://nedbatchelder.com/code/coverage/)&nbsp;

win32版本下载地址：
  
[http://pypi.python.org/pypi/coverage](http://pypi.python.org/pypi/coverage)

或者通过easy-install来安装： 

<div class="cnblogs_code">
<div class="cnblogs_code_open" id="cnblogs_code_open_d9d5f156-136f-4093-84fe-ef27e162cb54">
<div><span style="color: #000000;">easy_install&nbsp;coverage</span></div>
</div>
</div>

 装好后，在c:\Python25.cripts\（假设装在c盘）目录会有一个coverage.exe。通过这个exe基本上可以完成我们所有需要的功能。运行一下，如果发现少了那个模块，请先安装easy_install。

#### Coverage Command Line 

命令行使用说明： 详见：[http://nedbatchelder.com/code/coverage/cmd.html](http://nedbatchelder.com/code/coverage/cmd.html)

最关键核心的几个参数使用如下：

1. **run**

执行代码覆盖率统计，只需要通过coverage的run参数执行被统计代码即可。

<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_57e8d8c6-3d18-40ed-a3bd-bbe48d35c5d1"><div><span style="color: #000000;">$&nbsp;coverage&nbsp;run&nbsp;my_program.py&nbsp;arg1&nbsp;arg2</span></div></div></div>
<br />
跑完后，会自动生成一个覆盖率统计结果文件（data file）：.coverage。如果要修改这个默认的文件名也可以，只要设置COVERAGE_FILE环境变量。
<br />
2. **report**
<br />
有了覆盖率统计结果文件，只需要再运行report参数，就可以在命令里看到统计的结果。
<br />
<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_eb354b98-fdbc-4c5f-ad62-5bb225d11017"><div><span style="color: #000000;">$&nbsp;coverage&nbsp;report
Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stmts&nbsp;&nbsp;&nbsp;Exec&nbsp;&nbsp;Cover
</span><span style="color: #000000;">---------------------------------------------</span><span style="color: #000000;">
my_program&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">20</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">16</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">80</span><span style="color: #000000;">%</span><span style="color: #000000;">
my_module&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">15</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">13</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">86</span><span style="color: #000000;">%</span><span style="color: #000000;">
my_other_module&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">56</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">50</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">89</span><span style="color: #000000;">%</span><span style="color: #000000;">
</span><span style="color: #000000;">---------------------------------------------</span><span style="color: #000000;">
TOTAL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">91</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">79</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #000000;">87</span><span style="color: #000000;">%</span></div></div></div>

3. **html**

最帅最酷的功能了，直接生成html的测试报告。

<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_1f694398-3d9e-40b6-83c9-1b345ca3bd9d"><div><span style="color: #000000;">$&nbsp;coverage&nbsp;html&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">d&nbsp;covhtml</span></div></div></div>
<br />
生成的报告非常酷，直接关联代码，高亮显示覆盖和未覆盖的代码，支持排序。可以在这个地址预览一下：
  
[http://nedbatchelder.com/code/coverage/sample_html/](http://nedbatchelder.com/code/coverage/sample_html/)&nbsp;
<br />
效果如下：
<br />
![](http://images.cnblogs.com/cnblogs_com/coderzh/coverage/coverage1.jpg)&nbsp;
<br />
![](http://images.cnblogs.com/cnblogs_com/coderzh/coverage/coverage2.jpg)&nbsp;
<br />
4. **combine**
<br />
用过代码覆盖率工具的都知道，多份结果的合并至关重要。combine这个参数我琢磨了很久，开始总是合并不成功。后来终于明白了。执行合并操作很简单，只要把需要合并的覆盖率结果数据文件放在同一个目录里，然后执行：
<br />
<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_8324b692-6bd2-4c57-997f-9dce465925ac"><div><span style="color: #000000;">coverage&nbsp;combine</span></div></div></div>
<br />
&nbsp;即可。但是，其实对目录里的结果文件是有要求的，要求就是文件名的格式，需要合并的文件必须有同样的前缀，然后后面跟一个名称（通常是机器名），然后再跟一个数字（通常是进程ID），比如：
<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_2a28d3d2-1435-44dd-a179-520b7725a3ae"><div><span style="color: #000000;">.coverage.CoderZh.</span><span style="color: #000000;">1234</span><span style="color: #000000;">
.coverage.Cnblogs.</span><span style="color: #000000;">5678</span></div></div></div>

为了方便执行结果的合并，我们在前面执行统计时，在run参数后面跟一个-p参数，会自动生成符合合并条件的结果文件。

<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_942a2835-7bd5-4874-99eb-07542fb66bcf"><div><span style="color: #000000;">$&nbsp;coverage&nbsp;run&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">p&nbsp;my_program.py&nbsp;arg1&nbsp;arg2</span></div></div></div>
<br />
合并后，会再生成一个.coverage文件，然后再执行html查看合并后的报告吧。
<br />
其他几个**erase** **annotate** **debug** 参数就不介绍了。
<br />
#### Coverage API 
<br />
除了使用命令行，还可以在python代码中直接调用coverage模块执行代码覆盖率的统计。使用方法也非常简单：
<br />
<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div class="cnblogs_code_open" id="cnblogs_code_open_6ee3d71a-bc57-47d8-8632-c520c72ead7b"><div><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;coverage
<br />
cov&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;coverage.coverage()
cov.start()
<br />
</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;..&nbsp;run&nbsp;your&nbsp;code&nbsp;..</span><span style="color: #008000;">
</span><span style="color: #000000;">
cov.stop()
cov.save()</span></div></div></div>

<span style="color: #000000;">coverage</span>的构造函数可以设置结果文件的名称等。有个函数容易弄错，就是<tt>use_cache</tt>，如果设置的<tt>use_cache</tt>(0)，表示不在硬盘上读写结果文件。如果需要结果数据用来合并，一定要设置use_cache(1)。

coverage提供一些很好用的函数，如：<tt style="font-weight: bold;">exclude</tt>（排除统计的代码），<tt style="font-weight: bold;">html_report</tt>（生成html报告），<tt style="font-weight: bold;">report</tt>（控制台输出结果）

下篇讲讲如何在测试django应用时，编写一个自己的test runner来执行代码覆盖率的统计。 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/12/01/pythoncoverage.html](http://www.cnblogs.com/coderzh/archive/2009/12/01/pythoncoverage.html)**