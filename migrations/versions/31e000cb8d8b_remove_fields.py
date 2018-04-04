"""remove fields

Revision ID: 31e000cb8d8b
Revises: 1bd6b81cdaed
Create Date: 2018-04-03 11:46:55.087000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e000cb8d8b'
down_revision = '1bd6b81cdaed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pkvinvoice_patient', table_name='pkvinvoice')
    op.drop_column('pkvinvoice', 'patient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pkvinvoice', sa.Column('patient', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
    op.create_index('ix_pkvinvoice_patient', 'pkvinvoice', ['patient'], unique=False)
    # ### end Alembic commands ###