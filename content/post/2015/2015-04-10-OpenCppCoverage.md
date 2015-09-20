---
categories:
- 技术文章
date: '2015-04-10'
description: C++开源代码覆盖率工具OpenCppCoverage
keywords:
- 开源
- C++覆盖率
- Windows
- 单元测试
- gcov
- Jenkins
- OpenCppCoverage
tags: []
title: C++开源代码覆盖率工具OpenCppCoverage介绍(Windows)
url: /2015/04/10/OpenCppCoverage/

---

Windows平台下开源的C++代码覆盖率工具，使用简单，功能齐全而强大。2014年才推出的，只恨没有早点发现。

<!--more-->

关于代码覆盖率统计工具，Linux平台下，gcc内置支持gcov，通过编译时加参数选项，进行代码插桩，从而实现代码覆盖率。在Windows平台下，早在几年前，我还没找到特别好用又开源的覆盖率工具，所以以前公司是自己实现了一套，使用起来也不是很方便。

最近又遇到同样的问题，不过非常幸运的是，一款开源的Windows平台的C++代码覆盖率工具出现了在我的面前：OpenCppCoverage。使用起来非常简单，它不需要在编译时插桩，只需要有pdb文件，运行时插桩，通过OpenCppCoverage启动进程即可。

官网：[https://opencppcoverage.codeplex.com/](https://opencppcoverage.codeplex.com/)

功能也比较全，主要特点有：

1. 不需要重新编译被测程序，只需要使用OpenCppCoverage运行程序。
1. 性能开销比较小。
1. 按模块、代码路径过滤。
1. 自动生成html覆盖率结果报告。
1. 支持多个覆盖率结果合并。
1. 集成Jenkins

使用起来不要太简单，执行：

```
OpenCppCoverage.exe --sources MySourcePath -- YourProgram.exe arg1 arg2
```

使用文档：[https://opencppcoverage.codeplex.com/documentation](https://opencppcoverage.codeplex.com/documentation)

Jenkins集成：[https://opencppcoverage.codeplex.com/wikipage?title=Jenkins](https://opencppcoverage.codeplex.com/wikipage?title=Jenkins)

**覆盖率详细结果**

![codecoverage](http://7xlx3k.com1.z0.glb.clouddn.com/codecoverage.png)

**Jenkins集成**

![JenkinsOpenCppCoverage](http://7xlx3k.com1.z0.glb.clouddn.com/JenkinsModuleCoverage_thumb.jpg)
