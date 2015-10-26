---
categories:
- 技术文章
date: 2015-10-25T23:37:16+08:00
description: "Hugo中文文档网站gohugo.org上线"
keywords:
- gohugo
- 中文文档
title: "Hugo中文网站gohugo.org上线"
url: "/2015/10/25/gohugo-org/"

---

之前我在博客里写了一篇文章：[使用hugo搭建个人博客站点](http://blog.coderzh.com/2015/08/29/hugo/)，之后有很多人给我留言或者邮件，列举了在搭建Hugo时遇到的各种问题，并且提出希望能有一个中文的Hugo网站。

于是，我利用周末的时间，注册域名（居然注册到了 `gohugo.org` 这个域名），用`Hugo`本身搭建了这个网站，运行在 [DigitalOcean](https://www.digitalocean.com/?refcode=e131e2bba197) 的 `VPS` 上。这就是 [http://www.gohugo.org](http://www.gohugo.org)。

<!--more-->

### gohugo.org

网站的地址是：[http://www.gohugo.org](http://www.gohugo.org)

网站所有内容都在 `GitHub` 开源，地址：

[https://github.com/coderzh/gohugo.org](https://github.com/coderzh/gohugo.org)

该Repository已经设置了WebHook，只要有push就会自动触发 `VPS` 更新部署。如果你感兴趣，可以加入进来，你提的PR一旦被Merged将立即在网站更新出来。

### 截图

#### 首页

![gohugo-index](http://7xlx3k.com1.z0.glb.clouddn.com/gohugo-index.jpg-w)

#### 文章列表

![gohugo-post](http://7xlx3k.com1.z0.glb.clouddn.com/gohugo-post.jpg-w)

#### 皮肤列表

![gohugo-theme](http://7xlx3k.com1.z0.glb.clouddn.com/gohugo-theme.jpg-w)

#### 示例网站

![gohugo-showcase](http://7xlx3k.com1.z0.glb.clouddn.com/gohugo-showcase.jpg-w)


### 关于Hugo

使用Hugo可以快速的制作一个静态站点，同时Hugo还在不断更新和发展中，相信未来会更加易用、功能越来越好。我给Hugo提过几次PR，看过Hugo的代码，从代码的角度来看，Hugo的代码写非常简洁清晰，模块分类非常的清楚，并且配备完善的单元测试。

对于如此优秀的东西，希望能与更多人分享，通过分享和交流，希望能促进Hugo变得越来越好，让它更加广为人知。

因此，所有对Hugo感兴趣的朋友欢迎加入贡献内容，同时也欢迎有任何疑问、建议或交流的朋友加入Hugo交流QQ群：512499080。

或者微信扫一扫关注我的微信公众号：hacker-thinking

![qrcode](http://blog.coderzh.com/public/qrcode.jpg)
