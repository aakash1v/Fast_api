"""create post table

Revision ID: c6568867e0b7
Revises: 
Create Date: 2024-03-09 23:27:20.518959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6568867e0b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key = True),sa.Column('title',sa.String(40),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
