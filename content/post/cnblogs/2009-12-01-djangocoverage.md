---
categories:
- 技术文章
date: '2009-12-01'
title: Django单元测试案例代码覆盖率统计 - 自定义test runner
url: /2009/12/01/djangocoverage/

---


如何在Django中编写单元测试案例，以及使用测试用的test_setting和test runner，见：[django单元测试历险记](http://www.cnblogs.com/coderzh/archive/2009/11/15/1603315.html)

 代码很好懂，不做什么解释了。如果需要拷过去，根据自己的需要修改一下，不是什么难事。

test_settings.py

<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)
<div class="cnblogs_code_open" id="cnblogs_code_open_c390a331-4040-415e-bdc1-09d257622a0e">
<div><span style="color: #000000;">COVERAGE_MODULES&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[</span><span style="color: #800000;">'</span><span style="color: #800000;">testapp.models</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">testapp.lib</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">testapp.common</span><span style="color: #800000;">'</span><span style="color: #000000;">]</span></div>
</div>
<span style="color: #000000;">TEST_RUNNER&nbsp;&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">testapp.testrunner.test_runner_with_coverage</span><span style="color: #800000;">'</span>

</div>

testrunner.py
<div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](http://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)<span class="cnblogs_code_collapse">代码</span><div class="cnblogs_code_open" id="cnblogs_code_open_51fbc306-707b-437f-a50d-cf4a9662504b" style="display: none;"><div><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;os,&nbsp;shutil,&nbsp;sys,&nbsp;unittest
<br />
</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Look&nbsp;for&nbsp;coverage.py&nbsp;in&nbsp;__file__/lib&nbsp;as&nbsp;well&nbsp;as&nbsp;sys.path</span><span style="color: #008000;">
</span><span style="color: #000000;">sys.path&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[os.path.join(os.path.dirname(</span><span style="color: #800080;">__file__</span><span style="color: #000000;">),&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">lib</span><span style="color: #800000;">"</span><span style="color: #000000;">)]&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;sys.path
<br />
</span><span style="color: #0000ff;">from</span><span style="color: #000000;">&nbsp;coverage&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;coverage
</span><span style="color: #0000ff;">from</span><span style="color: #000000;">&nbsp;inspect&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;getmembers,&nbsp;ismodule
<br />
</span><span style="color: #0000ff;">from</span><span style="color: #000000;">&nbsp;django.test.simple&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;run_tests&nbsp;as&nbsp;django_test_runner
<br />
</span><span style="color: #0000ff;">from</span><span style="color: #000000;">&nbsp;django.conf&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;settings
<br />
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_all_coverage_modules(module_path):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #800000;">
&nbsp;&nbsp;&nbsp;&nbsp;Returns&nbsp;all&nbsp;possible&nbsp;modules&nbsp;to&nbsp;report&nbsp;coverage&nbsp;on,&nbsp;even&nbsp;if&nbsp;they
&nbsp;&nbsp;&nbsp;&nbsp;aren't&nbsp;loaded.
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;app_path&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;module_path.split(</span><span style="color: #800000;">'</span><span style="color: #800000;">.</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;app_package&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__import__</span><span style="color: #000000;">(module_path,&nbsp;{},&nbsp;{},&nbsp;app_path[</span><span style="color: #000000;">-</span><span style="color: #000000;">1</span><span style="color: #000000;">])
&nbsp;&nbsp;&nbsp;&nbsp;app_dirpath&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;app_package.</span><span style="color: #800080;">__path__</span><span style="color: #000000;">[</span><span style="color: #000000;">-</span><span style="color: #000000;">1</span><span style="color: #000000;">]
<br />
&nbsp;&nbsp;&nbsp;&nbsp;mod_list&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;root,&nbsp;dirs,&nbsp;files&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;os.walk(app_dirpath):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_path&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;app_path&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;root[len(app_dirpath):].split(os.path.sep)[</span><span style="color: #000000;">1</span><span style="color: #000000;">:]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;file&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;files:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;file.lower().endswith(</span><span style="color: #800000;">'</span><span style="color: #800000;">.py</span><span style="color: #800000;">'</span><span style="color: #000000;">):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod_name&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;file[:</span><span style="color: #000000;">-</span><span style="color: #000000;">3</span><span style="color: #000000;">].lower()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">try</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__import__</span><span style="color: #000000;">(</span><span style="color: #800000;">'</span><span style="color: #800000;">.</span><span style="color: #800000;">'</span><span style="color: #000000;">.join(root_path&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;[mod_name]),&nbsp;{},&nbsp;{},
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod_name)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">&nbsp;ImportError:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">pass</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">else</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mod_list.append(mod)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;mod_list
<br />
</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;test_runner_with_coverage(test_labels,&nbsp;verbosity</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">,&nbsp;interactive</span><span style="color: #000000;">=</span><span style="color: #000000;">True,&nbsp;extra_tests</span><span style="color: #000000;">=</span><span style="color: #000000;">[]):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #800000;">Custom&nbsp;test&nbsp;runner.&nbsp;&nbsp;Follows&nbsp;the&nbsp;django.test.simple.run_tests()&nbsp;interface.</span><span style="color: #800000;">"""</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Start&nbsp;code&nbsp;coverage&nbsp;before&nbsp;anything&nbsp;else&nbsp;if&nbsp;necessary</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;cov&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;None
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;hasattr(settings,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">COVERAGE_MODULES</span><span style="color: #800000;">'</span><span style="color: #000000;">):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;coverage()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov.use_cache(</span><span style="color: #000000;">1</span><span style="color: #000000;">)&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Do&nbsp;not&nbsp;cache&nbsp;any&nbsp;of&nbsp;the&nbsp;coverage.py&nbsp;stuff</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">cov.exclude('if&nbsp;__name__&nbsp;==&nbsp;.__main__.:')</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov.start()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;test_results&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;django_test_runner(test_labels,&nbsp;verbosity,&nbsp;interactive,&nbsp;extra_tests)
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Stop&nbsp;code&nbsp;coverage&nbsp;after&nbsp;tests&nbsp;have&nbsp;completed</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;hasattr(settings,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">COVERAGE_MODULES</span><span style="color: #800000;">'</span><span style="color: #000000;">):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov.stop()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Print&nbsp;code&nbsp;metrics&nbsp;header</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">''</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">----------------------------------------------------------------------</span><span style="color: #800000;">'</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">&nbsp;Unit&nbsp;Test&nbsp;Code&nbsp;Coverage&nbsp;Results</span><span style="color: #800000;">'</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">----------------------------------------------------------------------</span><span style="color: #800000;">'</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Report&nbsp;code&nbsp;coverage&nbsp;metrics</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;hasattr(settings,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">COVERAGE_MODULES</span><span style="color: #800000;">'</span><span style="color: #000000;">):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;coverage_modules&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;module&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;settings.COVERAGE_MODULES:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;coverage_modules.extend(get_all_coverage_modules(module))
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov.report(coverage_modules,&nbsp;show_missing</span><span style="color: #000000;">=</span><span style="color: #000000;">1</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">cov.html_report(directory='covhtml')</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">cov.combine()</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cov.save()
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">#</span><span style="color: #008000;">&nbsp;Print&nbsp;code&nbsp;metrics&nbsp;footer</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">----------------------------------------------------------------------</span><span style="color: #800000;">'</span><span style="color: #000000;">
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;test_results</span></div></div></div>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/12/01/djangocoverage.html](http://www.cnblogs.com/coderzh/archive/2009/12/01/djangocoverage.html)**