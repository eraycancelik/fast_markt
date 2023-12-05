"""revision

Revision ID: 1368fe7c1470
Revises: 
Create Date: 2023-12-04 22:48:18.231798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1368fe7c1470'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
dir


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
