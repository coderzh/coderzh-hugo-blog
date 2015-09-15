---
categories:
- 技术文章
date: '2010-09-24'
title: 瘦客户端那些事 - 远程传输协议
url: /2010/09/24/thinclient-protocol/

---

  
[上篇](http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html)说到了关于瘦客户端的一些现状和遐想，接下来我们开始探索这种技术实现的可能。要实现瘦客户端，最重要的是选择一种客户端和服务端都能理解的沟通方式，这种沟通方式就是通讯协议，或者远程传输协议。

本文不讨论Onlive之类的公司制定的私有未公开的传输协议，而是讨论一些现有的通用协议。其实大家对这些通用协议并不会陌生，他们分别是微软的RDP协议、Citrix的ICA协议、VNC的RFB协议、MIT的X11协议等等。

&nbsp;

常见协议列表： 

<table style="border: 1px none #aaaaaa;" cellpadding="2" cellspacing="0" width="600">
     <tbody>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa; background: none repeat scroll 0pt 0pt #f2f2f2;">Software </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa; background: none repeat scroll 0pt 0pt #f2f2f2;">Protocol </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa; background: none repeat scroll 0pt 0pt #f2f2f2;">License </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Citrix XenApp</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RDP, ICA </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Proprietary</td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">FreeNX </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">NX, RDP, RFB(VNC) </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">GPL </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">LogMeIn</td>
             <td style="border: 1px solid #aaaaaa;"  padding:0.2em;="">Proprietary</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Proprietary</td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Neatx</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">NX</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">GPL</td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">rdesktop</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RDP</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">GPL </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RealVNC</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RFB(VNC)</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">GPL </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">UltraVNC</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RFB(VNC)</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">GPL </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Remote Desktop Services/Terminal Services</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">RDP</td>
             <td style="border: 1px solid #aaaaaa;">Proprietary </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">SSH with X forwarding</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">X11</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">BSD</td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Symantec pcAnywhere</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Proprietary </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Proprietary </td>
         </tr>
         <tr>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Citrix XenAppRDP</td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">ICA </td>
             <td style="padding: 0.2em; border: 1px solid #aaaaaa;">Proprietary </td>
         </tr>
     </tbody>
</table>

更详细的列表见：[http://en.wikipedia.org/wiki/Comparison_of_remote_desktop_software](http://en.wikipedia.org/wiki/Comparison_of_remote_desktop_software)

#### 

RDP协议

![](http://images.cnblogs.com/cnblogs_com/coderzh/Remote_desktop_connection_icon.PNG)

RDP全称是Remote Desktop Protocol，这就是我们平时在Windows里远程桌面使用的协议。使用mstsc.exe我们就可以远程连接到一台Windows机器的桌面进行操作了。在Windows2008里，有一个更吸引人的东西，那就是<span id="ctl00_MainContentPlaceholder_ctl01_ctl00_lblEntry">Terminal Services RemoteApp。

<span id="ctl00_MainContentPlaceholder_ctl01_ctl00_lblEntry">Terminal Services RemoteApp</span>支持远程的执行单个应用程序，就好像这个应用程序是在本机运行的一样。有了RemoteApp，我们就可以实现在一台没有安装Office或者Visual Studio的客户端机器运行起来一个Excel或VS2010，而Excel和VS2010程序实际是安装在远程安装有RemoteApp服务端的机器。

设置远程应用程序：

![](http://images.cnblogs.com/cnblogs_com/coderzh/remoteapp-create.png)

RemoeApp架构图：

![](http://images.cnblogs.com/cnblogs_com/coderzh/rdp.gif)

客户端可以直接使用.rdp快捷方式运行远程App，也可以</span><span id="ctl00_MainContentPlaceholder_ctl01_ctl00_lblEntry">在浏览器里里</span><span id="ctl00_MainContentPlaceholder_ctl01_ctl00_lblEntry">通过TS Web Access运行一个远程App（远程App并不是运行在浏览器里的）。

比如，在一台Vista的机器里，通过TS Web Access运行远程的WordPad（非Vista风格）。

![](http://images.cnblogs.com/cnblogs_com/coderzh/remoteapp-web.jpg)

运行效果如下：

![](http://images.cnblogs.com/cnblogs_com/coderzh/remoteapp-example.jpg)

微软的这项技术很酷，是吧。不过，RemoteApp仅限于Windows平台。

</span>

#### ICA协议

![](http://images.cnblogs.com/cnblogs_com/coderzh/citrix_logo.jpg)

ICA全称是Independent Computing Architecture，即独立计算架构,它把应用程序的计算/执行逻辑与显示逻辑分离开来，把程序的计算/执行100%地保留在服务器端,而把运行结果图形化/界面化并通过网络传输到客户端,对于客户端而言,也只有键盘敲击和鼠标点击等会通过网络传给服务器。

ICA由Citrix公司设计的，Citrix可以算是这一领域的老大哥了，就连微软这样技术雄厚的公司，都是购买的Citrix的技术才做出上面的Remote Desktop和TS RemoteApp。技术的原创者是Citrix，因此Citrix拥有更大的优势，运用更多的创新，做出更好的产品出来。这个产品就是Citrix XenApp。

XenApp是个商业工具，我没有用过，自然算不上深入了，有兴趣的同学可以访问Citrix官网了解更多。下面是我找到的一个XenApp设计图：

![](http://images.cnblogs.com/cnblogs_com/coderzh/XenApp.gif)

#### 

RFB协议

![](http://images.cnblogs.com/cnblogs_com/coderzh/Vnc_logo.png)

RFB全称是Remote Frame Buffer，它是我们常用的VNC所使用的协议。RFB是一个远程图形用户的简单协议，因为它工作在帧缓存级别上，所以它可以应用于所有的窗口系统，例如：X11，Windows和Mac系统。远程终端用户使用机器（比如显示器、键盘、鼠标）的叫做RFB客户端，提供帧缓存变化的被称做RFB服务端。

![](http://images.cnblogs.com/cnblogs_com/coderzh/rfb.jpg)

由于使用的是帧缓存技术，因此VNC的性能一直被人所诟病。同时，VNC只能远程控制整个桌面，还没办法做到只单独运行一个程序。

#### 
X11协议

![](http://images.cnblogs.com/cnblogs_com/coderzh/100px-X11.svg.png)

X11（X Window System core protocol）是由MIT于1984年设计出来的开源传输协议，一直发展至今，最新版本是X11R7.5。它是X Window System的基本协议。而X Window System系统生来就是为瘦客户服务的，从设计之初，它就被设计成计算和显示分离的架构，即程序的运行可以在一台计算机，而显示又在另外一台计算机。随着X11的不断演变发展，出现了各种不同形式的改良版本，其中最著名的就是NoMachine公司开发的NX协议，NX协议在X11的基础上，加入了缓存机制、压缩传输等，使其性能得到飞跃的提升。这也是我下一篇要重点介绍的。

X11的设计原则是：**create Mechanism, not Policy**，所以X故意没有规范应用程式的使用者界面 ，例如按钮 、选单 和视窗的标题栏等等。这些都由视窗管理器 （window managers）、GUI 构件工具包 、桌面环境 （desktop environments）或者应用程序指定的GUI（䠋如 POS机 ）等等诸如此类的用户软件来提供。这样我们就可以理解，为什么Linux系统中会有诸多如Gnome，KDE之类桌面系统，同样使用X协议，绘制的界面却不尽相同。

![](http://images.cnblogs.com/cnblogs_com/coderzh/x11.jpg)

要了解X11，一个非常重要的概念一定要弄清楚。就是X Server和X Client。通常Server是指服务器端，Cilent是指用户的客户端，但是X11中要反过来理解。X11中，用于显示画面的是Server，用于计算处理的是Client。所以，如果通过X11远程连接，用户端必须起一个X Server，远程应用程序实际通过远程的X Cilent来执行。

X11本身并不复杂，Server和Client交互的请求一共四种：Requests, Replies, Events, Errors。

&nbsp;&nbsp; 1. Request: Client请求Server端返回信息或执行动作。

&nbsp;&nbsp; 2. Reply: Server针对Request的返回。不是所有Request都有返回。

&nbsp;&nbsp; 3. Event: Server发送的一些界面相关的事件给Client，例如：键盘、鼠标输入，窗口移动，Resize等等。

&nbsp;&nbsp; 4. Error: 当Request请求无效时，Server发送错误信息给Cilent。

![](http://images.cnblogs.com/cnblogs_com/coderzh/200px-Xcore-overview.svg.png)

如果你正使用X Window System，比如Linux，Debian，Ubuntu等，马上就可以试试了。运行下面的命令，就可以运行一个远程的gedit（文本编辑器）：

<div class="cnblogs_code">
<div><span style="color: #000000;">ssh&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">X&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">C&nbsp;root</span><span style="color: #000000;">@</span><span style="color: #000000;">192.168</span><span style="color: #000000;">.x.x&nbsp;gedit</span></div>
</div>

即使不是远程显示图像，本地执行的应用程序所使用的X11的架构也是一样的，都有一个Server和Client。我们可以通过修改Display环境变量，将画面显示到别处。

比如，Client端执行：

<div class="cnblogs_code">
<div><span style="color: #000000;">export&nbsp;DISPLAY</span><span style="color: #000000;">=</span><span style="color: #000000;">192.168</span><span style="color: #000000;">.x.x:</span><span style="color: #000000;">0</span></div>
</div>

远程Display的X Server要接受Client的连接，使用xhost加入允许列表，Server端执行：

<div class="cnblogs_code">
<div><span style="color: #000000;">xhost&nbsp;</span><span style="color: #000000;">+</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">192.168</span><span style="color: #000000;">.x.x</span></div>
</div>

然后，在Client端运行一个应用程序，比如：gedit，画面将显示在远程的Server端。

好了，这篇就到这了。下篇将带大家了解NoMachine的NX的秘密。如果你对此有兴趣，请告诉我。

瘦客户端那些事 系列：
  
[瘦客户端那些事 - 开篇](http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html)

<span>[瘦客户端那些事 - 远程传输协议](http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html)</span>

<span>[瘦客户端那些事 - NoMachine的秘密](http://www.cnblogs.com/coderzh/archive/2010/10/07/thinclient-secret-of-nomachine.html)</span><span></span>

......

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html](http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html)**