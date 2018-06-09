/**
 * Created by hynev on 2017/10/7.
 */

$(function () {
    $('.delete-role-btn').click(function (event) {
        event.preventDefault();
        var role_id = $(this).attr('data-role-id');
        xtalert.alertConfirm({
            msg: '您确定要删除这个分组吗？',
            confirmCallback: function () {
                // 发送ajax
                xtajax.post({
                    url: '/delete_role/',
                    data:{
                        'role_id': role_id
                    },
                    success: function (data) {
                        console.log(data);
                        if(data['code'] == 200){
                            setTimeout(function () {
                                xtalert.alertSuccessToast('恭喜！CMS组删除成功！');
                            },200);
                            setTimeout(function () {
                                // 重新加载这个页面
                                window.location.reload();
                            },1400);
                        }else{
                            setTimeout(function () {
                                xtalert.alertInfoToast(data['message']);
                            },200);
                        }
                    }
                })
            }
        });
    });
});