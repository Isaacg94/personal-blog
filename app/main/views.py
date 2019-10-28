from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes
from ..models import Comment,User
from .forms import CommentForm
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

