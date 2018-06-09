/**
 * Created by Administrator on 2017/4/1.
 */

$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var post_id = $(this).attr('data-post-id');
        var content = window.editor.$txt.html();
        var comment_id = $(".origin-comment-group").attr('data-comment-id');

        xtajax.post({
            'url': '/add_comment/',
            'data': {
                'post_id': post_id,
                'content': content,
                'comment_id': comment_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    xtalert.alertSuccessToast('恭喜！评论成功！');
                    setTimeout(function () {
                        window.location = '/post_detail/'+post_id+'/';
                    },500);
                }else{
                    xtalert.alertInfoToast(data['message']);
                }
            }
        })
    });
});
