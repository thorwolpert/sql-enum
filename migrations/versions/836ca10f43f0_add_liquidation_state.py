"""add_liquidation_state

Revision ID: 836ca10f43f0
Revises: 379c785d2a26
Create Date: 2021-12-05 00:41:51.248345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836ca10f43f0'
down_revision = '379c785d2a26'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TYPE state ADD VALUE 'LIQUIDATION'")


def downgrade():
    op.execute("ALTER TYPE state RENAME TO state_previous")
    op.execute("CREATE TYPE state AS ENUM('ACTIVE', 'HISTORICAL')")
    op.execute((
        "ALTER TABLE businesses ALTER COLUMN state TYPE state USING "
        "state::text::state"
    ))
    op.execute("DROP TYPE state_previous")
