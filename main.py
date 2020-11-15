import psycopg2
from psycopg2 import OperationalError, errorcodes
import sys
import datetime
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

def menu():
	print("""Opções:
	[1]: Inserir Tupla(s) e Dados
	[2]: Atualizar Atributos
	[3]: Deletar Atributos
	[4]: Alterar Gestor
	[5]: Finalizar Projeto
	[6]: Informar Saída de Colaborador
	[7]: Finalizar Atividade
	[8]: Atribuir Atividade a Colaborador
	[9]: Atribuir Projeto a Colaborador
	[10]: Atribuir Projeto(s) a Pedido e Ordem de Serviço
	[11]: Realizar Consultas e Obter Gráficos
	[12]: Sair
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
		getOut()

def _main():
	print("""=====================================================\nTrabalho Final de Banco de Dados
	Integrantes:
	--> Augusto Scarduelli Prudencio (18102140) 
	--> Horizonte Nazarete Magalhães Junior (17202046)
	--> Milena Seibert Fernandes (18102152)\n=====================================================""")

	while True:
		menu()

def consultas():
	print("""\nAs consultas disponíveis são:
	[1]: Média de salário por setor
	[2]: Número de projetos por colaborador
	[3]: Valor obtido por cliente""")

	consulta = input("Insira o número da consulta desejada: ")

def inserir():
	print("""\nÉ possível inserir tuplas nas seguintes tabelas:
	[1]: Cliente
	[2]: Colaborador
	[3]: Setor
	[4]: Atividade
	[5]: Pedido e Ordem de Servico
	[6]: Projeto Web
	[7]: Cancelar inserção""")
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
		tweakOrdemdeServico('inserir')
	elif opt == '6': 
		tweakProjeto('inserir')
	elif opt == '7':
		print("Inserção cancelada")
	else:
		print("Opção inválida...")
		inserir()

def atualizar():
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

def deletar():
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

def tweakCliente(opt):
	global logClientes
	stringlogClientes = []
	for cl in logClientes:
		stringlogClientes.append(str(cl))
	if opt == 'inserir':
		idcliente = str(len(logClientes)+1)

		if idcliente in stringlogClientes:
			idcliente = input("Insira o id do cliente a ser adicionado: ")			

		while idcliente in stringlogClientes:
			idcliente = input("O id inserido já consta no banco de dados. Tente novamente: ")

		nome = input('Insira o nome do cliente: ')
		nome = "'"+nome+"'"
		endereco = input("Insira o endereco do cliente: ")
		if endereco != 'null':
			endereco = "'"+endereco+"'"
		tipo = input('Insira o tipo de cliente (Fisica ou Juridica): ')
		while tipo != 'Fisica' and tipo != 'Juridica':
			tipo = input('TIPO INVÁLIDO. Tente novamente (Fisica ou Juridica): ')
		if tipo == 'Fisica':
			cnpj = 'null'
			razaosocial = 'null'
			cpf = input("Insira o CPF do cliente: ")
			cpf = "'"+cpf+"'"
		elif tipo == 'Juridica':
			cpf = 'null'
			cnpj = input('Insira o CNPJ do cliente: ')
			cnpj = "'"+cnpj+"'"
			razaosocial = input("Insira a razão social do cliente: ")
			razaosocial = "'"+razaosocial+"'"


		insertQuery = """insert into cliente
		(idcliente, tipo, endereco, cpf, nome, cnpj, razaosocial)
		values
		({}, 'Pessoa {}', '{}', {}, '{}', {}, {});""".format(idcliente, tipo, endereco, cpf, nome, cnpj, razaosocial)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idcliente = input("Insira o id do cliente a ser atualizado: ")
		while idcliente not in stringlogClientes:
			idcliente = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'nome' or atributo == 'endereco' or atributo == 'cpf' or atributo == 'cnpj' or atributo == 'razaosocial':
			novo_valor = "'"+novo_valor+"'"
		if atributo == 'tipo':
			novo_valor = "'Pessoa {}'".format(novo_valor)

		updateQuery = """update cliente
		set {} = {}
		where idCliente = {};
		""".format(atributo, novo_valor, idcliente)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idcliente = input("Insira o id do cliente a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from cliente'

		if idcliente == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idcliente not in logClientes:
			try:
				idcliente = int(idcliente)
				print("O id de cliente inserido não consta no banco de dados.")
			except:
				print("O id de cliente inserido não é um número inteiro.")
				
		elif idCliente != '':
			deleteQuery = deleteQuery+" where idCliente = {};".format(idcliente)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log:
	logClientes = []
	instrucao = "select idcliente from cliente;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logClientes.append(elemento[0])

def tweakColaborador(opt):
	global logColaboradores, logSetores
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))
	stringlogSetores = []
	for st in logSetores:
		stringlogSetores.append(str(st))
	if opt == 'inserir':
		idcolaborador = str(len(logColaboradores)+1)

		if idcolaborador in stringlogColaboradores:
			idcolaborador = input("Insira o id do colaborador a ser adicionado: ")			

		while idcolaborador in stringlogColaboradores:
			idcolaborador = input("O id inserido já consta no banco de dados. Tente novamente: ")

		nome = input('Insira o nome do colaborador: ')
		nome = "'"+nome+"'"
		cpf = input("Insira o CPF do colaborador: ")
		cpf = "'"+cpf+"'"
		idsetor = input("Insira o id do setor do colaborador: ")
		while idsetor not in stringlogSetores:
			print('O id de setor inserido não consta no banco de dados.')
			opt = input("Você deseja cadastrar um novo setor [y/n]? ")
			if opt == 'y':
				tweakSetor('inserir')
				print("\nVoltando à inserção de colaborador:\n")
				idsetor = input("Insira o id do setor do colaborador: ")
			else:
				idsetor = input("Insira um id de setor existente para o colaborador: ")

		dataEntrada = input("Insira a data de entrada (formato AAAA-MM-DD): ")
		dataEntrada = "'"+dataEntrada+"'"
		dataSaida = 'null'
		especialidade = input("Insira a especialidade do colaborador: ")
		especialidade = "'"+especialidade+"'"
		salario = input("Insira o salário do colaborador: ")

		insertQuery = """insert into colaborador
		(idcolaborador, idSetor, DataEntrada, DataSaida, cpf, Nome, Especialidade, Salario)
		values
		({}, {}, {}, {}, {}, {}, {}, {});""".format(idcolaborador, idsetor, dataEntrada, dataSaida, cpf, nome, especialidade, salario)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idcolaborador = input("Insira o id do colaborador a ser atualizado: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'nome' or atributo == 'cpf' or atributo == 'especialidade' or atributo == 'DataEntrada' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update colaborador
		set {} = {}
		where idColaborador = {};
		""".format(atributo, novo_valor, idcolaborador)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idcolaborador = input("Insira o id do colaborador a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from colaborador'

		if idcolaborador == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idcolaborador not in stringlogColaboradores:
			try:
				idcolaborador = int(idcolaborador)
				print("O id de colaborador inserido não consta no banco de dados.")
			except:
				print("O id de colaborador inserido não é um número inteiro.")
				
		elif idcolaborador != '':
			deleteQuery = deleteQuery+" where idColaborador = {};".format(idcolaborador)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log:
	logColaboradores = []
	instrucao = "select idcolaborador from colaborador;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logColaboradores.append(elemento[0])

def tweakSetor(opt):
	global logColaboradores, logSetores
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))
	stringlogSetores = []
	for st in logSetores:
		stringlogSetores.append(str(st))
	if opt == 'inserir':
		idsetor = str(len(logSetores)+1)

		if idsetor in stringlogSetores:
			idsetor = input("Insira o id do setor a ser adicionado: ")			

		while idsetor in stringlogSetores:
			idsetor = input("O id inserido já consta no banco de dados. Tente novamente: ")

		nome = input('Insira o nome do setor: ')
		nome = "'"+nome+"'"
		idgestor = 'null'
		optGestor = input("O gestor desse setor já está cadastrado [y/n]?")
		if optGestor == 'y':
			idgestor = input('Insira o id do gestor do setor: ')

		salariobase = input("Insira o salário base do setor: ")
		descricao = input("Insira a descricao do setor: ")
		descricao = "'"+descricao+"'"

		insertQuery = """insert into setor
		(idSetor, idGestor, nome, descricao, salarioBase)
		values
		({}, {}, {}, {}, {});""".format(idsetor, idgestor, nome, descricao, salariobase)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idsetor = input("Insira o id do setor a ser atualizado: ")
		while idsetor not in stringlogSetores:
			idsetor = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'nome' or atributo == 'descricao' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update setor
		set {} = {}
		where idSetor = {}
		""".format(atributo, novo_valor, idsetor)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idsetor = input("Insira o id do setor a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from setor'

		if idsetor == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idsetor not in stringlogSetores:
			try:
				idsetor = int(idsetor)
				print("O id de setor inserido não consta no banco de dados.")
			except:
				print("O id de setor inserido não é um número inteiro.")
				
		elif idsetor != '':
			deleteQuery = deleteQuery+" where idSetor = {};".format(idsetor)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()
	# atualiza o log:
	logSetores = []
	instrucao = "select idsetor from setor;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logSetores.append(elemento[0])

def tweakAtividade(opt):
	global logAtividades
	stringlogAtividades = []
	for at in logAtividades:
		stringlogAtividades.append(str(at))
	
	if opt == 'inserir':
		idatividade = str(len(logAtividades)+1)

		if idatividade in stringlogAtividades:
			idatividade = input("Insira o id da atividade a ser adicionada: ")			

		while idatividade in stringlogAtividades:
			idatividade = input("O id inserido já consta no banco de dados. Tente novamente: ")

		tipo = input('Insira o tipo da atividade: ')
		tipo = "'"+tipo+"'"

		dataFim = 'null'
		dataInicio = input("Insira a data de início da atividade (formato AAAA-MM-DD): ")
		dataInicio = "'"+dataInicio+"'"
		
		descricao = input("Insira a descrição da atividade: ")
		descricao = "'"+descricao+"'"

		status = input("Insira o status da atividade: ")
		status = "'"+status+"'"

		insertQuery = """insert into atividade
		(idAtividade, tipo, DataInicio, DataFim, descricao, status)
		values
		({}, {}, {}, {}, {}, {});""".format(idatividade, tipo, dataInicio, dataFim, descricao, status)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idatividade = input("Insira o id da atividade a ser atualizada: ")
		while idatividade not in stringlogAtividades:
			idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'tipo' or atributo == 'dataInicio' or atributo == 'dataFim' or atributo == 'descricao' or atributo == 'status' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update atividade
		set {} = {}
		where idAtividade = {}
		""".format(atributo, novo_valor, idatividade)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idatividade = input("Insira o id da atividade a ser deletada (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from atividade'

		if idatividade == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idatividade not in stringlogAtividades:
			try:
				idatividade = int(idatividade)
				print("O id de atividade inserido não consta no banco de dados.")
			except:
				print("O id de atividade inserido não é um número inteiro.")
				
		elif idatividade != '':
			deleteQuery = deleteQuery+" where idAtividade = {};".format(idatividade)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log:
	logAtividades = []
	instrucao = "select idatividade from atividade;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logAtividades.append(elemento[0])

def tweakProjeto(opt): 
	global logProjetos
	stringlogProjetos = []
	for at in logProjetos:
		stringlogProjetos.append(str(at))
	
	if opt == 'inserir':
		idprojeto = str(len(logProjetos)+1)

		if idprojeto in stringlogProjetos:
			idprojeto = input("Insira o id do projeto a ser adicionado: ")			

		while idprojeto in stringlogProjetos:
			idprojeto = input("O id inserido já consta no banco de dados. Tente novamente: ")

		descricao = input("Insira a descrição do projeto: ")
		descricao = "'"+descricao+"'"

		plataforma = input('Insira o plataforma do projeto: ')
		plataforma = "'"+plataforma+"'"

		linguagem = input('Insira o linguagem do projeto: ')
		linguagem = "'"+linguagem+"'"

		dataFinal = 'null'
		dataInicio = input("Insira a data de início do projeto (formato AAAA-MM-DD): ")
		dataInicio = "'"+dataInicio+"'"
		estimativaDataFinal = input("Insira a data estimada para fim do projeto (formato AAAA-MM-DD): ")
		estimativaDataFinal = "'"+estimativaDataFinal+"'"

		insertQuery = """insert into projetoweb
		(idProjeto, descricao, plataforma, linguagem, datainicio, estimativadatafinal, datafinal)
		values
		({}, {}, {}, {}, {}, {}, {});""".format(idprojeto, descricao, plataforma, linguagem, dataInicio, estimativaDataFinal, dataFinal)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idprojeto = input("Insira o id do projeto a ser atualizado: ")
		while idprojeto not in stringlogProjetos:
			idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'plataforma' or atributo == 'dataInicio' or atributo == 'estimativaDataFinal' or atributo == 'descricao' or atributo == 'linguagem' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update projetoweb
		set {} = {}
		where idProjeto = {}
		""".format(atributo, novo_valor, idprojeto)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idprojeto = input("Insira o id do projeto a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from projetoweb'

		if idprojeto == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idprojeto not in stringlogProjetos:
			try:
				idprojeto = int(idprojeto)
				print("O id de projeto inserido não consta no banco de dados.")
			except:
				print("O id de projeto inserido não é um número inteiro.")
				
		elif idprojeto != '':
			deleteQuery = deleteQuery+" where idProjeto = {};".format(idprojeto)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

	# atualiza o log:
	logProjetos = []
	instrucao = "select idprojeto from projetoweb;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logProjetos.append(elemento[0])

def tweakPedido(opt): 
	global logPedidos, logClientes
	stringlogPedidos = []
	for pd in logPedidos:
		stringlogPedidos.append(str(pd))
	stringlogClientes = []
	for cl in logClientes:
		stringlogClientes.append(str(cl))
	if opt == 'inserir':
		idpedido = str(len(logPedidos)+1)

		if idpedido in stringlogPedidos:
			idpedido = input("Insira o id do pedido a ser adicionado: ")			

		while idpedido in stringlogPedidos:
			idpedido = input("O id inserido já consta no banco de dados. Tente novamente: ")

		idcliente = input("Insira o id do cliente que realizou o pedido: ")
		while idcliente not in stringlogClientes:
			idcliente = input("o id inserido não consta no banco de dados. Tente novamente: ")

		descricao = input("Insira a descricao do pedido: ")
		descricao = "'"+descricao+"'"

		insertQuery = """insert into pedido
		(idPedido, idCliente, descricao)
		values
		({}, {}, {});""".format(idpedido, idcliente, descricao)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idpedido = input("Insira o id do pedido a ser atualizado: ")
		while idpedido not in stringlogPedidos:
			idpedido = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'descricao' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update pedido
		set {} = {}
		where idPedido = {}
		""".format(atributo, novo_valor, idpedido)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização Realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idpedido = input("Insira o id do pedido a ser deletado (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from pedido'

		if idpedido == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idpedido not in stringlogPedidos:
			try:
				idpedido = int(idpedido)
				print("O id de pedido inserido não consta no banco de dados.")
			except:
				print("O id de pedido inserido não é um número inteiro.")
				
		elif idpedido != '':
			deleteQuery = deleteQuery+" where idPedido = {};".format(idpedido)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()
	# atualiza o log:
	logPedidos = []
	instrucao = "select idpedido from pedido;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logPedidos.append(elemento[0])

def tweakOrdemdeServico(opt):
	global logOrdens
	stringlogOrdens = []
	for od in logOrdens:
		stringlogOrdens.append(str(od))
	
	if opt == 'inserir':
		idordem = str(len(logOrdens)+1)

		if idordem in stringlogOrdens:
			idordem = input("Insira o id da ordem de serviço a ser adicionada: ")			

		while idordem in stringlogOrdens:
			idordem = input("O id inserido já consta no banco de dados. Tente novamente: ")

		orcamentoprevisto = input("Insira o orçamento previsto da ordem de serviço: ")
		valor = 0

		tiposervico = input("Insira o tipo do serviço: ")
		tiposervico = "'"+tiposervico+"'"

		insertQuery = """insert into OrdemDeServico
		(idOrdem, orcamentoprevisto, valor, tiposervico)
		values
		({}, {}, {}, {});""".format(idordem, orcamentoprevisto, valor, tiposervico)

		try:
			cursor.execute(insertQuery)
			connection.commit()
			print("\nInserção realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'atualizar':
		idordem = input("Insira o id da ordem de serviço a ser atualizada: ")
		while idordem not in stringlogOrdens:
			idordem = input("O id inserido não consta no banco de dados. Tente novamente: ")
		atributo = input("Insira o atributo a ser atualizado: ")
		novo_valor = input("Insira o novo valor do atributo: ")
		# adiciona aspas se atributo for varchar
		if atributo == 'tiposervico' and novo_valor != 'null':
			novo_valor = "'"+novo_valor+"'"

		updateQuery = """update ordemdeservico
		set {} = {}
		where idOrdem = {}
		""".format(atributo, novo_valor, idordem)

		try:
			cursor.execute(updateQuery)
			connection.commit()
			print("\nAtualização realizada com sucesso!\n")

		except Exception as err:
			imprimeErro(err)
			connection.rollback()

	elif opt == 'deletar':
		idordem = input("Insira o id da ordem de servico a ser deletada (deixar em branco caso deseje deletar todos): ")
		
		deleteQuery = 'delete from OrdemDeServico'

		if idordem == '':
			deleteQuery = deleteQuery+";"
			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()

		elif idordem not in stringlogOrdens:
			try:
				idordem = int(idordem)
				print("O id de ordem de serviço inserido não consta no banco de dados.")
			except:
				print("O id de ordem de serviço inserido não é um número inteiro.")
				
		elif idordem != '':
			deleteQuery = deleteQuery+" where idordem = {};".format(idordem)

			try:
				cursor.execute(deleteQuery)
				connection.commit()
				print("\nExclusão realizada com sucesso!\n")
				
			except Exception as err:
				imprimeErro(err)
				connection.rollback()
	# atualiza o log:
	logOrdens = []
	instrucao = "select idordem from ordemdeservico;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logOrdens.append(elemento[0])

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

def alteraGestor():
	global logSetores, logColaboradores
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))
	stringlogSetores = []
	for st in logSetores:
		stringlogSetores.append(str(st))

	idsetor = input("Insira o id do setor cujo gestor deve ser alterado: ")
	while idsetor not in stringlogSetores:
		idsetor = input("O id do setor não consta no banco de dados. Tente novamente: ")
	idgestor = input("Insira o id do novo gestor: ")
	while idgestor not in stringlogColaboradores:
		idgestor = input("O id do gestor não consta no banco de dados. Tente novamente: ")

	instrucao = "update setor set idgestor = {} where idsetor = {};".format(idgestor, idsetor)
	try:
		cursor.execute(instrucao)
		connection.commit()
		print("\nAlteração de gestor realizada com sucesso!\n")

	except Exception as err:
		imprimeErro(err)
		connection.rollback()

def finalizaProjeto():

	print("Quando um projeto é finalizado, é criada uma nota fiscal associada à ordem de serviço à qual ele pertence.")

	global logProjetos, logOrdens, logPedidos, logNotas
	stringlogProjetos = []
	for at in logProjetos:
		stringlogProjetos.append(str(at))
	stringlogPedidos = []
	for pd in logPedidos:
		stringlogPedidos.append(str(pd))
	stringlogOrdens = []
	for od in logOrdens:
		stringlogOrdens.append(str(od))
	stringlogNotas = []
	for nt in logNotas:
		stringlogNotas.append(str(nt))

	idprojeto = input("Insira o id do projeto a ser finalizado: ")
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")
	dataFinal = input("Insira a data de finalização do projeto (formato AAAA-MM-DD): ")
	dataFinal = "'"+dataFinal+"'"

	addDataFinal = """update projetoweb
	set datafinal = {}
	where idprojeto = {}""".format(dataFinal, idprojeto)

	try:
		cursor.execute(addDataFinal)
		print("\nData de finalização pode ser inserida.\n")
		instrucao = """select g.idordem
		from projetoweb as p, gera as g, ordemdeservico as ord
		where p.idprojeto = g.idprojeto 
		and g.idordem = ord.idordem
		and g.idprojeto = {};""".format(idprojeto)

		cursor.execute(instrucao)
		record = cursor.fetchone()
		if record == None:
			print("Esse projeto não foi associado com nenhuma ordem de serviço ou pedido, e, portanto, nenhuma nota fiscal foi gerada.")
			ordem = None
			connection.commit()
		else:
		 	ordem = record[0]

		if ordem!=None:
			idnota = len(logNotas)+1
			if idnota in stringlogNotas:
				idnota = input("Insira o id da nota fiscal a ser gerada: ")
			while idnota in stringlogNotas:
				idnota = input("O id inserido já consta no banco de dados. Tente novamente: ")
			valor= input('Insira o custo do projeto finalizado: ')
			criaNota = """insert into notafiscal
			(idnota, idordem, valortotal)
			values 
			({}, {}, {});""".format(idnota, ordem, valor)
			try:
				cursor.execute(criaNota)
				print("\nA nota fiscal pode ser criada.\n")

				atOrdem = """update ordemdeservico
				set valor = valor+{}
				where idordem = {}""".format(valor, ordem)
				try:
					cursor.execute(atOrdem)
					print("\nO valor da ordem de servico pode ser atualizado.\n")
					connection.commit()
					print("\nTodas as operações foram realizadas com sucesso!\n")

				except Exception as err:
					imprimeErro(err)
					connection.rollback()

			except Exception as err:
				imprimeErro(err)
				connection.rollback()
				
	except Exception as err:
		imprimeErro(err)
		connection.rollback()

	# atualiza o log:
	logNotas = []
	instrucao = "select idnota from notafiscal;"

	cursor.execute(instrucao)

	record = cursor.fetchall()

	for elemento in record:
		logNotas.append(elemento[0])

def informaSaida():
	global logColaboradores
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))

	idcolaborador = input("Insira o id do colaborador que saiu: ")
	while idcolaborador not in stringlogColaboradores:
		idcolaborador - input("O id inserido não consta no banco de dados. Tente novamente: ")
	dataSaida = input("Insira a data de saída do colaborador (formato AAAA-MM-DD): ")
	dataSaida = "'"+dataSaida+"'"
	infSaida = """update colaborador
	set dataSaida = {}
	where idcolaborador = {};""".format(dataSaida, idcolaborador)

	retiraSetor = """update colaborador
	set idSetor = null
	where idcolaborador = {}""".format(idcolaborador)

	try:
		cursor.execute(infSaida)
		cursor.execute(retiraSetor)
		connection.commit()
		print("\nInformação de saída de funcionário realizada com sucesso!\n")

	except Exception as err:
		imprimeErro(err)
		connection.rollback()

def finalizaAtividade():
	global logAtividades
	stringlogAtividades = []
	for at in logAtividades:
		stringlogAtividades.append(str(at))

	idatividade = input("Insira o id da atividade que está sendo encerrada: ")
	while idatividade not in stringlogAtividades:
		idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")

	dataFim = input("Insira a data de encerramento da atividade (formato AAAA-MM-DD): ")
	dataFim = "'"+dataFim+"'"

	encerraAtividade = """update atividade
	set dataFim = {}
	where idatividade = {}""".format(dataFim, idatividade)
	try:
		cursor.execute(encerraAtividade)
		connection.commit()
		print("\nFinalização de atividade realizada com sucesso!\n")

	except Exception as err:
		imprimeErro(err)
		connection.rollback()

def AtividadeColaborador():
	global logColaboradores, logAtividades
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))
	stringlogAtividades = []
	for at in logAtividades:
		stringlogAtividades.append(str(at))

	idatividade = input("Insira o id da atividade a ser atribuída: ")
	while idatividade not in stringlogAtividades:
		idatividade = input("O id inserido não consta no banco de dados. Tente novamente: ")

	verificaAtividade = """select * from atividade
	where idatividade = {} and datafim is not null;""".format(idatividade)

	cursor.execute(verificaAtividade)
	record = cursor.fetchone()
	if record == None:
		idcolaborador = input("Insira o id do colaborador a quem a atividade será atribuída: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")

		pegaData = """select datasaida
		from colaborador
		where idcolaborador = {};""".format(idcolaborador)
		cursor.execute(pegaData)
		record = execute.fetchone()

		if record == None:

			pegaData = """select dataentrada 
			from colaborador
			where idcolaborador = {};""".format(idcolaborador)
			cursor.execute(pegaData)
			record = execute.fetchone()
			dataEntradaColaborador = record
			dataEntrada = input("Insira a data de entrada do colaborador na atividade (formado AAAA-MM-DD): ")
			dataEntradadatetime = datetime.datetime.strptime(dataEntrada, '%Y-%m-%d')
			while dataEntradadatetime < dataEntradaColaborador: 
				print("Não foi possível fazer a atribuição, pois o colaborador não estava na empresa nessa data.")
				dataEntrada = input("Tente inserir uma data posterior: ")

			dataEntrada = "'"+dataEntrada+"'"
			insercao = """insert into possui (idColaborador, idAtividade, dataEntrada)
			values ({}, {}, {});""".format(idcolaborador, idatividade, dataEntrada)

			try:
				cursor.execute(insercao)
				connection.commit()
				print("\nAtribuição de atividade ao colaborador realizada com sucesso!\n")

			except Exception as err:
				imprimeErro(err)
				connection.rollback()
		else: print("O colaborador em questão já saiu da empresa. A atribuição não pode ser realizada.")


	else: 
		print("A atividade em questão já foi encerrada. A atribuição não pode ser realizada.")

def ProjetoColaborador():
	global logColaboradores, logProjetos
	stringlogColaboradores = []
	for col in logColaboradores:
		stringlogColaboradores.append(str(col))
	stringlogProjetos = []
	for pj in logProjetos:
		stringlogProjetos.append(str(pj))

	idprojeto = input("Insira o id do projeto a ser atribuído: ")
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")

	verificaProjeto = """select * from projeto
	where idprojeto = {} and datafinal is not null;""".format(idprojeto)

	cursor.execute(verificaProjeto)
	record = cursor.fetchone()
	if record == None:
		idcolaborador = input("Insira o id do colaborador a quem o projeto será atribuído: ")
		while idcolaborador not in stringlogColaboradores:
			idcolaborador = input("O id inserido não consta no banco de dados. Tente novamente: ")

		pegaData = """select datasaida 
		from colaborador
		where idcolaborador = {};""".format(idcolaborador)
		cursor.execute(pegaData)
		record = execute.fetchone()

		if record == None:

			insercao = """insert into desenvolve (idColaborador, idProjeto)
			values ({}, {});""".format(idcolaborador, idprojeto)

			try:
				cursor.execute(insercao)
				connection.commit()
				print("\nAtribuição do projeto ao colaborador realizada com sucesso!\n")

			except Exception as err:
				imprimeErro(err)
				connection.rollback()
		else: print("O colaborador em questão já saiu da empresa. A atribuição não pode ser realizada.")


	else: 
		print("O projeto em questão já foi encerrado. A atribuição não pode ser realizada.")

def ligaProjeto():
	global logProjetos, logPedidos, logOrdens
	stringlogPedidos = []
	for pd in logPedidos:
		stringlogPedidos.append(str(pd))
	stringlogProjetos = []
	for at in logProjetos:
		stringlogProjetos.append(str(at))
	stringlogOrdens = []
	for od in logOrdens:
		stringlogOrdens.append(str(od))

	idprojeto = input("Insira o id do projeto a ser atribuído: ")
	while idprojeto not in stringlogProjetos:
		idprojeto = input("O id inserido não consta no banco de dados. Tente novamente: ")


	idpedido = input("Insira o id do pedido a ser atribuído: ")
	while idpedido not in stringlogPedidos:
		idpedido = input("O id inserido não consta no banco de dados. Tente novamente: ")

	idordem = input("Insira o id da ordem de serviço a ser atribuída: ")
	while idordem not in stringlogOrdens:
		idordem = input("O id insetido não consta no banco de dados. Tente novamente: ")

	atribuicao = """insert into Gera (idprojeto, idordem, idpedido)
	values ({}, {}, {});""".format(idprojeto, idordem, idpedido)

	try:
		cursor.execute(atribuicao)
		connection.commit()
		print("\nAtribuição de projeto a pedido e ordem de serviço realizada com sucesso!\n")

	except Exception as err:
		imprimeErro(err)
		connection.rollback()

def getOut():
	cursor.close()
	connection.close()
	print('Execução finalizada.')
	sys.exit(1)

def getLogs():
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

	instrucao = "select idsetor from setor;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logSetores.append(elemento[0])

	instrucao = "select idatividade from atividade;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logAtividades.append(elemento[0])

	instrucao = "select idprojeto from projetoweb;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logProjetos.append(elemento[0])

	instrucao = "select idpedido from pedido;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logPedidos.append(elemento[0])

	instrucao = "select idordem from ordemdeservico;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logOrdens.append(elemento[0])

	instrucao = "select idnota from notafiscal;"
	cursor.execute(instrucao)
	record = cursor.fetchall()
	for elemento in record:
		logOrdens.append(elemento[0])

if __name__ == '__main__':
	getLogs()
	_main()
