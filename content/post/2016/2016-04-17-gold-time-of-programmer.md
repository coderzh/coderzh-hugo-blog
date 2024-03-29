---
title: 程序员的黄金时代
date: '2016-04-17T08:47:35+08:00'
categories:
  - 技术文章
url: 2016/04/17/gold-time-of-programmer/
---

![goldtime](images/goldtime.jpg)

（第一次尝试写小说，本文仅向王小波致敬，情节纯属虚构，切勿对号入座。）

我叫张三，身高 1.9 米，不要看我身材高大，我的手可细的很。我敲键盘的速度可以达到 APM 666，不带一个按错的键。其实可以达到更高，但我对 666 这个数字情有独钟。

你也许猜到了，我是一个程序员。我在全球第一的软件公司上班，公司名字叫「猎狗」。我觉得这个名字很贴切，适合大多数的程序员和产品经理前来工作，我就是其中一个。

「小黄」是我在公司的花名，每个进公司的员工都会分配一个花名，我被随机抽到了「小黄」这个花名，但是我不喜欢。每次别人叫我小黄，我都要解释我不姓黄，他们总是抿抿一笑。

我在公司升职的很快，从 D1 到 D6，我只用了 3 年的时间（心智正常的程序员一般需要 10 年）。不是因为我写代码又快又好，也不是我的代码让公司产品占据一个又一个 Store 畅销榜单第一。我写的代码没什么技术含量，因为榜单基本靠刷。

我升职快的原因是讨老板喜欢。只要老板出席的会议，我总是第一个到。我会把老板说过的每句话都记下来，一字不差，会后还会组织大家学习，深刻领悟老板提到的每一个方法论。

公司群里只要老板一发话，我总是第一个回复我来解决。只要产品一出问题，我总能说成是别人的锅。我会仔细揣摩老板发的每一条朋友圈，精准定位老板的喜好，投其所好。一旦发现老板开始发表观点了，点赞和转发是不够的，我还会第一时间准备上万字的软文往各大网站和社交媒体里发。

曾经有一次我写代码的时候睡着了，把错误的代码提交到了上线系统。用户投诉一个接着一个，我被老板的电话叫醒，我一拍桌子，愤愤的说到：「他妈的昨天隔壁老王写的什么狗屎代码，老板你不用担心，我分分钟就可以搞定！」

我用了 1 个小时理解了昨天写的代码，然后真的只用了 1 分钟就修复了 Bug。我十分得意，为此老板在给全公司的邮件里表扬了我，还许诺今年的优秀员工、重大技术突破奖非我莫属。他后来确实做到了，这点看来是很诚信的。当然，被我栽赃的王二也被开除了。

类似的事情实在太多，我不能再细说下去，我怕你们学了去我丢了饭碗。我认为这是程序员最好的黄金时代，像我这样的三流程序员也可以在全球第一的公司里混的风生水起。然而我还是想错了。有一天，我收到了 HR 寄来的解雇信，没有一点征兆。

我想一定是搞错了，解雇老板的可能性或许还要高一些，要解雇我，必须给我一个理由。我思前想后，觉得不对劲。距离上次我在软件出错对话框里弹老板裸照已经过去一年了，虽然我只设了老板一个人的白名单，同事也一直没有揭发过我。

我想是「二蛋」告的密，他一定是眼红我。但我还是要找老板问个究竟。我找到老板，老板「啪」的一声拿出一叠打印好的 A4 纸，说到：「看看！这都是什么！」

我只见最上面的一张纸工工整整的写到：

```python
secret_key = '6ICB5p2/5piv5Liq5aSnU0I='
```

我大惊失色，「老板，这可是掌握公司上亿数据的加密密钥，可不带这么随便打印出来，万一让人捡了去，可不好了。」

老板根本没有理睬我，继续问道：「这行代码是你写的不？」

对于公司保密性最高的代码，也只能是我写的了，我只好承认。

这时老板哼了一声，显得有点得意：「别以为我不知道，这段密钥是一个 Base64 加密过的字符串，我写了一个小程序，解密了一下，你过来看看！」

我很好奇老板居然懂 Base64 加密，更好奇他还会写代码。我知道了，一定是二蛋写好的代码发给了老板。我凑过去看，老板找了半天没找到点哪个按钮可以执行，然后我告诉了他。接着，屏幕的赫赫的输出了解密的结果：

```
老板是个大SB
```

我突然想起来了，确实有这么回事，但我不能承认，说到：「老板，这你也相信？」

老板：「这程序执行的结果千真万确，『老板是个大SB』绝对没错。 」

我噗呲一笑，又感觉不太好，气氛有点尴尬，正想怎么把这事推到二蛋身上。老板继续发飙起来，你看看后面的，比如这个：

```
<html>
<!-- 老板是个大SB -->
</html>
```

还有这个单元测试案例：

```python
def test_stupid_boss(self):
    self.assertEquals('老板是个大SB', dog_company().get_boss())
```

我看着这些代码，心里想着我的代码写的还是不错的，代码工整，命名也很规范。我和老板说：「有人要诬陷我。」

「整个公司就你写单元测试，刚才的测试代码除了你写的，还能有谁？」

这时老板的逻辑性变的强了起来。的确，这一点我无可辩驳，暗暗发誓以后再也不写什么单元测试了，都是害人的东西。

「那你怎么确认不是别人偷偷改了我的代码？」

「这里的每一行我都 git blame 过了，就是你写的！」

我突然有种感觉，老板也不是那么 SB，至少逻辑性非常强。我正打算和他解释 git 的 commit log 也是可以随便修改的，老板只和我说了一句「滚！」。

在猎狗公司，只要老板说出「滚」字，你是不能进行任何辩驳的，就像一道圣旨，没有任何回旋的余地。也不会有任何回旋的余地，因为假如我没有滚，就相当于老板承认了是大 SB 的事实。我也必须滚，因为我还在更多的代码里藏了骂他的话，骂的更不堪入目，假如哪天他发现了，我还是得滚。

有人问我，老板对你这么好，为什么还骂他？我说我没有，我只是说了实话。

生活还得继续，我依然相信现在是我的黄金时代，像我这种高高级开发狗，肯定会有大量的公司抢着要。然而我还是想错了。

那天我来到程序猿拍卖基地，和很多程序员站成一排，等待上台拍卖，希望被好的雇主看中。我们被分成了几个组，由于我之前在猎狗公司工作过，自然被分配到了狗组。我看见对面站了一排人，他们左顾右盼，不停的用眼角余光警惕别人，时而露出奸诈的微笑，他们是狼组。最受雇主青睐的一个组。

我和拍卖基地的人说，我应该属于狼组，我凶的很，警惕性高，写代码可以不休息，进攻性也强，把我派去竞争对手公司做卧底分分钟将它搞垮。我说了很多，他们说你说什么没用，他们说你是狗，你就是狗。我看看对面的一群即将失业的羊组，想想还是有道理的。

轮到我上台了，主持人开始介绍我：「张三，猎狗高高级开发狗，...... 离职原因：在代码里辱骂老板是大SB。」我的天，本来以为三路破塔拿下高地只是分分钟的事情，想不到猎狗的老板还给我来了这么一出，感觉就像被剑圣偷了基地。雇主们纷纷灭灯，我闭上眼睛，等待导播放「可惜不是你」。

最后我被一个雇主雇佣了，原因是他在听介绍时睡着了没有灭灯，也不知道我辱骂老板的事。这家公司叫「巨狼」，是个游戏公司。我顺理成章的从狗晋升到了狼，十分高兴。

我被分配到了开宝箱组，每天的任务就是写游戏里开宝箱的功能。我和老板说，开宝箱涉及到人工智能、大数据分析、心理学、社会学等众多领域，技术难度高，开发时间长，吸金能力强，所以得加钱加人。老板是聪明人，说：「叫你写开宝箱，别叽叽歪歪。」我不确定我是不是听错了，这不是羊才干的事情的吗？但老板就是老板，肯定比我高瞻远瞩，我不敢骂他，偷偷的也不行。

有一天我去 UI 组提宝箱界面需求，是一个面容清秀的 UI 妹子，她叫陈清羊。我提完需求后正要走，她一把拉住了我，问我晚上有时间没，要找我单独谈谈。我再次不确定是不是听错了，虽然我身高 1.9，但平时邋遢的很，头发蓬松，拖着拖鞋上班，几天也不洗一次脸。我环顾四周，确认了她确实是在和我说话。淡淡的说了一句：「行吧。」

陈清羊很漂亮，她肯定不会看上我，这点是可以确定的。我们在约好的咖啡厅见面，她上来就说，「别人都说我和老板有一腿，可是我不是，你能帮我证明吗？」原来是她看我天天写开宝箱比较老实，没有像其他同事一样天天去骚扰她，就想找我证明。

「别人都说你和老板有一腿，那就是有一腿，没有什么好辩驳的。」

「可是我没有啊，而且我也不认为和老板有一腿有什么不好的。」

「你看你面色红润，ru 房高耸，穿着时髦，时不时往老板办公室里钻，上班比谁都晚，下班比谁都早，升职比谁都快。就是我也相信你和老板有一腿啊。」

陈清羊看我分析的头头是道，但回想到我夸她的用词，脸上泛出一道红晕。

「要是你每天像我蓬头垢面，别人上班你下班，就没有人再说你。」

之后，陈清羊还是经常来找我，要我证明。这样一来，在同事间反倒传出了我和她的绯闻来。绯闻闹的越厉害，她越是不怕，越是来找我。

她和我说，同事都说她和我有一腿，要我证明没有。我想了想，说到：「我倒挺希望证明有。」她有点生气，她并不介意有一腿，介意的是没有的事，却被别人说成了有，感觉吃了亏。

那天晚上我和她讲了很多故事，特别是水泊梁山的故事。我和她说，义气就是不管你是什么人，有多坏，都会无条件的支持你。我称它为「伟大友谊」，我和她就是伟大友谊。她听了很感动，仿佛某根神经被电触到，对我说的话深信不疑。

我心里一阵窃喜，看了看外面，天色已晚，接着说到：「我来公司这么久了，一直都是一个人，有件事情，只有你才能帮我。」

陈清羊的脸更红了，她知道是什么，为了伟大友谊，她什么都可以做。于是我们不约而同的拿出了笔记本电脑，我写代码她画画。我接了个私活，就缺一个设计师。

我们接了不少私活，赚了不少钱。别人都知道我和她接私活，也就不再说有一腿的事了。后来有人向老板举报，老板要我们交代事情经过，不能遗漏任何一个细节。我把所有细节都交代了，唯独没有交代那天我指着陈清羊的设计稿大骂「什么狗屁设计」这件事，老板更关心的是敦伟大友谊的细节。

后来陈清羊也交了一份自我检讨的材料上去，第二天我们就被开除了。老板给了我们 N+10 补偿，叫人帮我们收拾好，还特定送我们出了公司。

我和陈清羊开了一家游戏公司，公司里没有狼，没有狗，也没有羊，只有人。现在公司已经有 168 人，一年的利润有 12 亿美元。我们的公司名叫「超级人」，我们尊重公司里的每个人，我们用正确的方式激励员工，发挥他们最大的创造力。他们工作的很开心，既实现了人生的价值，又收获了财富。

陈清羊说，这是她的黄金时代，特别怀念当时敦伟大友谊时的紧张和兴奋。

但是有一件事情我一直不敢问她，就是当年她写的那份材料到底写的什么，会让老板给了我们 N+10 的补偿，才有了第一笔启动资金。直到我去参加她和老板的婚礼，我才有勇气问她。

她说，她只写了一件事。就是关于那天我指着她的设计稿，毫不留情面的大骂「什么狗屁设计」的这件事。在检讨材料里她写道，我骂她的一瞬间，她觉得如春藤绕树，小鸟依人，再也不想理会别的事，就在那一瞬间，她已经把一切都遗忘，她已经爱上我了，而且这件事永远都不能变。

之后我再也没见过她。这就是我的黄金时代，一个程序员的黄金时代。

题图摄影：chillmimi

图片授权基于：CC BY 2.0 协议
