#create database ucpel;

use ucpel;

create table aluno (
	matricula numeric (6),
	nome varchar (200),
	telefone numeric (10),
	dtaNascimento timestamp,
	cidade varchar (100)
);

alter table aluno add column email varchar(100);

alter table aluno add column idade numeric (3);



create table disciplina(
	cod numeric (6),
	nome varchar (200),
	cargaHoraria numeric (3)
);

alter table disciplina add column turma numeric (4);

alter table disciplina add column numero_alunos numeric (4);



create table matricula (
	matricula numeric (6),
	cod_disciplina numeric (6)
);

alter table matricula add column dtefetivado timestamp;



create table departamento(
	cod numeric (6),
	descricao varchar (500)
);

alter table departamento add column sigla varchar (25);



create table funcionario(
	cod numeric (6),
	nome varchar (200),
	cargo varchar (100),
	salario numeric (6),
    coddepartamento numeric (3)
);

alter table funcionario add column dtcontratacao timestamp;

alter table funcionario add column codgerente numeric (6);


drop table aluno;
drop table matricula;
drop table disciplina;
drop table funcionario;
drop table departamento;