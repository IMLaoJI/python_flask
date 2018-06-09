# response笔记：

### 视图函数中可以返回哪些值：
1. 可以返回字符串：返回的字符串其实底层将这个字符串包装成了一个`Response`对象。
2. 可以返回元组：元组的形式是(响应体,状态码,头部信息)，也不一定三个都要写，写两个也是可以的。返回的元组，其实在底层也是包装成了一个`Response`对象。
3. 可以返回`Response`及其子类。


### 实现一个自定义的`Response`对象：
1. 继承自`Response`类。
2. 实现方法`force_type(cls,rv,environ=None)`。
3. 指定`app.response_class`为你自定义的`Response`对象。
4. 如果视图函数返回的数据，不是字符串，也不是元组，也不是Response对象，那么就会将返回值传给`force_type`，然后再将`force_type`的返回值返回给前端。