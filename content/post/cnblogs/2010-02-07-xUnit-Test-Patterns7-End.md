---
categories:
- 技术文章
- 读书笔记
date: '2010-02-07'
title: 《xUnit Test Patterns》学习笔记7(完) - 总结
url: /2010/02/07/xUnit-Test-Patterns7-End/

---


总体来说，这本书是不错的。后面的第二部分和第三部分，主要针对Test Smells和Test Patterns进行了更加具体的描述，主要的内容和第一部分还是基本一致的。因此，我主要的精力都花在了第一部分，对于后面的第二部分和第三部分，我是跳着看完的。后面的内容当作字典来查询会比较好，因为写的比较详细。

其中有一个观点我觉得是比较新颖的，如果你分不清现在做的测试是不是属于单元测试，就请参照一下下面的吧：

A test is not a unit test if: 

1.  It talks to the database.
2.  It communicates across the network.
3.  It touches the ﬁle system.
4.  It can&#8217;t run correctly at the same time as any of your other unit tests.
5.  You have to do special things to your environment (such as editing conﬁg ﬁles) to run it.  

在讲到代码的可测性设计时，作者提出主要从以下几个方面来提高可测性：

#### Dependency Injection

依赖注入，代码设计中并不依赖于具体的实现，并且运行将特定的实现注入到系统中。注入主要有三种方式：

1.  Parameter Injection
2.  Constructor Injection
3.  Setter Injection  

#### Dependency Lookup

依赖查找，运行时动态查找到所依赖的具体对象。

#### Humble Object

这个名称很抽象，我的理解是在代码中提供一些接口出来，方面测试。

#### Test Hook

在代码中加入一些测试逻辑，比如，如果是测试模块，就怎么怎么样。不过，我想这种方式应该是不值得推荐的。

最后，很欣慰在春节前把这本书看完了，可以说收获还是蛮大的。以后遇到什么问题，可以拿这本书当资料来查。xUnit Test Patterns的官方地址如下：
  
[http://xunitpatterns.com/](http://xunitpatterns.com/)

可以在这个地址查询到每个测试模式和相关的名称解释。&nbsp;

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/02/07/xUnit-Test-Patterns7-End.html](http://www.cnblogs.com/coderzh/archive/2010/02/07/xUnit-Test-Patterns7-End.html)**
