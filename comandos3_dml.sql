select * from ucpel.aluno where telefone is null;

select * from ucpel.aluno;
update aluno set idade = (idade + 1) where dtaNascimento >= '2010-08-20 20:59:13';

select * from ucpel.disciplina;
SET SQL_SAFE_UPDATES = 0; update disciplina set cargaHoraria = 60; SET SQL_SAFE_UPDATES = 1;

select * from ucpel.funcionario where salario >= 800;

select nome, coddepartamento from funcionario where cod = 459;

select nome, salario from funcionario where salario between 950.00 and 2300.00;

##################################################################################

select nome, cargo, dtcontratacao from funcionario where dtcontratacao between '2004-02-20 00:00:00' and '2007-05-01 00:00:00';

select nome, coddepartamento from funcionario where coddepartamento in(10,30) order by nome;

select nome as 'Funcionario', salario as 'Salario do mes' from funcionario where coddepartamento in(10,30) and salario > 1500;

select nome, dtcontratacao from funcionario where dtcontratacao between '2004-01-01 00:00:00' and '2004-31-12 23:59:59';

##################################################################################

select nome, cargo from funcionario where codgerente is null;

select nome from funcionario where nome like '_A%';

select * from funcionario where nome like '%A%A%' and departamento = 30 or codgerente = 7529 order by coddepartamento desc;

update funcionario set salario = (salario + 300) where salario < 700;

update funcionario set salario = (salario + 300) where coddepartamento = 20;
