---
categories:
- 技术文章
- 读书笔记
date: '2010-01-23'
title: 《xUnit Test Patterns》学习笔记4 - Principles of Test Automation
url: /2010/01/23/xUnit-Test-Patterns-4/

---


自动化测试过程中，有一些基本的原则，就如同宣言(Manifesto)。由于大部分的原则在前面其实都提到的，因此，有的不做太多说明了。

原则：**Write the Tests First**

原则：**Design for Testability**

原则：**Use the Front Door First**

意思是说，从最外层暴露的publish方法开始测试。

原则：**Communicate Intent**

意思是说，测试案例要意图明确，这样才容易理解和维护。比如，命名时，使用Intent-Revealing Names[SBPP]。参考：[http://architects.dzone.com/news/intention-revealing-designs](http://architects.dzone.com/news/intention-revealing-designs)

原则：**Don&#8217;t Modify the SUT**

不要修改被测的对象。但有时需要使用一些Test Double或Fake对象时，要注意每个替代的对象都被测试。举了个例子，有X,Y,Z三个模块，X依赖于Y和Z，Y依赖于Z，测试X时，可以使用Test Double代替Y和Z，测试Y时，可以使用Test Double代替Z，但是在测试Z时，不能再把Z替换成Test Double了，因为Z就是被测对象。

原则：**Keep Tests Independent**

让测试案例独立，能够单独的执行，不依赖于别的案例。

原则：**Isolate the SUT**

让SUT独立，不依赖外部的环境。SUT往往会依赖一些外部的其他环境，比如，依赖一个外部的应用程序，依赖一个可用的http服务器等等。这使得测试变得不稳定，或者减慢了执行的速度。去除SUT依赖的方法是使用Test Double替换掉外部的因素。比如，需要http服务器，可以自己搭一个假的http服务器。

原则：**Minimize Test Overlap**

最小化重复的测试。我们知道，测试案例的组合是无穷无尽的，我们不可能覆盖所有的组合。但我们可以选择最佳的组合。对被测代码的同一个条件进行重复的测试是没有多少意义的。

原则：**Minimize Untestable Code**

最小化不可测试的代码，方法就是，重构！

原则：**Keep Test Logic Out of Production Code**

上一节提到了，不要在产品的代码里添加任何测试的逻辑。比如，像if tesing之类的判断。

原则：**Verify One Condition per Test**

解释的过程中，有个观点比较有意思。手工测试时，通常会做一些复杂的操作，复杂的条件组合在一起，然后看是否出错。这看起来和自动化测试或单元测试完全相反了，为什么呢？这是因为，人能够在复杂的情况下去判断各种执行结果，并能够去分析其中的问题。而我们的案例其实并没有那么智能，为了让案例能够更加精确的定位问题，我们只能检查每个案例只检查一种情况。

原则：**Test Conerns Separtely**

Separation of concerns的解释见：[http://en.wikipedia.org/wiki/Separation_of_concerns](http://en.wikipedia.org/wiki/Separation_of_concerns)

这里的意思大概是让测试案例做好分层，减少重复的部分，从而更加容易定位问题。

原则：**Ensure Commensurate Effort and Responsibility**

编写和维护测试案例的时间，不能超过实现产品代码的时间。因此，要平衡好测试与开发的付出。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/23/xUnit-Test-Patterns-4.html](http://www.cnblogs.com/coderzh/archive/2010/01/23/xUnit-Test-Patterns-4.html)**
