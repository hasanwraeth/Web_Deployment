"""added breed column

Revision ID: ca23259e7dcc
Revises: 
Create Date: 2024-01-17 16:48:12.527722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca23259e7dcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pup', schema=None) as batch_op:
        batch_op.add_column(sa.Column('breed', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pup', schema=None) as batch_op:
        batch_op.drop_column('breed')

    # ### end Alembic commands ###
