/**
 * Created by hynev on 2017/11/10.
 */

// jquery
// XMLHTTTPRequest

// 整个文档都加载完毕后才会执行这个函数
$(function () {
    $('#submit').click(function (event) {
        // 阻止默认的提交表单的行为
        event.preventDefault();
        var email = $('input[name=email]').val();
        var password = $('input[name=password]').val();
        
        zlajax.post({
            'url': '/login/',
            'data': {
                'email': email,
                'password': password
            },
            'success': function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
});