"""commit

Revision ID: 509f82ad9d80
Revises: e96f605ed818
Create Date: 2023-12-05 17:15:46.825365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '509f82ad9d80'
down_revision: Union[str, None] = 'e96f605ed818'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
