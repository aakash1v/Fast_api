"""add foreign-key to post table

Revision ID: 1278cdaa7e56
Revises: 02d6bf08327c
Create Date: 2024-03-09 23:53:22.258965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1278cdaa7e56'
down_revision: Union[str, None] = '02d6bf08327c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
            local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_column("posts","owner_id")
    op.drop_constraint("post_users_fk",table_name="posts")
    pass
