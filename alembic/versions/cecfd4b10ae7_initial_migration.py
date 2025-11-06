"""initial migration

Revision ID: cecfd4b10ae7
Revises: 40b41d46fa42
Create Date: 2025-11-06 02:24:07.605380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cecfd4b10ae7'
down_revision: Union[str, Sequence[str], None] = '40b41d46fa42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
