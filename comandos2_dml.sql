insert into aluno (matricula,nome,telefone,cidade,email,idade) values(123,'MARIA',1199,'PELOTAS','maria@teste',20);

insert into aluno (matricula,nome,telefone,cidade,email,idade) values(123,'JOAO',45332,'PELOTAS','joao@teste',21);

insert into aluno (matricula,nome,telefone,cidade,email,idade) values(123,'JOSE',45332,'BAGE','jose@teste',22);

insert into aluno (matricula,nome,telefone,cidade,email,idade) values(123,'MARIA',1199,'PELOTAS','maria@teste',20);

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


insert into aluno values(201810420,'GABRIEL ZOPPO',null,null,'PELOTAS','gabriel.zoppo@sou.ucpel.edu.br',19);

insert into aluno values(201810763,'GUILHERME CARVALHO',991919191,null,null,'guilherme.carvalho@sou.ucpel.edu.br',null);

insert into aluno values(201810644,'GUILHERME BACCARIN',991010101,null,'PELOTAS','guilherme.baccarin@sou.ucpel.edu.br',null);

insert into aluno values(201810938,'HELENA TAVARES',991555555,null,'PELOTAS','helena.tavares@sou.ucpel.edu.br',null);

insert into aluno values(201810695,'ICARO SIQUEIRA',null,null,'SAO LOURENCO DO SUL','icaro.siqueira@sou.ucpel.edu.br',21);

insert into aluno values(201811057,'MATHEUS STIGGER',null,null,'SAO LOURENCO DO SUL','matheus.goncalves@sou.ucpel.edu.br',20);


insert into disciplina values(369084,'PROBABILIDADE E ESTATÍSTICA',60,123,8);

insert into disciplina values(369085,'SISTEMAS DE CONTROLE',60,123,8);

insert into disciplina values(369078,'SISTEMAS DIGITAIS I',60,123,7);

insert into disciplina values(369038,'PROGRAMAÇÃO ORIENTADA A OBJETOS',60,123,6);

insert into disciplina values(369066,'ARQUITETURA E ORGANIZAÇÃO DE COMPUTADORES',30,123,8);

insert into disciplina values(369072,'PROJETO INTEGRADOR V',30,123,8);


insert into departamento values(5468126,'pos grad','PPG');

insert into departamento values(5405621,'organizacao','ucp');


insert into funcionario values(1634650,'seguranca1','seg',6568,5405621,null,7465416);

insert into funcionario values(1634651,'secretario1','sec',7834,5405621,null,7465416);

insert into funcionario values(1634652,'faxineiro1','faxi',5667,5405621,null,7465416);

insert into funcionario values(1634652,'professor1','prof',6453,5468126,null,7465416);


insert into matricula values(201810420,369084,null);

insert into matricula values(201810763,369085,null);

insert into matricula values(201810644,369078,null);

insert into matricula values(201810938,369038,null);

insert into matricula values(201810695,369066,null);

insert into matricula values(201811057,369072,null);

#############################################################################

select * from funcionario;

select nome, matricula from aluno;

select nome, cod as codigo, salario , (salario + (salario/10)) as novoSalario from funcionario;

select distinct sigla from departamento;


select distinct descricao as nomeDepartamento, sigla as codigoReduzido from departamento;

select distinct idade from aluno;

select matricula,nome,idade,(idade + 2) as provavel_idade_formando from aluno;

select concat("Aluno: ", nome, " nascido em: ", dtaNascimento, " com idade aproximada de: ", (idade + 5)) from aluno;