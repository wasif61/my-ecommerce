# coding: utf8

# criamos um validador pré definido
notempty=IS_NOT_EMPTY(error_message=e_m['empty'])

# definição da tabela de categoria
db.define_table('categoria',
Field('nome', unique=True, notnull=True),
format='%(nome)s')

# validadores da tabela de categoria
db.categoria.nome.requires=[notempty, IS_NOT_IN_DB(db, 'categoria.nome',
error_message=e_m['in_db'])]

# definição da tabela de itens
db.define_table('itens',
Field('categoria', db.categoria, notnull=True),
Field('nome', notnull=True),
Field('valor', 'double'),
Field('desc', 'text'),
Field('foto', 'upload'),
format='%(nome)s - %(desc)s - %(valor)s'
)
# validação da tabela carro
db.itens.categoria.requires=IS_IN_DB(db, 'categoria.id','categoria.nome',error_message=e_m['not_in_db'])
db.itens.categoria.requires=notempty
db.itens.foto.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg', 'png', '.gif'),error_message=e_m['image']))
