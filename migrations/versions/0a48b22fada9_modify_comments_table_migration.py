"""modify comments table Migration

Revision ID: 0a48b22fada9
Revises: 8eb8a629f46e
Create Date: 2019-10-28 20:39:15.260269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a48b22fada9'
down_revision = '8eb8a629f46e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment_by', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
