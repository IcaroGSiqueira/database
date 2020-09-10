create table aluno (
	matricula int(10) auto_increment not null,
	nome varchar (200) not null,
	telefone numeric (10),
	dtaNascimento date,
	cidade varchar (100) default null,
    email varchar(100) unique,
    idade numeric (3),
    primary key(matricula)
);


create table disciplina(
	cod int(10) auto_increment not null,
	nome varchar (200) not null,
	cargaHoraria numeric (3) default 30,
    turma numeric (4),
    numero_alunos numeric (4),
    primary key(cod)
);


create table matricula (
	matriculaaluno int(10),
	cod_disciplina int(10),
    dtefetivado timestamp,
    foreign key(matriculaaluno) references aluno (matricula), 
    foreign key(cod_disciplina) references disciplina (cod) 
);


create table departamento(
	cod int(10) auto_increment not null,
	descricao varchar (500),
    sigla varchar (25),
    primary key(cod)
);


create table funcionario(
	cod int(10) auto_increment not null,
	nome varchar (200) not null,
	cargo varchar (100),
	salario numeric (6),
    coddepartamento int(10),
    dtcontratacao timestamp,
	codgerente int(10),
    primary key(cod),
    foreign key(coddepartamento) references departamento (cod),
    foreign key(codgerente) references funcionario (cod) 
);