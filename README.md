# Trabalho Final Banco de Dados 2020.1

## Integrantes:

Augusto Scarduelli Prudencio (18102140)

Horizonte Nazarete Magalhães Junior (17202046)

Milena Seibert Fernandes (18102152)

## Descrição do desenvolvimento:

Linguagem: Python 3.6.9

Driver: Psycopg2 2.7.4

Fornecedor de Bando de Dados: PostgreSQL

## Descrição do funcionamento:

Estabelecendo a conexão por 

connection = psycopg2.connect(user="", password = "", port = "", database = "")

Cursor utilizado para a execução de comandos:

cursor = connection.cursor()

#### No caso de consultas: 

cursor.execute(consulta)

resultado = crusor.fetchall() ou cursor.fetchone()

#### No caso de operações (insert, update, delete):

cursor.execute(operação)

try:

  cursor.commit()
  
exept:

  cursor.rollback()
  
## Outros módulos utilizados:

- *sys* para terminar a execução do programa.

- *datetime* para comparar e processar datas.

- *tabulate* para tornar a visualização das tabelas mais atrativa.

- *matplotlib.pyplot* para gerar os gráficos de barra das consultas realizadas.

## Descrição das funções:

#### [1]: Inserir Tupla(s) e Dados

> Permite inserir uma tupla de dados em uma tabela do banco de dados. Isso pode ser feito com: Cliente, Colaborador, Setor, Atividade, Pedido, OrdemdeServico, e ProjetoWeb.

#### [2]: Atualizar Atributos

> Permite atualizar o valor de um atributo de uma tupla de uma tabela, determinada pelo seu id único (chave primária), e o atributo em questão e o seu novo valor devem ser inseridos pelo usuário. Isso pode ser feito com: Cliente, Colaborador, Setor, Atividade, Pedido, ProjetoWeb e OrdemdeServiço.

#### [3]: Deletar Tuplas

> Permite deletar uma tupla de uma tabela determinada. A tupla é escolhida a partir da sua chave primária. Isso pode ser feito com: Cliente, Colaborador, Setor, Atividade, Pedido, ProjetoWeb e OrdemdeServiço.

#### [4]: Alterar Gestor

> Atualiza o atributo idGestor da tabela Setor, adicionando ou atualizando o valor, um id de um colaborador. Vale atentar que um setor pode ser cadastrado sem gestor, mas um colaborador não pode ser cadastrado sem um setor. Sendo assim, durante a inserção de um colaborador, existe a opção da criação de um setor no meio dessa operação.

#### [5]: Finalizar Projeto

> Atualiza o atributo DataFinal da tabela ProjetoWeb, identificado a partir do seu id. Além disso, verifica se o projeto está associado a uma instância de OrdemDeServico. Em caso afirmativo, é solicitado o valor do pedido, gerado uma linha em NotaFiscal com esse valor como ValorTotal, que é associada à ordem de serviço em questão. Por fim, ao atributo Valor da ordem de serviço é incrementado o valor inserido do projeto finalizado. Após essa ação, não se pode mais atribuir esse projeto a colaboradores.

#### [6]: Informar Saída de Colaborador

> Atualiza o atributo DataSaida de um colaborador, identificado a partir do seu id. Após essa operação, a esse colaborador não se pode mais atribuir projetos e/ou atividades. Em adição, o id do setor do gestor passa a ser null.

#### [7]: Finalizar Atividade

> Atualiza o valor do atributo DataFim da tabela Atividade, e automaticamente muda o seu status para 'Terminado'.

#### [8]: Atribuir Atividade a Colaborador

> Adiciona uma linha à tabela Possui, que associa as tabelas Colaborador e Atividade, solicitando, além dos ids do colaborador e da atividade em questão, uma data de entrada do colaborador na atividade. Vale ressaltar que a operação de inserção só é realizada caso a data de entrada do colaborador na empresa seja anterior à data de entrada do colaborador na atividade. Em adição, é também verificado se o colaborador já não saiu da empresa nessa data de atribuição.

#### [9]: Atribuir Projeto a Colaborador

>  Adiciona uma linha à tabela Desenvolve, que associa as tabelas Colaborador e ProjetoWeb, solicitando os ids do colaborador e do projeto em questão. Vale ressaltar que a operação só é realizada caso o projeto em questão ainda não tenha sido finalizado. Em adição, caso o colaborador já tenha saído da empresa, essa operação também não pode ser realizada.

#### [10]: Atribuir Projeto(s) a Pedido e Ordem de Serviço

> Adiciona uma linha à tabela Gera, que associa as tabelas ProjetoWeb, OrdemdeServico e Pedido, solicitando os ids do Projeto, Ordem de Serviço e Pedido em questão.

#### [11]: Realizar Consultas e Obter Gráficos

> Permite a realização das consultas elaboradas e, além de mostrar o resultado da consulta em uma tabela, gera também o gráfico de barras da mesma com o uso do módulo *matplotlib*.

#### [12]: Ver Tabelas

> Permite a visualização de todos os atributos de todas as linhas de todas as tabelas que constam no Bando de Dados. É aberto um menu de visualização em que uma única tabela por vez deve ser selecionada para a visualização.

#### [13]: Sair

> Fecha o cursor, bem como a conexão com o banco de dados, e encerra a execução do programa com o uso do módulo *sys*.

## Observações:

- Em cada operação, seja de inserção, deleção ou atualização, é perguntado ao usuário se ele deseja ver os dados que já constam no banco de dados. Em caso afirmativo, as tabelas relevantes para aquela operação são apresentadas.

- O programa usa variáveis logs que guardam as chaves primárias de algumas tabelas que já constam no banco de dados. Isso é feito para que a disponibilidade de uma id possa ser verificada antes da sua inserção no banco de dados. Além disso, também é verificada a sua existência antes de uma atualização ou deleção.

