"""empty message

Revision ID: ef52e75a2aec
Revises: c3a8a01b1af0
Create Date: 2023-08-13 14:10:54.326987

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef52e75a2aec'
down_revision = 'c3a8a01b1af0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('uw_course', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('uw_course', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
