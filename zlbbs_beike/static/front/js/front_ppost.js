/**
 * Created by hynev on 2017/12/30.
 */

$(function () {
    var ue = UE.getEditor("editor",{
        "serverUrl": '/ueditor/upload/'
    });

    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $("input[name='title']");
        var boardSelect = $("select[name='board']");

        var title = titleInput.val();
        var content = ue.getContent();
        var board_id = boardSelect.val();

        zlajax.post({
            'url': '/ppost/',
            'data': {
                'title': title,
                'content': content,
                'board_id': board_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    zlalert.alertConfirm({
                       'msg': '恭喜！帖子发表成功！',
                        'confirmButtonText': '再发一篇',
                        'cancelButtonText': '回到首页',
                        'cancelCallback': function () {
                            window.location = '/';
                        },
                        'confirmCallback': function () {
                            titleInput.val("");
                            ue.setContent("");
                        }
                    });
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});