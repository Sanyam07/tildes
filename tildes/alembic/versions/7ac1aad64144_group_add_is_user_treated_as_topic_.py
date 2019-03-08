"""Group: add is_user_treated_as_topic_source

Revision ID: 7ac1aad64144
Revises: 61f43e57679a
Create Date: 2019-03-08 23:02:33.848382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7ac1aad64144"
down_revision = "61f43e57679a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "groups",
        sa.Column(
            "is_user_treated_as_topic_source",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("groups", "is_user_treated_as_topic_source")
    # ### end Alembic commands ###
