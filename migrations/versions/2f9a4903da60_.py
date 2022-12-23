"""empty message

Revision ID: 2f9a4903da60
Revises: 93f1a9ac07ef
Create Date: 2022-12-22 21:08:15.666811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9a4903da60'
down_revision = '93f1a9ac07ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orcaments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', app.models.tables.MyDateTime(), nullable=True),
    sa.Column('client', sa.String(), nullable=True),
    sa.Column('pedido', sa.String(), nullable=True),
    sa.Column('valor', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('orcaments')
    # ### end Alembic commands ###
