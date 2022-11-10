"""empty message

Revision ID: ff74defebafd
Revises: ea07bc44f468
Create Date: 2022-11-10 00:57:44.707654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff74defebafd'
down_revision = 'ea07bc44f468'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=256),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
    op.alter_column('items', 'price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)
    # ### end Alembic commands ###
