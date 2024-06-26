"""Init

Revision ID: 01ee99757d3e
Revises: edd14ac624df
Create Date: 2024-06-28 21:26:35.184763

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "01ee99757d3e"
down_revision: Union[str, None] = "edd14ac624df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("email", sa.String(length=250), nullable=False),
        sa.Column("password", sa.String(length=250), nullable=False),
        sa.Column("access_token", sa.String(length=250), nullable=True),
        sa.Column("refresh_token", sa.String(length=250), nullable=True),
        sa.Column(
            "role", sa.Enum("admin", "moderator", "user", name="role"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "verification",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=250), nullable=False),
        sa.Column("verification_code", sa.Integer(), nullable=True),
        sa.Column("email_confirmation", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("verification")
    op.drop_table("users")
    # ### end Alembic commands ###
