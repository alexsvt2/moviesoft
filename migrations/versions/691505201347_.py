"""empty message

Revision ID: 691505201347
Revises: 
Create Date: 2018-06-21 11:22:39.546592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '691505201347'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('testdata', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'testdata')
    # ### end Alembic commands ###
