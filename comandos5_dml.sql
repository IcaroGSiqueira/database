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
	cod int auto_increment primary key,
	menor int(3),
	maior int(3),
	nivel char(2),
	foreign key (matriculaaluno) references aluno (matricula)
);

-- insert into faixaNivel(nivel,matriculaaluno) select 'A', matricula  from aluno where idade between 15 and 20;
-- insert into faixaNivel(nivel,matriculaaluno) select 'B', matricula from aluno where idade between 21 and 25;
-- insert into faixaNivel(nivel,matriculaaluno) select 'C', matricula from aluno where idade between 26 and 30;
-- insert into faixaNivel(nivel,matriculaaluno) select 'D', matricula from aluno where idade between 31 and 100;

select aluno.nome, faixaNivel.nivel from aluno left join faixaNivel where aluno.idade BETWEEN menor, maior order by nivel;

-- D.
select disciplina.nome , count(aluno.matricula) from disciplina right join matricula on disciplina.cod = matricula.cod_disciplina 
left join aluno on matricula.matriculaaluno = aluno.matricula 
group by matricula.cod_disciplina
order by matricula.cod_disciplina;

-- D
select disciplina.cod ,disciplina.nome, coalesce(count(aluno.matricula),0) n_alunos from disciplina left join matricula on matricula.cod_disciplina = disciplina.cod 
left join aluno on aluno.matricula = matricula.matriculaaluno 
group by disciplina.cod 
order by disciplina.cod;

-- E.
select aluno.nome, disciplina.nome from aluno right join matricula on aluno.matricula = matricula.matriculaaluno 
left join disciplina on matricula.cod_disciplina = disciplina.cod 
group by matricula.matriculaaluno 
order by matricula.matriculaaluno;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 01
select funcionario.nome , coalesce(gerente.nome," Sem gerente ") gerente from funcionario left join gerente on gerente.codgerente = funcionario.cod_gerente;

-- 02
select funcionario.nome, funcionario.nome from aluno union all
select funcionario.nome from funcionario;

-- 03
select aluno.nome from aluno union
select funcionario.nome from funcionario;

-- 04
select concat(aluno.nome , " está matriculado em: ", coalesce(disciplina.nome,"Nenhuma disciplina ")) from aluno 
left join matricula on matricula.matriculaaluno = aluno.matricula 
left join disciplina on disciplina.cod = matricula.cod_disciplina;

-- 05
select concat("insert into aluno (nome,telefone,cidade,email,idade) values (", aluno.nome, " ," ,
aluno.telefone, " ,", aluno.cidade, " ," ,aluno.email, " ,", aluno.cidade, ");")
from aluno union all 
select concat("insert into funcionario (nome,cargo,salario,coddepartamento,cod_gerente) values(",funcionario.nome," ,",funcionario.cargo," ,",funcionario.salario," ,",
funcionario.coddepartamento, ");")
from funcionario;


