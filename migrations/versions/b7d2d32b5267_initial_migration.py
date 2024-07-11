"""Initial migration

Revision ID: b7d2d32b5267
Revises: 
Create Date: 2024-07-08 19:01:44.674160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d2d32b5267'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('pais_origen', sa.String(length=70), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('num_telefono', sa.Float(), nullable=True),
    sa.Column('provincia', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Float(), nullable=True),
    sa.Column('disponibilidad', sa.Boolean(), nullable=True),
    sa.Column('ubicacion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('fabricante', sa.String(length=50), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('modelo_id', sa.Integer(), nullable=False),
    sa.Column('fabricante_id', sa.Integer(), nullable=False),
    sa.Column('caracteristicas_id', sa.Integer(), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=False),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['caracteristicas_id'], ['caracteristicas.id'], ),
    sa.ForeignKeyConstraint(['fabricante_id'], ['fabricante.id'], ),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['modelo.id'], ),
    sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipo')
    op.drop_table('modelo')
    op.drop_table('marca')
    op.drop_table('stock')
    op.drop_table('proveedor')
    op.drop_table('fabricante')
    # ### end Alembic commands ###
