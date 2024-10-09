-- Criado o banco de dados. --
drop database Connected_Barber;
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
create table tabela_endereco (
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


-- Criação da tabela das barbearias. -- 
create table tabela_barbearias (
	id int(10) not null auto_increment,
	nome varchar(100) not null,
	fk_endereco int(10) not null, -- chave estrangeira para a tabela de endereco --
	fk_portfolio int(10) not null, -- chave estrangeira para o endereco de seu portfólio --
	primary key (id),
	foreign key (fk_endereco) references tabela_endereco(id)
);


-- Criação da tabela dos usuários. --
-- Conterá informação de todos os usuários, clientes, funcionários, adminsitradores... --
create table tabela_usuarios (
	email varchar(100) not null,
	senha varchar(16) not null,
	nome varchar(100) not null,
	data_de_nascimento date not null,
	telefone varchar(12) not null,
	nivel enum('cliente', 'funcionário', 'administrador') not null,
	primary key (email)
);


-- Organização para criação da tabela de clientes. --
create table tabela_clientes (
	fk_usuario varchar(100) not null,
	CEP int(8) not null,
	primary key (fk_usuario),
	foreign key (fk_usuario) references tabela_usuarios(email)
);


create table tabela_preferencias (
	id int(10) not null auto_increment,
	descricao varchar(500) not null,
	fk_cliente varchar(100) not null,
	primary key (id),
	foreign key(fk_cliente) references tabela_clientes(fk_usuario)
);


-- Orgganização da tabela de funcionários. --
create table tabela_funcionarios (
	fk_usuario varchar(100) not null,
	fk_portfolio int(10) not null,
	fk_barbearia int(10) not null,
	primary key (fk_usuario),
	foreign key (fk_usuario) references tabela_usuarios(email),
	foreign key (fk_barbearia) references tabela_barbearias(id)
);


-- Criação das tabelas de servicos e produtos. --
create table tabela_oferecimentos (
	id int(10) not null auto_increment,
	fk_barbearia int(10) not null,
	nome varchar(100) not null,
	descricao varchar(500) not null,
	preco float(10) not null,
	primary key (id),
	foreign key (fk_barbearia) references tabela_barbearias(id)
);

create table tabela_fotos_oferecimento (
	fk_oferecimento int(10) not null,
	endereco varchar(100) not null,
	primary key (fk_oferecimento),
	foreign key (fk_oferecimento) references tabela_oferecimentos(id)
);

create table tabela_produtos (
	fk_oferecimento int(10) not null,
	marca varchar(100) not null,
	validade date not null,
	primary key (fk_oferecimento),
	foreign key (fk_oferecimento) references tabela_oferecimentos(id)
);

create table tabela_servicos (
	fk_oferecimento int(10) not null,
	duracao int(3) not null,
	primary key (fk_oferecimento),
	foreign key (fk_oferecimento) references tabela_oferecimentos(id)
);


-- Criação da tabela que armazenará a informação dos portfólios. --
create table tabela_portfolios_barbearia (
	id int(10) not null auto_increment,
	fk_barbearia int(10) not null,
	descricao varchar(500) not null,
	primary key (id),
	foreign key (fk_barbearia) references tabela_barbearias(id)
);
create table tabela_fotos_barbearia (
	id int(10) not null auto_increment,
	fk_portfolio int(10) not null,
	endereco varchar(100) not null,
	primary key (id),
	foreign key (fk_portfolio) references tabela_portfolios_barbearia(id)
);


create table tabela_portfolios_funcionario (
	id int(10) not null auto_increment,
	fk_funcionario varchar(100) not null,
	descricao varchar(500) not null,
	primary key (id),
	foreign key (fk_funcionario) references tabela_funcionarios(fk_usuario)
);
create table tabela_fotos_funcionario (
	id int(10) not null auto_increment,
	fk_portfolio int(10) not null,
	endereco varchar(100) not null,
	primary key (id),
	foreign key (fk_portfolio) references tabela_portfolios_funcionario(id)
);


-- Criação da tabela de agendamentos --
create table tabela_agendamentos (
	id int(100) not null auto_increment,
	fk_cliente varchar(100) not null,
	fk_funcionario varchar(100) not null,
	fk_servico int(10) not null,
	situacao enum('pendente', 'cancelado', 'concluido', 'marcado') not null,
	primary key (id),
	foreign key (fk_funcionario) references tabela_funcionarios(fk_usuario),
	foreign key (fk_cliente) references tabela_clientes(fk_usuario),
	foreign key (fk_servico) references tabela_servicos(fk_oferecimento)
);


-- Definição de chaves estrangeiras que não puderam ser feitas durante a criação da tabela (ou não). --
-- funcionário com seu portfólio. --
alter table tabela_funcionarios add constraint tabela_funcionarios.fk_portfolio foreign key tabela_funcionarios(fk_portfolio) references tabela_portfolios_funcionario(id);
-- barbearia com seu portfólio. --
alter table tabela_barbearias add constraint tabela_barbearias.fk_portfolio foreign key tabela_barbearias(fk_portfolio) references tabela_portfolios_barbearia(id);
