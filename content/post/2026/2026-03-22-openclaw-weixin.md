---
title: "AI 时代来临，我用微信联系上了小龙虾"
date: 2026-03-22T11:29:08+08:00
description: ""
categories:
 - 技术文章
keywords:
 - OpenClaw
 - 微信
 - weixin
url: "/2026/03/22/openclaw-weixin/"

---

“AI 来的太快就像龙卷风，离不开 AI Coding 来不及逃，我不能再 Vibe，我不能再 Vibe，我不我不，我不能再 Vibe Coding～“

开头一曲，自证本文纯手工打造，绝不掺杂 AI 味道。如今 AI 迅猛发展，日新月异，不仅可以回答问题，查阅资料，还可以画图、生成视频、写文章、打代码。传统编程已经被戏称为“古法编程“，我们也即将成为最后一代掌握“古法编程“的人类。

作为人类非物质文化遗产，前 AI 时代的人类的传统技艺：古法编程，需要有人传承。当然不是说的我，能传承这种古法技艺必须是大才，通才，全才。上知徒手撸 HTML，下知 C++ 断点调汇编。而我能做的，不过是沧海一粟，不过是 AI 洋洋洒洒生成大量代码中，依然能辨别什么是代码之美。

说远了。最近兴起一阵养龙虾🦞的热潮，我也不能免俗的收养了一只。我叫它“小爪“，为了和小爪联系上，我使用了飞书。当时收养时，还不能连接微信，所以，按照指引配置了飞书渠道，步骤虽多，但很顺利。今天，微信上线了官方的 OpenClaw 插件，只需要两步，就可以和小爪联系上。我第一时间就用上了。


### 微信龙虾插件

微信是我日常使用最多的 APP，如果能在微信里和 AI 对话，体验会比切换到别的 APP 流畅很多。先来看下，用微信连接上龙虾下爪，一共要几步。

#### 第一步：更新最新微信版本 8.0.70

在 “我 - 设置 - 插件“ 界面，会出现“微信 ClawBot“ 的插件。如果没有这个插件，杀掉进程重进几次试试。

![clawbot](images/clawbot.png)

进去之后，是个连接的指引：

![clawbot-detail](images/clawbot-detail.png)

#### 第二步：OpenClaw 上安装微信插件

我是古法编程程序员，这一步对我来说，就是 2 秒钟的事情。

第 1 秒，ssh 连接上我的龙虾服务器：

```bash
ssh openclaw
```

第 2 秒，登录上后，执行命令：

```bash
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

然后会开始安装插件，一堆输出后，终端里会出现一个大大的**二维码**，提示你“使用微信扫描以下二维码，以完成连接“

如果你不懂古法编程，不会登录服务器终端，也没关系。直接问你的小龙虾，让它自己想办法。

#### 第三步：微信扫二维码，完成

扫码完成后，可以查找到新的好友：搜索“微信ClawBot“，就可以开始对话了。当然，也是可以给你的小助手改名字的。

![clawbot-profile](images/clawbot-profile.png)

### 进阶使用

#### 多 Agent 使用

总的来说，微信的龙虾插件安装使用起来非常简单，值得点赞。

但作为古法程序员，绝对不会止步于此。微信连接上后，微信上的小龙虾和飞书上的小龙虾是同一只吗？通过问小爪你的工作区和人格设定等问题，看出微信和飞书连接的是同一个 Agent，也是默认的 main Agent。

但是，在微信上和龙虾说过的话，回到飞书里，它是不会认的。说明，即使他们是同个 Agent，但是却属于不同会话（Session）。

这显然不是我要的结果。我希望微信和飞书连接的是不同的 Agent，我会赋予他们不同的人格设定，不同的任务。

所以，我需要创建一个专属于微信的 Agent。登录到龙虾服务器，创建一只鲜活龙虾：

```bash
openclaw agents add wechat
```

新创建的 wechat Agent 会有单独的工作区，单独的人格设定（SOUL.md）等等。然后编辑 `~/.openclaw/openclaw.json` 文件，进行更详细的设定。

```
{
  agents: {
    list: [
      { id: "work", workspace: "~/.openclaw/workspace-work" },
      { id: "wechat", workspace: "~/.openclaw/workspace-wechat" },
    ],
  },
  bindings: [
    { agentId: "work", match: { channel: "feichu","peer": { "kind": "dm", "id": "ou_xxx" }}}
    { agentId: "wechat", match: { channel: "openclaw-weixin", accountId: "xxx-im-bot" } },
  ],
}
```

关键点：单独给 wechat 这个 Agent 配置 bindings。其中 accountId 可以对应扫码连接的微信号，但不是直接填微信号，具体内容可以在 `~/.openclaw/openclaw-weixin/accounts.json` 里查看到。

如果你想连接多个不同微信账号，可以执行这个，生成新的二维码进行连接。连接好后，会有单独的 accountId。

```bash
openclaw channels login --channel openclaw-weixin
```

配置好后，重启 openclaw 就生效了

```bash
openclaw gateway restart
```

微信里试下和小爪说一句“你好“：

![clawbot-hello](images/clawbot-hello.png)

看到龙虾问你名字，就成功了，一个全新的龙虾就创建好了，它拥有单独的人格，工作区等等。

#### 待改善的地方

PC 微信里找不到小龙虾账号，PC 微信里找不到小龙虾账号，PC 微信里找不到小龙虾账号…

### 总结

AI 时代来临，我终于用微信联系上了我的小龙虾。后续更多玩法和经验分享，敬请期待。

文章纯手打，欢迎赞善支持。