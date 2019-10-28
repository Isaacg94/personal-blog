from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('Post comment', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):

    title = StringField('Post Title',validators=[Required()])
    blogpost = TextAreaField('Post Content', validators=[Required()])
    submit = SubmitField('Submit')