---
categories:
- 技术文章
date: 2016-02-05T23:55:45+08:00
keywords:
- hugo
- rapid
- theme
title: "博客皮肤单独建了个仓库"
url: "/2016/02/05/new-hugo-rapid-theme-repo/"

---

有同学提到希望将这个博客的皮肤单独建个仓库，方便使用：

[https://github.com/coderzh/coderzh-hugo-blog/issues/1](https://github.com/coderzh/coderzh-hugo-blog/issues/1)

的确，早就应该这么做了。趁着放春节假期了，把这个撸了一遍，单独的皮肤仓库叫：`hugo-rapid-theme`

只是将它从原博客中抽离出来，还有很大优化的空间，需要的同学先用着吧。

地址：[https://github.com/coderzh/hugo-rapid-theme](https://github.com/coderzh/hugo-rapid-theme)

## 说明文档

以下是 hugo-rapid-theme 的 README 文档：

Demo: [http://blog.coderzh.com/](http://blog.coderzh.com/)

### Step1 Install Hugo

Set [Hugo Install](http://www.gohugo.org/doc/overview/installing/)

### Step2 Create your site

```
hugo new site your-blog-name
cd your-blog-name
```

### Step3 Clone the theme repo

```
git clone https://github.com/coderzh/hugo-rapid-theme.git themes/hugo-rapid-theme

# replace config file
rm config.toml
cp themes/hugo-rapid-theme/config.yaml .
```

### Step4 Start your site

```
# new content
hugo new about.md
# start server
hugo server
```

### Step5 Have Fun

Now you can open [http://localhost:1313](http://localhost:1313)

Modify the config.yaml and other things, and have fun!

You can also make this repo as submodule:

```
git init
git submodule add https://github.com/coderzh/hugo-rapid-theme.git themes/hugo-rapid-theme
``` 

<!--more-->