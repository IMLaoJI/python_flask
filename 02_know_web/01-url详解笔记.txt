# url详解：
URL是Uniform Resource Locator的简写，统一资源定位符。

一个URL由以下几部分组成：
```python
scheme://host:port/path/?query-string=xxx#anchor
```

* scheme：代表的是访问的协议，一般为http或者https以及ftp等。
* host：主机名，域名，比如www.baidu.com。
* port：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
* path：查找路径。比如：www.jianshu.com/trending/now，后面的trending/now就是path。
* query-string：查询字符串，比如：www.baidu.com/s?wd=python，后面的wd=python就是查询字符串。
* anchor：锚点，后台一般不用管，前端用来做页面定位的。比如：https://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923?fr=aladdin#7