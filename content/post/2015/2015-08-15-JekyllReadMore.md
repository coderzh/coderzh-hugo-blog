---
categories:
- 技术文章
date: '2015-08-15'
title: 使用Jekyll官方的ReadMore摘要功能
url: /2015/08/15/JekyllReadMore/

---


今天才发现，Jekyll官方就支持ReadMore摘要功能，记录一下。

<!--more-->

我之前的方法，在index.html中

```html
 {{ post.content ||split:'<!--more-->' | first }} 
```

然后在Post里，需要分隔的摘要后面加`<!--more-->。`

```html
摘要内容...
<!--more-->
正文内容...
```

### 官方做法: excerpt

官方的方法是，在_config.yml里，指定摘要的分隔符：

```html
excerpt_separator:  '<!--more-->'
```

然后，在index.html中：

```html
 {{ post.excerpt }} 
```

一般情况下，摘要需要去掉html标签，所以一般这样用：

```html
  {{ post.excerpt | strip_html }} 
```

然后，和前一种方法一样，在摘要后面加`<!--more-->`  即可。
