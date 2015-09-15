---
categories:
- 技术文章
date: '2010-10-07'
title: 瘦客户端那些事 - NoMachine的秘密
url: /2010/10/07/thinclient-secret-of-nomachine/

---

  
[上篇](http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html)中我们介绍了各种远程传输协议用于实现瘦客户端，在各种协议当中，NX要我要重点推荐和介绍的。理由很简单，性能！大家都知道，网络带宽、网络传输是瘦客户端的重大瓶颈，谁能够在低带宽、慢速率的网络环境下工作良好，谁就是王者。本文将讲述NoMachine是如何做到这些的。     

199x年，满怀梦想的[Keith Packard](http://en.wikipedia.org/wiki/Keith_Packard)，当时工作于[SuSE](http://en.wikipedia.org/wiki/SuSE)，是[XFree86](http://en.wikipedia.org/wiki/Xfree86)的核心开发成员，一心想要开发一个在低带宽下依然性能完好的传输协议（[LBX](http://en.wikipedia.org/wiki/LBX) - Low Bandwidth X）。他为了LBX倾注心血，将LBX视为自己的孩子，然而最后他还是失败了，LBX最终并没有得到广泛应用。原因是LBX的性能还不够好。于是，他在2001年写一篇LBX的验尸报告 - [An LBX Postmortem](http://keithp.com/%7Ekeithp/talks/lbxpost/paper.html)，以告慰后人，想要实现这样一个高性能的协议是多么的不可能。     

2001年3月，XFree86的邮件组里横空出现了一篇题为[About our effort at NoMachine](http://www.xfree86.org/pipermail/forum/2003-March/002325.html)的文章，作者是Gian Filippo Pinzari。文章隆重的介绍了经过作者三年研究，在低带宽下依然工作良好的，兼容RDP，VNC等协议的[NX](http://en.wikipedia.org/wiki/NX_technology)协议。Gian将NX的核心组件基于GPL[开源](http://www.nomachine.com/sources.php)出来，他说，&#8220;它就在这，大家都来用吧！&#8221;。     

Gian的公司[NoMachine](http://www.nomachine.com/)开发的NX Client、Server等都是收费的产品。但是NX核心组件是开源的，于是出现了大量的开源的NX Client和NX Server。比如，NX Client就有[OpenNX](http://www.opennx.net/)，[QtNX](http://blog.gwright.org.uk/articles/2006/08/23/qtnx-ready-for-public-consumption)，NX Server又有[FreeNX](http://www.google.com/url?sa=t&amp;source=web&amp;cd=1&amp;sqi=2&amp;ved=0CBMQFjAA&amp;url=http%3A%2F%2Ffreenx.berlios.de%2F&amp;rct=j&amp;q=freenx&amp;ei=RTytTMaINZKssAPz1oHcDA&amp;usg=AFQjCNHrVhiiKIAf_8gjKnwOiZqnzgiXZQ&amp;cad=rja)，[NeatX](http://www.google.com/url?sa=t&amp;source=web&amp;cd=1&amp;ved=0CBMQFjAA&amp;url=http%3A%2F%2Fcode.google.com%2Fp%2Fneatx%2F&amp;rct=j&amp;q=neatx&amp;ei=XjytTIGbIIr2swP04Mn_Cw&amp;usg=AFQjCNE7E3WuLZl-C-WJKJpWaKbGsldMVA&amp;cad=rja)等等。     

NoMachine的NX是如何做到的呢？NoMachine的秘密，主要有三个：     
1. 在X协议的基础上，使用优化的压缩算法，进行压缩传输。压缩比达到10:1，甚至100：1。     
2. 在客户端和服务端使用了缓存机制(Cache)，避免同样的数据进行不必要的重复传输。     
3. 减少客户端与服务端请求、回应的时间。     

#### NX使用 

NoMachien的NX主要分为两部分：NX Client和NX Server。NX Server的部署见[文档](http://www.nomachine.com/documents/server/install.php)，还不算复杂。部署完成后，就可以使用NX Client进行连接了。NX Client有Windows版本，Linux版本，Mac版本和Solaris版本。    

![NxNoMachine](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/NxNoMachine_thumb.png "NxNoMachine")    

点击&#8220;Configure&#8221;进行设置，可以看到，NX支持多种桌面协议。   

![nomachine-protocol](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nomachine-protocol_thumb.png "nomachine-protocol")    

如果要单独运行某个远程的应用程序，点击&#8220;Settings..&#8221;进行设置，比如，运行Linux中的星际译王（stardict）   

![nomachine-run-app](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nomachine-run-app_thumb.png "nomachine-run-app")    

以下是我在Win7下运行远程服务器中的文本编辑器(gedit)和星际译王(stardict)的效果：   

![nomachine-demo](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nomachine-demo_thumb_1.png "nomachine-demo")    

NX可以设置共享本地磁盘，默认情况下，远程应用访问的远程设备。比如，在gedit中点击打开，可以看到   

![nomachine-filesys](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nomachine-filesys_thumb.png "nomachine-filesys") 

#### NX组件

我们知道，NX是在X11的基础上优化而来的。我们先来回忆以下X11的工作过程。

![x11](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/x11_thumb.jpg "x11") 

&nbsp;

X Server和X Client是通过X11协议直接通讯的，我们之前讲到过，NX基于X11做了如下的优化：

1. 使用压缩传输。

2. 使用缓存机制。

下面就来看看NX是如何工作的：

![nx](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nx_thumb.jpg "nx")

&nbsp;

可以看到，X Server和X Client不直接通讯了，而是通过NxProxy进行通讯。用户端的X Server误以为NxProxy就是X Client，使用原生的X11于其通讯，而用户端的NxProxy接收到X11协议数据后，经过压缩，再通过NX协议与服务端的NxProxy通讯。在服务端，NxProxy内嵌于NxAgent中，NxAgent再将NX协议与X11进行转化，并且冒充X Server与X Client进行通讯，从而达到优化的目的。NxAgent是从XNest演变过来的，既充当X Server又冒充X Client。

上图还可以看到，用户端和服务端的NxProxy都对数据进行了缓存。这样，他们之前传输数据时，可以将不变的数据缓存起来，传输的只是差异数据。

接下来我们来看看完整的交互过程：

![nxserver](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nxserver_thumb.jpg "nxserver") 

当用户端的NxClient，比如OpenNX启动连接后，会通过客户端的一个NxSsh组件与服务端的NxServer建立连接(Connect)，确认连通之后，NxSsh会向NxServer发出Start Session命令，命令包含需要启动桌面还是哪个应用程序，分辨率是多少等等。服务端收到命令后，准备好Session所需环境，然后启动NxAgent，内置的NxProxy也同时启动起来，同时，需要服务端执行的应用程序也被NxServer执行起来。随后，NxServer生成一个Xauth Cookie（相当于访问令牌）并返回给NxSsh，NxSsh收到Xauth Cookie后，再启动NxProxy，并且通过Xauth Cookie与服务端的NxProxy取得了联系。    

  <table border="1" cellpadding="5" cellspacing="0" width="473"><tbody>     <tr>       <td valign="top" width="118">         

Nxservice
       </td>        <td valign="top" width="353">         

用来把其他组件以服务方式启动的东西
       </td>     </tr>      <tr>       <td valign="top" width="124">         

NXWin 
       </td>        <td valign="top" width="348">         

NX的X Server，从cygwin/X演变过来的
       </td>     </tr>      <tr>       <td valign="top" width="129">         

Nxagent
       </td>        <td valign="top" width="345">         

从XNest演变而来。在服务端，作为一个假装的X Server，与服务端程序进行交互，接收绘图命令（X协议），但并不绘制任何窗口，而是将X协议转换为NX协议（压缩，减少传输次数），然后传递给服务端的nxproxy
       </td>     </tr>      <tr>       <td valign="top" width="132">         

Nxproxy
       </td>        <td valign="top" width="343">         

客户端和服务端都执行，保存缓存，并且互相传输NX数据。服务端中，nxproxy集成到了nxagent中
       </td>     </tr>      <tr>       <td valign="top" width="134">         

Nxssh
       </td>        <td valign="top" width="341">         

负责与服务端建立连接，并启动nxproxy
       </td>     </tr>      <tr>       <td valign="top" width="136">         

Xauth
       </td>        <td valign="top" width="340">         

用于用户验证，相关信息保存在.XAUTHORITY文件中
       </td>     </tr>   </tbody></table>  

#### NX与VNC，RDP

前面我们讲过，NX基于X11，同时还能兼容VNC和RDP协议，那么它是如何兼容的呢？首先，我们再回头看看NX于X11是如何结合的。

![nx-x](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nx-x_thumb_1.jpg "nx-x") 

这个图和我上面的&#8220;NX基本组件流程图&#8221;是一样的。可以看到，关键部分是nxagent，负责将X11与NX进行了转换。接下来，我们继续看通过NX连接VNC服务端的过程：

![nx-vnc](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nx-vnc_5.jpg "nx-vnc") 

原来还是通过agent，将NX协议与RFB协议进行了转换。这样，用户通过NX连接VNC Server，其实是通过NX Server访问VNC Server，然后再将信息通过NX协议传输回来，最终还是通过X Display Server在用户本地显示。RDP也是同样的原理：    

&nbsp;![nx-rdp](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nx-rdp_6.jpg "nx-rdp") 

下面是一个完整的图：

![nx-full](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/ffea4898ff31_BD68/nx-full_5.jpg "nx-full") 

#### NX Library编译

NX的Library使用GPL开源协议，意味着我们也可以使用NX Library开发我们自己的NX Server或Client。首先，我们必须解决编译的问题。NX Library的编译过程并不复杂。

在Linux环境下，参考[官方文档](http://www.nomachine.com/documents/technology/building-components-3.x.php)：编译步骤如下：    

  <div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)    <div id="cnblogs_code_open_ba78c766-e056-4d6d-aa76-9cdbf8199e47">     <div><span style="color: #000000;">需要先安装：&nbsp; 
yum install libjpeg&nbsp; 
openssl</span><span style="color: #000000;">-</span><span style="color: #000000;">devel&nbsp; 
netcat&nbsp; 
expect&nbsp; 
<br />
源码安装libpng&nbsp; 
wget http:</span><span style="color: #000000;">//</span><span style="color: #000000;">download.sourceforge.net</span><span style="color: #000000;">/</span><span style="color: #000000;">libpng</span><span style="color: #000000;">/</span><span style="color: #000000;">libpng</span><span style="color: #000000;">-</span><span style="color: #000000;">1.4</span><span style="color: #000000;">.</span><span style="color: #000000;">3</span><span style="color: #000000;">.tar.gz         
<br />
下载以下包，比如，下载到：~</span><span style="color: #000000;">/</span><span style="color: #000000;">NX&nbsp; 
nxcomp</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">4</span><span style="color: #000000;">.tar.gz&nbsp; 
nxproxy</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">2</span><span style="color: #000000;">.tar.gz&nbsp; 
nxagent</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">13</span><span style="color: #000000;">.tar.gz&nbsp; 
nxcompext</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">4</span><span style="color: #000000;">.tar.gz&nbsp; 
nxauth</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">1</span><span style="color: #000000;">.tar.gz&nbsp; 
nxcompshad</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">3</span><span style="color: #000000;">.tar.gz&nbsp; 
nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11</span><span style="color: #000000;">-</span><span style="color: #000000;">3.3</span><span style="color: #000000;">.</span><span style="color: #000000;">0</span><span style="color: #000000;">-</span><span style="color: #000000;">6</span><span style="color: #000000;">.tar.gz&nbsp; 
<br />
解压所有：&nbsp; 
find . </span><span style="color: #000000;">-</span><span style="color: #000000;">name </span><span style="color: #800000;">"</span><span style="color: #800000;">*tar.gz</span><span style="color: #800000;">"</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">-</span><span style="color: #000000;">exec tar </span><span style="color: #000000;">-</span><span style="color: #000000;">zxf {} \;&nbsp; 
<br />
编译：&nbsp; 
cd nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11&nbsp; 
</span><span style="color: #000000;">/</span><span style="color: #000000;">make World&nbsp; 
cd ..&nbsp; 
cd nxproxy&nbsp; 
.</span><span style="color: #000000;">/</span><span style="color: #000000;">configure </span><span style="color: #000000;">&amp;&amp;</span><span style="color: #000000;"> make&nbsp; 
<br />
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11</span><span style="color: #000000;">/</span><span style="color: #000000;">lib</span><span style="color: #000000;">/</span><span style="color: #000000;">X11</span><span style="color: #000000;">/</span><span style="color: #000000;">libX11.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11</span><span style="color: #000000;">/</span><span style="color: #000000;">lib</span><span style="color: #000000;">/</span><span style="color: #000000;">Xext</span><span style="color: #000000;">/</span><span style="color: #000000;">libXext.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11</span><span style="color: #000000;">/</span><span style="color: #000000;">lib</span><span style="color: #000000;">/</span><span style="color: #000000;">Xrender</span><span style="color: #000000;">/</span><span style="color: #000000;">libXrender.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nxcomp</span><span style="color: #000000;">/</span><span style="color: #000000;">libXcomp.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nxcompext</span><span style="color: #000000;">/</span><span style="color: #000000;">libXcompext.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nxcompshad</span><span style="color: #000000;">/</span><span style="color: #000000;">libXcompshad.so</span><span style="color: #000000;">*</span><span style="color: #000000;">&nbsp;</span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">lib&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nx</span><span style="color: #000000;">-</span><span style="color: #000000;">X11</span><span style="color: #000000;">/</span><span style="color: #000000;">programs</span><span style="color: #000000;">/</span><span style="color: #000000;">Xserver</span><span style="color: #000000;">/</span><span style="color: #000000;">nxagent </span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">bin&nbsp; 
cp </span><span style="color: #000000;">-</span><span style="color: #000000;">a nxproxy</span><span style="color: #000000;">/</span><span style="color: #000000;">nxproxy </span><span style="color: #000000;">/</span><span style="color: #000000;">usr</span><span style="color: #000000;">/</span><span style="color: #000000;">NX</span><span style="color: #000000;">/</span><span style="color: #000000;">bin&nbsp; 
<br />
设置LD_LIBRARY_PATH&nbsp; 
export LD_LIBRARY_PATH</span><span style="color: #000000;">=/</span><span style="color: #000000;">usr</span><span>/</span><span>NX</span><span>/</span><span>lib:</span><span>$LD_LIBRARY_PATH</span><span style="color: #000000;">&nbsp; 
<br />
</span><span>这时，</span><span>/</span><span>usr</span><span>/</span><span>NX</span><span>/</span><span>bin</span><span>/</span><span>nxproxy 和 </span><span>/</span><span>usr</span><span>/</span><span>NX</span><span>/</span><span>bin</span><span>/</span><span>nxagent 应该可以用了         
</span></div>   </div> </div>  

&nbsp;

<span>Window平台下，NXWin的编译过程，参考</span>[<span>这里</span>](http://www.nomachine.com/ar/view.php?ar_id=AR01F00503)<span>：</span>
  <div class="cnblogs_code">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)    <div id="cnblogs_code_open_9e16b9ac-c139-4202-92d0-1754cb15c7eb">     <div><span>下载：         
</span><span>nx</span><span>-</span><span>X11</span><span>-</span><span>compat</span><span>-</span><span>X.Y.Z</span><span>-</span><span>N.tar.gz&nbsp; 
</span><span>nxwin</span><span>-</span><span>X.Y.Z</span><span>-</span><span>N.tar.gz&nbsp; 
</span><span>nxauth</span><span>-</span><span>X.Y.Z</span><span>-</span><span>N.tar.gz&nbsp; 
</span><span>nxcomp</span><span>-</span><span>X.Y.Z</span><span>-</span><span>N.tar.gz&nbsp; 
<br />
</span><span>在cygwin中，执行：         
</span><span>#</span><span> tar zxvf nx-X11-compat-X.Y.Z-N.tar.gz </span><span style="color: #008000;">         
</span><span>#</span><span> tar zxvf nxwin-X.Y.Z-N.tar.gz </span><span style="color: #008000;">         
</span><span>#</span><span> tar zxvf nxauth-X.Y.Z-N.tar.gz </span><span style="color: #008000;">         
</span><span>#</span><span> tar zxvf nxcomp-X.Y.Z-N.tar.gz </span><span style="color: #008000;">         
</span><span>#</span><span> cd nxcomp </span><span style="color: #008000;">         
</span><span>#</span><span> ./configure </span><span style="color: #008000;">         
</span><span>#</span><span> make </span><span style="color: #008000;">         
</span><span>#</span><span> cd .. </span><span style="color: #008000;">         
</span><span>#</span><span> cd nx-X11 </span><span style="color: #008000;">         
</span><span>#</span><span> make World </span><span style="color: #008000;">         
</span><span style="color: #000000;">         
</span></div>   </div> </div>  

#### <span>     
NX Cilent开发步骤</span>

<span>基于NX Library开发一个NX Client并不是什么难事，在freenx的svn库里有好几个NX Client工程，比如：qtnx，还有Python的实现版本gnx（仅限linux系统），因此，可以参照这些工程的实现。 </span>

<span>svn co </span>[<span>http://svn.berlios.de/svnroot/repos/freenx/trunk</span>](http://svn.berlios.de/svnroot/repos/freenx/trunk)<span> freenx</span>

<span>NX Client与NX Server的交互过程见：</span>[<span>NX Client开发步骤</span>](http://www.cnblogs.com/coderzh/archive/2010/10/07/nxclient-develop.html)    

&nbsp;

<span>瘦客户端那些事 系列：</span>    
  
[<span>瘦客户端那些事 - 开篇</span>](http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html)    
  
[<span>瘦客户端那些事 - 远程传输协议</span>](http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html)
  
[<span>瘦客户端那些事 - NoMachine的秘密</span>](http://www.cnblogs.com/coderzh/archive/2010/10/07/thinclient-secret-of-nomachine.html)
 <span>......</span>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/10/07/thinclient-secret-of-nomachine.html](http://www.cnblogs.com/coderzh/archive/2010/10/07/thinclient-secret-of-nomachine.html)**