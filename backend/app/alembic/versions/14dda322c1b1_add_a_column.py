"""Add a column

Revision ID: 14dda322c1b1
Revises: 3cf5582ade47
Create Date: 2019-04-27 16:44:19.866679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14dda322c1b1'
down_revision = '3cf5582ade47'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('attempted_login_count', sa.Integer))


def downgrade():
    op.drop_column('users', 'attempted_login_count')
