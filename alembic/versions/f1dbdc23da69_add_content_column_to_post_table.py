"""add content column to post table

Revision ID: f1dbdc23da69
Revises: 4be725f29cf5
Create Date: 2026-06-09 10:28:02.287653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1dbdc23da69'
down_revision: Union[str, Sequence[str], None] = '4be725f29cf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
