---
categories:
- 技术文章
date: '2010-01-01'
title: Tornado Unit Testing - Tornado应用的单元测试
url: /2010/01/01/Tornado-Unit-Testing/

---


之前在测试Django应用时，使用了非常方便的django.test.TestCase。在测试Tornado时，我也包装了一个TestCase类，提供和Django一样便捷的测试方法。最终，测试案例的代码将会是这样：
<div class="cnblogs_code"><div><span style="color: #0000ff;">from</span><span style="color: #000000;">&nbsp;testclient&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;TestCase
<br />
</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;QueryTest(TestCase):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;setUp(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">pass</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;test_query(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;open(</span><span style="color: #800000;">'</span><span style="color: #800000;">uploadfile.dat</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">rb</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;response&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;self.client.post(</span><span style="color: #800000;">'</span><span style="color: #800000;">/query</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;{&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">a</span><span style="color: #800000;">'</span><span style="color: #000000;">:&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">1</span><span style="color: #800000;">'</span><span style="color: #000000;">,&nbsp;<span style="color: #800000;">'</span><span style="color: #800000;">b</span><span style="color: #800000;">'</span><span style="color: #000000;">:&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">2</span><span style="color: #800000;">'</span><span style="color: #000000;">,</span> </span><span style="color: #800000;">'upload</span><span style="color: #800000;">'</span><span style="color: #000000;">:&nbsp;file&nbsp;})
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.failUnlessEqual(response.status_code,&nbsp;</span><span style="color: #000000;">200</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.failUnlessEqual(response.content,&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">ok</span><span style="color: #800000;">'</span><span style="color: #000000;">)</span></div></div>
  
[testclient.py](http://coderzh.googlecode.com/svn/trunk/CodeSnippet/testclient.py)的代码如下：&nbsp;
<div class="cnblogs_code" onclick="cnblogs_code_show('fff10722-a93a-42d1-afd6-002962c65b03')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](http://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)<span class="cnblogs_code_collapse">代码</span><div id="cnblogs_code_open_fff10722-a93a-42d1-afd6-002962c65b03"><div><span style="color: #008000;">#</span><span style="color: #008000;">!/usr/bin/env&nbsp;python</span><span style="color: #008000;">
#</span><span style="color: #008000;">coding:utf-8</span><span style="color: #008000;">
#
#</span><span style="color: #008000;">&nbsp;Copyright&nbsp;2009&nbsp;CoderZh.com.</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;Licensed&nbsp;under&nbsp;the&nbsp;Apache&nbsp;License,&nbsp;Version&nbsp;2.0&nbsp;(the&nbsp;"License");</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;you&nbsp;may&nbsp;not&nbsp;use&nbsp;this&nbsp;file&nbsp;except&nbsp;in&nbsp;compliance&nbsp;with&nbsp;the&nbsp;License.</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;You&nbsp;may&nbsp;obtain&nbsp;a&nbsp;copy&nbsp;of&nbsp;the&nbsp;License&nbsp;at</span><span style="color: #008000;">
#
#</span><span style="color: #008000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://www.apache.org/licenses/LICENSE-2.0</span><span style="color: #008000;">
#
#</span><span style="color: #008000;">&nbsp;Unless&nbsp;required&nbsp;by&nbsp;applicable&nbsp;law&nbsp;or&nbsp;agreed&nbsp;to&nbsp;in&nbsp;writing,&nbsp;software</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;distributed&nbsp;under&nbsp;the&nbsp;License&nbsp;is&nbsp;distributed&nbsp;on&nbsp;an&nbsp;"AS&nbsp;IS"&nbsp;BASIS,</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;WITHOUT&nbsp;WARRANTIES&nbsp;OR&nbsp;CONDITIONS&nbsp;OF&nbsp;ANY&nbsp;KIND,&nbsp;either&nbsp;express&nbsp;or&nbsp;implied.</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;See&nbsp;the&nbsp;License&nbsp;for&nbsp;the&nbsp;specific&nbsp;language&nbsp;governing&nbsp;permissions&nbsp;and</span><span style="color: #008000;">
#</span><span style="color: #008000;">&nbsp;limitations&nbsp;under&nbsp;the&nbsp;License.</span><span style="color: #008000;">
</span><span style="color: #000000;">
</span><span style="color: #800080;">__author__</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">CoderZh</span><span style="color: #800000;">'</span><span style="color: #000000;">

</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;tornado.ioloop
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;unittest
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;mimetypes

</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;tornado.httpclient
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;tornado.ioloop

TEST_PORT&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">8989</span><span style="color: #000000;">

</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;encode_multipart_formdata(fields,&nbsp;files):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #800000;">
&nbsp;&nbsp;&nbsp;&nbsp;fields&nbsp;is&nbsp;a&nbsp;sequence&nbsp;of&nbsp;(name,&nbsp;value)&nbsp;elements&nbsp;for&nbsp;regular&nbsp;form&nbsp;fields.
&nbsp;&nbsp;&nbsp;&nbsp;files&nbsp;is&nbsp;a&nbsp;sequence&nbsp;of&nbsp;(name,&nbsp;filename,&nbsp;value)&nbsp;elements&nbsp;for&nbsp;data&nbsp;to&nbsp;be&nbsp;uploaded&nbsp;as&nbsp;files
&nbsp;&nbsp;&nbsp;&nbsp;Return&nbsp;(content_type,&nbsp;body)&nbsp;ready&nbsp;for&nbsp;httplib.HTTP&nbsp;instance
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;BOUNDARY&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">----------ThIs_Is_tHe_bouNdaRY_$</span><span style="color: #800000;">'</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;CRLF&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">\r\n</span><span style="color: #800000;">'</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;L&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;(key,&nbsp;value)&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;fields:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">--</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;BOUNDARY)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">Content-Disposition:&nbsp;form-data;&nbsp;name="%s"</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;key)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">''</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(value)
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;(key,&nbsp;filename,&nbsp;value)&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;files:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">--</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;BOUNDARY)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">Content-Disposition:&nbsp;form-data;&nbsp;name="%s";&nbsp;filename="%s"</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;(key,&nbsp;filename))
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">Content-Type:&nbsp;%s</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;get_content_type(filename))
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">''</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L.append(value)
&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">'</span><span style="color: #800000;">--</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;BOUNDARY&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">--</span><span style="color: #800000;">'</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;L.append(</span><span style="color: #800000;">''</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;body&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;CRLF.join(L)
&nbsp;&nbsp;&nbsp;&nbsp;content_type&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">multipart/form-data;&nbsp;boundary=%s</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;BOUNDARY
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;content_type,&nbsp;body

</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;get_content_type(filename):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;mimetypes.guess_type(filename)[0]&nbsp;</span><span style="color: #0000ff;">or</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">application/octet-stream</span><span style="color: #800000;">'</span><span style="color: #000000;">

</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Response:
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__init__</span><span style="color: #000000;">(self,&nbsp;status_code,&nbsp;content):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.status_code&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;status_code
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.content&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;content

</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;Client:
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;handle_request(self,&nbsp;response):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.response&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;response
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tornado.ioloop.IOLoop.instance().stop()
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;post(self,&nbsp;url,&nbsp;data</span><span style="color: #000000;">=</span><span style="color: #000000;">{}):
&nbsp;&nbsp;&nbsp;&nbsp;url&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #800000;">'</span><span style="color: #800000;">http://127.0.0.1:%s%s</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">%</span><span style="color: #000000;">&nbsp;(TEST_PORT,&nbsp;url)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fields&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;files&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;[]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">for</span><span style="color: #000000;">&nbsp;key,&nbsp;value&nbsp;</span><span style="color: #0000ff;">in</span><span style="color: #000000;">&nbsp;data.items():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">if</span><span style="color: #000000;">&nbsp;isinstance(value,&nbsp;file):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;files.append([key,&nbsp;value.name,&nbsp;value.read()])
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">else</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fields.append([key,&nbsp;value])
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;content_type,&nbsp;body&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;encode_multipart_formdata(fields,&nbsp;files)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;headers&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;{</span><span style="color: #800000;">'</span><span style="color: #800000;">Content-Type</span><span style="color: #800000;">'</span><span style="color: #000000;">&nbsp;:&nbsp;content_type}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;tornado.httpclient.HTTPRequest(url</span><span style="color: #000000;">=</span><span style="color: #000000;">url,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</span><span style="color: #000000;">=</span><span style="color: #800000;">'</span><span style="color: #800000;">POST</span><span style="color: #800000;">'</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;headers</span><span style="color: #000000;">=</span><span style="color: #000000;">headers,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;body</span><span style="color: #000000;">=</span><span style="color: #000000;">body)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;tornado.httpclient.AsyncHTTPClient()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client.fetch(request&nbsp;,&nbsp;self.handle_request)&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tornado.ioloop.IOLoop.instance().start()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;Response(self.response.code,&nbsp;self.response.body)
&nbsp;&nbsp;&nbsp;&nbsp;
</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;TestCase(unittest.TestCase):
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;_pre_setup(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="color: #0000ff;">pass</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;_post_teardown(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="color: #0000ff;">pass</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;</span><span style="color: #800080;">__call__</span><span style="color: #000000;">(self,&nbsp;result</span><span style="color: #000000;">=</span><span style="color: #000000;">None):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #800000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Wrapper&nbsp;around&nbsp;default&nbsp;__call__&nbsp;method&nbsp;to&nbsp;perform&nbsp;My&nbsp;test
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set&nbsp;up.&nbsp;This&nbsp;means&nbsp;that&nbsp;user-defined&nbsp;Test&nbsp;Cases&nbsp;aren't&nbsp;required&nbsp;to
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include&nbsp;a&nbsp;call&nbsp;to&nbsp;super().setUp().
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #800000;">"""</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.client&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;Client()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">try</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self._pre_setup()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">&nbsp;(KeyboardInterrupt,&nbsp;SystemExit):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">raise</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">&nbsp;Exception:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;sys
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.addError(self,&nbsp;sys.exc_info())
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super(TestCase,&nbsp;self).</span><span style="color: #800080;">__call__</span><span style="color: #000000;">(result)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">try</span><span style="color: #000000;">:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self._post_teardown()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">&nbsp;(KeyboardInterrupt,&nbsp;SystemExit):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">raise</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">except</span><span style="color: #000000;">&nbsp;Exception:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;sys
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result.addError(self,&nbsp;sys.exc_info())
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">
</span></div></div></div>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/01/Tornado-Unit-Testing.html](http://www.cnblogs.com/coderzh/archive/2010/01/01/Tornado-Unit-Testing.html)**