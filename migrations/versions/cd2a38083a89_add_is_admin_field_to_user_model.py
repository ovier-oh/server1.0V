"""Add is_admin field to USer model

Revision ID: cd2a38083a89
Revises: aaaef4c29849
Create Date: 2024-10-19 12:30:20.086663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd2a38083a89'
down_revision = 'aaaef4c29849'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
