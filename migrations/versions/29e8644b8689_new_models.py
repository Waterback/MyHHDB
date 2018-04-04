"""new models

Revision ID: 29e8644b8689
Revises: c06afcd8ad77
Create Date: 2018-03-26 16:51:15.672000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29e8644b8689'
down_revision = 'c06afcd8ad77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('insurance_statement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('amount_repaid', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pkvinvoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient', sa.String(length=64), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('comment', sa.String(length=250), nullable=True),
    sa.Column('sent_to_pkv', sa.Boolean(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('paid_at', sa.DateTime(), nullable=True),
    sa.Column('repaid', sa.Boolean(), nullable=True),
    sa.Column('repaid_at', sa.DateTime(), nullable=True),
    sa.Column('state', sa.String(length=16), nullable=True),
    sa.Column('insurance_statement', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['insurance_statement'], ['pkvinvoice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pkvinvoice_patient'), 'pkvinvoice', ['patient'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pkvinvoice_patient'), table_name='pkvinvoice')
    op.drop_table('pkvinvoice')
    op.drop_table('insurance_statement')
    # ### end Alembic commands ###
