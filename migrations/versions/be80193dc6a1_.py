"""empty message

Revision ID: be80193dc6a1
Revises: 
Create Date: 2021-03-11 15:14:27.090852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be80193dc6a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
