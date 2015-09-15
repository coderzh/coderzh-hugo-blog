---
categories:
- 思考感悟
date: '2009-09-07'
title: 我的测试生活感悟2 - Art Of Unit Testing
url: /2009/09/07/MyTestingThink2/

---


<div>今天把《Art Of Unit Testing》的前四个章节读完了，作者以自己的亲身经历，使用简洁清晰的语言，为我们展现了单元测试的艺术。

</div>

<div>

1.  怎么定义一个好的测试案例呢？<span style="color: red;">好的测试案例应该是在N年后还能运行良好并易于维护的。</span>

2.  **TOOD - Testabled Object-Oriended Design**。作者也提到了这个颇有争议的问题，许多人认为，增加代码的可测性的同时，会使得代码变得更加丑陋。而作者不认为是这样，作者认为这样的修改 是<span style="color: red;">另外一种面向对象，同样的也是优美的，这就是TOOD。</span>
3.  为了代码的可测性增加的一些代码，常常不希望编译到最后的产品中。可以有很多办法，比如用宏判断，如果使用的是.NE，还有一种办法，就是在相应的函数或类上面使用这个Attribute：<span style="color: #0000ff;">[Conditional("DEBUG")]</span>
4.  **Action-Driven Testing** 与 **Result-Driven Testing**，两种不同的测试流派，一种检测行为本身，一种检查最后结果。不能说一定谁优谁劣，但作为单元测试，更多的应该是**Action-Driven Testing**，因为这样可以<span style="color: red;">隔离一些其他外部的不稳定因素，当你的案例失败时，能够更加准备的定位问题所在</span>。（事实上，集成测试就是Result-Driven Testing，一个很大的困惑就是集成测试案例失败了，通常是很难马上定位到原因的。）

5.  Stubs和Mocks的区别，这两个东西看起来几乎是一样的，事实上也确实很相似。但是，他们的区别也同样明显：**Stubs不会导致案例失败，而Mocks会**。换成我的理解就是，<span style="color: red;">Stubs是一些假的东西，它能模拟一些我们想要的结果，而Mock呢，它就是一间谍(Test Spy)，告诉我们被测代码做了些什么，于是，我们通过Mock对象来进行检查。</span>
6.  **<span>One Mock Per Test</span>**<span>，一个测试案例中，</span><span>通常的模式是</span><span>N个Stub对应1个Mock。如果一个测试案例有多于一个的Mock对象，说明你的案例感情不够专一。而一个测试案例，是可以有多个Stub对象的，他们共同协作模拟一些特定的虚拟场景，然后通过Mock对象，验证我们的被测对象是否对此做出了反应。</span>

如果您觉得有用，请您告诉我，谢谢！
</div>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2009/09/07/MyTestingThink2.html](http://www.cnblogs.com/coderzh/archive/2009/09/07/MyTestingThink2.html)**