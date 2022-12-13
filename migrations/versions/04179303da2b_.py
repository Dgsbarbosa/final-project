"""empty message

Revision ID: 04179303da2b
Revises: d1121b2701f0
Create Date: 2022-12-13 13:05:53.843532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04179303da2b'
down_revision = 'd1121b2701f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('bairro', sa.String(), nullable=True),
    sa.Column('cep', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('phone2', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_column('users', 'state')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'cep')
    op.drop_column('users', 'bairro')
    op.drop_column('users', 'phone2')
    op.drop_column('users', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('phone2', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('bairro', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('cep', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('phone', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('state', sa.VARCHAR(), nullable=True))
    op.drop_table('clients')
    # ### end Alembic commands ###
