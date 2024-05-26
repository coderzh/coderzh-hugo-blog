---
title: "WebAssembly 的尾调用"
date: 2023-04-08T20:50:21+08:00
description: ""
categories:
 - 技术文章
keywords:
 - 尾调用
 - WebAssembly
 - tail call
url: "/2023/04/08/wasm-tail-call/"

---

V8 团队最新一篇[博客](https://v8.dev/blog/wasm-tail-call)里提到，在 V8 的 v11.2 版本里，支持了 WebAssembly 的尾调用指令。这一篇里，我们来看看尾调用相关的内容。首先，我们来看看，什么是尾调用。

首先，来看这样一段代码：

```c
int sum(List* list, int acc) {
  if (list == nullptr) return acc;
  return sum(list->next, acc + list->val);
}
```

上面的代码可以看到，这是一个递归的调用。每调用一次 `sum` 函数，调用的堆栈就要多一层。当函数堆栈多到一定数量，栈就会爆掉，出现 Stack overflow，或者 segmentation fault。

何为尾调用优化？

就是当出现尾调用时，不去执行 call 指令进行函数跳转，而是在原函数内展开，替换为相应的 jump 跳转指令。

我们来看一个具体的例子，比如下面这段代码：

```c
#include <stdio.h>

unsigned fib_rec(unsigned n, unsigned a, unsigned b) {
  if (n == 0) {
    return a;
  }
  return fib_rec(n - 1, b, a + b);
}

unsigned fib(unsigned n) {
  return fib_rec(n, 0, 1);
}

int main() {
  for (unsigned i = 0; i < 10; i++) {
    printf("fib(%d): %d\n", i, fib(i));
  }

  printf("fib(1000000): %d\n", fib(1000000));
}
```

fib_rec 函数里递归调用了 fib_rec 函数，递归次数一多，函数栈就会爆。我们试试用 gcc 编译和执行：

```bash
$ gcc test.c -o test
$ ./test
fib(0): 0
fib(1): 1
fib(2): 1
fib(3): 2
fib(4): 3
fib(5): 5
fib(6): 8
fib(7): 13
fib(8): 21
fib(9): 34
[1]    57017 segmentation fault  ./test
```

gcc 和 clang 本身是可以对尾调用做优化的，只要编译的时候，加上 `-O2` 参数就行，我们试一试：

```bash
$ gcc -O2 test.c -o test
$ ./test
fib(0): 0
fib(1): 1
fib(2): 1
fib(3): 2
fib(4): 3
fib(5): 5
fib(6): 8
fib(7): 13
fib(8): 21
fib(9): 34
fib(1000000): 1884755131
```

没有出错了，所以开启 O2 优化后，尾调用被优化了。

---

这是一篇未写完的文章。今天是 2024 年  5 月 26 日，看到这里，我竟然想不起来还有一篇未完的文章。这一年里，我在干嘛，我在干嘛，是一个问题。