-- Criado o banco de dados. --
-- drop database Connected_Barber; --
create database Connected_Barber;
use Connected_Barber;


-- Tabelas contendo os países do mundo e estados e cidades do brasil. --
-- Criação da tabela de países. --
create table tabela_paises (
	id int(10) not null auto_increment,
	nome varchar(100) not null,
	primary key (id)
);
-- A FAZER: INSERIR TODOS OS PAÍSES EXISTENTES NESSA TABELA. --


-- Criação da tabela de estados. --
create table tabela_estados (
	id int(10) not null auto_increment,
	fk_pais int(10) not null,	
	nome varchar(18) not null,
	primary key (id),
	foreign key (fk_pais) references tabela_paises(id)
);
-- A FAZER: INSERIR TODOS OS ESTADOS BRASILEIROS NESSA TABELA. --


-- Criação da tabela de cidades. --
create table tabela_cidades (
	id int(10) not null auto_increment,
	nome varchar(100) not null,
	fk_estado int(10) not null,
	primary key (id),
	foreign key (fk_estado) references tabela_estados(id)
);
-- A FAZER: INSERIR TODAS AS CIDADES BRASILEIRAS NESSA TABELA. --


-- Criação da tabela do endereço. --
-- Contém as informações do endereço da respectiva barbearia. --
create table tabela_enderecos (
	id int(10) not null auto_increment,
	fk_pais int(10) not null,
	fk_estado int(10) not null,
	fk_cidade int(10) not null,
	CEP int(8) not null,
	complemento varchar(500) not null,
	primary key(id),
	foreign key(fk_pais) references tabela_paises(id),
	foreign key(fk_estado) references tabela_estados(id),
	foreign key(fk_cidade) references tabela_cidades(id)
);


-- Criação da tabela portfólios. --
create table tabela_portfolios (
	id int(10) not null auto_increment,
	descricao varchar(500) not null,
	primary key (id)
);

-- Tabela que vai guardar o endereço das fotos de todos os seres do sistema. --
-- Barbearias, Funcionários, Produtos e Serviços. --
create table tabela_fotos (
	id int(15) not null auto_increment,
	endereco varchar(500) not null,
	fk_portfolio int(10) not null,
	primary key (id),
	foreign key (fk_portfolio) references tabela_portfolios(id)
);


-- Criação da tabela das barbearias. -- 
create table tabela_barbearias (
	nome varchar(100) not null,
	fk_endereco int(10) not null, -- chave estrangeira para a tabela de endereco --
	fk_portfolio int(10) not null, -- chave estrangeira para o endereco de seu portfólio --
	primary key (nome),
	foreign key (fk_endereco) references tabela_enderecos(id),
	foreign key (fk_portfolio) references tabela_portfolios(id)
);


-- Criação da tabela dos usuários. --
-- Conterá informação de todos os usuários, clientes, funcionários, adminsitradores... --
-- separados pelo campo nível. --
create table tabela_usuarios (
	email varchar(100) not null,
	senha varchar(16) not null,
	nome varchar(100) not null,
	data_de_nascimento date not null,
	telefone varchar(12) not null,
	cep varchar(8) not null,
	nivel enum('cliente', 'funcionário', 'administrador') not null,
	primary key (email)
);


-- Organização para criação da tabela de clientes. --
create table tabela_preferencias (
	id int(10) not null auto_increment,
	descricao varchar(500) not null,
	fk_cliente varchar(100) not null,
	primary key (id),
	foreign key(fk_cliente) references tabela_usuarios(email)
);


-- Orgganização da tabela de funcionários. --
create table tabela_funcionarios (
	fk_usuario varchar(100) not null,
	fk_portfolio int(10) not null,
	fk_barbearia varchar(100) not null,
	primary key (fk_usuario),
	foreign key (fk_usuario) references tabela_usuarios(email),
	foreign key (fk_barbearia) references tabela_barbearias(nome)
);


-- Criação das tabelas de servicos e produtos. --
create table tabela_produtos (
	id int(10) not null auto_increment,
	fk_barbearia varchar(100) not null,
	nome varchar(100) not null,
	preco float(8) not null,
	marca varchar(100) not null,
	validade date not null,
	fk_info int(10) not null, -- contém as fotos e descricao do produto --
	primary key (id),
	foreign key (fk_barbearia) references tabela_barbearias(nome),
	foreign key (fk_info) references tabela_portfolios(id)
);
create table tabela_servicos (
	id int(10) not null auto_increment,
	fk_barbearia varchar(100) not null,
	nome varchar(100) not null,
	preco float(8) not null,
	tempo_estimado int(5) not null, -- em minutos --
	fk_info int(10) not null,
	primary key (id),
	foreign key (fk_barbearia) references tabela_barbearias(nome),
	foreign key (fk_info) references tabela_portfolios(id)
);


-- Criação da tabela de agendamentos --
create table tabela_agendamentos (
	id int(100) not null auto_increment,
	fk_cliente varchar(100) not null,
	fk_funcionario varchar(100) not null,
	fk_servico int(10) not null,
	data date not null,
	situacao enum('pendente', 'cancelado', 'concluido', 'marcado') not null,
	primary key (id),
	foreign key (fk_funcionario) references tabela_funcionarios(fk_usuario),
	foreign key (fk_cliente) references tabela_usuarios(email),
	foreign key (fk_servico) references tabela_servicos(id)
);
