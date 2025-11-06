"""second update

Revision ID: 4e6d687bb4bd
Revises: cecfd4b10ae7
Create Date: 2025-11-06 02:24:57.376647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e6d687bb4bd'
down_revision: Union[str, Sequence[str], None] = 'cecfd4b10ae7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
