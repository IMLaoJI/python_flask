"""empty message

Revision ID: 6a8915ffd845
Revises: aab1d0db9122
Create Date: 2018-01-04 14:04:06.366580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a8915ffd845'
down_revision = 'aab1d0db9122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'highlight_post', ['post_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'highlight_post', type_='unique')
    # ### end Alembic commands ###
