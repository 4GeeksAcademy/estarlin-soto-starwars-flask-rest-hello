"""empty message

Revision ID: b9c09766f411
Revises: 11361be8c9f5
Create Date: 2023-11-26 00:11:17.374218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9c09766f411'
down_revision = '11361be8c9f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites__people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('char_fav_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['char_fav_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites__planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_fav_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_fav_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('planet_fav_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('char_fav_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['char_fav_id'], ['people.id'], name='favorites_char_fav_id_fkey'),
    sa.ForeignKeyConstraint(['planet_fav_id'], ['planets.id'], name='favorites_planet_fav_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorites_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorites_pkey')
    )
    op.drop_table('favorites__planets')
    op.drop_table('favorites__people')
    # ### end Alembic commands ###
