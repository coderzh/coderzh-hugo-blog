---
categories:
- 技术文章
date: 2015-11-07T08:44:26+08:00
description: "前端开发的历史，框架比较，以及对未来的思考。"
keywords:
- 前端
- Ajax
- jQuery
- Angular.js
- Backbone.js
- React.js
title: "走进前端开发之：框架的演变"
url: "/2015/11/07/front-end-dev/"

---

![angular-backbone-react-logo](http://7xlx3k.com1.z0.glb.clouddn.com/angular-backbone-react-logo.jpg-wt)

<!--more-->

上周挖了个坑，这周末怎么也得填上。对于大多数前端框架，我都并未用过，但我还是想聊一聊，这些前端框架从何而来，解决了什么问题，又有哪些高明之处。

认识了解问题，切忌一头扎进去研究而未了解其全貌。为此，我们追溯到20世纪90年代，网景浏览器横空出世，占据了浏览器市场第一的份额。那时的网景浏览器已经搭载了 Cookie、 Frames 和 JavaScript 等功能，可惜好景不长，再后来与微软的“浏览器大战”中败下了阵来。

于是网景公司将代码开源，创造了 Mozilla ，也就是现在的 Firefox。可以说，浏览器大战从未停止过，Opera 、 Safari 、 Google Chrome …… 当然，还有微软的 Internet Explorer 以及一些其他的浏览器。各浏览器引擎不同，标准不一，苦了的就是我们的主角：前端开发。

### 排版引擎

![web-kit-renders](http://7xlx3k.com1.z0.glb.clouddn.com/web-kit-renders.jpg-wt)

所有这些浏览器，使用最广泛的无非是这些引擎： **Gecko 、 WebKit 和 Trident** 。最早的 Netscape 使用的是 Gecko 排版引擎，后来的 Firefox 继承了它的衣钵。微软从 Spyglass 公司买来技术开发了 Internet Explorer ， 使用了 Trident 引擎。苹果开发了 WebKit ，做出了 Safari 浏览器，后来引擎开源， Google 做出了基于 WebKit 的 Chrome 。

有人会说，那 QQ浏览器、360浏览器、世界之窗、搜狗浏览器之类的，这些浏览器只是套了 Chrome 或 IE 的内核罢了。

而和前端程序员打交道的，最终就是这三样东西： HTML 、 CSS 、 JavaScript 。

### JavaScript

HTML 负责描述界面的元素结构， CSS 负责描述界面的样式表现， JavaScript 负责界面元素的交互和与后台数据的交互。早期的静态网页，甚至不需要 JavaScript ，因为不需要太多的交互。即使用到 JavaScript ，最多也是用于表单验证、弹弹提示框。

随着 Web2.0 的概念炒起来，动态网站逐渐成为主流。早期的动态网站，随便的一个数据更新都要刷新整个页面，体验逐渐变得不可接受。于是，局部数据刷新成了当时的热点，这就是当年炒的很热的 Ajax 技术。

![Ajax](http://7xlx3k.com1.z0.glb.clouddn.com/ajax.jpg)

Ajax 的全称是 Asynchronous JavaScript and XML , 即异步 JavaScript 和 XML 技术。当时炒的神乎其神，而其根本本质其实很简单，就是 XMLHttpRequest ，然后配合 DOM 的操作，就可以变化出各种不同的花样出来。 XMLHttpRequest 负责和服务器交互，返回数据后通过 DOM 的操作动态实时的更新界面元素。

然而，一个简简单单的 Ajax ，各个浏览器的支持却不同。为了兼容不同的浏览器，导致写 Ajax 变得异常痛苦。比如，一个 XmlHttpRequest 的跨浏览器的通用写法就必须写成这样：

```javascript
// Provide the XMLHttpRequest class for IE 5.x-6.x:
// Other browsers (including IE 7.x-8.x) ignore this
//   when XMLHttpRequest is predefined
var xmlHttp;
if (typeof XMLHttpRequest != "undefined") {
    xmlHttp = new XMLHttpRequest();
} else if (window.ActiveXObject) {
    var aVersions = ["Msxml2.XMLHttp.5.0", "Msxml2.XMLHttp.4.0", "Msxml2.XMLHttp.3.0", "Msxml2.XMLHttp", "Microsoft.XMLHttp"];
    for (var i = 0; i < aVersions.length; i++) {
        try {
            xmlHttp = new ActiveXObject(aVersions[i]);
            break;
        } catch (e) {}
    }
}
```

单单一个 XmlHttpRequest 就让前端程序员百苦难辩，更别说跨浏览器的 DOM 选择与操作、 CSS 的差异…… 前端程序员只能默默檫干眼泪，为了解决这些问题， jQuery 横空出世。

### jQuery

![jQuery](http://7xlx3k.com1.z0.glb.clouddn.com/jQuery.jpg)

jQuery 是一套跨浏览器的 JavaScript 库，既然大家都这么痛苦要处理兼容问题，那何不让我一个人来承受。自 jQuery 从 2006 年 1 月发布第一个版本以来，现在已完全占领市场。据统计，全球前10,000个访问最高的网站中，有65%使用了jQuery 。

jQuery 不仅解决了浏览器兼容的问题，还提供了大量的简便语法，用于选择和操作 DOM 对象、创建动画效果、处理事件以及 Ajax 的支持。

得麒麟才子者，可得天下。 jQuery 出来后，有种得 jQuery 者可得前端天下的感觉。随后基于 jQuery 的各种 UI 插件、组件层出不穷，如 YUI 等等，也呈现出百花齐放的气象。

似乎 jQuery 已经解决了所有问题，而我对前端开发的经验，也止于 jQuery 。 jQuery 的确能解决之前的诸多问题，然而互联网在发展，浏览器的地位不断提高，人们对浏览器里的体验的要求也逐渐变高，Web 端的功能越来越重。 Google 甚至认为你的电脑仅仅需要一个浏览器即可。

需求越来越多，功能越来越复杂，使得 JavaScript 本身的缺点暴露了出来。 JavaScript 过于灵活，代码的组织过于零散，一旦需求变得复杂，这一大坨一大坨的 JavaScript 代码将变得难以维护。特别是如今崇尚的快速开发、快速试错的开发模式，臃肿、难以组织和维护的 JavaScript 代码成了一个需要重要解决的问题。

于是，如何将 JavaScript 代码有效的组织和分类，如何简化代码的写法成为了研究的重点。就连 1978 年就被提出的 MVC 模式也被应用到了前端开发的框架之中。

### MVC

![MVC](http://7xlx3k.com1.z0.glb.clouddn.com/mvc.jpg)

MVC 是一种软件架构分层的思想。将软件系统分为三个基本部分：模型（Model）、视图（View）和控制器（Controller）。

* （控制器 Controller）- 负责转发请求，对请求进行处理。
* （视图 View） - 界面设计人员进行图形界面设计。
* （模型 Model） - 程序员编写程序应有的功能（实现算法等等）、数据库专家进行数据管理和数据库设计(可以实现具体的功能)。

MVC 的优点是将系统进行了分层，单独的分层变得逻辑更加清晰，便于维护，提高了代码的可重用性，由于各司其职，在响应变化时，也能做出快速反应。

更多关于 MVC 的历史和介绍，可以参考 Martin Fowler 的文章： [http://www.martinfowler.com/eaaDev/uiArchs.html](http://www.martinfowler.com/eaaDev/uiArchs.html)

应用到前端开发， MVC 里的 Model 、 View 、 Controller 分别对应：

* （控制器 Controller）：业务逻辑，URL Router
* （视图 View）：用户界面，DOM 处理。
* （模型 Model）：数据保存

除了 MVC ，还有 MVP、 MVVM 等模型。然而，这些所谓的概念真的重要吗？黑猫白猫都是好猫，能解决问题的才是好模型好框架。

### xxx.js

后面出来的 xxx.js 我就不太懂了。比如：**Ember.js、Angular.js、Backbone.js、Knockout.js、React.js** 。直到写这篇文章前，才打开各自的主页，粗略的浏览了一下各自的 Quick Start ， 了解了一点各自的特性。

首先，我们来对比一下这几个库在 GitHub 上的 关注度 ：

Type | Ember.js | Angular.js | Backbone.js | Knockout.js | React.js
:-- | :-- | :-- | :-- | :-- | :--
Watch | 1149 | 4036 | 1676 | 604 | 2261
Star | 15036 | 43986 | 23349 | 6903 | 30894
Fork | 3233 | 19973 | 5230 | 1180 | 4833

从上面的数据可以看出， **Angular.js 、 Backbone.js 、 React.js** 几乎占据了半壁江山。 

[Angular.js](https://angularjs.org/) 由 Google 推出，从上面的 Fork 数据看出， Angular 在社区支持和贡献上最为突出。从首页的介绍示例看出， Angular 使用简单，代码逻辑清晰一看就明白，比如数据双向绑定的示例：


```javascript
<!doctype html>
<html ng-app>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.7/angular.min.js"></script>
  </head>
  <body>
    <div>
      <label>Name:</label>
      <input type="text" ng-model="yourName" placeholder="Enter a name here">
      <hr>
      <h1>Hello {{yourName}}!</h1>
    </div>
  </body>
</html>
```

[Backbone.js](http://backbonejs.org/) 是一个老牌的 JavaScript 框架了，据说后来的 JavaScript 框架都受了它的影响。它的特点是简单、灵活，但是很多事情却要你自己来做。我只是不明白，为什么 Backbone.js 的 Getting Started 会写的那么冗长，对于初学者真的好吗？也许真的是应该是老牌框架的原因吧。

[React.js](https://facebook.github.io/react/) 由 FaceBook 开发，现在也是火的不行。 React.js 让人为之眼前一亮的功能是 **虚拟 DOM** 的机制。前面提到，为了能支持局部刷新，就需要通过 DOM 操作局部更新元素，一旦项目变大需求变的复杂，也会变得难以维护。而虚拟 DOM 解决了这一问题，通过虚拟 DOM ，你只需要关注整体的 DOM ，当数据发生变化时， React 会重新构建整个 DOM 树， 然后与上一次的 DOM 树进行对比，自己计算出需要变化的部分。由于虚拟 DOM 都是在内存中操作，所以性能会非常好。

React 推崇组件化开发，提供了专有的语言 JSX ，不过并非必须。一个简单的 React 组件的例子：

```javascript
var HelloMessage = React.createClass({
  render: function() {
    return <div>Hello {this.props.name}</div>;
  }
});

ReactDOM.render(<HelloMessage name="John" />, mountNode);
```

### 趋势

关于 Angular.js 、 Backbone.js 、 React.js ， 如果你是这三种的使用者，也许更有发言权一些。我在百度指数里对比了 angularjs , backbone , react 这三个关键字：

![angular-backbone-react](http://7xlx3k.com1.z0.glb.clouddn.com/angular-backbone-react.jpg-ws)

可见 Angular 一经推出便先发制人增长迅猛，而 React 开始阶段和 Backbone几乎并列，但从 2015 年开始爆发，增长速度直指 Angular ， 发展不可估量。

### 总结

未来前端的世界必定会是天翻地覆，过往的发展历史我能力有限也只能提到这么多。虽然前端框架还在一直往前发展，但我回过头来仔细想想，这样的发展方向正确吗？

即使很多人并不喜欢 JavaScript ， 但是 JavaScript 凭借早期的浏览器奠定了坚不可摧的地位， JavaScript 有诸多缺陷，后续的框架只是在不断的弥补它的缺陷而已。还有关于各浏览器的支持问题，后续的框架也是在不断的填坑。你们有没有想过，是否有一天，我们能从根本上去解决这些问题，而不是一次又一次的背上历史的包袱。

为了解决 JavaScript 的问题，甚至出现各种替代语言，而这些所谓的替代语言，也只能算是 JavaScript 的预处理语言，最终还是编译成了 JavaScript 代码，你不觉得有点可笑吗？

比如，**CoffeeScript、 Flow 、 Dart 、 Babel 、 TypeScript** 。 而说到 [TypeScript](http://www.typescriptlang.org/)，它的作者是鼎鼎大名的 **Anders Hejlsberg** 。刚才说麒麟之才，这个才真的是麒麟之才！他是 Turbo Pascal 编译器的作者，后来发明了 Delphi ， 加入微软后主导开发了 C# 。现在，他正致力于 TypeScript 的开发。看了最近关于的他的报道，他表示 TypeScript 并不追求替代 JavaScript ， 并不计划直接运行在浏览器或系统里，而仅仅关注如何编译成 JavaScript 。 这是一种妥协吗？ 还是暂时的低调？未来会如何发展，这是留给前端同学的问题。
