/**
 * Created by Administrator on 2017/3/21.
 */

$(function () {
   $('#submit').click(function (event) {
       event.preventDefault();

       var checkedInputs = $(':checkbox:checked');

       var roles = [];
       checkedInputs.each(function () {
          var role_id = $(this).val();
           roles.push(role_id);
       });
        var user_id = $(this).attr('data-user-id');
        xtajax.post({
            'url': '/edit_cmsuser/',
            'data':{
                'user_id': user_id,
                'roles': roles
            },
            'success': function (data) {
                if(data['code'] == 200){
                    xtalert.alertSuccessToast('恭喜！CMS用户信息修改成功！');
                }else{
                    xtalert.alertInfoToast(data['message']);
                }
            }
        })
   });
});

$(function () {
   $('#black-list-btn').click(function (event) {
       event.preventDefault();
        var user_id = $(this).attr('data-user-id');
        var is_active = parseInt($(this).attr('data-is-active'));

        var is_black = is_active;

        xtajax.post({
            'url': '/black_list/',
            'data':{
                'user_id': user_id,
                'is_black': is_black
            },
            'success': function (data) {
                if(data['code'] == 200){
                    var msg = '';
                    if(is_black){
                        msg = '恭喜！已经将该用户拉入黑名单！'
                    }else{
                        msg = '恭喜！已经将该用户移出黑名单！'
                    }
                    xtalert.alertSuccessToast(msg);
                    setTimeout(function () {
                        window.location.reload();
                    },500);
                }else{
                    xtalert.alertInfoToast(data['message']);
                }
            }
        })
   })
});
