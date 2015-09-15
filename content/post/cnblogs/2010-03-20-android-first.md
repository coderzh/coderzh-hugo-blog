---
categories:
- 技术文章
date: '2010-03-20'
title: Android应用开发初印象
url: /2010/03/20/android-first/

---


前段时间终于拿下了蓄谋已久的HTC G2 TIM，并且在手机上安装了各种各样的软件好好的玩了一把。总体感觉Android的应用相对来说还是少了一些，耐玩的游戏还不多。其中钻石迷情(jewels)还算是比较耐玩的，时间模式下我现在的最高分是<span style="color: #3366ff;">46230</span>，和高手比起来，不知道这个分数是不是还低了些呢，呵呵。我非常期待popcap的植物大战僵尸能够尽快移植到Android平台，这款游戏深受广大玩家的喜爱，原因就是非常的耐玩，并且考验智力。

智能手机的好处就是可以自己装软件，甚至是自己写在手机里运行的软件。Android的程序需要使用Java开发，这点让我有些不爽。因为一直以来我对Java都不太感冒，虽然在语法上看起来和C#很相似。但是没办法，我还是决定硬着头皮把eclipse装上，决定学习一下Android应用程序的开发，并且，打算第一个项目把之前使用Python写的NancyGLines游戏移植到Android中。这对我来说是一个激动人心的项目，第一次学习手机软件的开发，希望NancyGLines能够早点出来，放到Android Market里。

为了我的开山之作，自然要先了解Android开发的知识。于是，我在网上找了一圈，发现资料还不少，下面是我找到的电子书列表，都可以Google到，找不到的可以留言问我要：

Android-A-Programmer&#8217;s-Guide

Android-Essentials

Introduction-To-Android

Professional_Android_2_Application_Development

Android.Application.Development.-.Programming.With.The.Google.Sdk.(O'reilly,.2009,.0596521472)

由于刚入门，我还是选择先看Android的官方文档：
  
[http://developer.android.com/guide/index.html](http://developer.android.com/guide/index.html "http://developer.android.com/guide/index.html")

官方的文档非常的详细，从基础介绍，内部架构，到入门教学示例，到每个API的说明，都非常详细。因此，我花了2个晚上的时间，把Android开发的一些基础文章以及入门示例都看了一遍，对Android开发有了一些初印象，在这里做为自己的学习笔记记录一下。

工欲善其事必先利其器，首先我需要把Android的开发环境配置好。相信也有很多朋友和我一样，在这里耽误了不少了时间。其实官方的文档中已经写的很详细，只能怪我没有仔细的看清楚。ADT插件老是安装不少，最后的原因是没有安装JDK。

步骤如下：

1. 下载并安装[JDK](http://java.sun.com/javase/downloads/index.jsp)(5或6)。

2. 下载并解压[Eclipse](http://www.eclipse.org/downloads/)。

3. 下载Android的[SDK](http://developer.android.com/sdk/index.html)，解压后，设置环境变量PATH到Tool目录。

4. 在Eclipse中通过`[https://dl-ssl.google.com/android/eclipse/](https://dl-ssl.google.com/android/eclipse/)`下载并安装Android Development Tools (ADT) Plugin。

5. 装好重启Eclipse后，在Window - Preference中设置Android SDK的路径。

6. 打开Android SDK and AVD Manager，安装不同平台的Android SDK版本，比如Andoid2.1 Android1.6。

完成了，其实并不复杂。接下来了解一下Android的架构：

![](http://developer.android.com/images/system-architecture.jpg) 

由于是入门，看上面这张图还不是很有感觉。随着以后的深入，再回过头来看这张图，应该会更有感觉。

开发环境配置好后，最行之有效的学习方法是看官方的Tutorials，包括：

*   [Hello World ](http://developer.android.com/resources/tutorials/hello-world.html)
*   [Hello Views ](http://developer.android.com/resources/tutorials/views/index.html)
*   [Hello Localization ](http://developer.android.com/resources/tutorials/localization/index.html)
*   [Notepad Tutorial ](http://developer.android.com/resources/tutorials/notepad/index.html)  

通过上面的示例，我会了解到以下东西：

#### 1. Activity

Activity控制用户界面操作的实体，一个应用程序可以有多个Activity，但同时只能有一个Activity的用户界面呈现在用户面前。我们需要实现一个类，继承自Activity类，通过重写父类的一些特定方法，就能实现在某些事件发生下，执行一些特定的代码。比如，用户按键，触摸屏幕的某个点等等。其中，关于Activity的几个状态，需要重点搞清楚，见下图：

![](http://developer.android.com/images/activity_lifecycle.png)&nbsp;

#### 2. View

用户界面布局是通过xml来描述的，比如：

<div class="cnblogs_code" onclick="cnblogs_code_show('8cc75034-9171-4f0b-9a86-ca570fe26a9a')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)<div id="cnblogs_code_open_8cc75034-9171-4f0b-9a86-ca570fe26a9a"><div><span style="color: #0000ff;">&lt;?</span><span style="color: #ff00ff;">xml&nbsp;version="1.0"&nbsp;encoding="utf-8"</span><span style="color: #0000ff;">?&gt;</span><span style="color: #000000;">
</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">LinearLayout&nbsp;</span><span style="color: #ff0000;">xmlns:android</span><span style="color: #0000ff;">="http://schemas.android.com/apk/res/android"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">ListView&nbsp;</span><span style="color: #ff0000;">android:id</span><span style="color: #0000ff;">="@android:id/list"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">TextView&nbsp;</span><span style="color: #ff0000;">android:id</span><span style="color: #0000ff;">="@android:id/empty"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text</span><span style="color: #0000ff;">="@string/no_notes"</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">

</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">LinearLayout</span><span style="color: #0000ff;">&gt;</span></div></div></div>

里面的ListView ，TextView可以理解为自带的一些控件。同时，我们也可以实现自己自定义的View，只要继承自View类。比如：
  <div class="cnblogs_code"><div><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">com.coderzh.nancyglines.GLinesView
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #ff0000;">android:id</span><span style="color: #0000ff;">="@+id/glines"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #0000ff;">/&gt;</span></div></div>

然后实现GLinesView类：

<div class="cnblogs_code"><div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;GLinesView&nbsp;</span><span style="color: #0000ff;">extends</span><span style="color: #000000;">&nbsp;View&nbsp;{
<br />
}</span></div></div>

其中一个最重要的方法就是onDraw，用来画想要呈现的用户内容。比如，我想在屏幕上写一个Hello。
  <div class="cnblogs_code"><div><span style="color: #000000;">@Override
</span><span style="color: #0000ff;">protected</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;onDraw(Canvas&nbsp;canvas)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">super</span><span style="color: #000000;">.onDraw(canvas);
&nbsp;&nbsp;&nbsp;&nbsp;mPaint.setTextSize(</span><span style="color: #000000;">20</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;mPaint.setColor(Color.BLUE);
&nbsp;&nbsp;&nbsp;&nbsp;canvas.drawText(</span><span style="color: #000000;">"</span><span style="color: #000000;">Hello</span><span style="color: #000000;">"</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">20</span><span style="color: #000000;">,&nbsp;</span><span style="color: #000000;">20</span><span style="color: #000000;">,&nbsp;mPaint);
}</span></div></div>

#### 3. Intent

Intent表示你想要做什么，AndroidManifest.xml中的filterIntent表示你的应用程序能够处理什么样的Intent。有时，还可以通过Intent来实现不同窗体间互相传递信息。

#### 4. AndroidManifest.xml文件

相当于ASP.NET的Web.config文件了，全局的一些配置。比如，设置Activity，filterIntent等等。

#### 5. 资源访问的R.java

Android里访问资源非常简单，当我们添加了资源到res目录后，ADT插件会自动更新R.java文件，通过R类，就能轻松的访问到任何res中的资源。同时，也可以界面的xml中方面的使用。

#### 6. 数据库

使用sqlite，有现成的SQLiteDatabase类可用来操作数据库。

上面都只是非常粗略的介绍，想要更深的理解还需要更多的实践。不过，通过了解上面的基本内容，我们可以大致了解开发过程中的一些步骤的实施方式。比如，界面布局在哪里设置，事件如何触发，数据如何保存，资源如何使用等等。以后若有所得，再来总结了。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/03/20/android-first.html](http://www.cnblogs.com/coderzh/archive/2010/03/20/android-first.html)**