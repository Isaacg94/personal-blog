from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from ..models import Comment,User
from .forms import CommentForm,UpdateProfile
from flask_login import login_required
from .. import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'GZRU | Home'
    # random_quotes = get_quotes
    return render_template('index.html', title=title)


@main.route('/post/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    post = get_post(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(post.id,title,comment)
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