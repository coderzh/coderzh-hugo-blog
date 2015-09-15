---
categories:
- 技术文章
date: '2010-09-11'
title: 瘦客户端那些事 - 开篇
url: /2010/09/11/thincilent/

---


<span id="internal-source-marker_0.7384744474470117">人类活动最大的成本花费在哪里？我认为在沟通和学习上。我们从哇哇落地开始，就在不断的学习前人总结的经验。学校教育，大大加速了这一进程。随着互联网的发展，人们可以自由的分享知识和经验，使得我们平时遇到的问题基本上都可以从互联网上找到答案。因此，互联网当之无愧为人类最伟大的发明之一。它减少了多少
人们沟通和学习的成本啊！</span><span>这个系列里，我要说说瘦客户端的那些事。涉及的知识都是来自互联网，所以，要感谢Google，感谢Wikipedia。最后，我将我学习和总结的知识再回馈回互联网，希望能对他人有所帮助，有所启发。</span>

&nbsp;

<span>言归正传，让我们开始说说瘦客户那些事&#8230;&#8230;</span>

&nbsp;

<span>所谓&#8220;瘦客户端&#8221;，就是指，我们只需要一台配置一般的终端设备（PC电脑、手持设备等），就能拥有超计算机的计算处理能力。其实，这离我们并不遥远。BS应用的发展，已经让我们实现了只要一台配置一般的智能手机，就能通过Google完成亿万次的搜索计算。</span>

&nbsp;

<span></span>![](https://lh6.googleusercontent.com/W7ZyKulT15kh5W9dRZBhWfSF3lCrKJ4xQ-fvdXdHP7OLveWZ1gZQes80rS86NxI4d1r2aikTVCyqbpUJ0CZcnnY34V27QYp7rkK3qsOfBTwj9mz7zg)

<span></span>

<span></span>

<span>上面的这个模型大家已经熟悉的不能再熟悉了。客户端发出指令，服务端接收指令，执行完运算后，将结果返回给客户端。但是，这个系列我要讲的，并不是上面这个模型，而是：</span>

&nbsp;

<span></span>![](https://lh6.googleusercontent.com/HnjwnEKrqwecz4nVGXkr0DBxh9nlFPiupFakmQlq5kZLCtqlwDZLztdAZFHOQhL4UrCUj_ZzlFJMU1LbhvYsFGvX6c1ri0bqcQhVgqMWYl61EW9mJw)

<span></span>

<span>我们的手机（瘦客户端）不再是Google搜索中，搜索任务简单的发送者和接受者，而是一个更加实时的操作超级计算机的感受。我们的每一次鼠标移动，点击，键盘输入，触摸屏的滑动，仿佛手机本身就是一个超级计算机。有了这样的瘦客户端，我们不再需要购买价格昂贵、骨灰配置的电脑，而我们只需要一个很低配置的上网本，平板电脑，或是智能手机，就能一样畅快淋漓的玩魔兽世界、极品飞车。在未来科幻电影中的通话联络的智能手表、查看战斗指数的眼镜，都有可能实现。</span>

&nbsp;

<span>同时，我们不再为程序的跨平台所担心。瘦客户端中，能跨平台执行各种应用程序，比如Windows的Word，Linux的OpenOffice，Mac里
的XCode。更让人惊喜的是，我们运行一款软件之前，不再需要经过&#8220;下载&#8221;、&#8220;安装&#8221;的步骤，而是立即使用。不管是多大的游戏，多复杂配置的软件。我甚至大胆推测一下，在未来，人们将不再使用Windows，Linux，Mac之类的操作系统，取而代之的将是完全基于网络的网络操作系统。而现有的这些操作系统，失去了个人用户也很难再维持发展，必将慢慢被淘汰。最后必将涌现出的，是各种基于不同瘦客户端协议的完全基于网络的操作系统。谷歌现在开发的chromium操作系统，正是符合这个发展趋势的，不过具体是怎样的，我没用过，也不好说。</span>

&nbsp;

<span>在这个系列里，我尽量避免使用&#8220;云&#8221;之类炒的火热的词汇。我们见过了太多的所谓的&#8220;云&#8221;，十有八九是伪云，比如杀毒领域最大的忽悠云查杀。云计算和这里讲的瘦客户有一定的契合，但不完全相同。云计算强调的是大规模数据中心按需分配的计算能力，就像集中式发电厂。云计算是服务端的&#8220;胖&#8221;，瘦客户强调的是客户端的&#8220;瘦&#8221;，如果两者一结合，必将擦出火花。</span>

<span></span>

<span>未来并不遥远，我们能想的到的，都有人在尝试了。国外著名的有</span>[<span>Onlive</span>](http://www.onlive.com/)<span>，</span>[<span>Gaikai</span>](http://www.gaikai.com/)<span>，</span>[<span>OTOY</span>](http://www.otoy.com/)<span>等，
他们都实现了通过私有协议，在配置一般的机器上，远程玩像孤岛危机之类的大型游戏。特别是Onlive，由于其雄厚的实力，与硬件提供商、网络提供商、游
戏开发商都有深度的合作。比如，Onlive自主投资开发的定制硬件，和美国艺电有限公司（Electronic
Arts）、育碧（Ubisoft）、Take-Two互动软件（Take-Two Interactive
Software）、华纳兄弟、交互式娱乐和英佩数码美国艺电有限公司（Electronic
Arts）、育碧（Ubisoft）、Take-Two互动软件（Take-Two Interactive
Software）、华纳兄弟、交互式娱乐和英佩数码达成的深度合作。就连谷歌微软，都想买断Onlive的技术。</span>

&nbsp;

<span></span>![](https://lh6.googleusercontent.com/eTSxW6nljoFFTmfrzdsD_vZVMmC-z8HjLeEzpHAuXEQqvkYPSnwBEsJp4NyWOVpHDYbwpIrG8IILo0XLIv281KJhvG2vjBm9q4BO8Azjs9y-Bou2jg)

&nbsp;

<span>iPad展示OnLive </span><span>Demo：</span><span></span>[<span>http://v.youku.com/v_show/id_XMTgyMzYzNjI4.html</span><span></span>](http://v.youku.com/v_show/id_XMTgyMzYzNjI4.html)

<span></span>

<span>国内也有一家公司实现了这样的技术，叫</span>[<span>云联科技</span>](http://www.godhd.com/)<span>。公司仅仅成立一年多，在中国现有的网络环境下，在没有定制硬件的前提下，就做出如此惊人的成果，不得不让人称叹。</span>

<span></span>

<span>但是，这么好的技术，为什么现在还没有普及开来呢？最大的障碍，是&#8220;延迟&#8221;和巨大的服务端消耗。</span>

<span></span>

<span>先来说说延迟。这里提到的是&#8220;延迟&#8221;，而不是&#8220;带宽&#8221;。为什么呢？延迟的英文是latency，带宽的英文是bandwidth。很多时候，人们会把两者混淆。有些人搞不清楚，为什么我的带宽提升到了联通4M，玩电信的服务器网游还会卡？带宽是指每秒最大的传输能力，延迟是指信号请求从发出到接收到所经过的时间。</span>

<span></span>![](https://lh3.googleusercontent.com/FnTbUFD1VLXEpqxmFrnc-CIy3mOR6LFuMR7yg6EvHs5RQZCEm-vnNcMdpK6SlxpGrC4tUmZO514rum3XLu-gW1JcjmqgSswcE9ngFT-l3QqErDbeVw)

<span>误区：随着带宽越来越大，延迟也会越来越小。</span>

<span>上面的图已经很清楚，如果传输的数据未达到带宽限制，即便带宽再大，信号从发生到接收的时间T1-T0，只取决于其传输的速度和距离。假如服务器在美国，距离没办法改变，爱因斯坦说，速度的极限是光速。而光纤的传播速度也许只能达到40%光速。所以说，如果你要给远在4000公里之外的地方传输数据，比如从美国的加利福尼亚到马萨诸塞州，延迟不可能再低于44毫秒。</span>

<span></span>

&nbsp;

<span>游戏或软件实际消耗的带宽其实并不多，而且，带宽在理论上是可以无限增加的，而延迟才是最大的问题，因为传播的速度不可能超过光速。比如，我以前用电信
512K带宽的网络玩剑三，非常的流畅。现在我用联通4M带宽玩剑三，延迟却很高。就像Gaikai这样的公司，由于距离的限制，目前也只能接受洛杉矶地
区玩家的试玩申请。</span>

<span></span>

&nbsp;

<span>减少延迟的办法，在有限的情况下加快传输速率，以及尽可能的缩短传输的距离，比如，就近部署服务器。</span>

<span></span>

<span>另外一个障碍，是巨大的服务端消耗。我们可以想象，我们需要花费很多钱购买很好性能的机器才能流畅的玩孤岛危机之类的大型游戏。像Onlive这种云游戏服
务器供应商，相当于需要给我们每个人都配一台这样服务器。成本可见是巨大的。即便是Onlive自己定制的硬件，一台服务器同时也只能服务几个人。</span>

<span></span>

<span>除了使用瘦客户端玩大型游戏，我们还可以用瘦客户端运行我们日常使用的软件或小游戏。无需下载，无需安装，一点即用，跨平台，多么有吸引力！而且，软件相对于游戏来说，不需要高清的传输画面，因此对带宽要求也低很多。软件开发商也不再需要针对各平台进行开发。理论上我们只需要一个版本的《植物大战僵尸》，就可以在iphone, android, pc等各种终端设备上运行。</span>

<span></span>

<span>这样的技术，是如何实现的呢？像Onlive，Gaikai之类的公司，使用的是自己的专有传输协议，我无从考证。但是，接下来的文章，我会从现有的一些知名的或开源的远程传输协议开始，逐步深入技术细节，把我知道的那点瘦客户端的事告诉大家。敬请期待~</span>

瘦客户端那些事 系列：
  
[瘦客户端那些事&nbsp; - 开篇](http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html)

<span>[瘦客户端那些事 - 远程传输协议](http://www.cnblogs.com/coderzh/archive/2010/09/24/thinclient-protocol.html)</span>

<span>[瘦客户端那些事 - NoMachine的秘密](http://www.cnblogs.com/coderzh/archive/2010/10/07/thinclient-secret-of-nomachine.html)</span><span></span>

...... 

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html](http://www.cnblogs.com/coderzh/archive/2010/09/11/thincilent.html)**