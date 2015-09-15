---
categories:
- 技术文章
date: '2009-12-26'
title: 最常用的Emacs的基本操作
url: /2009/12/26/CommonEmacs/

---


### 什么是Emacs？

Emacs是一种强大的文本编辑器，在程序员和其他以技术工作为主的计算机用户中广受欢迎。EMACS，即Editor MACroS（编辑器宏）的缩写，最初由Richard Stallman(理查德&#183;马修&#183;斯托曼)于1975年在MIT协同Guy Steele共同完成。&nbsp;

Emacs不仅仅是一个编辑器，他是一个整合环境，或可称它为集成开发环境。在里面你可以收发电子邮件，FTP，上新闻组，日历，游戏，写代码，调试等等。对于某些人，打开电脑后，只要打开一个Emacs和FireFox，就可以完成所有的事情。甚至还流传着这么一句话：Emacs除了不能修理自行车，其他都可以做。 

Emacs主页：[http://www.gnu.org/software/emacs/](http://www.gnu.org/software/emacs/)

### 入手Emacs

Emacs入手有些难度，很多初学者很快就放弃了。因为Emacs的很多快捷键让人开始很难适应，比如习惯了狂按ctrl + s保存的同学会不适应，大多数人习惯的复制粘贴ctrl + c，ctrl + v，变成了alt + w, ctrl + y。《卓有成效的程序员》中，作者说到，一个程序员需要坚持使用Emacs一年以上，才能真正熟练掌握。我也是个初学者，现在为止才坚持了几个星期，还要努力啊。如果你也是Emacs初学者，和我一起互勉吧。开始可能会遇到输入障碍，但是没关系，坚持下来，当掌握更多的东西时，效率就会提高上来。

### Emacs基本操作

Emacs的一些基本操作非常重要，必须牢记在心。一个最好的办法就是看Emacs的中文指南(ctrl + h, t)，然后反复练习。

Emacs的快捷键都是绑定在ctrl和alt(或称meta)上的，例如c-x就是ctrl+x，m-x就是alt+x&nbsp;

#### 文件操作

 　　<span style="color: #800080; font-size: 14pt;">C-x C-f</span><span style="font-size: 14pt;"> </span>打开文件
 　　<span style="color: #800080; font-size: 14pt;">C-x C-s</span><span style="font-size: 14pt;"> </span>保存文件
 　　<span style="color: #800080; font-size: 14pt;">C-x C-w</span><span style="font-size: 14pt;"> </span>存为新文件
 　　<span style="color: #800080; font-size: 14pt;">C-x C-c</span><span style="font-size: 14pt;"> </span>退出Emacs

#### 编辑操作

 　　<span style="color: #800080; font-size: 14pt;">C-f</span><span style="font-size: 14pt;"> </span>前进一个字符
 　　<span style="color: #800080; font-size: 14pt;">C-b</span><span style="font-size: 14pt;"> </span>后退一个字符
 　　<span style="color: #800080; font-size: 14pt;">M-f</span><span style="font-size: 14pt;"> </span>前进一个字
 　　<span style="color: #800080; font-size: 14pt;">M-b</span><span style="font-size: 14pt;"> </span>后退一个字
 　　<span style="color: #800080; font-size: 14pt;">C-a</span><span style="font-size: 14pt;"> </span>移到行首
 　　<span style="color: #800080; font-size: 14pt;">C-e</span><span style="font-size: 14pt;"> </span>移到行尾
 　　<span style="color: #800080; font-size: 14pt;">M-a</span><span style="font-size: 14pt;"> </span>移到句首
 　　<span style="color: #800080; font-size: 14pt;">M-e</span><span style="font-size: 14pt;"> </span>移到句尾
 　　<span style="color: #800080; font-size: 14pt;">C-p</span><span style="font-size: 14pt;"> </span>后退一行
 　　<span style="color: #800080; font-size: 14pt;">C-n</span><span style="font-size: 14pt;"> </span>前进一行
 　　<span style="color: #800080; font-size: 14pt;">M-x goto-line</span><span style="font-size: 14pt;"> </span>跳到指定行
 　　<span style="color: #800080; font-size: 14pt;">C-v</span><span style="font-size: 14pt;"> </span>向下翻页
 　　<span style="color: #800080; font-size: 14pt;">M-v</span><span style="font-size: 14pt;"> </span>向上翻页
 　　<span style="color: #800080; font-size: 14pt;">M-&lt;</span><span style="font-size: 14pt;"> </span>缓冲区头部
 　　<span style="color: #800080; font-size: 14pt;">M-&gt;</span><span style="font-size: 14pt;"> </span>缓冲区尾部
 　　<span style="color: #800080; font-size: 14pt;">C-l</span><span style="font-size: 14pt;"> </span>当前行居中
 　　<span style="color: #800080; font-size: 14pt;">M-n or C-u n</span><span style="font-size: 14pt;"> </span>重复操作随后的命令n次
 　　<span style="color: #800080; font-size: 14pt;">C-d</span><span style="font-size: 14pt;"> </span>删除一个字符
 　　<span style="color: #800080; font-size: 14pt;">M-d</span><span style="font-size: 14pt;"> </span>删除一个字
 　　<span style="color: #800080; font-size: 14pt;">C-k</span><span style="font-size: 14pt;"> </span>删除一行
 　　<span style="color: #800080; font-size: 14pt;">M-k</span><span style="font-size: 14pt;"> </span>删除一句
 　　<span style="color: #800080; font-size: 14pt;">C-w</span><span style="font-size: 14pt;"> </span>删除标记区域
 　　<span style="color: #800080; font-size: 14pt;">C-y</span><span style="font-size: 14pt;"> </span>粘贴删除的内容
 　　注意：C-y可以粘贴连续C-k删除的内容；先按C-y，然后按M-y可以选择粘贴被删除的内容
 　　<span style="color: #800080; font-size: 14pt;">C-空格</span><span style="font-size: 14pt;"> </span>标记开始区域(需修改输入法快捷键)
 　　<span style="color: #800080; font-size: 14pt;">C-x h</span><span style="font-size: 14pt;"> </span>标记所有文字
 　　<span style="color: #800080; font-size: 14pt;">M-w</span><span style="font-size: 14pt;"> </span>复制标记区域
 　　<span style="color: #800080; font-size: 14pt;">C-/ or C-x u</span><span style="font-size: 14pt;"> </span>撤消操作

#### 执行SHELL命令

 　　<span style="color: #800080; font-size: 14pt;">M-x shell</span><span style="font-size: 14pt;"> </span>打开SHELL
 　　<span style="color: #800080; font-size: 14pt;">M-!</span><span style="font-size: 14pt;"> </span>执行SHELL命令 (shell-command)

#### 窗口操作

 　　<span style="color: #800080; font-size: 14pt;">C-x 0</span><span style="font-size: 14pt;"> </span>关闭本窗口
 　　<span style="color: #800080; font-size: 14pt;">C-x 1</span><span style="font-size: 14pt;"> </span>只留下一个窗口
 　　<span style="color: #800080; font-size: 14pt;">C-x 2</span><span style="font-size: 14pt;"> </span>垂直均分窗口
 　　<span style="color: #800080; font-size: 14pt;">C-x 3</span><span style="font-size: 14pt;"> </span>水平均分窗口
 　　<span style="color: #800080; font-size: 14pt;">C-x o</span><span style="font-size: 14pt;"> </span>切换到别的窗口
 　　<span style="color: #800080; font-size: 14pt;">C-x s</span><span style="font-size: 14pt;"> </span>保存所有窗口的缓冲
 　　<span style="color: #800080; font-size: 14pt;">C-x b</span><span style="font-size: 14pt;"> </span>选择当前窗口的缓冲区

&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">C-M v</span><span style="font-size: 14pt;"> </span>另外一个窗口向下翻页(需要对照时很好用)

&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">c-M-Shift v</span><span style="font-size: 14pt;"> </span>另外一个窗口向上翻页 

#### 缓冲区列表操作

 　　<span style="color: #800080; font-size: 14pt;">C-x C-b</span><span style="font-size: 14pt;"> </span>打开缓冲区列表
 　　<span style="color: #800080; font-size: 14pt;">C-x k</span><span style="font-size: 14pt;"> </span>关闭缓冲区

#### 搜索模式

 　　<span style="color: #800080; font-size: 14pt;">C-s </span>向前搜索
 　　<span style="color: #800080; font-size: 14pt;">C-s</span><span style="font-size: 14pt;"> </span>查找下一个
 　　<span style="color: #800080; font-size: 14pt;">ENTER</span><span style="font-size: 14pt;"> </span>停止搜索
 　　<span style="color: #800080; font-size: 14pt;">C-r </span>反向搜索
 　　<span style="color: #800080; font-size: 14pt;">C-s C-w</span><span style="font-size: 14pt;"> </span>以光标所在位置的字为关键字搜索
 　　<span style="color: #800080; font-size: 14pt;">M-x replace-string ENTER search-string ENTER</span><span style="font-size: 14pt;"> </span>替换
 　　<span style="color: #800080; font-size: 14pt;">C-M-s</span><span style="font-size: 14pt;"> </span>向前正则搜索
 　　<span style="color: #800080; font-size: 14pt;">C-M-r</span><span style="font-size: 14pt;"> </span>向后正则搜索
 　　<span style="color: #800080; font-size: 14pt;">C-M-%</span><span style="font-size: 14pt;"> </span>正则交互替换

#### 帮助

&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">C-h t</span><span style="font-size: 14pt;"> </span>入门指南
&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">C-h v</span><span style="font-size: 14pt;"> </span>查看变量
&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">C-h f</span><span style="font-size: 14pt;"> </span>查看函数
&nbsp; &nbsp; &nbsp; <span style="color: #800080; font-size: 14pt;">C-h ?</span><span style="font-size: 14pt;"> </span>查看帮助列表&nbsp; 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/12/26/CommonEmacs.html](http://www.cnblogs.com/coderzh/archive/2009/12/26/CommonEmacs.html)**