---
categories:
- 技术文章
date: '2010-04-18'
title: 三言两语话敏捷(1) - 反馈
url: /2010/04/18/talk-about-agile-1/

---


最近很多人都在体验VS2010，我忙着很多事，没有去体验。但我了解到其中一点，VS2010为敏捷开发提供了更多的支持。以前我所认为的敏捷开发，只有在理想公司，理想团队才可能开展，现在微软通过IDE，将敏捷的思想进行大范围的普及，让敏捷更加的深入人心。
  
[敏捷宣言](http://agilemanifesto.org/)中只有简短的几句话，但是能真正做到不是那么容易。
  <div class="cnblogs_code"><div><span style="color: #000000;">Individuals&nbsp;and&nbsp;interactions&nbsp;over&nbsp;processes&nbsp;and&nbsp;tools
Working&nbsp;software&nbsp;over&nbsp;comprehensive&nbsp;documentation
Customer&nbsp;collaboration&nbsp;over&nbsp;contract&nbsp;negotiation
Responding&nbsp;to&nbsp;change&nbsp;over&nbsp;following&nbsp;a&nbsp;plan</span></div></div>  
  
[Practices of an Agile Developer](http://book.douban.com/subject/1767907/)一书中，对敏捷开发做了一个精辟的概括：

<span style="color: red;">敏捷开发就是在一个高度协作的环境中，不断地使用反馈进行自我调整和完善。</span>

今天我就谈谈&#8220;反馈&#8221;。

最近我在做一个项目，单枪匹马，只有我一个人，看上去一点都不敏捷对吗？敏捷团队通常是一些小型团队，但是小到一个人，也不好。理想的团队应该是10人左右。每天早上的站立式会议上，我都是自报进度，对于遇到的困难，别人也很难给出意见，因为他们都没有参与进来。但是有一点，他们是这个项目未来的客户，站立式会议上，我可以听到作为客户的反馈。

这个项目是一个基于VMWare Esx的虚拟化管理平台，我有一个大客户，就是服务器管理员C。和C讨论过系统的需求和基本实现后，我开始将任务分成了以下几个部分：

1. VMWare Esx API的封装。

2. 分布式Controller, Agent控制系统。

3. 数据库设计

4. Web界面

整个过程计划在一周的时间完成，并且能够上线，提供一个基本可用的版本。看上去几乎是不可完成的任务，于是我开始了高效的Coding。过程中，我不断的收到了来自&#8220;用户&#8221;的反馈：

1. &#8220;_可以暂时使用原有系统的数据库系统，用户才不关心他的数据存在哪里。_&#8221;
  > 于是，&#8220;数据库设计&#8221;暂时砍掉。  

2. &#8220;_我最关心的是系统最基本的申请和释放功能，至于其他的细节问题，我可以暂时不关心。_&#8221;
  > 于是，&#8220;分布式Controller, Agent控制系统。&#8221;也暂时被砍掉了。不过，这个反馈来的太晚，我已经花费了一天的时间实现和调试。  

3. &#8220;_这个数据列表我希望是横着排的。_&#8221;
  > 在我把数据列表做好，自我感觉很好给C演示时，他表示希望列表是横着排列的。而这时我已经在这个竖的列表花费了不少时间。  

4. &#8220;_也许，我们可以考虑使用另外一种方式实现。_&#8221;
  > 听到这句崩溃的话时，已经周五了。这是我将系统实现的差不多的时候，找C聊天，C蹦出来的一句话。经过分析，确实可行，亡羊补牢，为时未晚。新的方案一定程度上还是对之前方案的简化，并且更加可行。  

&#8230;

在不断的用户反馈中，不断的纠正了我的方向，才使得我能够在一周的时间内完成。

有时，

我们关注的，用户不一定关注。

我们认为重要的，用户不一定觉得重要。

我们认为很酷的，用户不一定想要。

我们认为没所谓的，用户反而觉得非常重要！

所以，做用户最想要的软件，关注用户的反馈，如果可能，让用户也加入到团队的开发中来。这就是敏捷宣言中所说的：

**Customer collaboration over contract negotiation（客户协作胜过合同谈判）**

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/04/18/talk-about-agile-1.html](http://www.cnblogs.com/coderzh/archive/2010/04/18/talk-about-agile-1.html)**