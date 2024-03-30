from flask import Blueprint,render_template, request
from database.cliente import CLIENTES
from database.models.cliente import Cliente



cliente_route = Blueprint('cliente', __name__)
"""
    rota do clliente
    
    - /clientes/ GET- listar os clientes
    - /clientes/ POST- insere o cliente no server
    - /clientes/new GET- renderiza o formulario para criar um cliente
    -/clientes/<id> GET- obtem os dados do cliente
    - /cliente/<id>/edit GET- renderiza um formulario para alterar os dados de um cliente
    - /cliente/<id>/update PUT- atualiza os dados do cliente 
    - /cliente/<id>/delete DELETE - deleta o registro do usuário    
"""


@cliente_route.route('/')
def lista_clientes():
    '''listar clientes'''
    clientes = Cliente.select()
    return render_template('lista_clientes.html',clientes = clientes)



@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''insere os dados do cliente no bnaco de dados'''
    data = request.json
    
    novo_usuario = Cliente.create(
        nome =data['nome'],
        email =data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)



@cliente_route.route('/new')
def form_cliente():
    '''formulatio pra cadastraar um cliente'''
    return render_template('form_clientes.html')



@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    '''exibe os detalhes do cliente'''
    
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    '''formulario pra editar os dados do cliente'''
    
    cliente = None
    
    cliente = Cliente.get_by_id(cliente_id)
    
    return render_template('form_clientes.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    data = request.json
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
            
    return render_template('item_cliente.html', cliente=cliente_editado)         


   
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_clientes(cliente_id):
    '''deleta os dados do cliente'''
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted' : 'ok'}