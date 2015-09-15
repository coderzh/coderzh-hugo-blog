---
categories:
- 技术文章
date: '2015-01-14'
description: ''
keywords:
- skynet
- ubuntu
- VirtualBox
- 安装增强功能
- 共享文件夹
- GuestAdditions
tags: []
title: skynet Windows开发方式：VirtualBox中共享文件夹
url: /2015/01/14/SkynetUbuntuVirtualBox/

---


[skynet](https://github.com/cloudwu/skynet)是一个c和lua实现的轻量级actor模型服务端框架。看了所有文档，对skynet有了大致的了解。还需进一步考察看是否合适做为手游mmo服务端框架。

<!--more-->

由于skynet只有linux版本，如果开发平台是windows就会比较麻烦。于是打算使用虚拟机执行skynet程序，lua脚本放在虚拟机的共享目录里。于是lua可以方便的在Windows中编写，在Linux虚拟机里执行。

### VirtualBox

开始我用了个老版本的VirtualBox，增强功能插件总是安装不上，提示：

> grep: /lib/modules/3.13.0-24-generic/build/include/linux/version.h: No such file or directory

最后通过下面的帖子才发现，安装个最新版本的VirtualBox就解决问题了。([http://ubuntuforums.org/showthread.php?t=2231775](http://ubuntuforums.org/showthread.php?t=2231775))

### 安装增强功能(Install Guest Additions)

直接挂载共享目录，报错：

> unknown filesystem type vboxsf.

原因是没安装VirtualBox增强功能插件，点击菜单挂载iso：

![Insall Guest Additions](http://i.stack.imgur.com/ZAIEt.png)

虚拟机中安装依赖的编译环境套件:

> $sudo apt-get install build-essential

执行:

> uname -r

看装的是哪个kernel type，然后选择性的安装下面3个之一：

```
{something}-generic-pae = sudo apt-get install linux-headers-generic-pae
{something}-generic = sudo apt-get install linux-headers-generic
{something}-server = sudo apt-get install linux-headers-server
```

挂载光驱

> $sudo mount /dev/cdrom /media/cdrom

安装增强功能，如果出现以下错误是因为Server未安装图形界面，不影响使用

```
#Installing the Window System drivers ...fail!
#(Could not find the X.Org or XFree86 Window System.)
$sudo /media/cdrom/VBoxLinuxAdditions.run
```

卸载cdrom

> $sudo umount /media/cdrom

将共享文件夹(share)挂载到mnt下

> $sudo mount -t vboxsf share /mnt

### 其他问题

在mount目录里，sudo执行脚本，总是Read-only file system。google了一会，发现原来是在mount的盘里去写系统路径下的文件就会出这个错。所以，不要执行mount目录的脚本就行了。（拷出来外面执行）
