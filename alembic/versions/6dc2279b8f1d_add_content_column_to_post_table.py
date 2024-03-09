"""add content column to post table;


Revision ID: 6dc2279b8f1d
Revises: c6568867e0b7
Create Date: 2024-03-09 23:38:54.335118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dc2279b8f1d'
down_revision: Union[str, None] = 'c6568867e0b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(60),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
