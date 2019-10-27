from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    review = TextAreaField('Post comment', validators=[Required()])
    submit = SubmitField('Submit')