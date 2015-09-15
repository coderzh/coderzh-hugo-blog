---
categories:
- 技术文章
date: '2010-01-11'
title: Python查询Google PageRank
url: /2010/01/11/python-googlerank/

---

  
[Corey Goldberg](http://coreygoldberg.blogspot.com/)为我们实现的Python脚本，用于查询Google PageRank。[Corey Goldberg](http://coreygoldberg.blogspot.com/)还有很多很好玩的开源项目，比如开源的性能测试工具[Pylot](http://www.pylot.org/)等等。下面是他的主页：
  
[http://www.goldb.org/](http://www.goldb.org/ "http://www.goldb.org/")

查询Google PageRank的Python代码：
  
[pagerank.py](http://code.google.com/p/corey-projects/source/browse/trunk/python2/pagerank.py)

使用方法：
  <div class="cnblogs_code"><div><span style="color: #008000;">#</span><span style="color: #008000;">!/usr/bin/env&nbsp;python</span><span style="color: #008000;">
</span><span style="color: #000000;">
</span><span style="color: #0000ff;">import</span><span style="color: #000000;">&nbsp;pagerank
<br />
rank&nbsp;</span><span style="color: #000000;">=</span><span style="color: #000000;">&nbsp;pagerank.get_pagerank(</span><span style="color: #800000;">'</span><span style="color: #800000;">http://www.google.com</span><span style="color: #800000;">'</span><span style="color: #000000;">)
</span><span style="color: #0000ff;">print</span><span style="color: #000000;">&nbsp;rank</span></div></div>

<pre></pre>

**[温馨提示]：该文章由原博客园导入而来，如排版效果不佳，请移步：[http://www.cnblogs.com/coderzh/archive/2010/01/11/python-googlerank.html](http://www.cnblogs.com/coderzh/archive/2010/01/11/python-googlerank.html)**