"""Initial migration to add password_hash column to User model

Revision ID: 8e457f63fc83
Revises: 
Create Date: 2024-08-20 10:37:30.118453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e457f63fc83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('bookID', sa.String(length=250), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('authors', sa.String(length=250), nullable=True),
    sa.Column('average_rating', sa.String(length=250), nullable=True),
    sa.Column('isbn', sa.String(length=250), nullable=True),
    sa.Column('isbn13', sa.String(length=250), nullable=True),
    sa.Column('language_code', sa.String(length=250), nullable=True),
    sa.Column('num_pages', sa.Integer(), nullable=True),
    sa.Column('ratings_count', sa.Integer(), nullable=True),
    sa.Column('text_reviews_count', sa.Integer(), nullable=True),
    sa.Column('publication_date', sa.String(length=250), nullable=True),
    sa.Column('publisher', sa.String(length=250), nullable=True),
    sa.Column('no_of_copies_total', sa.Integer(), nullable=True),
    sa.Column('no_of_copies_current', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('bookID')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=150), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('books')
    # ### end Alembic commands ###