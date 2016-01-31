---
categories:
- 技术文章
- 读书笔记
date: '2010-01-18'
title: 《xUnit Test Patterns》学习笔记2 - Goal Of Test Automation
url: /2010/01/18/xUnit-Test-Patterns-2/

---


或许有人觉得单元测试可有可无，因为觉得需要付出太多的精力，而客户并不需要它。这就涉及到投资回报率的问题，其实所付出的用于测试的投资，往往会收获到更多回报。它让我们减少了Bug的数量，减少了调试代码寻找Bug的时间。看下图，有效的自动化测试投资下，测试和开发付出的努力的时间图：
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns2GoalOfTestAutomation_FF5C/image_thumb.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns2GoalOfTestAutomation_FF5C/image_2.png) 

初期，随着测试的介入，开发付出的投入逐渐减少。后期，随着测试案例的完善和自动化，测试和开发所需要付出的投入都减少到一个很低的水平。阴影部分是节省的开发投入。

同时，如果自动化测试做的不好，在后期，将可能加大测试和开发的负担：
  
[![image](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns2GoalOfTestAutomation_FF5C/image_thumb_2.png "image")](http://images.cnblogs.com/cnblogs_com/coderzh/WindowsLiveWriter/xUnitTestPatterns2GoalOfTestAutomation_FF5C/image_6.png) 

&nbsp;

### 自动化测试的目标

1.  Tests should help us improve quality.
2.  Tests should help us understand the SUT.
3.  Tests should reduce (and not introduce) risk.
4.  Tests should be easy to run.
5.  Tests should be easy to write and maintain.
6.  Tests should require minimal maintenance as the system evolves around them.  

#### Tests should help us improve quality

1.  Tests as Specification 测试案例可以验证产品的行为，验证是否&#8220;building the right software&#8221;
2.  Bug Repellent 自动化测试的主要目的不是发现Bug，而是预防或防止Bug的出现。
3.  Defect Localization 顶层的customer tests只会告诉你案例失败了，unit tests会告诉你为什么失败了，能定位到具体的问题。如果customer tests失败了而所有的unit tests却通过的话，说明单元测试案例缺失了。(Missing Unit Test)  

#### Tests should help us understand the SUT

测试案例是非常好的文档，它告诉了你SUT做了些什么。同时，它还让你可以直接调试测试案例，单步跟踪，去了解整个系统是如何运作的。

#### Tests should reduce (and not introduce) risk

1.  Tests as Safety Net 测试案例应该成为修改代码安全的保障，让我们在重构旧代码时能够大刀阔斧，而不必担心会破坏什么。
2.  Do No Harm 测试案例不能对产品造成影响，一个重要的原则是，不要修改SUT。  

#### Tests should be easy to run

1.  Fully Automated Test 完全自动化
2.  Self-Checking Test 能够自我检查，说白了就是不需要人工去检查案例执行的结果对不对
3.  Repeatable Test 需要具备可重复性。鼓励开发人员在每一次按下保存按钮时都执行一次测试案例(我没事就喜欢Ctrl+S)。案例需要具备可重复性，必须具备自我清理能力(self-cleaning)，通常，是在Test Fixture的TearDown中进行环境的清理。  

#### Tests should be easy to write and maintain

1.  Simple Tests 一个首要的原则是，让测试案例尽量的简单，使得其更容易维护。一次只测一种条件（Verify One Condition per Test）
2.  Expressive Tests 测试案例要达到表达清晰的目的，比如，可以使用一些Creation Mehods和Custom Assertion。有点像BDD。
3.  Separation of Concerns 测试案例要尽量测试单一，独立的功能，不要依赖过多。往往需要前期就介入参与产品的可测性设计(design for testability)。  

#### Tests should require minimal maintenance as the system evolves around them

测试案例需要最小化维护的工作，因此，我们需要编写健壮的测试案例(Robust Test)。

### ---------------

这章讲的是测试的目标，保持案例简单，稳定，容易维护的声音似乎总是在不停的重复着，是不是有点烦了？也许作者就是希望通过这种不停的唠叨，让我们真正记住、接受，并最终体会和感悟到这些东西给我们带来的好处吧。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/18/xUnit-Test-Patterns-2.html](http://www.cnblogs.com/coderzh/archive/2010/01/18/xUnit-Test-Patterns-2.html)**
