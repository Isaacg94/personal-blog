from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from ..models import Comment,User,Post
from .forms import CommentForm,UpdateProfile,PostForm
from flask_login import login_required,current_user
import datetime
from .. import db,photos

# Views
@main.route('/')
def index():
    posts = Post.query.all()
    

    title = 'GZRU | Home'
    # random_quotes = get_quotes
    return render_template('index.html', title=title,posts=posts,)

@main.route('/new_post/', methods = ['GET','POST'])
@login_required
def new_post():

    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_content = post_form.blogpost.data

        new_post = Post(post_title = post_title,post_content = post_content, user_id = current_user.id)
        new_post.save_post()
        return redirect(url_for('main.index'))

    return render_template('new_post.html',post_form=post_form)

@main.route('/post/<int:id>', methods = ['GET','POST'])
def single_post(id):
    post = Post.query.get(id)
    return render_template('single_post.html',title=post.post_title, post=post)

@main.route('/post/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    post = get_post(id)

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(post.id,comment)
        new_comment.save_comment()
        return redirect(url_for('post',id = post.id ))

    title = f'{post.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form, post=post)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))