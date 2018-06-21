"""empty message

Revision ID: 0c9d65859bfc
Revises: 691505201347
Create Date: 2018-06-21 11:38:14.746706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c9d65859bfc'
down_revision = '691505201347'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'testdata')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('testdata', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
