---
categories:
- 技术文章
date: '2010-01-26'
title: 将母版页或ASPX等其他资源编译到DLL，在多个ASP.NET工程中共享
url: /2010/01/26/Sharing-Master-Pages-By-DLL/

---


这篇文章的标题实在不好取，因为需求比较复杂：<span style="color: red;">希望将母版页或ASPX等其他资源编译到一个动态链接库中，然后在Web Application中添加这个动态链接库的引用，就能使用该Dll内部的aspx页面或母版页。</span>

以模板页为例，实现的方法如下：

1. 将母版页文件作为资源编译进动态链接库中。

方法是：文件右键 - 属性 - Build Action - Embedded Resource 

2. 实现自定义的**VirtualPathProvider**，从动态链接库的中加载母版页

3. 在global.asax中注册自定义的**VirtualPathProvider**

我在博客园搜了一下**VirtualPathProvider**，曾经有人写过这方面的东西了，我就不重复了，最后我会链接一个代码示例工程并给出一些资料链接。

总之，基本原理是：<span style="color: red;">注册自定义的</span><span style="color: red;">VirtualPathProvider</span><span style="color: red;">后，asp.net网站每当访问一个虚拟路径的资源时，都会经过我的</span><span style="color: red;">VirtualPathProvider</span><span style="color: red;">，由我去加载其中的文件内容，因此，即使这个文件物理上并不存在，我也可以从数据库中加载，或者像本文的从DLL的资源中加载。</span>

参考文章：
  
[Virtualizing Access to Content: Serving Your Web Site from a ZIP File](http://msdn.microsoft.com/en-us/library/aa479502.aspx "Virtualizing Access to Content: Serving Your Web Site from a ZIP File")&nbsp;
  
[Sharing Master Pages amongst Applications by Embedding it in a Dll](http://blogs.msdn.com/shahpiyush/archive/2007/03/09/Sharing-Master-Pages-amongst-Applications-by-Embedding-it-in-a-Dll_2E00_.aspx "Sharing Master Pages amongst Applications by Embedding it in a Dll")&nbsp;

代码示例：
  
[http://blogs.msdn.com/shahpiyush/attachment/1847195.ashx](http://blogs.msdn.com/shahpiyush/attachment/1847195.ashx)&nbsp;

在博客园上曾经有人讨论过的 VirtualPathProvider：
  
[http://www.cnblogs.com/firstyi/archive/2008/04/19/1161431.html](http://www.cnblogs.com/firstyi/archive/2008/04/19/1161431.html)&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/26/Sharing-Master-Pages-By-DLL.html](http://www.cnblogs.com/coderzh/archive/2010/01/26/Sharing-Master-Pages-By-DLL.html)**