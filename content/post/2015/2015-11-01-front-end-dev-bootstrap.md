---
categories:
- 技术文章
date: 2015-11-01T07:37:56+08:00
description: "走进前端开发之：Bootstrap"
keywords:
- bootstrap
- CSS
- Javascript
- 自适应
- 响应式布局
- 终端适配
- 布局
title: "走进前端开发之：Bootstrap"
url: "/2015/11/01/front-end-dev-bootstrap/"

---

![bootstrap](http://7xlx3k.com1.z0.glb.clouddn.com/bootstrap.jpg-wt)

<!--more-->

如今互联网创业热潮此起彼伏，特别是移动互联网，使得前端开发这一职位变得愈加炙手可热。大量公司欲求高端前端开发而不得，进入前端开发浩瀚大军的同学也是日益增多，大家相互厮杀，占领 `GitHub` ，只为获得前端开发的一席之地。新技术新框架如雨后春笋，层出不穷，未跟上步伐者也以迅雷不及掩耳之势被取代淘汰。这是一个前端开发百花齐放的时代。

这段文绉绉的开场白，只为说明一个道理：再不了解学习前端，你就老了。在我们那个年代（好吧，其实也不久），还未有前端开发这样的职位。那时的网站开发同学哪个不是一把辛酸一把泪的不断挑弄着 `CSS` 和 `JavaScript` ，纵然有一万个草泥马崩腾而过，也只能默默忍受这混乱不堪的一切，在浏览器兼容这一世纪难题面前，心中只能默念：能用就行，习惯就好。除了搬弄前端的 CSS 和 Javascript ，那时的网站开发同学还要兼顾后端。那时的MVC更像是一个整体的概念，而如今随着前端表现日益丰富，重心不断往前端移，后端只需提供类似 `Restful` 接口、处理逻辑、存储数据。单单一个前端，已经衍生出各种MVC框架：Embejs、Angular.js、Backbone.js、Knockout.js、React.js……

然而，这些前端框架我一个也没有用过。我也不是一个前端程序员，所以在写这篇文章时，我也是诚惶诚恐的。毕竟我一个外行，要是让专做前端开发的读者看了，难免班门弄斧贻笑大方，也许还少不了几句点评指责。当然，我也是虚心接受的。“走进前端开发”我打算写成一个系列文章，目的并不是多深入的介绍和学习前端开发，而是“走进”，或者说“走近”、“了解”，站在一个旁观者的角度去观察了解，前端开发到底是怎样一个群体。

这是第一篇，主角是： `Bootstrap` 。我在做 [http://www.gohugo.org/](http://www.gohugo.org/) 时就使用到了 Bootstrap 。或多或少你也许听过 Bootstrap 的大名，或者“响应式布局”是否在哪里听过？何为“响应式布局”？响应式布局是指，一个网站只需要做一个版本，就能自动适应和兼容各个终端平台，比如：PC、手机、平板，呈现出最好的表现效果。

### 多终端适配

这样又要说到“多终端适配”的问题了。在响应式布局出现之前，人们是怎么处理多终端适配的呢？主要有两种方式：

1. 跳转适配

    跳转适配会根据你使用的设备类型跳转到对应的单独地址。比如：你在手机浏览器里输入 163.com ，会自动跳转到 3g.163.com 。实现的方法是在通过 Meta 信息申明，或是 Server 根据 User-Agent 进行跳转。跳转适配需要针对不同设备类型，使用不同的url，做多套界面。

2. 代码适配

    代码适配在不同设备中使用同一个 URL ， Server 会根据 User-Agent 的不同生成不同的 HTML 页面。比如在手机里输入： weixin.qq.com ，虽然地址一样，但看到的内容和PC端是完全不一样的。（你会发现找不到“公众平台”的入口）

显然，这两种适配方式的维护成本都比较大。因为要针对不同平台维护不同版本，常常会出现移动版和 PC 版不同步的问题。

接着，就要提到第三种适配方式：

**自适应：同一 URL ，同一套 HTML 界面，根据使用设备（PC、移动设备、平板电脑）的不同，根据屏幕尺寸呈现出不同的结果。**

“响应式布局”就是自适应适配的一种布局方式。为了让自适应适配更加方便易用，Bootstrap框架应运而生。

### Bootstrap

[Bootstrap](http://getbootstrap.com/) 是 Twitter 推出的一个用于前端开发的开源工具包。它由 Twitter 的设计师 Mark Otto 和 Jacob Thornton 合作开发，是一个 CSS/HTML 框架。通过 Bootstrap ，你可以非常轻松的设计出移动端友好，又能在不同设备适配良好的网站。

Bootstrap 天生为移动设备而设计，框架由内到外默认都是移动设备优先的。使用 Bootstrap 非常简单，首先将页面设置成 HTML5 文档类型：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  ...
</html>
```

在 `<head>` 之间添加 viewport 元数据标签：

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

你还可以设置禁用缩放功能，让你的网站在浏览器里看上去更像一个原生应用：

```html
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

使用 Bootstrap 最简单快速的方式是直接使用 Bootstrap 中文网提供的 CDN 加速服务。

```html
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- 可选的Bootstrap主题文件（一般不用引入） -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
```

你还可以使用 `Bower` 、 `npm` 、 `Composer` 等工具进行安装。为了更强的定制性，你还可以使用 `Less/Sass` 源码进行编译。 

编译？其实就是CSS文件的生成过程。我们知道，CSS 在处理样式时异常灵活，以至于不同人写出来的样式代码五花八门，各种元素之间相互影响相互制约，某处稍一改动就有牵一发而动全身的效果。再加上不同浏览器支持的特性千差万别，使得CSS代码变得非常难以组织和维护。

由此，CSS 预处理应运而生。通过定义一种新的语言，自动实现浏览器兼容、变量、结构体等功能，还支持逻辑判断和循环，最后通过编译生成最终的 CSS 目标文件。使得代码更加简洁，容易维护。而 Less/Sass 就是目前最流行的CSS预处理器。

除了上面的方式，你还可以像我这种懒人一样直接下载现成的示例模板，然后再做一些细微的调整。

### Bootstrap 布局

Bootstrap 提供了一套完整的基础 CSS 模块，预定义了一套简单易用的样式组件，同时结合jQuery 提供了一套基础的方便的 Javascript 交互组件。简直就是提供了 Web 前端的一站式解决方案。

这里我只介绍一下自适应适配最核心之处： Bootstrap 的栅格布局系统。

首先，我们要为页面内容和栅格系统包裹一个 `.container` 容器：

```html
<div class="container">
  ...
</div>
```

`.container` 类用于固定宽度和响应式布局的容器，如果占据 100% 的宽度，使用 `.container-fluid` 类：

```html
<div class="container-fluid">
  ...
</div>
```

栅格系统会根据屏幕和视口（viewport）的尺寸，将一行分为最多 **12** 列，通过预设好的栅格类表示需要占多少个列宽度。比如，可以使用 3 个 `.col-xs-4` 可以将页面容器分成 3 个等分。使用 1 个 `.col-xs-3` 和 1 个 `.col-xs-9` ，可以对页面容器进行 3：9 比例分割，实现一个左侧 Sidebar 的效果。

比如：

![bootstrap-grid](http://7xlx3k.com1.z0.glb.clouddn.com/bootstrap-grid.jpg)

```html
<div class="row">
  <div class="col-md-8">.col-md-8</div>
  <div class="col-md-4">.col-md-4</div>
</div>
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4">.col-md-4</div>
</div>
<div class="row">
  <div class="col-md-6">.col-md-6</div>
  <div class="col-md-6">.col-md-6</div>
</div>
```

除了指定宽度，还可以通过指定 `.col-md-offset-*` 等进行偏移。回到一个重要的问题，知道了大致如何布局，那如何进行移动适配呢？

上面的例子我们看到，有 `.col-xs-*` 和 `.col-md-*` 等等，其实 xs 、 md 等对应的是不同显示设备。比如：

* `.col-xs-*` ：超小屏幕、手机 (<768px)
* `.col-sm-*` ：小屏幕 平板 (≥768px)
* `.col-md-*` ：中等屏幕 桌面显示器 (≥992px)
* `.col-lg-*` ：大屏幕 大桌面显示器 (≥1200px)

通过给 div 定义多个 `col-xx-*` 的组合就可以达到不同移动设备进行布局适配的目的。

比如下面的示例：

```html
<div class="row">
  <div class="col-xs-6 col-md-3">.col-xs-6 .col-md-3</div>
  <div class="col-xs-6 col-md-9">.col-xs-6 .col-md-9</div>
</div>
```

将实现在手机端进行 6：6 布局，在中等屏幕的PC端进行 3 : 9 布局。

### 总结

如今 Bootstrap 已经被广泛使用，国内外大量网站使用 Bootstrap 数不胜数。如果你需要开发一个移动端友好的网站， Bootstrap 是你的不二选择。本文只是 Bootstrap 的粗浅入门，有兴趣的同学可以找资料进行更加深入的学习。

Bootstrap 官方网站：[http://getbootstrap.com/](http://getbootstrap.com/)

对于前端开发的 Bootstrap 这把利器多少有了一些了解，接下来可以去了解了解那些号称1，2周就有大更新，1，2个月就有新冒出来的，3，4个月不学就要落伍的前端框架了。