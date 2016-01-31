---
categories:
- 技术文章
- 读书笔记
date: '2010-01-21'
title: 《xUnit Test Patterns》学习笔记3 - Philosophy of Test Automation
url: /2010/01/21/xUnit-Test-Patterns-3/

---


这一章主要讲自动化测试的原则。前面的章节介绍了很多测试的思想，而思想的东西难免有点虚，这一章就是告诉你，遇到了具体的什么问题时，应该怎么办。作者咨询了很多的开发人员和测试人员，同时也和Martin Fowler就自动化测试的一些原则问题进行了交流，有些是显而易见的，有些又是让人把握不定。因此，这章主要讨论了以下几个问题：

1.  Test First or Last?2.  Tests or Examples?3.  Test-by-Test or Test All-at-Once?4.  Outside-In or Inside-Out?5.  State or Behavior Verification?6.  Fixture Design Upfront or Test-by-Test?  

#### Test First or Last?

是应该先写代码还是先写测试案例？作者认为应该先写测试案例，然后再写代码。这也是测试驱动开发和敏捷测试的一个重要原则。这样做的原因有很多，比如：

1.  对一个已完成或旧的代码编写测试案例，比在代码完成前编写测试案例难的多。（面对一个庞大的已完成的系统时，确实会让人无从下手）2.  先写测试案例，可以极大的增强代码的可测性。使得后面编写的代码，天生就具备可测试的能力，因为测试案例已经早于它写好了。3.  先写测试案例，可以对后面的编码起到约束作用，避免编码时添加一些臃肿的、根本就不会用到的函数，使得代码看起来更加精简。  

个人感受：

先编写测试案例再写代码，的确有很多好处。但是发现真正这样做的人很少，一方面，对于传统的软件开发公司，要做出一些改变确实有些困难。一方面，先编写测试案例带来的好处并不是立竿见影，很多人尝试了一下就放弃了。因此，需要不断的实践，坚持。(我也要努力了)

#### Tests or Examples?

这一段，说实话，没看懂在讨论什么问题。只看出在表达一个观点，测试案例相对于文档。同时，还提出一个名词：EDD（example-driven development），但后又提到EDD的框架，如RSpec，JBehave，让我有点摸不着头脑，据我说知，RSpec，JBehave应该是BDD框架才对。

作者最后的观点：Tests are examples.

#### Test-by-Test or Test All-at-Once?

到底是应该写一个测试案例，写一段代码呢，还是应该先把测试案例都写好，再写代码？这个问题比较有意思，因为这是一个非常实际的问题。迭代开发(incremental development)中，有一句话：Test a bit, code a bit, test a bit more。当然，这样的做法是比较理想的，因为这样能够更加准确的定位到代码的问题。但是，作者提到，一个更好的办法，是先列一个提纲，把测试案例的函数都填好，里面的实现为空。然后，每次填充一个测试案例，写一段代码。

我的观点：

和作者一样。比如，在需要编写一个类前，先假设自己就是代码的调用者，把Test Fixture中的测试案例罗列一下，然后再逐个完成测试案例。每编写完一个测试案例，就把相应的代码实现一下。

#### Outside-In or Inside-Out?

通常，模块之间会有一些依赖和层次结构，应该从最外层的调用模块开始写案例呢，还是从最里层开始写案例呢？作者的观点是从外到里。

先看下从里到外的情形：
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns3PhilosophyofTestAutoma_12F0A/image_thumb.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns3PhilosophyofTestAutoma_12F0A/image_2.png) 

上图，从里到外的开发过程更像传统的开发过程，容易理解，实施起来相对简单。但是，这样的顺序有个缺点，就是上层的SUT必须依赖于已经实现的底层的SUT。如果两个模块是不同的人开发的，上层模块的开发必须等底层模块的开发编写完成才能开始工作。同时，最底层的SUT先实现的话，有可能会过度设计，设计出一些上层模块根本就不使用的一些特性。最终使得整个程序的可测性降低。因此，从外向里的过程会好一些：
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns3PhilosophyofTestAutoma_12F0A/image_thumb_1.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns3PhilosophyofTestAutoma_12F0A/image_4.png) 

先编写最外层的测试案例，可以使用Test Double对象替代被调用的底层模块，使得SUT天然就具备很好的可测性（依赖注入）。同时，由于时刻都是保持&#8220;从用户或调用者的角度去思考&#8221;，使得SUT对象实现起来目标更加明确，实现的更加精简，从而避免了过度的设计。 

#### State or Behavior Verification?

提出的问题是，应该使用基于状态的验证，还是基于行为的验证？基于状态的验证是指在调用SUT后只检查SUT的状态，比如返回值，比如一个求和函数，最后检查一下求和的结果是否正确。而基于行为的验证，通常是，SUT被调用后，不仅仅改变SUT的状态，还会产生其他影响。比如，一个用户注册的函数，除了要检查返回值是否注册成功，还要坚持数据库中是否写入了新的用户记录。BDD(behavior-driven development)，就是基于行为的验证方式。作者最后说，他主要使用基于状态的验证，但有时为了追求代码覆盖率，会使用基于行为的验证。

我的理解：

对于功能单一，简单，设计良好的代码，使用State Verification确实已经足够。但往往真实的系统是很复杂的，模块之间互相调用，单个函数的功能可能也不是那么单一。基于行为的测试，其实就是站在了用户的角度，去验证各种行为所产生的各种影响。

#### Fixture Design Upfront or Test-by-Test?

Fixture是某一类案例的集合，一种观点是，让很多案例都共享一个Fixture，每个测试案例的方法执行时都会创建一个新的Fixture实例，并在案例前执行其中的SetUp方法。另一种观点是，前一个观点的做法，会让案例看起来不那么清晰，不容易找到一个测试案例的方法到底会执行哪些SetUp或TearDown的方法。因此，提出了在每个测试案例方法中，使用自定义的Minimal Fixture，而不是使用一个大的，不容易找到或理解的Fixture。

我的感受：

这一点我也有感受，我也发现我写的一些测试案例，都喜欢让很多Test Class继承一个基类Fixture，在里面定义SetUp和TearnDown，同时，子类中，还可以添加额外方法执行一些准备和清理的操作。这样，使得我的测试案例看起来并不清晰，因为很难从我的测试案例的函数中看出，我到底在SetUp里做了些什么，以及执行了哪些SetUp操作。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/21/xUnit-Test-Patterns-3.html](http://www.cnblogs.com/coderzh/archive/2010/01/21/xUnit-Test-Patterns-3.html)**
