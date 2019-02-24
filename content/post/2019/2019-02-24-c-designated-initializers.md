---
title: "C++ 的指定初始化器"
date: 2019-02-24T21:01:02+08:00
categories:
 - 技术文章
keywords:
 - C++
 - Designated Initializers
url: "/2019/02/24/cpp-designated-initializers/"


---

C99 开始支持了指定初始化器（Designated Initializers），用来方便的初始化结构体或者数组数据。

比如下面的结构体：

```cpp
typedef struct Rect {
    int x;
    int y;
    int width;
    int height;
} Rect;
```

可以这样初始化：

```cpp
Rect r = {
    .width = 100,
    .height = 100,
};
```

其中 x, y 未指定的话，会自动初始化为 0。花括号里的字段顺序也没有要求。如果要初始化一个全是 0 的结构体，可以这样：

```cpp
Rect r = {0};
// Or
Rect r1 = {};
```

需要特别注意的是，第一种写法 `{0}`，里的 0，并不是说每个字段都赋值成 0，而是说第一个字段赋值为 0，其余字段用默认值（刚好也是 0）。

假如我们写成：

```cpp
Rect r = {1};
// r will be { 1, 0, 0, 0}, not {1, 1, 1, 1}
```

再来看看几个数组初始化的列子：

```cpp
int a[8] = {[5] = 25, [2] = 15 };
// Or
int a[8] = {[5]25 , [2]15 };
// Equals
int a[8] = { 0, 0, 15, 0, 0, 25, 0, 0 };
```

甚至可以用 `[first...last]=value` 来指定一个区间的值：

```cpp
int a[] = {[2 ... 3] = 2, [5] = 25};
// Equals
int a[] = { 0, 0, 2, 2, 0, 25 }
```

注意 `[first...last]` 是从 first 到 last 的闭区间。

指定初始化甚至还可以嵌套，假如结构体定义是这样的：

```
typedef struct Point {
  int x;
  int y;
} Point;

typedef struct PointCloud {
  Point p[10];
  int width;
  int height;
} PointCloud;
```

可以这样初始化 PointCloud:

```cpp
Rect r = {
    .p[0] = {
        .x= 10,
        .y= 10
    },
    .width = 100,
    .height = 100
};
```

然后，甚至可以写出像这样的代码：

```
void init_some(PointCloud* p) {
  // do some init
}

int main(int argc, char* argv[]) {

  init_some(&(PointCloud){
    .p[0] = {
      .x = 10,
      .y = 10
    },
    .width = 100,
    .height = 100
  });
  // ...
}
```

> 上面代码如果使用 C++ 编译，会报错：`error: taking the address of a temporary object of type 'PointCloud' [-Waddress-of-temporary]`，可以加编译参数 -Wno-address-of-temporary 解决。不过不是很推荐这么做，关掉这个可能会带来其他隐藏的 BUG。

上面的代码看上去已经不像 C 了，像是另外一门语言。但是简化了初始化的过程。

好了，看上去非常酷，但前面的代码都是纯 C 的，那 C++ 支不支持指定初始化器呢？遗憾的是，直到 C++20 才开始支持指定初始化器（都什么年代了，别人家的 C，99 年就支持了）。

如果在 linux 上用 gcc C++11 去编译上面的代码，会报下面的错：

```shell
sorry, unimplemented: non-trivial designated initializers not supported
```

也别太难过，好消息是作为现代编译器的 `clang`，早早的就通过扩展的方式实现了指定初始化器。所以，即使是 C++11，使用 clang 编译和跑上面的代码，也是没有问题的。（Windows 的 MSVC 大概是指望不上了）

回到移动平台，Android NDK 开发时，能不能使用这一特性呢？Android NDK r11 开始就建议大家从 GCC 切到 clang，而且从 NDK r13 开始，默认使用 clang 编译。所以，只要 NDK r13 及以上，都可以愉快的使用这一特性。
