---
categories:
- 技术文章
date: 2016-03-27T12:57:37+08:00
description: "Hugo 的 pacman 主题"
keywords:
- Hugo
- pacman
- 主题
title: "做了一个 Hugo 的主题：hugo-pacman-theme"
url: "/2016/03/27/hugo-pacman-theme/"

---

Hugo 是由 Go 语言实现的静态网站生成器，通过 Hugo 可以快速生成一个静态网站，比如个人博客。在 [StaticGen](https://www.staticgen.com/) 的静态网站生成器排名里，Hugo 排名第五，也是相当的不错。

<!--more-->

Hugo 本身有很多不错的主题，但挑剔的朋友可能会觉得还不够，希望看到 Jeklly 或 Hexo 里漂亮的主题时也能在 Hugo 里找到对应的主题。其实 Hugo 的主题制作并不复杂，有兴趣的同学可以尝试自己制作主题，或者将其他静态网站生成器里的主题转成 Hugo 的主题。

不会做的话参考我做的这个主题（[hugo-pacman-theme](https://github.com/coderzh/hugo-pacman-theme)）代码，基本的 Hugo 模板功能都用上了。

### Pacman

[Pacman](https://yangjian.me/pacman/) 是一个不错的 Hexo 主题，一直有冲动把这个主题转成 Hugo 的，再加上 Hugo 交流群里有朋友也提到了这个主题，于是利用周末的时间制作了这个主题：[hugo-pacman-theme](https://github.com/coderzh/hugo-pacman-theme)

演示地址：[http://coderzh.github.io/hugo-pacman-theme/](http://coderzh.github.io/hugo-pacman-theme/)

#### 截图

主页：

![hugo-pacman-tn](http://image.coderzh.com/hugo-pacman-tn.png)

文章页面：

![hugo-pacman-theme](http://image.coderzh.com/hugo-pacman-theme.png)

#### 支持功能

1. 分类
1. 标签（标签云）
1. 归档
1. RSS
1. 文章大纲（Table Of Content）
1. 文章分享功能
1. 图片点击预览（FancyBox）
1. 多说评论（及 Disqus 评论）
1. Google Analytics
1. 代码高亮优化（GitHub 配色）
1. 高度配置化，你要的东西都可以通过 config.toml 进行配置。

### 使用方法

1. 首先，确保安装了最新版 Hugo。下载地址：[Hugo Release](https://github.com/spf13/hugo/releases)，如果使用 Mac ，直接用 Homebrew 安装：

    ```
    $ brew install hugo
    ```

2. 把 hugo-pacman-theme clone 下来，放到你的 Hugo 站点的 themes 目录里（Hugo 的使用方法详见：[http://www.gohugo.org/](http://www.gohugo.org/)）。

    ```
    $ cd themes
    $ git clone https://github.com/coderzh/hugo-pacman-theme
    ```

3. 配置文件，拷贝一份或者参考：`hugo-pacman-theme/exampleSite/config.toml`，配置如下：

    ```toml
    BaseURL = "http://coderzh.github.io/"
    LanguageCode = "zh-CN"
    HasCJKLanguage = true
    Title = "Hugo PacMan Theme Demo"
    Theme = "hugo-pacman-theme"
    pygmentsStyle = "default"
    pygmentsUseClasses = true
    RSSUri = "feed.xml"

    [Author]
      Name = "coderzh"

    [Params]
      AuthorHomepage = "http://blog.coderzh.com"
      BottomIntroduce = "Introduce1 <br/> Introduce2"
      Description = ""
      Subtitle = "subtitle"
      Weibo = "coderzh"
      WeiboID = 1816308191
      Twitter = "coderzh"
      GitHub = "coderzh"
      Facebook = "coderzh"
      LinkIn = "coderzh"
      Imglogo = "img/logo.svg"
      AuthorImg = "img/author.jpg"
      # 日期时间格式
      DateFormat = "2006年01月02日"
      MonthFormat = "2006年01月"
      FancyBox = true

      # 使用多说评论
      #[Params.DuoShuo]
      #  ShortName = "coderzh"

      # 使用 Disqus 评论
      [Params.Disqus]
        ShortName = "coderzh"

      # Google 统计
      [Params.GoogleAnalytics]
        ID = "UA-10147768-2"

      # 多语言字符串
      [Params.Strings]
        Search = "搜索"
        PageNotFound = "你访问的页面不存在"
        ShowSideBar = "显示侧边栏"
        HideSideBar = "隐藏侧边栏"
        Categories = "分类"
        Archive = "归档"
        Tags = "标签"
        TagCloud = "标签云"
        Rss = "RSS 订阅"
        TableOfContents = "文章目录"

    [Menu]
      [[Menu.Main]]
        Name = "首页"
        URL = "/"
        Weight = 1
      [[Menu.Main]]
        Name = "关于"
        URL = "/about"
        Weight = 2
    ```

### 最后

该主题参考的 [Pacman](https://github.com/A-limon/pacman)，使用 Hugo 的模板语法纯手工一行一行打造。有需要的朋友尽管拿去使用，有问题欢迎反馈：

GitHub 地址：[https://github.com/coderzh/hugo-pacman-theme](https://github.com/coderzh/hugo-pacman-theme)

Hugo 中文文档：[http://www.gohugo.org/](http://www.gohugo.org/)

Hugo 交流 QQ 群：512499080

该主题已经[提交](https://github.com/spf13/hugoThemes/issues/121)到官方的主题列表，相信不久就可以在官方的 [http://themes.gohugo.io/](http://themes.gohugo.io/) 上看到了。
