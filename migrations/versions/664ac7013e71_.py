"""empty message

Revision ID: 664ac7013e71
Revises: e0ae4b80fb0a
Create Date: 2017-10-27 20:29:58.347579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664ac7013e71'
down_revision = 'e0ae4b80fb0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('answer_timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('answer_creator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer_creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    # ### end Alembic commands ###
