---
categories:
- 技术文章
date: '2010-05-02'
title: 成功将ubuntu9.10升级到了10.04
url: /2010/05/02/ubuntu-upgrade-from-910-to-1004/

---


今天早上起来折腾Ubuntu10.04LTS，于是，首先我打算直接使用cn99的源通过sudo apt-get upgrade升级上来。但是升级完成后，发现并没有完全升级成功，虽然查看Ubuntu版本已经是10.04LTS了，但是从内核版本和界面上看来，显然没有升级成功。

于是，从网上下载了[ubuntu-10.04-alternate-i386.iso](http://mirrors.163.com/ubuntu-releases/.pool/ubuntu-10.04-alternate-i386.iso)，打算通过CDROM的方式升级上来。

下载完成后，通过下面的命令挂载到CDROM中：

<div class="cnblogs_code">
<div><span style="color: #000000;">sudo&nbsp;mount&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">o&nbsp;loop&nbsp;~</span><span style="color: #000000;">/</span><span style="color: #000000;">Desktop</span><span style="color: #000000;">/</span><span style="color: #000000;">ubuntu</span><span style="color: #000000;">-</span><span style="color: #000000;">10.04</span><span style="color: #000000;">-</span><span style="color: #000000;">alternate</span><span style="color: #000000;">-</span><span style="color: #000000;">i386.iso&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">media</span><span style="color: #000000;">/</span><span style="color: #000000;">cdrom0</span></div>
</div>
然后，如果自动运行了的话，会弹出一个升级的对话框：

![](https://help.ubuntu.com/community/KarmicUpgrades?action=AttachFile&amp;do=get&amp;target=umcd1.png)&nbsp;

如果，没有弹出，按ALT＋F2，输入下面的命令执行：

<div class="cnblogs_code">
<div><span style="color: #000000;">gksu&nbsp;</span><span style="color: #800000;">"</span><span style="color: #800000;">sh&nbsp;/cdrom/cdromupgrade</span><span style="color: #800000;">"</span>
<br />
</div>
</div>
<pre>如果你运气好，直接就升级成功了。但是我一般没有那么幸运，老是遇到这样那样的错误。比如，这次折腾中就遇到了下面的问题。

</pre>

#### 1. 安装的python崩溃，请修复'/usr/bin/python'链结

<pre>解决办法：升级时，python的默认版本需要是2.6，但我的机器默认是2.5。所以出错了。修改一下Python的链接：
</pre>
<div class="cnblogs_code">
<div><span style="color: #000000;">sudo&nbsp;ln&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">sf&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">bin</span><span style="color: #000000;">/</span><span style="color: #000000;">python2.</span><span style="color: #000000;">6</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">bin</span><span style="color: #000000;">/</span><span style="color: #000000;">python</span></div>
</div>

#### 2. 'E:Internal Error, Could not perform immediate configuration (2) on util-linux'

<pre>解决办法：我也不确定是怎么解决的，各种命令执行了一通。
首先把&#8220;软件源&#8221;里的&#8220;可从互联网下载&#8221;的可选框都去掉。执行：
</pre><div class="cnblogs_code"><div><span style="color: #000000;">sudo&nbsp;dpkg&nbsp;</span><span style="color: #000000;">--</span><span style="color: #000000;">configure&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">a
<br />
sudo&nbsp;apt</span><span style="color: #000000;">-</span><span style="color: #000000;">get&nbsp;upgrade&nbsp;</span><span style="color: #000000;">--</span><span style="color: #000000;">all</span></div>
</div>

#### 
3. 升级过程中python2.6出错，导致升级终止。

<pre>解决办法：重新安装python2.6。
</pre><div class="cnblogs_code"><div><span style="color: #000000;">sudo&nbsp;apt</span><span style="color: #000000;">-</span><span style="color: #000000;">get&nbsp;install&nbsp;python2.</span><span style="color: #000000;">6</span>
</div>
</div>
<pre>
折腾来折腾去，终于升级成功了。重启，内核版本已经是10.04的了，然后登录界面也变了。
进来后，发现窗口的&#8220;关闭，最小化，最大化&#8221;按钮跑到左上角了，还真有点不习惯。秀一下我的桌面吧。
![](http://images.cnblogs.com/cnblogs_com/coderzh/ubuntu/ubuntu10.04.png)&nbsp;
</pre>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/05/02/ubuntu-upgrade-from-910-to-1004.html](http://www.cnblogs.com/coderzh/archive/2010/05/02/ubuntu-upgrade-from-910-to-1004.html)**