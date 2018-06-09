# 自定义URL转换器：

# 自定义URL转换器

### 自定义URL转换器的方式：
1. 实现一个类，继承自`BaseConverter`。
2. 在自定义的类中，重写`regex`，也就是这个变量的正则表达式。
3. 将自定义的类，映射到`app.url_map.converters`上。比如：
    ```python
    app.url_map.converters['tel'] = TelephoneConverter
    ```

### `to_python`的作用：
这个方法的返回值，将会传递到view函数中作为参数。

### `to_url`的作用：
这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。