"""add created_at and last_updated columns

Revision ID: 10781f5837eb
Revises: 8f2c61295047
Create Date: 2020-12-28 17:23:53.134090

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '10781f5837eb'
down_revision = '8f2c61295047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('created_at', sa.DateTime, nullable=True, default=datetime.now))
    op.add_column('address', sa.Column('last_updated', sa.DateTime, nullable=True, default=datetime.now, onupdate=datetime.now))
    op.add_column('customer', sa.Column('created_at', sa.DateTime, nullable=True, default=datetime.now))
    op.add_column('customer', sa.Column('last_updated', sa.DateTime, nullable=True, default=datetime.now, onupdate=datetime.now))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'last_updated')
    op.drop_column('customer', 'created_at')
    op.drop_column('address', 'last_updated')
    op.drop_column('address', 'created_at')
    # ### end Alembic commands ###
