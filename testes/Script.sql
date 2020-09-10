alter table aluno add primary key (matricula);

select * from ucpel.aluno;

create table aluno (
	matricula numeric (10),
	nome varchar (200),
	telefone numeric (10),
	dtaNascimento timestamp,
	cidade varchar (100),
    email varchar(100),
    idade numeric (3),
    primary key(matricula)
);


create table disciplina(
	cod numeric (10),
	nome varchar (200),
	cargaHoraria numeric (3),
    turma numeric (4),
    numero_alunos numeric (4),
    primary key(cod)
);


create table matricula (
	matriculaaluno numeric (10),
	cod_disciplina numeric (10),
    dtefetivado timestamp,
    primary key(matriculaaluno, cod_disciplina)
    #foreign key(cod_disciplina) references disciplina (cod) 
);


create table departamento(
	cod numeric (10),
	descricao varchar (500),
    sigla varchar (25),
    primary key(cod)
);


create table funcionario(
	cod numeric (10),
	nome varchar (200),
	cargo varchar (100),
	salario numeric (6),
    coddepartamento numeric (10),
    dtcontratacao timestamp,
	codgerente numeric (10),
    primary key(cod)
);