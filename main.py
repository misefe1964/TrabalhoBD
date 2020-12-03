import psycopg2
from psycopg2 import OperationalError, errorcodes
import sys
import datetime
import tabulate
import matplotlib.pyplot as plt

# estabelece conexão com o BD
connection = psycopg2.connect(user="milena", 
password = "17071964", 
port = "5432", 
database = "trabalhoFinal")

# declara cursor
cursor = connection.cursor()

# declara logs
logClientes = [] 
logColaboradores = []
logSetores = []
logAtividades = []
logProjetos = []
logPedidos = []
logOrdens = []
logNotas = []

# define estilo dos gráficos de barra
plt.style.use('ggplot')

# função menu principal
# mostra opções da aplicação e invoca função desejada

def menu():
	print('MENU PRINCIPAL\n')
	print("""Opções:
	[1]: Inserir Tupla(s) e Dados
	[2]: Atualizar Atributos
	[3]: Deletar Tuplas
	[4]: Alterar Gestor
	[5]: Finalizar Projeto
	[6]: Informar Saída de Colaborador
	[7]: Finalizar Atividade
	[8]: Atribuir Atividade a Colaborador
	[9]: Atribuir Projeto a Colaborador
	[10]: Atribuir Projeto(s) a Pedido e Ordem de Serviço
	[11]: Realizar Consultas e Obter Gráficos
	[12]: Ver Tabelas
	[13]: Sair
	""")
	opt = input("Insira a opção desejada: ")

	if opt == '1':
		inserir()
	elif opt == '2':
		atualizar()
	elif opt == '3':
		deletar()
	elif opt == '4':
		alteraGestor()
	elif opt == '5':
		finalizaProjeto()
	elif opt == '6':
		informaSaida()
	elif opt == '7':
		finalizaAtividade()
	elif opt == '8':
		AtividadeColaborador()
	elif opt == '9':
		ProjetoColaborador()
	elif opt == '10':
		ligaProjeto()
	elif opt == '11':
		consultas()
	elif opt == '12':
		menuView()
	elif opt == '13':
		getOut()
	else: 
		print("Opção Inválida.")

# função main
# mostra integrantes e invoca loop infinito do menu principal

def _main():
	print("""=====================================================\nTrabalho Final de Banco de Dados
	Integrantes:
	--> Augusto Scarduelli Prudencio (18102140) 
	--> Horizonte Nazarete Magalhães Junior (17202046)
	--> Milena Seibert Fernandes (18102152)\n=====================================================""")

	while True:
		menu()

# menu de consultas
# mostra opções de consulta e invoca função desejada

def consultas():
	print('MENU DE CONSULTAS\n')
	print("""\nAs consultas disponíveis são:
	[1]: Média de salário por setor
	[2]: Número de projetos por colaborador
	[3]: Valor obtido por cliente
	[4]: Cancelar consulta""")

	consulta = input("Insira o número da consulta desejada: ")
	if consulta == '1':
		consulta1()
	elif consulta == '2':
		consulta2()
	elif consulta == '3':
		consulta3()
	elif consulta == '4':
		print("Consulta Cancelada.")
	else:
		print("Opção inválida. Tente novamente.\n")
		consultas()

# menu de inserções
# mostra opções de inserção e invoca função desejada

def inserir():
	print("MENU DE INSERÇÕES\n")
	print("""\nÉ possível inserir tuplas nas seguintes tabelas:
	[1]: Cliente
	[2]: Colaborador
	[3]: Setor
	[4]: Atividade
	[5]: Pedido
	[6]: Ordem de Servico
	[7]: Projeto Web
	[8]: Cancelar inserção""")
	opt = input("Indique o número da tabela: ")

	if opt == '1':
		tweakCliente('inserir')
	elif opt == '2':
		tweakColaborador('inserir')
	elif opt == '3':
		tweakSetor('inserir')
	elif opt == '4':
		tweakAtividade('inserir')
	elif opt == '5':
		tweakPedido('inserir')
	elif opt == '6':
		tweakOrdemdeServico('inserir')
	elif opt == '7': 
		tweakProjeto('inserir')
	elif opt == '8':
		print("Inserção cancelada")
	else:
		print("Opção inválida...")
		inserir()

# menu de atualizações
# mostra opções de atualização e invoca função desejada

def atualizar():
	print("MENU DE ATUALIZAÇÕES\n")
	print("""\nÉ possível atualizar tuplas nas seguintes tabelas:
	[1]: Cliente
	[2]: Colaborador
	[3]: Setor
	[4]: Atividade
	[5]: Pedido
	[6]: Projeto Web
	[7]: Ordem de Serviço
	[8]: Cancelar atualização""")
	opt = input("Indique o número da tabela: ")

	if opt == '1':
		tweakCliente('atualizar')
	elif opt == '2':
		tweakColaborador('atualizar')
	elif opt == '3':
		tweakSetor('atualizar')
	elif opt == '4':
		tweakAtividade('atualizar')
	elif opt == '5':
		tweakPedido('atualizar')
	elif opt == '6': 
		tweakProjeto('atualizar')
	elif opt == '7':
		tweakOrdemdeServico('atualizar')
	elif opt == '8':
		print("Atualização cancelada")
	else:
		print("Opção inválida...")
		atualizar()

# menu de exclusões
# mostra opções de exclusão e invoca função desejada

def deletar():
	print("MENU DE EXCLUSÕES\n")
	print("""\nÉ possível deletar tuplas das seguintes tabelas:
	[1]: Cliente
	[2]: Colaborador
	[3]: Setor
	[4]: Atividade
	[5]: Pedido
	[6]: Projeto Web
	[7]: Ordem de Serviço
	[8]: Cancelar exclusão""")
	opt = input("Indique o número da tabela: ")

	if opt == '1':
		tweakCliente('deletar')
	elif opt == '2':
		tweakColaborador('deletar')
	elif opt == '3':
		tweakSetor('deletar')
	elif opt == '4':
		tweakAtividade('deletar')
	elif opt == '5':
		tweakPedido('deletar')
	elif opt == '6': 
		tweakProjeto('deletar')
	elif opt == '7':
		tweakOrdemdeServico('deletar')
	elif opt == '8':
		print("Exclusão cancelada")
	else:
		print("Opção inválida...")
		atualizar()

# menu de visualização
# mostra opções de visualização e invoca função desejada

def menuView():
	print("MENU DE VISULIZAÇÃO")
	print("""\nVocê pode visualizar as seguintes tabelas:
	[1]: Cliente
	[2]: Colaborador
	[3]: Setor
	[4]: Atividade
	[5]: Pedido
	[6]: Ordem de Serviço
	[7]: Projeto Web
	[8]: Nota Fiscal
	[9]: Possui (Relacionamento entre Colaborador e Atividade)
	[10]: Gera (Relacionamento entre Projeto Web, Ordem de Serviço e Pedido)
	[11]: Desenvolve (Relacionamento entre Colaborador e Projeto Web)
	[12]: Cancelar visualização\n""")

	opt = input("Insira o número da tabela que deseja ver: ")
	if opt == '1':
		showCliente()
	elif opt == '2':
		showColaborador()
	elif opt == '3': 
		showSetor()
	elif opt == '4':
		showAtividade()
	elif opt == '5':
		showPedido()
	elif opt == '6':
		showOrdem()
	elif opt == '7':
		showProjeto()
	elif opt == '8':
		showNota()
	elif opt == '9':
		showPossui()
	elif opt == '10':
		showGera()
	elif opt == '11':
		showDesenvolve()
	elif opt == '12':
		print("Visualização cancelada")

# funções de visualização
# imprimem tabelas inteiras

def showCliente():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Cliente: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idCliente', 'Tipo', 'Endereço', 'CPF', 'Nome', 'CNPJ', 'Razão Social']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from cliente"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showColaborador():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Colaborador: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idColaborador', 'idSetor', 'DataEntrada', 'DataSaida', 'CPF', 'Nome', 'Especialidade', 'Salario']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from colaborador"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showSetor():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Setor: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idSetor', 'Nome', 'Descrição', 'idGestor', 'Salário Base']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from setor"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showAtividade():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Atividade: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idAtividade', 'Tipo', 'Data Início', 'Data Fim', 'Descrição', 'Status']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from atividade"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showPedido():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Pedido: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idPedido', 'idCliente', 'Descrição']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from pedido"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showOrdem():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Ordem de Serviço: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idOrdem', 'Orçamento Previsto', 'Valor', 'Tipo de Serviço']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from ordemdeservico"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showProjeto():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Projeto Web: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idProjeto', 'Descrição', 'Plataforma', 'Linguagem', 'Data Início', 'Estimativa Data Final', 'Data Final']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from projetoweb"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showNota():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Nota Fiscal: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idNota', 'idOrdem', 'Valor Total']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from notafiscal"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showPossui():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Possui: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idColaborador', 'idAtividade', 'Data Entrada']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from possui"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showGera():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Gera: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idProjeto', 'idOrdem', 'idPedido']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from gera"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

def showDesenvolve():
	# imprime nome da tabela
	print("=========================================================")
	print("Tabela Desenvolve: ")
	print("=========================================================")
	# define atributos em ordem
	header = ['idColaborador', 'idProjeto']
	table = []
	table.append(header)
	# realiza consulta
	inst = """select * from Desenvolve"""
	cursor.execute(inst)
	data = cursor.fetchall()
	# insere dados em uma única lista de listas
	for dataset in data:
		dataset = list(dataset)
		table.append(dataset)
	# imprime tabela
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")

# funções de operações
# realizam inserts, updates e deletes
# a operação é definida pelo valor de opt

def tweakCliente(opt):
	# considera variável global de log
	global logClientes

	# converte conteúdo do log para string
	stringlogClientes = [str(logClientes[i]) for i in range(len(logClientes))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showCliente()

	# se opção selecionada é inserir
	if opt == 'inserir':
		# determina id do cliente a ser inserido
		idcliente = str(len(logClientes)+1)

		if idcliente in stringlogClientes:
			idcliente = input("Insira o id do cliente a ser adicionado: ")			

		while idcliente in stringlogClientes:
			idcliente = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		nome = input('Insira o nome do cliente: ')
		nome = "'"+nome+"'" if nome != 'null' else nome
		endereco = input("Insira o endereco do cliente: ")
		endereco = "'"+endereco+"'" if endereco != 'null' else endereco
		tipo = input('Insira o tipo de cliente (Fisica ou Juridica): ')
		while tipo != 'Fisica' and tipo != 'Juridica':
			tipo = input('TIPO INVÁLIDO. Tente novamente (Fisica ou Juridica): ')

		# dependendo do tipo do cliente, alguns atributos serão nulos
		if tipo == 'Fisica':
			cnpj = 'null'
			razaosocial = 'null'
			cpf = input("Insira o CPF do cliente: ")
			cpf = "'"+cpf+"'" if cpf != 'null' else cpf
		elif tipo == 'Juridica':
			cpf = 'null'
			cnpj = input('Insira o CNPJ do cliente: ')
			cnpj = "'"+cnpj+"'" if cnpj != 'null' else cnpj
			razaosocial = input("Insira a razão social do cliente: ")
			razaosocial = "'"+razaosocial+"'" if razaosocial != 'null' else razaosocial

		# insere instrução de inserção
		insertQuery = """insert into cliente
		(idcliente, tipo, endereco, cpf, nome, cnpj, razaosocial)
		values
		({}, 'Pessoa {}', {}, {}, {}, {}, {});""".format(idcliente, tipo, endereco, cpf, nome, cnpj, razaosocial)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id do cliente
		idcliente = input("Insira o id do cliente a ser atualizado: ")
		while idcliente not in stringlogClientes:
			idcliente = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'nome' or atributo == 'endereco' or atributo == 'cpf' or atributo == 'cnpj' or atributo == 'razaosocial' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"
		if atributo == 'tipo':
			novo_valor = "'Pessoa {}'".format(novo_valor)

		# insere instrução de atualização
		updateQuery = """update cliente
		set {} = {}
		where idCliente = {};
		""".format(atributo, novo_valor, idcliente)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id do cliente
		idcliente = input("Insira o id do cliente a ser deletado (deixar em branco caso deseje deletar todos): ")

		# insere início da instrução de deleção		
		deleteQuery = 'delete from cliente'

		# se idcliente for string vazia
		if idcliente == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idcliente inserido não consta no banco de dados
		elif idcliente not in stringlogClientes:

			# verifica se valor inserido é um número inteiro
			try:
				idcliente = int(idcliente)
				print("O id de cliente inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de cliente inserido não é um número inteiro.")
			
		# se idcliente consta no banco de dados
		elif idcliente != '':
			deleteQuery = deleteQuery+" where idCliente = {};".format(idcliente)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de clientes
	logClientes = []
	instrucao = "select idcliente from cliente;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logClientes.append(elemento[0])

def tweakColaborador(opt):
	# considera variáveis globais de log
	global logColaboradores, logSetores

	# converte conteúdo dos logs para string
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]
	stringlogSetores = [str(logSetores[i]) for i in range(len(logSetores))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()
		showSetor()

	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id do colaborador a ser inserido
		idcolaborador = str(len(logColaboradores)+1)

		if idcolaborador in stringlogColaboradores:
			idcolaborador = input("Insira o id do colaborador a ser adicionado: ")			

		while idcolaborador in stringlogColaboradores:
			idcolaborador = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		nome = input('Insira o nome do colaborador: ')
		nome = "'"+nome+"'" if nome != 'null' else nome
		cpf = input("Insira o CPF do colaborador: ")
		cpf = "'"+cpf+"'" if cpf != 'null' else cpf
		idsetor = input("Insira o id do setor do colaborador: ")
		while idsetor not in stringlogSetores:
			# verifica se a criação de um novo setor é necessária
			print('O id de setor inserido não consta no banco de dados.')
			opt = input("Você deseja cadastrar um novo setor [y/n]? ")
			if opt == 'y':
				tweakSetor('inserir')
				stringlogSetores = [str(logSetores[i]) for i in range(len(logSetores))]

				print("\nVoltando à inserção de colaborador:\n")
				idsetor = input("Insira o id do setor do colaborador: ")
			else:
				idsetor = input("Insira um id de setor existente para o colaborador: ")

		dataEntrada = input("Insira a data de entrada (formato AAAA-MM-DD): ")
		dataEntrada = "'"+dataEntrada+"'" if dataEntrada != 'null' else dataEntrada
		dataSaida = 'null'
		especialidade = input("Insira a especialidade do colaborador: ")
		especialidade = "'"+especialidade+"'" if especialidade != 'null' else especialidade
		salario = input("Insira o salário do colaborador: ")

		# insere instrução de inserção
		insertQuery = """insert into colaborador
		(idcolaborador, idSetor, DataEntrada, DataSaida, cpf, Nome, Especialidade, Salario)
		values
		({}, {}, {}, {}, {}, {}, {}, {});""".format(idcolaborador, idsetor, dataEntrada, dataSaida, cpf, nome, especialidade, salario)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id do colaborador
		idcolaborador = input("Insira o id do colaborador a ser atualizado: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'nome' or atributo == 'cpf' or atributo == 'especialidade' or atributo == 'DataEntrada' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update colaborador
		set {} = {}
		where idColaborador = {};
		""".format(atributo, novo_valor, idcolaborador)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id do colaborador
		idcolaborador = input("Insira o id do colaborador a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from colaborador'

		# se idcolaborador for string vazia
		if idcolaborador == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idcolaborador inserido não consta no banco de dados
		elif idcolaborador not in stringlogColaboradores:

			# verifica se valor inserido é um número inteiro
			try:
				idcolaborador = int(idcolaborador)
				print("O id de colaborador inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de colaborador inserido não é um número inteiro.")

		# se idcolaborador consta no banco de dados				
		elif idcolaborador != '':
			deleteQuery = deleteQuery+" where idColaborador = {};".format(idcolaborador)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de colaboradores
	logColaboradores = []
	instrucao = "select idcolaborador from colaborador;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logColaboradores.append(elemento[0])

def tweakSetor(opt):
	# considera variáveis globais de log
	global logColaboradores, logSetores

	# converte conteúdo dos logs para string
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]
	stringlogSetores = [str(logSetores[i]) for i in range(len(logSetores))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()
		showSetor()

	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id do setor a ser inserido
		idsetor = str(len(logSetores)+1)

		if idsetor in stringlogSetores:
			idsetor = input("Insira o id do setor a ser adicionado: ")			

		while idsetor in stringlogSetores:
			idsetor = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		nome = input('Insira o nome do setor: ')
		nome = "'"+nome+"'" if nome != 'null' else nome
		idgestor = 'null'
		optGestor = input("O gestor desse setor já está cadastrado [y/n]?")
		if optGestor == 'y':
			idgestor = input('Insira o id do gestor do setor: ')

		salariobase = input("Insira o salário base do setor: ")
		descricao = input("Insira a descrição do setor: ")
		descricao = "'"+descricao+"'" if descricao != 'null' else descricao

		# insere instrução de inserção
		insertQuery = """insert into setor
		(idSetor, idGestor, nome, descricao, salarioBase)
		values
		({}, {}, {}, {}, {});""".format(idsetor, idgestor, nome, descricao, salariobase)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id da ordem do setor
		idsetor = input("Insira o id do setor a ser atualizado: ")
		while idsetor not in stringlogSetores:
			idsetor = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'nome' or atributo == 'descricao' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update setor
		set {} = {}
		where idSetor = {}
		""".format(atributo, novo_valor, idsetor)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id do setor
		idsetor = input("Insira o id do setor a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from setor'

		# se idsetor for string vazia
		if idsetor == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idsetor inserido não consta no banco de dados
		elif idsetor not in stringlogSetores:

			# verifica se valor inserido é um número inteiro
			try:
				idsetor = int(idsetor)
				print("O id de setor inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de setor inserido não é um número inteiro.")

		# se idsetor consta no banco de dados				
		elif idsetor != '':
			deleteQuery = deleteQuery+" where idSetor = {};".format(idsetor)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de setores
	logSetores = []
	instrucao = "select idsetor from setor;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logSetores.append(elemento[0])

def tweakAtividade(opt):
	# considera variável global de log
	global logAtividades

	# converte conteúdo do log para string
	stringlogAtividades = [str(logAtividades[i]) for i in range(len(logAtividades))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showAtividade()
	
	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id da atividade a ser inserida
		idatividade = str(len(logAtividades)+1)

		if idatividade in stringlogAtividades:
			idatividade = input("Insira o id da atividade a ser adicionada: ")			

		while idatividade in stringlogAtividades:
			idatividade = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		tipo = input('Insira o tipo da atividade: ')
		tipo = "'"+tipo+"'" if tipo != 'null' else tipo

		dataFim = 'null'
		dataInicio = input("Insira a data de início da atividade (formato AAAA-MM-DD): ")
		dataInicio = "'"+dataInicio+"'" if dataInicio != 'null' else dataInicio
		
		descricao = input("Insira a descrição da atividade: ")
		descricao = "'"+descricao+"'" if descricao != 'null' else descricao

		status = input("Insira o status da atividade: ")
		status = "'"+status+"'" if status != 'null' else status

		# insere instrução de inserção
		insertQuery = """insert into atividade
		(idAtividade, tipo, DataInicio, DataFim, descricao, status)
		values
		({}, {}, {}, {}, {}, {});""".format(idatividade, tipo, dataInicio, dataFim, descricao, status)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id da atividade
		idatividade = input("Insira o id da atividade a ser atualizada: ")
		while idatividade not in stringlogAtividades:
			idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'tipo' or atributo == 'dataInicio' or atributo == 'dataFim' or atributo == 'descricao' or atributo == 'status' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update atividade
		set {} = {}
		where idAtividade = {}
		""".format(atributo, novo_valor, idatividade)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id da atividade
		idatividade = input("Insira o id da atividade a ser deletada (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from atividade'

		# se idatividade for string vazia
		if idatividade == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idatividade inserido não consta no banco de dados
		elif idatividade not in stringlogAtividades:

			# verifica se valor inserido é um número inteiro
			try:
				idatividade = int(idatividade)
				print("O id de atividade inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de atividade inserido não é um número inteiro.")

		# se idatividade consta no banco de dados				
		elif idatividade != '':
			deleteQuery = deleteQuery+" where idAtividade = {};".format(idatividade)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de atividades
	logAtividades = []
	instrucao = "select idatividade from atividade;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logAtividades.append(elemento[0])

def tweakProjeto(opt): 
	# considera variável global de log
	global logProjetos

	# converte conteúdo do log para string
	stringlogProjetos = [str(logProjetos[i]) for i in range(len(logProjetos))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showProjeto()
	
	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id do projeto web a ser inserido
		idprojeto = str(len(logProjetos)+1)

		if idprojeto in stringlogProjetos:
			idprojeto = input("Insira o id do projeto a ser adicionado: ")			

		while idprojeto in stringlogProjetos:
			idprojeto = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		descricao = input("Insira a descrição do projeto: ")
		descricao = "'"+descricao+"'" if descricao != 'null' else descricao

		plataforma = input('Insira o plataforma do projeto: ')
		plataforma = "'"+plataforma+"'" if plataforma != 'null' else plataforma

		linguagem = input('Insira o linguagem do projeto: ')
		linguagem = "'"+linguagem+"'" if linguagem != 'null' else linguagem

		dataFinal = 'null'
		dataInicio = input("Insira a data de início do projeto (formato AAAA-MM-DD): ")
		dataInicio = "'"+dataInicio+"'" if dataInicio != 'null' else dataInicio
		estimativaDataFinal = input("Insira a data estimada para fim do projeto (formato AAAA-MM-DD): ")
		estimativaDataFinal = "'"+estimativaDataFinal+"'" if estimativaDataFinal != 'null' else estimativaDataFinal

		# insere instrução de inserção
		insertQuery = """insert into projetoweb
		(idProjeto, descricao, plataforma, linguagem, datainicio, estimativadatafinal, datafinal)
		values
		({}, {}, {}, {}, {}, {}, {});""".format(idprojeto, descricao, plataforma, linguagem, dataInicio, estimativaDataFinal, dataFinal)

		# tenta realizar inserção 
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id do projeto web
		idprojeto = input("Insira o id do projeto a ser atualizado: ")
		while idprojeto not in stringlogProjetos:
			idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'plataforma' or atributo == 'dataInicio' or atributo == 'estimativaDataFinal' or atributo == 'descricao' or atributo == 'linguagem' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update projetoweb
		set {} = {}
		where idProjeto = {}
		""".format(atributo, novo_valor, idprojeto)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id do projeto web
		idprojeto = input("Insira o id do projeto a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from projetoweb'

		# se idprojeto for string vazia
		if idprojeto == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idprojeto inserido não consta no banco de dados
		elif idprojeto not in stringlogProjetos:

			# verifica se valor inserido é um número inteiro
			try:
				idprojeto = int(idprojeto)
				print("O id de projeto inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de projeto inserido não é um número inteiro.")

		# se idprojeto consta no banco de dados				
		elif idprojeto != '':
			deleteQuery = deleteQuery+" where idProjeto = {};".format(idprojeto)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de projetos web
	logProjetos = []
	instrucao = "select idprojeto from projetoweb;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logProjetos.append(elemento[0])

def tweakPedido(opt):
	# considera variáveis globais de log
	global logPedidos, logClientes

	# converte conteúdo dos logs para string
	stringlogPedidos = [str(logPedidos[i]) for i in range(len(logPedidos))]
	stringlogClientes = [str(logClientes[i]) for i in range(len(logClientes))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showCliente()
		showPedido()

	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id do pedido a ser inserido
		idpedido = str(len(logPedidos)+1)

		if idpedido in stringlogPedidos:
			idpedido = input("Insira o id do pedido a ser adicionado: ")			

		while idpedido in stringlogPedidos:
			idpedido = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		idcliente = input("Insira o id do cliente que realizou o pedido: ")
		while idcliente not in stringlogClientes:
			idcliente = input("o id inserido não consta no banco de dados. Tente novamente: ")

		descricao = input("Insira a descrição do pedido: ")
		descricao = "'"+descricao+"'" if descricao != 'null' else descricao

		# insere instrução de inserção
		insertQuery = """insert into pedido
		(idPedido, idCliente, descricao)
		values
		({}, {}, {});""".format(idpedido, idcliente, descricao)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id do pedido
		idpedido = input("Insira o id do pedido a ser atualizado: ")
		while idpedido not in stringlogPedidos:
			idpedido = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'descricao' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update pedido
		set {} = {}
		where idPedido = {}
		""".format(atributo, novo_valor, idpedido)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id do pedido
		idpedido = input("Insira o id do pedido a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from pedido'

		# se idpedido for string vazia
		if idpedido == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se idpedido inserido não consta no banco de dados
		elif idpedido not in stringlogPedidos:

			# verifica se valor inserido é um número inteiro
			try:
				idpedido = int(idpedido)
				print("O id de pedido inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de pedido inserido não é um número inteiro.")
				
		# se idpedido consta no banco de dados
		elif idpedido != '':
			deleteQuery = deleteQuery+" where idPedido = {};".format(idpedido)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de pedidos
	logPedidos = []
	instrucao = "select idpedido from pedido;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logPedidos.append(elemento[0])

def tweakOrdemdeServico(opt):
	# considera variável global de log
	global logOrdens

	# converte conteúdo do log para string
	stringlogOrdens = [str(logOrdens[i]) for i in range(len(logOrdens))]

	# verifica se visualização é desejada 
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showOrdem()
	
	# se opção selecionada é inserir
	if opt == 'inserir':

		# determina id da ordem de serviço a ser inserida
		idordem = str(len(logOrdens)+1)

		if idordem in stringlogOrdens:
			idordem = input("Insira o id da ordem de serviço a ser adicionada: ")			

		while idordem in stringlogOrdens:
			idordem = input("O id inserido já consta no banco de dados. Tente novamente: ")

		# coleta valores dos demais atributos
		orcamentoprevisto = input("Insira o orçamento previsto da ordem de serviço: ")
		valor = 0

		tiposervico = input("Insira o tipo do serviço: ")
		tiposervico = "'"+tiposervico+"'" if tiposervico != 'null' else tiposervico

		# insere instrução de inserção
		insertQuery = """insert into OrdemDeServico
		(idOrdem, orcamentoprevisto, valor, tiposervico)
		values
		({}, {}, {}, {});""".format(idordem, orcamentoprevisto, valor, tiposervico)

		# tenta realizar inserção
		# se possível, realiza commit
		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	# se a opção selecionada é atualizar
	elif opt == 'atualizar':

		# coleta o id da ordem de serviço
		idordem = input("Insira o id da ordem de serviço a ser atualizada: ")
		while idordem not in stringlogOrdens:
			idordem = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# coleta o atributo
		atributo = input("Insira o atributo a ser atualizado: ")

		# coleta o novo valor do atributo
		novo_valor = input("Insira o novo valor do atributo: ")

		# adiciona aspas se atributo for varchar e não nulo
		if atributo == 'tiposervico' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		# insere instrução de atualização
		updateQuery = """update ordemdeservico
		set {} = {}
		where idOrdem = {}
		""".format(atributo, novo_valor, idordem)

		# tenta realizar atualização
		# se possível, realiza commit
		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização realizada com sucesso!\n")

		# se não for possível, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':

		# coleta id da ordem de serviço
		idordem = input("Insira o id da ordem de servico a ser deletada (deixar em branco caso deseje deletar todos): ")
		
		# insere início da instrução de deleção
		deleteQuery = 'delete from OrdemDeServico'

		# se idordem for string vazia
		if idordem == '':
			deleteQuery = deleteQuery+";"

			# tenta deletar todas as linhas da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()


		# se idordem inserido não consta no banco de dados
		elif idordem not in stringlogOrdens:
			# verifica se valor inserido é um número inteiro
			try:
				idordem = int(idordem)
				print("O id de ordem de serviço inserido não consta no banco de dados.")

			# se não, informa que não é um número inteiro
			except:
				print("O id de ordem de serviço inserido não é um número inteiro.")

		# se idordem consta no banco de dados				
		elif idordem != '':
			deleteQuery = deleteQuery+" where idordem = {};".format(idordem)

			# tenta deletar linha específica da tabela
			# se possível, realiza commit
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
			
			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log de ordens
	logOrdens = []
	instrucao = "select idordem from ordemdeservico;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logOrdens.append(elemento[0])

# função que imprime erros relacionados ao banco de dados

def imprimeErro(err):
    # detalhes:
    err_type, err_obj, traceback = sys.exc_info()

    # linha onde ocorreu o erro:
    line_num = traceback.tb_lineno

    # imprime a mensagem de erro
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # imprime os códigos da excessão
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

# função para alterar gestor de setor

def alteraGestor():
	# considera variáveis globais de log
	global logSetores, logColaboradores

	# converte conteúdo dos logs para strings
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]
	stringlogSetores = [str(logSetores[i]) for i in range(len(logSetores))]

	# verifica se visualisação é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()
		showSetor()

	# coleta id do setor e do colaborador que será o gestor
	idsetor = input("Insira o id do setor cujo gestor deve ser alterado: ")
	while idsetor not in stringlogSetores:
		idsetor = input("O id do setor não consta no banco de dados. Tente novamente: ")
	idgestor = input("Insira o id do novo gestor: ")
	while idgestor not in stringlogColaboradores:
		idgestor = input("O id do gestor não consta no banco de dados. Tente novamente: ")

	# insere instrução de atualização
	instrucao = "update setor set idgestor = {} where idsetor = {};".format(idgestor, idsetor)
	
	# tenta realizar operação
	# se possível, realiza commit
	try:
		cursor.execute(instrucao)
		connection.commit()
		print("\nAlteração de gestor realizada com sucesso!\n")

	# se não for possível, imprime mensagem de erro e realiza rollback
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

# função para finalizar projeto
# atualiza o valor da data final do projeto
# gera uma nota fiscal associada à ordem de serviço associada
# atualiza valores da nota fiscal e da ordem de serviço

def finalizaProjeto():	
	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showProjeto()
		showPedido()
		showOrdem()
		showNota()
	
	# considera variáveis globais de log
	global logProjetos, logOrdens, logPedidos, logNotas

	# converte o conteúdo dos logs para strings
	stringlogProjetos = [str(logProjetos[i]) for i in range(len(logProjetos))]
	stringlogPedidos = [str(logPedidos[i]) for i in range(len(logPedidos))]
	stringlogOrdens = [str(logOrdens[i]) for i in range(len(logOrdens))]
	stringlogNotas = [str(logNotas[i]) for i in range(len(logNotas))]

	# coleta id e data final do projeto
	idprojeto = input("Insira o id do projeto a ser finalizado: ")
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")
	dataFinal = input("Insira a data de finalização do projeto (formato AAAA-MM-DD): ")
	while dataFinal == 'null': 
		dataFinal = input("A data de finalização do projeto deve ser informada (formato AAAA-MM-DD): ")
	dataFinal = "'"+dataFinal+"'"

	# insere instrução de atualização da data final
	addDataFinal = """update projetoweb
	set datafinal = {}
	where idprojeto = {}""".format(dataFinal, idprojeto)

	# tenta realizar operação de atualização 
	try:
		# se possível, verifica a que pedido e ordem de serviço o projeto está associado
		cursor.execute(addDataFinal)
		print("\nData de finalização pode ser inserida.\n")
		instrucao = """select g.idordem
		from projetoweb as p, gera as g, ordemdeservico as ord
		where p.idprojeto = g.idprojeto 
		and g.idordem = ord.idordem
		and g.idprojeto = {};""".format(idprojeto)

		cursor.execute(instrucao)
		record = cursor.fetchone()

		# se o projeto não estiver associado a pedido e ordem de serviço
		# imprime mensagem de não criação de nota fiscal e realiza commit
		if record == None:
			print("Esse projeto não foi associado com nenhuma ordem de serviço ou pedido, e, portanto, nenhuma nota fiscal foi gerada.")
			ordem = None
			connection.commit()

		# caso contrário, coleta id da ordem associada
		else:
		 	ordem = record[0]

		if ordem!=None:
			# determina id da nota fiscal a ser criada
			idnota = len(logNotas)+1
			if idnota in stringlogNotas:
				idnota = input("Insira o id da nota fiscal a ser gerada: ")
			while idnota in stringlogNotas:
				idnota = input("O id inserido já consta no banco de dados. Tente novamente: ")

			# coleta valor do projeto, que será valor total da nota fiscal
			# e será incrementado ao valor da ordem de serviço
			valor= input('Insira o custo do projeto finalizado: ')

			# insere instrução de inserção de nota fiscal
			criaNota = """insert into notafiscal
			(idnota, idordem, valortotal)
			values 
			({}, {}, {});""".format(idnota, ordem, valor)
			# tenta realizar inserção
			try:
				# se possível, insere instrução de atualização de valor da ordem de serviço
				cursor.execute(criaNota)
				print("\nA nota fiscal pode ser criada.\n")

				atOrdem = """update ordemdeservico
				set valor = valor+{}
				where idordem = {}""".format(valor, ordem)
				# tenta realizar atualização
				# se possível, realiza commit
				try:
					cursor.execute(atOrdem)
					print("\nO valor da ordem de servico pode ser atualizado.\n")
					connection.commit()
					print("\nTodas as operações foram realizadas com sucesso!\n")

				# se não for possível realizar a atualização do valor da ordem, imprime mensagem de erro e realiza rollback
				except Exception as err:
					imprimeErro(err)
					connection.rollback()

			# se não for possível realizar inserção, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# se não for possível realizar atualização da data final do projeto, imprime mensagem de erro e realiza rollback				
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

	# atualiza o log de notas
	logNotas = []
	instrucao = "select idnota from notafiscal;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logNotas.append(elemento[0])

# função para informar saída de colaborador
# atualiza data de saída e id setor do colaborador

def informaSaida():
	# considera variável global de log
	global logColaboradores

	# converte conteúdo do log em strings
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]

	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()

	# coleta atributos idcolaborador e dataSaida
	idcolaborador = input("Insira o id do colaborador que saiu: ")
	while idcolaborador not in stringlogColaboradores:
		idcolaborador - input("O id inserido não consta no banco de dados. Tente novamente: ")
	dataSaida = input("Insira a data de saída do colaborador (formato AAAA-MM-DD): ")

	# certifica-se de que a data de saída inserida não é nula
	while dataSaida == 'null':
		print("A data de saída do colaborador deve ser informada (formato AAAA-MM-DD): ")
	dataSaida = "'"+dataSaida+"'"
	
	# insere instrução de atualização
	infSaida = """update colaborador
	set dataSaida = {}
	where idcolaborador = {};""".format(dataSaida, idcolaborador)

	# torna o setor do colaborador nulo
	retiraSetor = """update colaborador
	set idSetor = null
	where idcolaborador = {}""".format(idcolaborador)

	# tenta atualizar atributos
	# se possível, realiza commit
	try:
		cursor.execute(infSaida)
		cursor.execute(retiraSetor)
		connection.commit()
		print("\nInformação de saída de funcionário realizada com sucesso!\n")

	# se não for possível, imprime mensagem de erro e realiza rollback
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

# função que finaliza uma atividade
# adiciona valor ao atributo DataFim e altera status para 'Terminado'

def finalizaAtividade():
	# considera variável global de log
	global logAtividades

	# converte conteúdo do log em strings 
	stringlogAtividades = [str(logAtividades[i]) for i in range(len(logAtividades))]

	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showAtividade()

	# coleta atributos para finalização
	idatividade = input("Insira o id da atividade que está sendo encerrada: ")
	while idatividade not in stringlogAtividades:
		idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")

	dataFim = input("Insira a data de encerramento da atividade (formato AAAA-MM-DD): ")
	# certifica-se que a data final inserida não é nula
	while dataFim == 'null':
		dataFim = input("A data de encerramento da atividade deve ser informada (formato AAAA-MM-DD): ")
	dataFim = "'"+dataFim+"'"

	# instrução de atualização
	encerraAtividade = """update atividade
	set dataFim = {}
	where idatividade = {}""".format(dataFim, idatividade)
	# tenta realizar atualização de data final
	try:
		cursor.execute(encerraAtividade)
		# se possível, atualiza status
		atualizaStatus = """update atividade
		set status = 'Terminado'
		where idatividade = {}""".format(idatividade)
		# se possível, realiza commit
		try:
			cursor.execute(atualizaStatus)
			connection.commit()
			print("\nFinalização de atividade realizada com sucesso!\n")
		# se não for possível atualizar status da atividade, imprime mensagem de erro e realiza rollback
		except Exception as err:
			imprimeErro(err)
			connection.rollback()
			
	# se não for possível atualizar data fim da atividade, imprime mensagem de erro e realiza rollback
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

# função que atribui atividade a um colaborador
# insere linha na tabela Possui

def AtividadeColaborador():
	# considera variáveis globais de log
	global logColaboradores, logAtividades

	# converte o conteúdo dos logs em strings
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]
	stringlogAtividades = [str(logAtividades[i]) for i in range(len(logAtividades))]

	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()
		showAtividade()
		showPossui()

	# coleta id da atividade
	idatividade = input("Insira o id da atividade a ser atribuída: ")
	while idatividade not in stringlogAtividades:
		idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")

	# verifica se a atividade não foi finalizada
	verificaAtividade = """select * from atividade
	where idatividade = {} and datafim is not null;""".format(idatividade)

	cursor.execute(verificaAtividade)
	record = cursor.fetchone()

	# se atividade não foi finalizada, continua a operação
	if record == None:

		# coleta o id do colaborador
		idcolaborador = input("Insira o id do colaborador a quem a atividade será atribuída: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# verifica se o colaborador não saiu da empresa
		pegaData = """select datasaida
		from colaborador
		where idcolaborador = {} and datasaida is not null;""".format(idcolaborador)
		cursor.execute(pegaData)
		record = cursor.fetchone()

		# se o colaborador não saiu da empresa, continua a operação
		if record == None:

			# busca a data de entrada do colaborador na empresa
			pegaData = """select dataentrada 
			from colaborador
			where idcolaborador = {};""".format(idcolaborador)
			cursor.execute(pegaData)
			record = cursor.fetchone()
			dataEntradaColaborador = record[0]
			tmp = datetime.datetime.min.time()
			dataEntradaColaborador = datetime.datetime.combine(dataEntradaColaborador, tmp)

			# coleta data de entrada do colaborador na atividade
			dataEntrada = input("Insira a data de entrada do colaborador na atividade (formado AAAA-MM-DD): ")
			dataEntradadatetime = datetime.datetime.strptime(dataEntrada, '%Y-%m-%d')

			# verifica se o colaborador já estava na empresa na data de entrada na atividade
			while dataEntradadatetime < dataEntradaColaborador: 
				# se não, solicita data posterior para entrada na atividade
				print("Não foi possível fazer a atribuição, pois o colaborador não estava na empresa nessa data.")
				dataEntrada = input("Tente inserir uma data posterior (AAAA-MM-DD): ")
				dataEntradadatetime = datetime.datetime.strptime(dataEntrada, '%Y-%m-%d')

			dataEntrada = "'"+dataEntrada+"'" if dataEntrada != 'null' else dataEntrada
			# continua a operação
			insercao = """insert into possui (idColaborador, idAtividade, dataEntrada)
			values ({}, {}, {});""".format(idcolaborador, idatividade, dataEntrada)

			# tenta realizar a operação
			# se possível, realiza commit
			try:
				cursor.execute(insercao)
				connection.commit()
				print("\nAtribuição de atividade ao colaborador realizada com sucesso!\n")

			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		# se o colaborador já saiu da empresa, imprime mensagem de erro
		else: print("O colaborador em questão já saiu da empresa. A atribuição não pode ser realizada.")

	# se a atividade já foi finalizada, imprime mensagem de erro
	else: 
		print("A atividade em questão já foi encerrada. A atribuição não pode ser realizada.")

# função que atribui projeto a um colaborador
# insere linha na tabela Desenvolve

def ProjetoColaborador():
	# considera variáveis globais de log
	global logColaboradores, logProjetos

	# converte o conteúdo dos logs em strings
	stringlogColaboradores = [str(logColaboradores[i]) for i in range(len(logColaboradores))]
	stringlogProjetos = [str(logProjetos[i]) for i in range(len(logProjetos))]

	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showColaborador()
		showProjeto()
		showDesenvolve()

	# coleta id do projeto
	idprojeto = input("Insira o id do projeto a ser atribuído: ")
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")

	# verifica se projeto está finalizado
	verificaProjeto = """select * from projetoweb
	where idprojeto = {} and datafinal is not null;""".format(idprojeto)

	cursor.execute(verificaProjeto)
	record = cursor.fetchone()
	# se projeto não está finalizado, continua a operação
	if record == None:
		# coleta id do colaborador
		idcolaborador = input("Insira o id do colaborador a quem o projeto será atribuído: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")

		# verifica se colaborador ainda está na empresa
		pegaData = """select datasaida 
		from colaborador
		where idcolaborador = {} and datasaida is not null;""".format(idcolaborador)
		cursor.execute(pegaData)
		record = cursor.fetchone()

		# se colaborador está na empresa, continua a operação
		if record == None:

			insercao = """insert into desenvolve (idColaborador, idProjeto)
			values ({}, {});""".format(idcolaborador, idprojeto)

			# tenta realizar a operação
			# se possível, realiza commit
			try:
				cursor.execute(insercao)
				connection.commit()
				print("\nAtribuição do projeto ao colaborador realizada com sucesso!\n")

			# se não for possível, imprime mensagem de erro e realiza rollback
			except Exception as err:
				imprimeErro(err)
				connection.rollback()
		# se colaborador não está mais na empresa, imprime mensagem de erro
		else: 
			print("O colaborador em questão já saiu da empresa. A atribuição não pode ser realizada.")

	# se projeto já foi finalizado, imprime mensagem de erro
	else: 
		print("O projeto em questão já foi encerrado. A atribuição não pode ser realizada.")

# função para ligar produto a um pedido e uma ordem de serviço
# adiciona linha na tabela Gera

def ligaProjeto():
	# considera variáveis globais de log
	global logProjetos, logPedidos, logOrdens

	# converte o conteúdo dos logs em strings
	stringlogPedidos = [str(logPedidos[i]) for i in range(len(logPedidos))]
	stringlogProjetos = [str(logProjetos[i]) for i in range(len(logProjetos))]
	stringlogOrdens = [str(logOrdens[i]) for i in range(len(logOrdens))]

	# verifica se visualização é desejada
	view = input("Antes de realizar essa operação, você deseja visualizar os dados já existentes [y/n]? ")
	if view == 'y':
		showProjeto()
		showPedido()
		showOrdem()
		showGera()

	# coleta atributos a serem inseridos
	idprojeto = input("Insira o id do projeto a ser atribuído: ")
	# verifica se ids constam no banco de dados
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")


	idpedido = input("Insira o id do pedido a ser atribuído: ")
	while idpedido not in stringlogPedidos:
		idpedido = input("O id inserido não consta no banco de dados. Tente novamente: ")

	idordem = input("Insira o id da ordem de serviço a ser atribuída: ")
	while idordem not in stringlogOrdens:
		idordem = input("O id insetido não consta no banco de dados. Tente novamente: ")

	# insere operação de inserção
	atribuicao = """insert into Gera (idprojeto, idordem, idpedido)
	values ({}, {}, {});""".format(idprojeto, idordem, idpedido)

	# tenta executar a inserção, se for possível realiza commit
	try:
		cursor.execute(atribuicao)
		connection.commit()
		print("\nAtribuição de projeto a pedido e ordem de serviço realizada com sucesso!\n")

	# se não for possível, imprime mensagem de erro e realiza rollback
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

# Funções de consultas:

def consulta1():
	# insere a consulta
	query = """select s.idSetor, avg(Salario) 
	from Colaborador as c 
	inner join Setor as s 
	on c.idSetor = s.idSetor
	group by s.idSetor;"""

	# executa a consulta e coleta todos os resultados
	cursor.execute(query)
	result = cursor.fetchall()

	# divide o resultado em duas listas
	ids = []
	medias = []
	for tupla in result:
		ids.append(tupla[0])
		medias.append(tupla[1])
	ids = [str(i) for i in ids]
	nums = [i for i in range(len(ids))]

	# mostra o resultado
	print("=========================================================")
	print("Tabela Consulta 1: ")
	print("=========================================================")
	header = ['idSetor', 'Média Salarial']
	table = []
	table.append(header)
	for dataset in result:
		dataset = list(dataset)
		table.append(dataset)
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")
	
	# verifica se o resultado não está vazio
	if medias:
		# gera o gráfico de barra
		plt.bar(nums, medias)
		plt.title("Consulta 1: \nMédia de salário por setor")
		plt.ylabel('Média de Salário')
		plt.xticks(nums, ids)
		plt.xlabel("ID do setor")
		plt.grid(b=None, which='major', axis='y')
		passing = max(medias)-min(medias) if max(medias)-min(medias) <= 500 and max(medias)-min(medias)!= 0 else 500
		yticks = [i for i in range(0, int(max(medias)+passing), int(passing))]
		plt.yticks(yticks)
		plt.show()
	else:
		# mensagem de dados insuficientes
		print("Não existem dados suficientes para serem colocados em um gráfico.\n")

def consulta2():
	# insere a consulta
	query = """select c.idColaborador, count(pw.idProjeto) 
	from Colaborador as c 
	inner join Desenvolve as d 
	on c.idColaborador = d.idColaborador
	inner join ProjetoWeb as pw 
	on d.idProjeto = pw.idProjeto
	group by c.idColaborador;"""

	# executa a consulta e coleta todos os resultados
	cursor.execute(query)
	result = cursor.fetchall()

	# divide o resultado em duas listas
	ids = []
	medias = []
	for tupla in result:
		ids.append(tupla[0])
		medias.append(tupla[1])
	ids = [str(i) for i in ids]
	nums = [i for i in range(len(ids))]

	# mostra o resultado
	print("=========================================================")
	print("Tabela Consulta 2: ")
	print("=========================================================")
	header = ['idColaborador', 'Número de Projetos']
	table = []
	table.append(header)
	for dataset in result:
		dataset = list(dataset)
		table.append(dataset)
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")
	
	# verifica se o resultado não está vazio
	if medias:
		# gera o gráfico de barra
		plt.bar(nums, medias)
		plt.title("Consulta 2: \nNúmero de projetos por colaborador")
		plt.ylabel('Número de Projetos')
		plt.xticks(nums, ids)
		plt.xlabel("ID do colaborador")
		plt.grid(b=None, which='major', axis='y')
		passing = max(medias)-min(medias) if max(medias)-min(medias) <= 2 and max(medias)-min(medias) != 0 else 2
		yticks = [i for i in range(0, int(max(medias)+passing), int(passing))]
		plt.yticks(yticks)
		plt.show()
	else:
		# mensagem de dados insuficientes
		print("Não existem dados suficientes para serem colocados em um gráfico.\n")

def consulta3():
	# insere a consulta
	query = """Select c.idCliente, sum(Valor) 
	from Cliente as c inner join Pedido as p 
	on c.idCliente = p.idCliente
	inner join Gera as g 
	on p.idPedido = g.idPedido
	inner join OrdemdeServico as os 
	on g.idOrdem = os.idOrdem
	group by c.idCliente;"""

	# executa a consulta e coleta todos os resultados
	cursor.execute(query)
	result = cursor.fetchall()
	ids = []
	medias = []

	# divide o resultado em duas listas
	for tupla in result:
		ids.append(tupla[0])
		medias.append(tupla[1])
	ids = [str(i) for i in ids]
	nums = [i for i in range(len(ids))]

	# mostra o resultado
	print("=========================================================")
	print("Tabela Consulta 3: ")
	print("=========================================================")
	header = ['idCliente', 'Valor Total']
	table = []
	table.append(header)
	for dataset in result:
		dataset = list(dataset)
		table.append(dataset)
	print(tabulate.tabulate(table))
	print("\n=========================================================\n")
	
	# verifica se o resultado não está vazio
	if medias:
		# gera o gráfico de barra
		plt.bar(nums, medias)
		plt.title("Consulta 3: \nValor obtido por cliente")
		plt.ylabel('Valor Obtido')
		plt.xticks(nums, ids)
		plt.xlabel("ID do cliente")
		plt.grid(b=None, which='major', axis='y')
		passing = max(medias)-min(medias) if max(medias)-min(medias) <= 500 and max(medias)-min(medias) != 0 else 500
		yticks = [i for i in range(0, int(max(medias)+passing), int(passing))]
		plt.yticks(yticks)
		plt.show()
	else: 
		# mensagem de dados insuficientes
		print('Não existem dados suficientes para serem colocados em um gráfico.\n')

# função para terminar a execução

def getOut():
	# fechar o cursor e a conexão
	cursor.close()
	connection.close()
	# mensagem
	print('Execução finalizada.')
	# termina a execução do programa
	sys.exit(1)

# função para obter os logs

def getLogs():
	# considera variáveis globais de logs
	global logClientes, logColaboradores, logSetores, logProjetos, logAtividades, logPedidos, logOrdens, logNotas

	# obtem lista de ids de clientes já existentes
	instrucao = "select idcliente from cliente;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logClientes.append(elemento[0])

	# obtem lista de ids de colaboradores já existentes
	instrucao = "select idcolaborador from colaborador;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logColaboradores.append(elemento[0])

	# obtem lista de ids de setores já existentes
	instrucao = "select idsetor from setor;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logSetores.append(elemento[0])

	# obtem lista de ids de atividades já existentes
	instrucao = "select idatividade from atividade;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logAtividades.append(elemento[0])

	# obtem lista de ids de projetos web já existentes
	instrucao = "select idprojeto from projetoweb;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logProjetos.append(elemento[0])

	# obtem lista de ids de pedidos já existentes
	instrucao = "select idpedido from pedido;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logPedidos.append(elemento[0])

	# obtem lista de ids de ordens de serviço já existentes
	instrucao = "select idordem from ordemdeservico;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logOrdens.append(elemento[0])

	# obtem lista de ids de notas fiscais já existentes
	instrucao = "select idnota from notafiscal;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logNotas.append(elemento[0])

if __name__ == '__main__':
	# coleta ids já existentes no BD
	getLogs()
	# inicia os menus
	_main()
