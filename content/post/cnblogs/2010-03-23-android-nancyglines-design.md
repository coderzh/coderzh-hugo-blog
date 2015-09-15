---
categories:
- 技术文章
date: '2010-03-23'
title: Android游戏开发 - NancyGLines设计
url: /2010/03/23/android-nancyglines-design/

---


今天把之前用Python实现的NancyGLines游戏迁移到了Android中，虽然现在还只是算个毛坯版，界面比较丑陋，功能也不够完善，但是整个框架已经建立好，并且，游戏的基本功能已经实现了。见下图：

![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/AndroidNancyGLines_745/image_thumb.png "image")

&nbsp;

游戏规则：

1. 触摸某个球，然后选择一个需要移动到的没有球的地方。

2. 球移动过去后，如果满足横，竖，斜同颜色的球大于等于5个，则消去这些同颜色的球得分。

3. 如果没有消去，则会落下三个新的球。

4. 直到棋盘没有位置容下新的球，游戏结束。

下面是layout：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">&lt;?</span><span style="color: #ff00ff;">xml&nbsp;version="1.0"&nbsp;encoding="utf-8"</span><span style="color: #0000ff;">?&gt;</span><span style="color: #000000;">
</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">FrameLayout&nbsp;</span><span style="color: #ff0000;">xmlns:android</span><span style="color: #0000ff;">="http://schemas.android.com/apk/res/android"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">com.coderzh.nancyglines.GLinesView
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #ff0000;">android:id</span><span style="color: #0000ff;">="@+id/glines"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">RelativeLayout
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #ff0000;">android:layout_width</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="fill_parent"</span><span style="color: #ff0000;">&nbsp;</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">TextView
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #ff0000;">android:id</span><span style="color: #0000ff;">="@+id/text"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text</span><span style="color: #0000ff;">="@string/app_name"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:visibility</span><span style="color: #0000ff;">="visible"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height</span><span style="color: #0000ff;">="wrap_content"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_centerInParent</span><span style="color: #0000ff;">="true"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:gravity</span><span style="color: #0000ff;">="center_horizontal"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:textColor</span><span style="color: #0000ff;">="#88ffffff"</span><span style="color: #ff0000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:textSize</span><span style="color: #0000ff;">="24sp"</span><span style="color: #0000ff;">/&gt;</span><span style="color: #000000;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">RelativeLayout</span><span style="color: #0000ff;">&gt;</span><span style="color: #000000;">
</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">FrameLayout</span><span style="color: #0000ff;">&gt;</span></div></div>

&nbsp;

嗯，我使用了自定义的View - GLinesView，在GLinesView的原型是这样的：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;GLinesView&nbsp;</span><span style="color: #0000ff;">extends</span><span style="color: #000000;">&nbsp;SurfaceView&nbsp;</span><span style="color: #0000ff;">implements</span><span style="color: #000000;">&nbsp;SurfaceHolder.Callback&nbsp;{
<br />
}</span></div></div>

在这里继承了SurfaceView ，因为SurfaceView 在游戏制作上有一些优势。接着，我参考了Sample里的LunarLander代码，在建立了一个SurfaceView内部线程类，用来处理游戏的逻辑和绘制游戏画面。

<div class="cnblogs_code">
<div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;GLinesView&nbsp;</span><span style="color: #0000ff;">extends</span><span style="color: #000000;">&nbsp;SurfaceView&nbsp;</span><span style="color: #0000ff;">implements</span><span style="color: #000000;">&nbsp;SurfaceHolder.Callback&nbsp;{
<br />
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">class</span><span style="color: #000000;">&nbsp;GLinesThread&nbsp;</span><span style="color: #0000ff;">extends</span><span style="color: #000000;">&nbsp;Thread&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;initGame()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;setRunning(</span><span style="color: #0000ff;">boolean</span><span style="color: #000000;">&nbsp;running)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mRun&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;running;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;run()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;updateCanvas();
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;GLinesView(Context&nbsp;context,&nbsp;AttributeSet&nbsp;attrs)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">super</span><span style="color: #000000;">(context,&nbsp;attrs);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SurfaceHolder&nbsp;holder&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;getHolder();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;holder.addCallback(</span><span style="color: #0000ff;">this</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thread&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;GLinesThread(holder,&nbsp;context,&nbsp;</span><span style="color: #0000ff;">new</span><span style="color: #000000;">&nbsp;Handler()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;handleMessage(Message&nbsp;m)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mStatusText.setVisibility(m.getData().getInt(</span><span style="color: #000000;">"</span><span style="color: #000000;">viz</span><span style="color: #000000;">"</span><span style="color: #000000;">));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mStatusText.setText(m.getData().getString(</span><span style="color: #000000;">"</span><span style="color: #000000;">text</span><span style="color: #000000;">"</span><span style="color: #000000;">));
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;});
&nbsp;&nbsp;&nbsp;&nbsp;}
<br />
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;surfaceCreated(SurfaceHolder&nbsp;holder)&nbsp;{</span><span style="color: #008000;">
</span><span style="color: #000000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thread.initGame();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thread.setRunning(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thread.start();
&nbsp;&nbsp;&nbsp;&nbsp;}
}</span></div></div>

当surfaceCreated事件发生时，触发游戏开始，initGame()做一些游戏的初始设置，setRunning设置游戏的当前状态，start将线程运行起来。

因为我不需要实时的刷新画面，所以，我没有在线程的run方法中使用一个while循环，而只是调用了一个刷新画面的方法updateCanvas();

当用户触摸屏幕时，触发GLinesView 的onTouchEvent方法，因此，添加代码：

<div class="cnblogs_code">
<div><span style="color: #000000;">@Override
</span><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">boolean</span><span style="color: #000000;">&nbsp;onTouchEvent(MotionEvent&nbsp;event)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">float</span><span style="color: #000000;">&nbsp;x&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;event.getX();
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">float</span><span style="color: #000000;">&nbsp;y&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;event.getY();
&nbsp;&nbsp;&nbsp;&nbsp;thread.doTouch(x,&nbsp;y);
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">return</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">super</span><span style="color: #000000;">.onTouchEvent(event);
}</span></div></div>

&nbsp;

然后，实现GLinesThread的doTouch方法：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">public</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;doTouch(</span><span style="color: #0000ff;">float</span><span style="color: #000000;">&nbsp;posX,&nbsp;</span><span style="color: #0000ff;">float</span><span style="color: #000000;">&nbsp;posY)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #008000;">//</span><span style="color: #008000;">&nbsp;激活或移动某个球</span><span style="color: #008000;">
</span><span style="color: #000000;">}</span></div></div>

&nbsp;

我会使用一个二维数组来保存棋盘上每个格子的状态：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">private</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;mStatus[][];</span></div></div>

比如，mStatus[0][1] = Color.BLUE ，表示，第一行第二列的格子放置了一个蓝色的球。

当我需要移动某个球时，首先需要实现最短路径算法，因为如果有其他球的阻碍，是不能移动的。因此，我使用了一个类似的Dijkstra 最短路径算法，实现了球的移动函数：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">private</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;moveBall(</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;currentX,&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;currentY,&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;targetX,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000ff;">int</span><span style="color: #000000;">&nbsp;targetY)&nbsp;{
}</span></div></div>

&nbsp;

然后，球移动过去后，还需要实现判断是否满足横竖斜大于等于5个的情况，如果满足，则消除那些球。因此，添加clearBalls方法：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">private</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">boolean</span><span style="color: #000000;">&nbsp;clearBalls(Ball&nbsp;ball)&nbsp;{
}&nbsp;</span></div></div>

在没有满足得分条件时，需要落下新的三个球，因此，实现getThreeBalls方法：

<div class="cnblogs_code">
<div><span style="color: #0000ff;">private</span><span style="color: #000000;">&nbsp;</span><span style="color: #0000ff;">void</span><span style="color: #000000;">&nbsp;getThreeBalls()&nbsp;{
}</span></div></div>

&nbsp;

其实到这里，整个框架已经搭建起来了。整个的原理在与通过一些操作修改棋盘状态的mStatus数据结构，操作完成后，调用updateCanvas()刷新屏幕。

实现好上面的方法后，游戏已经可以运行起来了。就是上面截图中看到的效果了。之后我还需要做一些界面美化，加入菜单，关卡的操作。

最后附上：

完整代码：&nbsp;[/Files/coderzh/Code/NancyGLines.rar](http://files.cnblogs.com/coderzh/Code/NancyGLines.rar)

体验apk文件：[/Files/coderzh/Code/NancyGLines.apk.rar](http://files.cnblogs.com/coderzh/Code/NancyGLines.apk.rar)

希望大家提宝贵意见，同时，我也会继续完善这个游戏。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/03/23/android-nancyglines-design.html](http://www.cnblogs.com/coderzh/archive/2010/03/23/android-nancyglines-design.html)**