select funcionario.nome, departamento.descricao from funcionario left join departamento on coddepartamento = funcionario.cod;

select funcionario.cargo from funcionario right join departamento on departamento.cod = funcionario.coddepartamento 
where departamento.sigla like "CTB";

select count(aluno.matricula) from matricula inner join aluno on matricula.matriculaaluno = aluno.matricula 
group by matricula.cod_disciplina
order by matricula.cod_disciplina;

select funcionario.nome, departamento.descricao from funcionario left join departamento on funcionario.coddepartamento = departamento.cod
where funcionario.nome like "%A%";

select funcionario.* from funcionario left join departamento on departamento.cod = funcionario.coddepartamento
where funcionario.salario > 1500; 
-- and departamento.cidade like "Rio de Janeiro";

select aluno.nome, sum(disciplina.cargaHoraria) from aluno left join matricula on matricula.matriculaaluno = aluno.matricula 
left join disciplina on disciplina.cod = matricula.cod_disciplina 
group by aluno.nome;


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- A.
SELECT departamento.descricao , departamento.sigla, count(funcionario.cod) nFuncionarios, avg(funcionario.salario) mediaSalario FROM departamento 
left join funcionario on funcionario.coddepartamento = departamento.cod group by departamento.cod ;

-- B.

-- C.
create table faixaNivel(
	id int auto_increment primary key,
	nome varchar(200),
	nivel char(2)
);
insert into faixaNivel(nome,nivel) select nome, 'A' from aluno
where idade between 15 and 20;
insert into faixaNivel(nome,nivel) select nome, 'B' from aluno
where idade between 21 and 25;
insert into faixaNivel(nome,nivel) select nome, 'C' from aluno
where idade between 26 and 30;
insert into faixaNivel(nome,nivel) select nome, 'D' from aluno
where idade between 31 and 100;
select nome, nivel from faixaNivel;

-- D.
select disciplina.nome , count(aluno.matricula) from disciplina right join matricula on disciplina.cod = matricula.cod_disciplina 
left join aluno on matricula.matriculaaluno = aluno.matricula 
group by matricula.cod_disciplina
order by matricula.cod_disciplina;

-- E.
select aluno.nome, disciplina.nome from aluno right join matricula on aluno.matricula = matricula.matriculaaluno 
left join disciplina on matricula.cod_disciplina = disciplina.cod 
group by matricula.matriculaaluno 
order by matricula.matriculaaluno;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Faça retornar o nome do gerente e o nome do funcionário O funcionario que não possuir gerente deve aparecer também.
-- Faça uma consulta que retorne os nomes dos funcionários e os nomes dos alunos, ordenados de forma decrescente. Os nomes duplicados devem aparecer
-- A mesma consulta acima, sem duplicar nomes.
-- Faça retornar na mesma coluna o nome do aluno e o nome da disciplina sem repetições de nomes.
-- Faça um único select, que reproduza os inserts existentes nas tabelas Funcionário e Aluno, gerando o resultado no formato de script para ser executado em outra base de dados.


select funcionario.nome ,  from disciplina right join matricula on disciplina.cod = matricula.cod_disciplina 
left join aluno on matricula.matriculaaluno = aluno.matricula 
group by matricula.cod_disciplina
order by matricula.cod_disciplina;


