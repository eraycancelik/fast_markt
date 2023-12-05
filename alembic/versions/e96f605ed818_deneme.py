"""deneme

Revision ID: e96f605ed818
Revises: 1368fe7c1470
Create Date: 2023-12-04 23:24:58.636547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e96f605ed818'
down_revision: Union[str, None] = '1368fe7c1470'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
