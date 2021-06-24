"""Added users and items table

Revision ID: a90b80856b94
Revises:
Create Date: 2021-06-20 22:25:19.156985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a90b80856b94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(length=50), unique=True),
        sa.Column("hashed_password", sa.String(length=100)),
        sa.Column("is_active", sa.Boolean, default=False),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=True)
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(length=40)),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("owner_id", sa.Integer),
        sa.ForeignKeyConstraint(["owner_id"], ["users.id"]),
    )
    op.create_index(op.f("ix_items_id"), "items", ["id"], unique=True)
    op.create_index(op.f("ix_items_title"), "items", ["title"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_items_id"), table_name="items")
    op.drop_index(op.f("ix_items_title"), table_name="items")
    op.drop_table("items")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
