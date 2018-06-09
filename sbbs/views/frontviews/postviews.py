#coding: utf8

from flask import Blueprint
import flask
import constants
from models.frontmodels import FrontUser
from utils import xtjson
from models.commonmodels import BoardModel,PostModel,CommentModel,PostStarModel,HighlightPostModel
from decorators.frontdecorators import login_required
from forms.frontforms import AddPostForm,AddCommentForm,StarPostForm
from exts import db
import qiniu
from sqlalchemy import func
from models.modelhelpers import PostModelHelper


bp = Blueprint('post',__name__)

@bp.route('/')
def index():
    return post_list(1,1,0)


@bp.route('/list/<int:page>/<int:sort_type>/<int:board_id>/')
def post_list(page,sort_type,board_id):
    context = PostModelHelper.post_list(page,sort_type,board_id)
    return flask.render_template('front/front_index.html',**context)


@bp.route('/add_post/',methods=['GET','POST'])
@login_required
def add_post():
    if flask.request.method == 'GET':
        boards = BoardModel.query.all()
        return flask.render_template('front/front_addpost.html',boards=boards)
    else:
        form = AddPostForm(flask.request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            post_model = PostModel(title=title,content=content)
            # 直接通过get的方式获取数据，如果id不存在一个board_id的值，就会抛出异常
            board_model = BoardModel.query.filter_by(id=board_id).first()
            if not board_model:
                return xtjson.json_params_error(message=u'没有该板块!')
            post_model.board = board_model
            post_model.author = flask.g.front_user
            db.session.add(post_model)
            db.session.commit()
            return xtjson.json_result()
        else:
            return xtjson.json_params_error(message=form.get_error())

@bp.route('/post_detail/<int:post_id>/')
def post_detail(post_id):
    # 路径的形式：/post_detail/1/ 为了SEO的优化
    # 查询字符串的形式：/post_detail/?post_id=1/
    post_model = PostModel.query.filter(PostModel.is_removed==False,PostModel.id==post_id).first()
    if not post_model:
        flask.abort(404)
    post_model.read_count +=1
    db.session.commit()
    # 获取这篇帖子的所有赞的作者的id，方便模版中判断
    star_author_ids = [star_model.author.id for star_model in post_model.stars]
    context = {
        'post': post_model,
        'star_author_ids': star_author_ids
    }
    return flask.render_template('front/front_postdetail.html',**context)

@bp.route('/add_comment/',methods=['POST','GET'])
@login_required
def add_comment():
    if flask.request.method == 'GET':
        post_id = flask.request.args.get('post_id',type=int)
        comment_id = flask.request.args.get('comment_id',type=int)
        context = {
            'post': PostModel.query.get(post_id)
        }
        if comment_id:
            context['origin_comment'] = CommentModel.query.get(comment_id)
        return flask.render_template('front/front_addcomment.html',**context)
    else:
        form = AddCommentForm(flask.request.form)
        if form.validate():
            post_id = form.post_id.data
            content = form.content.data
            comment_id = form.comment_id.data

            comment_model = CommentModel(content=content)

            post_model = PostModel.query.get(post_id)
            comment_model.post = post_model
            comment_model.author = flask.g.front_user
            if comment_id:
                origin_comment = CommentModel.query.get(comment_id)
                comment_model.origin_comment = origin_comment

            db.session.add(comment_model)
            db.session.commit()
            return xtjson.json_result()
        else:
            return xtjson.json_params_error(message=form.get_error())

@bp.route('/star_post/',methods=['POST'])
@login_required
def star_post():
    form = StarPostForm(flask.request.form)
    if form.validate():
        post_id = form.post_id.data
        is_star = form.is_star.data

        post_model = PostModel.query.get(post_id)
        star_model = PostStarModel.query.filter_by(author_id=flask.g.front_user.id, post_id=post_id).first()
        if is_star:
            # 要从数据库中查找一下，当前这个点赞是否存在，如果不存在，就添加，否则就提示已经点赞了
            if star_model:
                return xtjson.json_params_error(message=u'您已经给这篇帖子点赞了，无需再点！')
            star_model = PostStarModel()
            star_model.author = flask.g.front_user
            star_model.post = post_model
            db.session.add(star_model)
            db.session.commit()
            return xtjson.json_result()
        else:
            if star_model:
                db.session.delete(star_model)
                db.session.commit()
                return xtjson.json_result()
            else:
                return xtjson.json_params_error(message=u'你尚未对该帖子进行点赞！')
    else:
        return xtjson.json_params_error(message=form.get_error())


@bp.route('/qiniu_token/')
def qiniu_token():
    # 授权
    q = qiniu.Auth(constants.QINIU_ACCESS_KEY, constants.QINIU_SECRET_KEY)

    # 选择七牛的云空间
    bucket_name = 'hyvideo'

    # 生成token
    token = q.upload_token(bucket_name)

    return flask.jsonify({'uptoken':token})

@bp.route('/test/')
def test():
    # author = FrontUser.query.first()
    # board = BoardModel.query.first()
    # for x in xrange(0,100):
    #     title = '帖子标题：%s' % x
    #     content = '帖子内容：%s' % x
    #     post_model = PostModel(title=title,content=content)
    #     post_model.author = author
    #     post_model.board = board
    #     db.session.add(post_model)
    # db.session.commit()
    # return 'success'
    comment_model = CommentModel(content='xxx')
    comment_model.post = PostModel.query.first()
    comment_model.author = FrontUser.query.first()
    comment_model.origin_comment = CommentModel.query.first()
    db.session.add(comment_model)
    db.session.commit()
    return 'success'
