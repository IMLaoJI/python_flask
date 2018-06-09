# web服务器和应用服务器以及web应用框架：

### web服务器：
负责处理http请求，响应静态文件，常见的有Apache，Nginx以及微软的IIS.

### 应用服务器：
负责处理逻辑的服务器。比如php、python的代码，是不能直接通过nginx这种web服务器来处理的，只能通过应用服务器来处理，常见的应用服务器有uwsgi、tomcat等。

### web应用框架：
一般使用某种语言，封装了常用的web功能的框架就是web应用框架，flask、Django以及Java中的SSH(Structs2+Spring3+Hibernate3)框架都是web应用框架。