"""mean migration

Revision ID: 134aa55ead92
Revises: 29e8644b8689
Create Date: 2018-03-27 17:13:38.992000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134aa55ead92'
down_revision = '29e8644b8689'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pkvinvoice', sa.Column('statement_id', sa.Integer(), nullable=True))
    op.alter_column('pkvinvoice', 'patient',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.drop_constraint(u'pkvinvoice_insurance_statement_fkey', 'pkvinvoice', type_='foreignkey')
    op.create_foreign_key(None, 'pkvinvoice', 'insurance_statement', ['statement_id'], ['id'])
    op.drop_column('pkvinvoice', 'insurance_statement')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pkvinvoice', sa.Column('insurance_statement', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pkvinvoice', type_='foreignkey')
    op.create_foreign_key(u'pkvinvoice_insurance_statement_fkey', 'pkvinvoice', 'pkvinvoice', ['insurance_statement'], ['id'])
    op.alter_column('pkvinvoice', 'patient',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_column('pkvinvoice', 'statement_id')
    # ### end Alembic commands ###
