"""add new columns to users table

Revision ID: 38afc1fc884c
Revises: 52cdef52f382
Create Date: 2019-10-28 12:16:51.352366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38afc1fc884c'
down_revision = '52cdef52f382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###