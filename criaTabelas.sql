create table Atividade(
idAtividade integer,
Tipo varchar(100),
DataInicio date,
DataFim date,
Descricao varchar(1000),
Status varchar(100));

alter table atividade add constraint pk_atividade primary key (idAtividade);

create table OrdemDeServico(
idOrdem integer,
OrcamentoPrevisto float,
Valor float,
TipoServico varchar(1000));

alter table OrdemDeServico add constraint pk_ordemdeservico primary key (idOrdem);

create table NotaFiscal(
idNota integer,
idOrdem integer;
valorTotal float);

alter table NotaFiscal add constraint fk_notafiscal foreign key (idOrdem) references OrdemDeServico (idOrdem);

alter table NotaFiscal add constraint pk_notafiscal primary key (idNota);

create table Colaborador(
idColaborador integer,
idSetor integer,
DataEntrada date,
DataSaida date,
cpf varchar(11),
Nome varchar(100),
Especialidade varchar(1000),
Salario float);

alter table Colaborador add constraint pk_colaborador primary key (idColaborador);

create table Setor(
idSetor integer,
Nome varchar(100),
Descricao varchar(1000),
idGestor integer,
SalarioBase float);

alter table Setor add constraint pk_setor primary key (idSetor);

alter table Colaborador add constraint fk_colaborador foreign key (idSetor) references Setor (idSetor);
alter table Setor add constraint fk_setor_gestor foreign key (idGestor) references Colaborador (idColaborador);

create table Possui(
idColaborador integer,
idAtividade integer,
DataEntrada date);

alter table Possui add constraint fk_possui_colaborador foreign key (idColaborador) references Colaborador (idColaborador);
alter table Possui add constraint fk_possui_atividade foreign key (idAtividade) references Atividade (idAtividade);
alter table Possui add constraint pk_possui primary key (idColaborador, idAtividade);

create table ProjetoWeb(
idProjeto integer,
Descricao varchar(1000),
Plataforma varchar(1000),
Linguagem varchar(100),
DataInicio date,
EstimativaDataFinal date,
DataFinal date);

alter table ProjetoWeb add constraint pk_projetoweb primary key (idProjeto); 

create table Desenvolve(
idColaborador integer,
idProjeto integer);

alter table Desenvolve add constraint fk_desenvolve_colaborador foreign key (idColaborador) references Colaborador (idColaborador);
alter table Desenvolve add constraint fk_desenvolve_projeto foreign key (idProjeto) references ProjetoWeb (idProjeto);
alter table Desenvolve add constraint pk_desenvolve primary key (idColaborador, idProjeto);

create table Cliente(
idCliente integer,
Tipo varchar(100),
Endereco varchar(1000),
cpf varchar(11),
Nome varchar(100),
CNPJ varchar(14),
RazaoSocial varchar(100));

alter table Cliente add constraint pk_cliente primary key (idCliente);

create table Pedido(
idPedido integer,
idCliente integer,
Descricao varchar(1000));

alter table Pedido add constraint fk_pedido foreign key (idCliente) references Cliente (idCliente);
alter table Pedido add constraint pk_pedido primary key (idPedido);

create table Gera(
idProjeto integer,
idOrdem integer,
idPedido integer);

alter table Gera add constraint fk_gera_projeto foreign key (idProjeto) references ProjetoWeb (idProjeto);
alter table Gera add constraint fk_gera_ordem foreign key (idOrdem) references OrdemDeServico (idOrdem);
alter table Gera add constraint fk_gera_pedido foreign key (idPedido) references Pedido (idPedido);
alter table Gera add constraint pk_gera primary key (idProjeto);