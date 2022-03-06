---
title: "用 vscode 写 C/C++ 代码"
date: 2022-03-06T11:30:31+08:00
description: ""
categories:
 - 技术文章
keywords:
 - vscode
 - cquery
 - ccls
 - clangd
url: "/2022/03/06/vscode-cpp/"

---

最近用上了 MacBookPro M1，使用 [dotfile](https://blog.coderzh.com/2022/02/13/mac-dotfiles/) 配置好基本环境后，发现我的 vscode 里 C/C++ 开发环境还没配置好。一直以来，vscode 都是我的主力 C/C++ 开发环境，这其中离不开 cquery 插件。2018 年我曾写过一篇文章：[Mac 上配置 VSCode 的 cquery 插件](https://blog.coderzh.com/2018/10/14/cquery/)。

cquery 在头文件搜索，符号跳转，代码提示和补全等方面都令人满意。甚至在 V8 这样的大型仓库上，官方也有说明如何配合 cquery 进行开发 V8([https://v8.dev/docs/ide-setup#visual-studio-code-and-cquery](https://v8.dev/docs/ide-setup#visual-studio-code-and-cquery))。

几年过去了，今天在 M1 上编译 cquery 时，才发现 cquery 已经很久不维护了，github 的 repo 已经 archived 很长一段时间了（应该是2018年就关了）。这就直接导致了在 Apple Silicon 上编译不了 cquery，也就无法使用 cquery 了。

于是，得寻找一套替代 cquery 的方案。一翻寻找，两个替代方案出现了：

1. [ccls](https://github.com/MaskRay/ccls)
2. [clangd](https://clangd.llvm.org/)

2018年 4月，一位中国的年轻小伙 [MaskRay](https://maskray.me/) 从 cquery fork 了一份代码出来，并且对原有代码进行了大刀阔斧的重构：

> 在cquery的代码库上做了大量清理工作：删除第三方库、精简代码、删除过度的抽象、合并拆得过碎的文件，当然还有改名、删除waf构建系统、删除无用blob、……自己用得舒服了再推己及人，希望别人也能用上满足自己的虚荣心。其实说穿了就是和cquery/clangd抢夺用户。精简并不能改变用户习惯，带来用户。我很快瞄准了cquery用户的一个痛点：auto-index pipeline的稳定性。最大的问题是，保存文件后容易导致重复或丢失的references。如果.h和.cc没有放在同一个目录，更容易出问题。 
>
> by MaskRay《[C++ language server ccls一周年](http://maskray.me/blog/2019-04-01-ccls-one-year)》

重构和优化后的 ccls 在社区里获得不错的评价。在 cquery 停止维护，clangd 还不成熟的时候，一度还是该领域的最佳选择。而我这种老旧派还一直固守着 cquery 这只已经不再前进的工具。cquery 的作者不再维护的原因之一，竟是期待 clangd 来取代自己。

这 clangd 从名字上看来就大有来头。它背后是著名的 llvm 官方团队。它基于 Clang C++ Compiler，默认集成到了 llvm 项目中。也就是说，只要你安装了 llvm，就默认带了 clangd，不需要像 cquery, ccls 一样额外安装。

但早期的 clangd 不够成熟，bug 不断，对使用的稳定性造成了不少影响。于是不少用户转向了 ccls，虽然是个人项目，但是功能稳定，在一些特性方面支持也很好。但 clangd 也在不断的更新迭代，早期的各种问题也在逐步的解决掉，稳定性也在逐步的加强。

我很敬佩 ccls 作者所做的贡献。但是，2022年，我会先选 clangd，原因是它默认随 llvm 安装，以及它背后的 llvm 团队。简单试用后，感觉也非常的不错。待我再用长一段时间，再回过来评价，至少，还有另一个选择：ccls，在等着我。

##### vscode + clangd 使用指南

1. 安装 clangd，安装 llvm 即可：

```bash
$ brew install llvm
```

2. vscode 安装 clangd 插件，搜索"clangd"安装即可

![clangd](images/clangd.jpg)

3. vscode 官方的 C/C++ 插件还是需要的，因为我们调试等功能还需要用到。但是需要关闭它的智能提示功能：

```json
"C_Cpp.intelliSenseEngine": "Disabled",
```

4. 为你的工程生成 compile_commands.json 文件，clangd 依赖它来分析所有的依赖关系。

如果使用 CMake 编译，编译时，添加参数（-DCMAKE_EXPORT_COMPILE_COMMANDS=YES）：

```bash
$ cmake .. -DCMAKE_EXPORT_COMPILE_COMMANDS=YES
```

或者在 CMakeLists.txt 里，指定生成：

```txt
set(CMAKE_EXPORT_COMPILE_COMMANDS YES)
```

生成的 compile_commands.json 文件可能在 build 目录下，这时需要在项目主目录里创建一个该文件的软链：

```bash
ln -s build/compile_commands.json .
```

5. 重启 vscode，或者 CMD+Shift+P 输入 Reload Window

我们以著名开源代码 libuv 为例，生成 compile_commands.json 后，打开工程， 所有头文件，符号都能正确的索引和跳转：

![vscode-clangd](images/vscode-clangd.jpg)

##### 关于 Python 和 C++ 的一则趣闻

Python 的作者 [Guido van Rossum](http://neopythonic.blogspot.com/2022/02/meeting-mike-burrows.html) 的博客几年没更新了，最新更新了一篇文章，翻译过来就是：

> 2005 年底，我加入了谷歌。采访花费了令人惊讶的长时间，这是另一个故事。今天我想讲一个故事，发生在我在谷歌园区的第一周。
> 
> 在主楼有一个令人印象深刻的楼梯，通往二楼。靠近顶部的地方是一间宽敞的办公室。一位非常重要的工程师在那里工作。我看了看门上的名字，发现我认识他：他曾经是英国的一名研究生，90 年代初曾在阿姆斯特丹的数学和计算机科学研究学会（CWI）访问过我们的研究小组（Amoeba 项目）。
> 
> 很高兴找到一个我很久以前就认识的人，有一天我敲门自我介绍。是的，他也记得我，但我的喜悦很快就结束了。不仅 Python 是 Mike 在 Google 的痛苦之源（他讨厌所有非 C++ 的东西），而且他在阿姆斯特丹逗留期间，留下的一个突出的记忆是，大约有一次我带他骑车穿过城镇，坐在我的自行车后面：“这是我一生中最糟糕的骑行。”