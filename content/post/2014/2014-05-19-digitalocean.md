---
categories:
- 技术文章
date: '2014-05-19'
description: ''
tags: []
title: DigitalOcean上使用Tornado+MongoDB+Nginx+Supervisor+DnsPod快速搭建个人博客
url: /2014/05/19/digitalocean/

---


### DigitalOcean
之前买了个便宜的VPS并且在上面搭建了我自己写的博客程序，后来VPS里运行MongoDB经常自己挂掉就索性没理了。直到现在VPS已经过期，服务器被强制关掉了。周末在家索性想着把这个博客程序重新搭建起来。

<!--more-->

选择Linode还是云主机（阿里云等等）？阿里云貌似有些贵，而且还有一堆备案的流程。Linode最近推出SSD服务，20刀/月的价格，加量不加价，很是吸引人。但无奈还是花的有些心疼。忽然另外一个VPS服务[DigitalOcean](https://www.digitalocean.com/?refcode=e131e2bba197)(链接含refcode喔)被我无意发现。DigitalOcean是一家IaaS服务提供商，其特色就是提供快速的固态硬盘服务器，该公司宣称可在55秒之内搭建好一台云服务器，所有的服务器均拥有1G的网络接口，每月基础套餐为1TB，最低套餐费用仅为5美元/月。

![DigitalOcean](http://images.cnitblog.com/blog/16913/201405/190032003752557.jpg)

每个月20刀的配置和Linode的20刀的配置几乎一样。但是DigitalOcean提供了最低5美元/月的配置，而且如果使用优惠码注册，还能免费送10美元。相当于免费使用2个月。于是我选择了5美元的配置，Google了一把优惠码，并且非常顺利的找到了能用的。Google搜索：digitalocean coupon。我是在这里找到： http://www.retailmenot.com/view/digitalocean.com

注册，填入优惠码，选择5$的主机类型，主机位置我选了旧金山（美国西部，据说比其他的稳定），操作系统选择了Ubuntu 14.04 x64。一切都非常顺利，正如他们的广告所说的，55秒内，一台热乎乎的VPS送到了我的手上。

有兴趣的同学可以用我的推荐链接注册哦，我也能得到一些好处。注册链接：[DigitalOcean](https://www.digitalocean.com/?refcode=e131e2bba197)
用到哪天不想用了，DigitalOcean还提供了生成一个镜像(Image)的功能，然后你取消掉VPS服务器(Droplets)，之后将不收取费用。哪天忽然又想用了再开通它，用之前的镜像一还原，马上就恢复了之前的环境，很是方便。

### VPS安装必要的软件

```
sudo apt-get install git
sudo apt-get install python-pip
sudo apt-get install nginx
sudo apt-get install supervisor
sudo pip install tornado
sudo pip install pymongo
sudo pip install beautifulsoup4
```

（我安装了beautifulsoup是因为我做了个工具把博客园的博客导入过来。）
mongodb 安装：http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

### 博客程序
之前我用python+tornado+pymongo写了一套博客程序，只是给我自己使用，所以我放在了私有仓库[bitbucket](http://bitbucket.org)上。
网站程序一般放在/var/www目录里。所以我用git clone把我的代码放到了/var/www/coderzh

```
sudo mkdir /var/www
cd /var/www
git clone https://xxxxx.xxxx.xxx
```

### MongoDB
由于我的程序没有使用MongoDB默认的端口27017，所以我需要修改端口的设置。找到MongoDB的配置文件，修改port字段：

```
vim /etc/mongodb.conf
#修改port=27017部分 
```

停止和重启mongodb：

```
sudo service mongodb stop
sudo service mongodb start
```

### 运行博客程序
博客程序运行需要的环境已经基本配置好，这时运行博客程序看是否能正常起来：

```
sudo python /var/www/coderzh/main.py --port 8001
```

打开浏览器试试能不能访问: ```http://服务器IP:8001```   OK，太棒了，一起正常。

### Supervisor
停掉刚才的main.py，这时候要上一个好东西。它就是Supervisor，它是一个进程监控守护程序。它负责开机时自动启动你配置好的程序，并且在你的程序莫名其妙挂掉时，Supervisor会自动去重启他们。可以说，它是网站稳定运行的后勤保障啊。

新建一个Supervisor配置文件，放到/ect/supervisor/conf.d目录下，因为/etc/supervisor/supervisord.conf里配置了自动读取conf.d目录下的文件：

```
vim /ect/supervisor/conf.d/coderzh.conf
```

编辑coderzh.conf

```
[program:coderzh]
command=python /var/www/coderzh/main.py --port=8001
directory=/var/www/coderzh
autorestart=true
redirect_stderr=true
```

重载配置，重启Supervisior：

```
supervisorctl reload 
supervisorctl start all
```

再次访问: ```http://服务器IP:8001```   试试，嗯，一起正常。Supervisor工作了。

### Nginx
接下来上Nginx，它是一个HTTP和反向代理服务器。最终网站的访问经过域名解析到服务器后，都要通过Nginx将访问请求转到main.py中处理。理解Nginx的配置文件很重要，好吧，说实话，我当初摸Nginx，Apache之类的东西时都是一头雾水的。Nginx的主要配置文件路径在：/etc/nginx/nginx.conf

为了让Nginx支持多域名，多Web服务。我修改/etc/nginx/nginx.conf 内容如下：

```
user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
    worker_connections 1024;
    use epoll;
}

http {
    types_hash_max_size 2048;
    server_names_hash_bucket_size 64;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;
 
    access_log /var/log/nginx/access.log;
 
    keepalive_timeout 65;
    proxy_read_timeout 200;
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    gzip on;
    gzip_min_length 1000;
    gzip_proxied any;
    gzip_types text/plain application/x-javascript text/css application/xml; 

    include /etc/nginx/conf.d/*;
}
```

注意最后一行：include /etc/nginx/conf.d/*，所以在conf.d目录里，可以为每个网站都配置一个.conf文件。我为博客程序生产的配置：vim /etc/nginx/conf.d/coderzh.conf

```
upstream coderzh {
    server 127.0.0.1:8001;
}

server {
    listen 80;
    server_name coderzh.com www.coderzh.com;

    location = /favicon.ico {
        rewrite (.*) /static/favicon.ico;
    }
    location = /robots.txt {
        rewrite (.*) /static/robots.txt;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://coderzh;
    }
}
```

重新启动nginx

```
service nginx restart
```

这时已经可以用80端口访问了。

### DnsPod
接下来就是通过DnsPod将域名解析到这台VPS服务器。应该不是什么问题，有问题可以查看DnsPod帮助。

### 部署完成
执行导入工具，将博客园的博客导入进来。访问：[http://www.coderzh.com](http://www.coderzh.com)。HOHO，大功告成。

