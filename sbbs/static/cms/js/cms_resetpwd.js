/**
 * Created by Administrator on 2017/3/15.
 */

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var oldpwdInput = $('input[name=oldpwd]');
        var newpwdInput = $('input[name=newpwd]');
        var newpwdRepeatInput = $('input[name=newpwd_repeat]');

        var oldpwd = oldpwdInput.val();
        var newpwd = newpwdInput.val();
        var newpwd_repeat = newpwdRepeatInput.val();

        xtajax.post({
           'url': '/resetpwd/',
            'data': {
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd_repeat': newpwd_repeat
            },
            'success': function (data) {
                if(data['code'] == 200){
                    oldpwdInput.val('');
                    newpwdInput.val('');
                    newpwdRepeatInput.val('');
                    xtalert.alertSuccessToast('恭喜您！密码修改成功！');
                }else{
                    xtalert.alertInfoToast(message);
                }
            },
            'fail': function (error) {
                // console.log(error);
                xtalert.alertNetworkError();
            }
        });
    });
});
