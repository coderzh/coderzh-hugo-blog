---
categories:
- 技术文章
date: '2009-12-26'
title: Emacs中打造强大的Python IDE
url: /2009/12/26/emacspythonide/

---


本文将介绍，在Emacs中，通过各种扩展，打造强大的Python IDE环境，包括<span style="color: #0000ff;">Snippet工具，智能提示，自动补全，重构工具，调试以及GAE的调试</span>，等等。以下各工具的安装前提是你对Emacs的配置文件有一定的了解，所有相关的el文件都必须放在load_path能够加载的地方。

#### <span>[1. YASnippet](http://code.google.com/p/yasnippet/) </span>

snippet工具，可自定义一些模板，必不可少的好东西！看了下面这个很酷的演示动画就明白了：
  
[http://yasnippet.googlecode.com/files/yasnippet.avi

](http://yasnippet.googlecode.com/files/yasnippet.avi)

安装方法：

<div class="cnblogs_code"><div><span style="color: #000000;">(</span><span style="color: #0000ff;">require</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">yasnippet)
(yas/initialize)
(yas/load-directory&nbsp;"~/.emacs.d/plugins/yasnippet-0.6.1c/snippets")</span></div></div>

#### [
2. AutoComplete](http://www.emacswiki.org/emacs/AutoComplete)

自动完成工具，会像VS里一样，弹出一个列表框让你去选择。

![](http://www.emacswiki.org/pics/static/AutoCompleteScreenshot.png)'

安装方法：
<div class="cnblogs_code" onclick="cnblogs_code_show('af09c201-90fc-4bbd-95f8-878f5b7405e9')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_af09c201-90fc-4bbd-95f8-878f5b7405e9"><div><span style="color: #000000;">(</span><span style="color: #0000ff;">require</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">auto-complete)
(require&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">auto</span><span style="color: #000000;">-</span><span style="color: #000000;">complete</span><span style="color: #000000;">-</span><span style="color: #000000;">config)
(global</span><span style="color: #000000;">-</span><span style="color: #000000;">auto</span><span style="color: #000000;">-</span><span style="color: #000000;">complete</span><span style="color: #000000;">-</span><span style="color: #000000;">mode&nbsp;t)
(setq</span><span style="color: #000000;">-</span><span style="color: #000000;">default&nbsp;ac</span><span style="color: #000000;">-</span><span style="color: #000000;">sources&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">(ac-source-words-in-same-mode-buffers))
(add-hook&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">emacs</span><span style="color: #000000;">-</span><span style="color: #000000;">lisp</span><span style="color: #000000;">-</span><span style="color: #000000;">mode</span><span style="color: #000000;">-</span><span style="color: #000000;">hook&nbsp;(lambda&nbsp;()&nbsp;(add</span><span style="color: #000000;">-</span><span style="color: #000000;">to</span><span style="color: #000000;">-</span><span style="color: #000000;">list&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">ac-sources&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">ac</span><span style="color: #000000;">-</span><span style="color: #000000;">source</span><span style="color: #000000;">-</span><span style="color: #000000;">symbols)))
(add</span><span style="color: #000000;">-</span><span style="color: #000000;">hook&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">auto-complete-mode-hook&nbsp;(lambda&nbsp;()&nbsp;(add-to-list&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">ac</span><span style="color: #000000;">-</span><span style="color: #000000;">sources&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">ac-source-filename)))
(set-face-background&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">ac</span><span style="color: #000000;">-</span><span style="color: #000000;">candidate</span><span style="color: #000000;">-</span><span style="color: #000000;">face&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">lightgray</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">)
(set</span><span style="color: #000000;">-</span><span style="color: #000000;">face</span><span style="color: #000000;">-</span><span style="color: #000000;">underline&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">ac-candidate-face&nbsp;"darkgray")
(set-face-background&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">ac</span><span style="color: #000000;">-</span><span style="color: #000000;">selection</span><span style="color: #000000;">-</span><span style="color: #000000;">face&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">steelblue</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">) ;;; </span>**<span style="color: #008000;">设置比上面截图中更好看的背景颜色</span>**<span style="color: #000000;">
(define</span><span style="color: #000000;">-</span><span style="color: #000000;">key&nbsp;ac</span><span style="color: #000000;">-</span><span style="color: #000000;">completing</span><span style="color: #000000;">-</span><span style="color: #0000ff;">map</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">\M-n</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">ac-next)&nbsp;&nbsp;;;;&nbsp;</span><span style="color: #008000; font-weight: bold;">列表中通过按M-n来向下移动</span><span style="color: #000000; font-weight: bold;">
(define-key&nbsp;ac-completing-map&nbsp;"\M-p"&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">ac</span><span style="color: #000000;">-</span><span style="color: #000000;">previous)
(setq&nbsp;ac</span><span style="color: #000000;">-</span><span style="color: #000000;">auto</span><span style="color: #000000;">-</span><span style="color: #000000;">start&nbsp;</span><span style="color: #800000;">2</span><span style="color: #000000;">)
(setq&nbsp;ac</span><span style="color: #000000;">-</span><span style="color: #000000;">dwim&nbsp;t)
(define</span><span style="color: #000000;">-</span><span style="color: #000000;">key&nbsp;ac</span><span style="color: #000000;">-</span><span style="color: #000000;">mode</span><span style="color: #000000;">-</span><span style="color: #0000ff;">map</span><span style="color: #000000;">&nbsp;(kbd&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">M-TAB</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">)&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">auto-complete)</span></div></div></div>

#### <span>[
3. Rope and Ropemacs](http://rope.sourceforge.net/ropemacs.html)     </span>

非常棒的重构工具，比如rename,move,extract method等等。还有非常好用的goto difinition(跳到定义)，show documents(显示文档)等等。安装Ropemacs前，必须先安装[rope](http://rope.sf.net/)和[pymacs](http://pymacs.progiciels-bpi.ca/pymacs.html) 。
  
[**rope**](http://rope.sf.net/)的安装方法：
<div class="cnblogs_code"><div><span style="color: #000000;">python&nbsp;setup.py install</span></div></div>
  
[**pymacs**](http://pymacs.progiciels-bpi.ca/pymacs.html)的安装方法：
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">python&nbsp;setup.py&nbsp;install</span></div></div>
<br />
.emacs中：
<div class="cnblogs_code"><div><span style="color: #000000;">(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">pymacs-apply&nbsp;"pymacs")
(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">pymacs</span><span style="color: #000000;">-</span><span style="color: #000000;">call&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">pymacs</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">)
(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">pymacs-eval&nbsp;"pymacs"&nbsp;nil&nbsp;t)
(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">pymacs</span><span style="color: #000000;">-</span><span style="color: #0000ff;">exec</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">pymacs</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">&nbsp;nil&nbsp;t)
(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">pymacs-load&nbsp;"pymacs"&nbsp;nil&nbsp;t)</span></div></div>

**[Ropmacs](http://rope.sourceforge.net/ropemacs.html)**的安装方法：

<div class="cnblogs_code"><div><span style="color: #000000;">python&nbsp;setup.py&nbsp;install</span></div></div>
<br />
.emacs中：
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">(pymacs</span><span style="color: #000000;">-</span><span style="color: #000000;">load&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">ropemacs</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">rope-</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">)
(setq&nbsp;ropemacs</span><span style="color: #000000;">-</span><span style="color: #000000;">enable</span><span style="color: #000000;">-</span><span style="color: #000000;">autoimport&nbsp;t)</span></div></div>

#### [
4. pycomplete](http://www.rwdev.eu/articles/emacspyeng)

一个更加强大的智能提示工具，比如，输入time.cl 然后按TAB键，会列出time模块所有cl开头的函数名。在调用函数时，还会在mini buffer中提示函数的参数类型。这个东西需要先安装pymacs。

安装方法：

1. 拷贝 [python-mode.el](http://www.rwdev.eu/python/pycomplete/python-mode.el) and [pycomplete.el](http://www.rwdev.eu/python/pycomplete/pycomplete.el) 到Emacs的load_path中。

2. 拷贝  [pycomplete.py](http://www.rwdev.eu/python/pycomplete/pycomplete.py) 到<cite>PYTHONPATH</cite> (比如： c:/<cite>python25/Lib/site-packages</cite>)

3. .emacs中添加：

<div class="cnblogs_code" onclick="cnblogs_code_show('b63ff589-0b0f-4325-8fd6-8790b097202d')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_b63ff589-0b0f-4325-8fd6-8790b097202d"><div><span style="color: #000000;">(</span><span style="color: #0000ff;">require</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">pycomplete)
(setq&nbsp;auto-mode-alist&nbsp;(cons&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">(</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">\\.py$</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">.</span><span style="color: #000000;">&nbsp;python</span><span style="color: #000000;">-</span><span style="color: #000000;">mode)&nbsp;auto</span><span style="color: #000000;">-</span><span style="color: #000000;">mode</span><span style="color: #000000;">-</span><span style="color: #000000;">alist))
(autoload&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">python-mode&nbsp;"python-mode"&nbsp;"Python&nbsp;editing&nbsp;mode."&nbsp;t)
(setq&nbsp;interpreter-mode-alist(cons&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000;">(</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000; font-weight: bold;">python</span><span style="color: #000000; font-weight: bold;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">.</span><span style="color: #000000;">&nbsp;python</span><span style="color: #000000;">-</span><span style="color: #000000;">mode)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interpreter</span><span style="color: #000000;">-</span><span style="color: #000000;">mode</span><span style="color: #000000;">-</span><span style="color: #000000;">alist))</span></div></div></div>

#### 5. pdb调试

在Emacs中，通过M-x pdb可调出pdb对python代码进行调试。但是发现在Windows系统中，总进入不了调试模式。主要原因有：

1. windows中，找不到pdb.py位置。需自己制定pdb的路径。可以通过下面的方法设置pdb的路径：
<div class="cnblogs_code" onclick="cnblogs_code_show('5223831d-7326-4397-84e7-3797b11b65ec')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_5223831d-7326-4397-84e7-3797b11b65ec"><div><span style="color: #000000;">;;&nbsp;pdb&nbsp;setup</span><span style="color: #000000;">,</span><span style="color: #000000;">&nbsp;note&nbsp;the&nbsp;python&nbsp;version
(setq&nbsp;pdb</span><span style="color: #000000;">-</span><span style="color: #000000;">path&nbsp;</span><span style="color: #000000; font-weight: bold;">'</span><span style="color: #000000; font-weight: bold;">c:/python25/Lib/pdb.py
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gud-pdb-command-name&nbsp;(symbol-name&nbsp;pdb-path))
&nbsp;(defadvice&nbsp;pdb&nbsp;(before&nbsp;gud-query-cmdline&nbsp;activate)
&nbsp;&nbsp;&nbsp;"Provide&nbsp;a&nbsp;better&nbsp;default&nbsp;command&nbsp;line&nbsp;when&nbsp;called&nbsp;interactively."
&nbsp;&nbsp;&nbsp;(interactive
&nbsp;&nbsp;&nbsp;&nbsp;(list&nbsp;(gud-query-cmdline&nbsp;pdb-path
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(file-name-nondirectory&nbsp;buffer-file-name)))))</span></div></div></div>

2. windows中，调用pdb时，未使用<span style="color: red;">python -i</span> 参数。 

针对上面两个问题，我的解决办法是，不设置pdb具体路径，M-x pdb 回车后，出现下面命令:
<div class="cnblogs_code"><div><span style="color: #000000;">Run&nbsp;pdb&nbsp;(like&nbsp;this):&nbsp;pdb&nbsp;</span></div></div>
<br />
然后手动修改一下：
<br />
<div class="cnblogs_code"><div><span style="color: #000000;">Run&nbsp;pdb&nbsp;(like&nbsp;this):&nbsp;</span><span style="color: red;">python&nbsp;</span><span style="color: red;">-</span><span style="color: red;">i&nbsp;</span><span style="color: red;">-</span><span style="color: red;">m</span><span style="color: #000000;">&nbsp;pdb&nbsp;test.py</span></div></div>
<br />
这样就搞定了。
<br />
#### 6. 如何调试GAE程序
<br />
GAE是一个Web应用，需要跨线程进行调试，而pdb本身对线程调试支持不好。使用pdb进行线程调试时，只有在需要调试的地方插入下面代码：
<div class="cnblogs_code"><div><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;pdb
pdb.set_trace()</span></div></div>

然后直接运行被调试代码，而不是通过python pdb来执行，就可以多线程代码进行调试了。

但是Google App Engine这样的Web应用，使用这个方法还是不能调试，和stdin和stdout有关，最后找到一个很好的解决方法：
<div class="cnblogs_code"><div><span style="color: #0000ff;">def</span><span style="color: #000000;">&nbsp;set_trace():
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;pdb,&nbsp;sys
&nbsp;&nbsp;&nbsp;&nbsp;debugger&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;pdb.Pdb(stdin</span><span style="color: #000000;">=</span><span style="color: #000000;">sys.</span><span style="color: #800080;">__stdin__</span><span style="color: #000000;">,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stdout</span><span style="color: #000000;">=</span><span style="color: #000000;">sys.</span><span style="color: #800080;">__stdout__</span><span style="color: #000000;">)
&nbsp;&nbsp;&nbsp;&nbsp;debugger.set_trace(sys._getframe().f_back)</span></div></div>

在任何需要调试的地方，调用上面的set_trace()函数。

<span style="color: #0000ff;">如果你还有更好玩的东西，一定要告诉我！</span>

参考文档：
  
[http://www.emacswiki.org/emacs/PythonMode](http://www.emacswiki.org/emacs/PythonMode)
  
[http://www.enigmacurry.com/2008/05/09/emacs-as-a-powerful-python-ide/](http://www.enigmacurry.com/2008/05/09/emacs-as-a-powerful-python-ide/)&nbsp;
  
[http://jjinux.blogspot.com/2008/05/python-debugging-google-app-engine-apps.html&nbsp;](http://jjinux.blogspot.com/2008/05/python-debugging-google-app-engine-apps.html)

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/12/26/emacspythonide.html](http://www.cnblogs.com/coderzh/archive/2009/12/26/emacspythonide.html)**