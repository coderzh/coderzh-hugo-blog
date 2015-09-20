---
categories:
- 技术文章
date: '2015-08-15'
description: ThreadSanitizer又叫TSan，是一个检查线程Data Race的C/C++工具。它集成在新版的gcc和clang中，通过编译时加-fsanitize=thread，可以在运行时检测出Data Race的问题。
keywords:
- ThreadSanitizer
- TSan
- 线程安全
- 代码扫描
title: 使用ThreadSanitizer线程检查工具
url: /2015/08/15/ThreadSanitizer/

---


ThreadSanitizer又叫TSan，是一个检查线程Data Race的C/C++工具。它集成在新版的gcc和clang中，通过编译时加-fsanitize=thread，可以在运行时检测出Data Race的问题。

<!--more-->

ThreadSanitizer官网：[https://code.google.com/p/thread-sanitizer](https://code.google.com/p/thread-sanitizer)

### Data Race

![DataRace](http://7xlx3k.com1.z0.glb.clouddn.com/Data-race.jpg)

Data Race是指多个线程在没有正确加锁的情况下，同时访问同一块数据，并且至少有一个线程是写操作，对数据的读取和修改产生了竞争，从而导致各种不可预计的问题。

Data Race的问题非常难查，Data Race一旦发生，结果是不可预期的，也许直接就Crash了，也许导致执行流程错乱了，也许把内存破坏导致之后某个时刻突然Crash了。

### 环境要求

1. Linux x86_64，内核版本不要太旧。（经测试，公司旧的开发机Linux内核是2.6.16是跑不了的，新的tlinux内核3.10.0可以）
1. gcc 4.8版本以上（clang也集成了，3.2版本以上）

### 官方示例

```cpp
$ cat simple_race.cc
#include <pthread.h>
#include <stdio.h>
 
int Global;
 
void *Thread1(void *x) {
  Global++;
  return NULL;
}
 
void *Thread2(void *x) {
  Global--;
  return NULL;
}
 
int main() {
  pthread_t t[2];
  pthread_create(&t[0], NULL, Thread1, NULL);
  pthread_create(&t[1], NULL, Thread2, NULL);
  pthread_join(t[0], NULL);
  pthread_join(t[1], NULL);
}
```

上面的代码在不加锁的情况下，两个线程同时去修改Global变量，从而导致Data Race。使用gcc的-fsanitize=thread 编译，执行

```cpp
$ g++ simple_race.cc -fsanitize=thread -fPIE -pie -g
$ ./a.out
==================
WARNING: ThreadSanitizer: data race (pid=26327)
  Write of size 4 at 0x7f89554701d0 by thread T1:
    #0 Thread1(void*) simple_race.cc:8 (exe+0x000000006e66)
 
  Previous write of size 4 at 0x7f89554701d0 by thread T2:
    #0 Thread2(void*) simple_race.cc:13 (exe+0x000000006ed6)
 
  Thread T1 (tid=26328, running) created at:
    #0 pthread_create tsan_interceptors.cc:683 (exe+0x00000001108b)
    #1 main simple_race.cc:19 (exe+0x000000006f39)
 
  Thread T2 (tid=26329, running) created at:
    #0 pthread_create tsan_interceptors.cc:683 (exe+0x00000001108b)
    #1 main simple_race.cc:20 (exe+0x000000006f63)
==================
ThreadSanitizer: reported 1 warnings
```

执行程序，如果发生Data Race，错误信息会直接输出出来。如果错误信息比较多，重定向输出流到文件里，慢慢分析：

```
$ ./a.out >result.txt 2>&1
```

### 关键要点

1. 除了加-fsanitize=thread外，一定要加-fPIE -pie。
1. -g 是为了能显示文件名和行号。
1. 如果分生成obj(-c)和link两个步骤，每一步都加：thread -fPIE -pie -g，并且在link的时候加-ltsan
1. 只支持64位，最好指定编译64位(-m64)
1. 如果依赖其他静态库，其他静态库编译时必须指定-fPIC（如果不是请重编）
