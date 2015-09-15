---
categories:
- 技术文章
date: '2011-03-06'
title: Android刷机备忘录
url: /2011/03/06/flash-android/

---


G2 Magic上的Android1.6用了好久一直没去刷，直到今天早上实在忍不住刷到了Android2.2。刷之前在网上看了很多教程和注意事项，感觉好复杂，一步一步跟着做，最后发现其实并不复杂。需要特别注意的几点是：

1. 找一个适合自己手机型号的、功能稳定、耗电量少的ROM。可到论坛上看看大家刷的评测，国内阿兴和蛋哥的评价还可以。

2. 查看ROM刷机的版本需要（SPL、Radio、Recovery的版本），比如：SPL1.33、Radio3.22、Recovery1.6.2。有一个一键转换工具[RadioSwitchGUI](http://www.hiapk.com/bbs/viewthread.php?tid=466183&amp;highlight=SPL)很好用。

3. 满足了刷机需求，有一个合适的ROM版本，就可以开始刷了。

备忘：

1. 进入fastboot模式的方法：关机状态下长按<span style="color: red; ">返回键和关机键。</span>

2. 查看SPL、Radio版本的方法：进入fastboot模式后有显示。

3.&nbsp;RadioSwitchGUI使用方法：PC上安装[Java](http://java.com/zh_CN/download/)环境，手机进入fastboot模式，连接USB数据线到PC，运行WinRun.bat。

4. fastboot模式，接入USB后，安装驱动程序：Win7下我没找到合适的独立驱动程序，所以我安装了[HTC Sync for all HTC Android Phones](http://www.htc.com/asia/SupportDownload.aspx?p_id=267&amp;cat=3&amp;dl_id=1073)，内含驱动。

5. 进入recovery模式进行刷机：关机状态下长按<span style="color: red; ">Home键和关机键</span>。如果长按后出现一个叹号和手机图片，原因是recovery版本较旧，这时同时按接听和挂机键，然后再按Home键和关机键可进入recovery模式。如果出现这种情况，建议升级recovery到1.6.2。

6. 进入recovery模式后，先执行WIPE，把所有选项都WIPE一遍，然后进入flash zip from sdcard，按照说明的顺序开刷。比如，先ROM，然后PORT，然后google补丁包。（前提先将下载好的ROM、PORT、Google补丁包文件拷贝到SD卡的根目录）

7. 刷之前先备份联系人和短信。联系人可同步到Google。如果之前的版本是阿兴版，短信有备份还原功能，这个功能最好不要用，因为刷到2.2很可能没有备份还原功能，我就是这么悲剧。所以找个第三方的软件备份一下短信吧。比如91助手。

8. 名词解释：&nbsp;

SPL： &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 类似于PC的BIOS

ROOT权限：刷SPL前必须获取的东西，一般也用不到（除官方rom外，大部分民间rom自带root）

金卡： &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;刷特定ROM要用到的东西，一般也用不到

RADIO: &nbsp; &nbsp; &nbsp; &nbsp;无线通信模块，负责手机通讯的东西

固件： &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;目前分为1.5~1.6~2.0~2.2

ROM： &nbsp; &nbsp; &nbsp; &nbsp; 基于固件基础上的刷机包

Recovery： 关机状态同时按挂机键+房子键，出来的界面就是recovery画面了。刷机、备份、恢复等都在此界面进行

&nbsp;&nbsp;

只要动手刷过一次，就不会觉得麻烦了。本文只是介绍大致刷机方法，提供的链接并不适合所有时期和型号的手机。所以，重要的是掌握方法，以后直接到论坛找最新的合适的ROM刷，就不是什么难事了。

不过还是要提醒一句：刷机有风险，动手请谨慎。刷前看清楚，否则成砖头。

参考资料：

1.&nbsp;[HTC MAGIC(G2) 刷机教程！四步刷机！ 全新更新](http://www.hiapk.com/bbs/viewthread.php?tid=479391&amp;extra=page%3D1%26amp;filter%3Dtype%26amp;typeid%3D149)

2.&nbsp;[最好用的G2 32A SPL&amp;Radio一键转换工具](http://www.hiapk.com/bbs/viewthread.php?tid=466183&amp;highlight=SPL)

3.&nbsp;[现今最完美2.2中文ROMS CM6.1RC1原版 加OC614 PORT 稳定 省电 快速 加入来电归属！](http://www.hiapk.com/bbs/viewthread.php?tid=616250&amp;extra=page%3D1%26amp;filter%3Dtype%26amp;typeid%3D211)

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2011/03/06/flash-android.html](http://www.cnblogs.com/coderzh/archive/2011/03/06/flash-android.html)**