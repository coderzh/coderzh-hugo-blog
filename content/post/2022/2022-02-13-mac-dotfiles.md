---
title: "懒程序员和他的 dotfiles (2022)"
date: 2022-02-13T10:48:03+08:00
description: ""
categories:
 - 技术文章
keywords:
 - dotfiles
url: "/2022/02/13/mac-dotfiles/"


---

如果你不知道什么是 dotfiles，那你就不会知道什么是 dotfiles。如果你知道什么是 dotfiles，那你就知道什么是 dotfiles。

16 年曾经写过一篇《[懒程序员和他的 dotfiles](https://blog.coderzh.com/2016/03/19/dotfiles/)》，这篇是 6 年后的更新版本。这些年来，软件有发生很多变化。比如编辑器软件 atom 日渐没落，vscode 已经成了主流。Homebrew casks 也默认集成进了 Homebrew 主程序。

之前曾用 mackup 软件用来自动备份和恢复各软件的配置。到今天，已经越来越多软件支持了云端同步配置。比如 vscode 的云端同步设置就非常好用，只要登录 Github 账号，所有的设置，插件瞬间恢复了。

这几天再试验 mackup，发现虽然它支持的软件很多，但难免对某些软件的设置备份存在问题。比如 iTerm2 的设置不能自动备份和恢复。如果需要经常对 mackup 的软件备份规则进行自定义，则维护的成本太高。随着软件的不断更新，通过 mackup 来维护配置会变得越来越困难。

所以，我打算放弃 mackup 备份配置文件。需要恢复设置的软件主要有两类：一类是常用的必要软件，比如 oh-my-zsh, vim 等，这类可以通过 dotfiles 脚本自动做软链恢复。另一类是通过软件本身的云端同步能力，或者配置导出/导入功能。手工导出和导入虽然麻烦一些，但操作不算频繁也是能接受的。

对于一台新装的电脑，这里主要指 Mac。我主要需要哪些软件和设置，这是 dotfiles 自动脚本要解决的问题。所以这里的 dotfiles 是根据我自己的开发和使用习惯定制的，而且是比较基础的一些设置。如果你觉得有用，完全可以针对自己的习惯再做定制。

对于我来说，新装电脑有几样东西对我来说是很重要的：

1. 输入法
2. Chrome 浏览器
3. Alfred + Iterm2 + oh-my-zsh
4. vim + vscode

有这几个东西，基本可以工作了。接下来才是一些常用的软件：Dropbox、Lemon、QQ、微信、IINA播放器等等。这些都可以通过 brew 或者 brew cask 来自动安装。

还有一类是 Mac 的系统设置，非常实用的设置如下：

```bash
# 关闭开机 Duang~ 的声音
sudo nvram SystemAudioVolume=" "

# 电池显示是百分百
defaults write com.apple.menuextra.battery -bool true

# 设置键盘按键重复的延迟
defaults write NSGlobalDomain KeyRepeat -int 3

# 支持长按连续输入
defaults write -g ApplePressAndHoldEnabled -bool false

# 禁止自动拼写纠正
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false

# Finder 显示状态栏
defaults write com.apple.finder ShowStatusBar -bool true

# Finder 显示地址栏
defaults write com.apple.finder ShowPathbar -bool true

# 禁止在网络驱动器上生成 .DS_Store 文件 
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true

# 设置日期时间格式为 24 小时制
defaults write com.apple.menuextra.clock "DateFormat" "EEE MMM d  H:mm"
```

### 我的 dotfiles

repo: [https://github.com/coderzh/dotfiles](https://github.com/coderzh/dotfiles)

使用方法，打开终端程序，执行：

```bash
# 1. Install XCode
$ sudo softwareupdate -i -a
$ xcode-select --install

# 2. Install
$ bash -c "$(curl -LsS https://raw.githubusercontent.com/coderzh/dotfiles/master/setup.sh)"
```

如果下载 githubusercontent.com 有问题，请先设置好代理。或者，先 git clone 下再执行：

```bash
$ cd ~
$ git clone https://github.com/coderzh/dotfiles
$ cd dotfile; sh setup.sh
```

执行后，会发生什么？

1. 创建 dotfiles 软链：.gitconfig .gitignore .vim .vimrc .zshrc
2. 设置各种 Mac OS 的系统设置：install/macos/osx.sh
3. 安装字体：Menlo for Powerline
4. 安装 Homebrew，以及各软件：install/macos/brew.sh
5. 安装设置 oh-my-zsh：install/oh-my-zsh.sh
6. 安装 npm 及相关的包：install/npm.sh
7. 安装 Pip 及相关的包：install/pip.sh
8. 安装 Vim 插件：install/vim.sh

![dotfiles](images/dotfiles.jpg)
