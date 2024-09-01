"""Initial migration

Revision ID: 380391d8426f
Revises: 
Create Date: 2024-08-31 20:55:41.034970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '380391d8426f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('additional_info', sa.String(length=510), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_city_city'), 'city', ['city'], unique=True)
    op.create_index(op.f('ix_city_id'), 'city', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_city_id'), table_name='city')
    op.drop_index(op.f('ix_city_city'), table_name='city')
    op.drop_table('city')
    # ### end Alembic commands ###