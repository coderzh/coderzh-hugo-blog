---
categories:
- 技术文章
date: 2015-11-15T21:53:51+08:00
description: "介绍一个小而美的前端框架：Vue.js"
keywords:
- vue.js
title: "走进前端开发之：Vue.js"
url: "/2015/11/15/front-end-dev-vuejs/"

---

上一篇中，探讨了前端框架的前世今生，最后还列举了当前比较火的几个前端框架，比如：Google 的 Angular，老牌的 Backbone , Facebook 的 React 等等。今天，我只想介绍一个小而美的前端框架：[Vue.js] 。

<!--more-->

为什么说 [Vue.js] 是一个小而美的前端框架呢？因为它小， min 版本大小是 72K （ gzip 压缩后是23 K），而 min 版本的 Angular 144K，React 132K。说它小而美并不单单指它的体积，因为还有很多体积比它小的框架，小而美主要是它使用起来太 TM 的简单直观了！

Vue.js 的中文主页：[http://cn.vuejs.org/](http://cn.vuejs.org/)

在主页中，号称“10 秒钟看懂 Vue.js”，的确是这么回事：


```
<div id="demo">
  <p>{{message}}</p>
  <input v-model="message">
</div>
``` 

```javascript
var demo = new Vue({
  el: '#demo',
  data: {
    message: 'Hello Vue.js!'
  }
})
```

上面例子的效果是在 input 里输入任何内容，会自动出现在 `<p>` 里。非常简单直观的进行了数据绑定，只要数据发生变化， View 会自动发生变化。这就是数据驱动的。

并不是每个人都需要或者有机会去开发一个大型的 Web 应用，那些流行的框架又需要一定的学习曲线，而且很多功能并不需要使用到。或者说，你只想干一件简单的事情，但是由于引入了那些框架，使得自己不得不按照框架的规定定义一个又一个东西，最后仅仅是为了实现一个简单的功能。

所以，[Vue.js] 非常适合用于一些小型项目（当然，大型项目也适合。），因为可以快速上手，简单的看下它的文档就可以开始动手了。而且， Vue.js 的执行速度也非常的快。

在 [TodoMVC Benchmark](https://github.com/lhorie/todomvc-perf-comparison) 的评测中，得出的综合评价：Mercury, **Vue** and Mithril are king.

在 Safari 6.1, OS X 的评测里，Vue.js 的性能直接排到了第一的位置：

![todomvc-perf-Safari](http://7xlx3k.com1.z0.glb.clouddn.com/todomvc-pef-Safari.png)

所以，我现在就有冲动拿 [Vue.js] 来做点东西了，刚好目前要做的一个项目可以用上，这样可以少写很多烦人的 JavaScript 代码了，简直完美。

[Vue.js]（读音 /vjuː/, 类似于 view），是一个构建数据驱动的 web 界面的库。它的作者是个中国人：尤小右，真名尤雨溪，之前在 Google Creative Lab 工作过。正是目睹了 Angular 、 Ember 框架的笨重不够灵活，Backbone 不支持数据绑定 ， Knockout 和 Ractive 在组件的嵌套和组合上不够理想，于是他决定自己重新设计一个简洁的 MVVM 数据绑定的前端框架。

在 GitHub 上， [Vue.js] 已经收集了 9500 多个 Star，为了让更多人参与进来贡献代码，作者坚持保持代码测试的覆盖率为 100% 。

![vue-cov](http://7xlx3k.com1.z0.glb.clouddn.com/vue-cov.jpg)

[Vue.js] 的目标是通过尽可能简单的 API 实现**响应的数据绑定**和**组合的视图组件**。

**响应的数据绑定** 就是数据驱动视图的概念。它让你在写 Web 应用界面时，只需要关注两件事：数据如何展示和数据如何变化。一旦数据发生变化时，比如用户输入，或者 ajax 请求返回后数据发现修改，对应的视图界面会自动的进行更新。（之前的做法是使用 jQuery 手动操作 DOM 更新界面元素。）

![mvvm](http://7xlx3k.com1.z0.glb.clouddn.com/mvvm.jpg)

定义好数据如何展示，绑定数据后，就只需要关心数据如何变化的事情了，是不是感觉 So Easy ！

**组合的视图组件** 是 [Vue.js] 的一个重要概念，有了组件系统，可以很好的复用组件，提高效率，从而也为开发一个大型应用提供了很好的技术保证。

本文并不是要详细介绍 [Vue.js] 的特点及使用方法，因为要学习 Vue.js ，看官方的文档是最好的学习方式。作者是中国人，自带中文文档已经足够方便让你学习起步。本文的目的只是想介绍 Vue.js ，因为我认为它很了不起。

在如此激烈的前端框架竞争环境下， 凭借作者一己之力，用小而美，精简易用，性能还那么好的 [Vue.js] 直接挑战了像 Google 、 Facebook 这样公司开发的前端框架。作者在设计框架时，时时刻刻遵循简单、精巧、易用的设计哲学让人钦佩。为保证代码的质量，获得更多的开发者的信赖，作者的每一行代码都经过单元测试，体现了作者的严谨性。这就是我从他身上学到的东西。

最后，再次给出 Vue.js 的链接：[http://cn.vuejs.org/](http://cn.vuejs.org/)

走进前端开发系列：

1. [走进前端开发之：Bootstrap](http://blog.coderzh.com/2015/11/01/front-end-dev-bootstrap/)
1. [走进前端开发之：框架的演变](http://blog.coderzh.com/2015/11/07/front-end-dev/)

[Vue.js]: http://cn.vuejs.org/ 
