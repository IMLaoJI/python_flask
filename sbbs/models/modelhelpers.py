#coding: utf8

# 这个文件专门用来给模型添加方法的

from models.commonmodels import PostModel,HighlightPostModel,CommentModel,PostStarModel,BoardModel
from exts import db
import constants

class PostModelHelper(object):

    class PostSortType(object):
        CREATE_TIME = 1
        HIGHLIGH_TIME = 2
        COMMENT_COUNT = 3
        STAR_COUNT = 4

    @classmethod
    def post_list(cls,page,sort_type,board_id):
        start = (page - 1) * constants.PAGE_NUM
        end = start + constants.PAGE_NUM

        # sort_type：1 - 代表是按时间排序
        # sort_type：2 - 代表是按加精排序
        # sort_type：3 - 代表是按评论量排序
        # sort_type：4 - 代表是按点赞量排序

        if sort_type == cls.PostSortType.CREATE_TIME:
            posts = PostModel.query.order_by(PostModel.create_time.desc())
        elif sort_type == cls.PostSortType.HIGHLIGH_TIME:
            posts = db.session.query(PostModel).outerjoin(HighlightPostModel).filter(
                PostModel.is_removed == False).order_by(HighlightPostModel.create_time.desc(),
                                                        PostModel.create_time.desc())
        elif sort_type == cls.PostSortType.COMMENT_COUNT:
            posts = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(
                db.func.count(CommentModel.id).desc(), PostModel.create_time.desc())
        elif sort_type == cls.PostSortType.STAR_COUNT:
            posts = db.session.query(PostModel).outerjoin(PostStarModel).group_by(PostModel.id).order_by(
                db.func.count(PostStarModel.id).desc(), PostModel.create_time.desc())
        else:
            posts = PostModel.query.order_by(PostModel.create_time.desc())

        posts = posts.filter(PostModel.is_removed == False)

        if board_id:
            posts = posts.filter(PostModel.board_id == board_id)

        total_post_count = posts.count()
        total_page = total_post_count // constants.PAGE_NUM
        if total_post_count % constants.PAGE_NUM > 0:
            total_page += 1

        pages = []
        tmp_page = page - 1
        while tmp_page >= 1:
            if tmp_page % 5 == 0:
                break
            pages.append(tmp_page)
            tmp_page -= 1

        tmp_page = page
        while tmp_page <= total_page:
            if tmp_page % 5 == 0:
                pages.append(tmp_page)
                break
            else:
                pages.append(tmp_page)
                tmp_page += 1

        pages.sort()

        context = {
            'posts': posts.slice(start, end),
            'boards': BoardModel.query.all(),
            'pages': pages,
            'c_page': page,
            't_page': total_page,
            'c_sort': sort_type,
            'c_board': board_id
        }
        return context