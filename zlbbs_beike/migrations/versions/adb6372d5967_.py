"""empty message

Revision ID: adb6372d5967
Revises: 9584f5bd5b71
Create Date: 2018-01-10 11:49:27.373628

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'adb6372d5967'
down_revision = '9584f5bd5b71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'qq')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('qq', mysql.VARCHAR(length=20), nullable=True))
    # ### end Alembic commands ###