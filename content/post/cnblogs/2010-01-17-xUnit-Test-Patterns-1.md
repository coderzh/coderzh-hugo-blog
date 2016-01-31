---
categories:
- 读书笔记
- 技术文章
date: '2010-01-17'
title: 《xUnit Test Patterns》学习笔记1 - Test Smell
url: /2010/01/17/xUnit-Test-Patterns-1/

---


这本书找来很久了，一直没读。关于软件测试的好书相当少，对于测试代码的重构及模式的书就更加难得了。虽然我才读了前几章，给我的感受是，这本书确实讲的很全面，并且给很多测试中的东西给出了专业的术语，相信当我读完并吸收完这本书后，会有更多的体会和收获。

第一章是全书概述，直接跳到第二章开始我的笔记。Test Smell，测试的坏味道。和我们通常讲的Code Smell是一样的，不同的是Test Smell是从测试的角度来分析测试过程中的坏味道。测试的坏味道主要分为三类：

1.  code smells
2.  behavior smells
3.  project smells

这三种坏味道通常不是独立存在的，project smells的根源可能来自code smells和behavior smells。

#### Project Smells

出现下面的情况，可以认为出现了Project Smells：

1.  Production Bugs 产品的Bug数量高居不下
2.  Daily Integration Build 持续构建总是失败，或者需要花费大量时间去解决一个编译不过的问题
3.  Buggy Tests 太多有问题的测试案例，相反会影响到项目的效率
4.  Devolopers Not Writing Tests 开发人员不编写测试案例，导致Production Bugs增多
5.  Lost Tests 测试案例不足

#### Behaivor Smells

比较容易发现，不需要刻意去监控，因为测试案例编译不通过，或者是测试案例失败时，通常就是Behavior Smell出现的时候：

1.  Fragile Tests 容易失败的测试案例，稍微一点变化就有可能造成案例失败。通常出现在&#8220;录制回放&#8221;的测试案例中，这样的案例不仅执行不稳定，维护起来也很麻烦。因为自动生成的代码通常难以理解和维护。
2.  造成Fragile Tests原因主要有：

*   Interface Sensitivity 这是最常见的，比如，开发修改了函数接口，界面上某个按钮进行了调整，都可能导致案例执行失败。
*   Behaivor Sensitivity 被测代码的行为发生了变化，测试案例当然要失败了。（如果不失败的话，都说明测试案例有问题）
*   Data Sensitivity 使用数据库的程序，如果数据库中的数据发生变化，可能导致案例失败
*   Context Sensitivity 环境的变化，导致案例失败。比如：时间变化，硬件设备，系统环境等等3.  Erratic Tests 不稳定的测试案例，有时成功，有时失败：

*   Interacting Tests 俗称，前面的案例影响了后面的案例。比如，使用Shared Fixture时，前一个案例将Shared Fixture的状态修改，导致后面的案例都失败。
*   Test Run Wars 多个Test Runners使用同一个Shared Fixture，在同一时间执行时。也是指在非常特殊的情况下，才会出现失败的情况。这种BUG，通常也是到最后才会去修复。
*   Unrepeatable Tests 不能保证每次执行都是同样的结果，有时候还需要人工干预一下。4.  Frequent Debugging 太频繁的调试说明自动化的单元测试做的不够，或者是单元测试中，一次测试了太多的功能，不够单一。
5.  Fully Automated Tests 使用TDD的敏捷开发人员每隔几分钟就执行一次测试案例，前提是测试案例一定要自动，不需要手工干预。如果需要手工干预(Manual Intervention)，没有几个人愿意经常执行那些测试案例。
6.  Slow Tests 案例执行一定要快，如果执行慢，将不能很快将结果反馈给开发。当然，也会使得开发不愿意去执行那些又慢又不稳定的案例。解决的办法也是使用Shared Fixture。

#### Code Smells

代码的坏味道，基本上和Martin Fowler的Refactoring中讲的一样。通过看代码，可以发现很多坏味道：

1.  Obscure Tests 如果你的测试案例令人费解，根本不知道你在测试什么。之后的维护者修改这个测试案例，很可能写错，导致成为另一个Buggy Tests。
2.  Conditional Test Logic 测试案例逻辑应该尽可能单一，只测试其中一个分支。如果一个测试案例中太多的逻辑，将会让人搞不清楚。
3.  Hard-Coded Test Data 测试中的用的数据，使用硬编码，会让人无法理解这些数据，以及这些数据有SUT的联系。
4.  Test Code Duplication 减少重复的代码，增加测试代码的复用性。一个常见的方法是使用Test Utility Methods。
5.  Test Logic in Production 在产品代码中加入测试的一些逻辑是不好的，永远也无法保证这些测试用的代码不会在产品中被执行。

这一章只是对Test Smell进行了一些简要的说明，在该书的第二部分有更加详细的针对Test Smell的介绍。

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/17/xUnit-Test-Patterns-1.html](http://www.cnblogs.com/coderzh/archive/2010/01/17/xUnit-Test-Patterns-1.html)**
