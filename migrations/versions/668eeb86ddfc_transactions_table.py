"""transactions table

Revision ID: 668eeb86ddfc
Revises: 8516dba1466e
Create Date: 2018-05-03 19:58:42.005346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '668eeb86ddfc'
down_revision = '8516dba1466e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=32), nullable=True),
    sa.Column('sub_category', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('tag', sa.String(length=32), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('insert_note', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_timestamp'), 'transaction', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_timestamp'), table_name='transaction')
    op.drop_table('transaction')
    # ### end Alembic commands ###
