CREATE or replace view v_funcionario as select funcionario.cod, funcionario.nome, departamento.descricao 
FROM ucpel.funcionario inner join departamento on funcionario.coddepartamento = departamento.cod order by 2;

-- -----------------------------------------------------------------------------------------------------------

-- Crie uma tabela faixaNivel, onde os alunos com idade de 15 à 20 são nível A, 21 à 25 nível B, 25 à 30 nível C e acima nível D. Crie uma View no qual a consulta informa a matricula do aluno, o nome do aluno e o nível em que ele se encontra.

-- Faça uma consulta utilizando a View acima, com as tabelas matricula e disciplina, informando o nome do aluno, o nome da disciplina que ele esta matriculado e o nível que ele se encontra.

-- Baseado nas consultas acima, faça uma nova consulta que informe o total de alunos matriculados por disciplinas e agrupados por nível. Ordenado por disciplina e em seguida por nível. Algo tipo:


CREATE or REPLACE view v_nivelAluno as select aluno.matricula, aluno.nome, faixaNivel.nivel 
FROM ucpel.aluno inner join faixaNivel on aluno.matricula = faixaNivel.matriculaaluno order by 3;

select aluno.nome, disciplina.nome, faixaNivel.nivel 
from aluno left join faixaNivel on faixaNivel.matriculaaluno = aluno.matricula 
left join matricula on matricula.matriculaaluno = faixaNivel.matriculaaluno left join disciplina on disciplina.cod = matricula.cod_disciplina order by nivel;

select disciplina.nome , count(aluno.matricula) from disciplina right join matricula on disciplina.cod = matricula.cod_disciplina 
left join aluno on matricula.matriculaaluno = aluno.matricula 
group by matricula.cod_disciplina
order by matricula.cod_disciplina;