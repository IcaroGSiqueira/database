
 -- 1
SELECT nome, dtcontratacao FROM funcionario WHERE (funcionario.coddepartamento = (SELECT funcionario.coddepartamento 
FROM funcionario WHERE funcionario.nome = 'maria')) and nome <> 'maria';

SELECT nome, dtcontratacao FROM funcionario WHERE funcionario.coddepartamento = (SELECT funcionario.coddepartamento
FROM funcionario WHERE funcionario.nome = 'maria') and nome IN (SELECT f2.nome FROM funcionario f2 WHERE f2.nome <> 'maria');

SELECT nome, dtcontratacao FROM funcionario WHERE funcionario.coddepartamento = (SELECT funcionario.coddepartamento
FROM funcionario WHERE funcionario.nome = 'maria') and EXISTS (SELECT * FROM funcionario f2 WHERE f2.nome <> 'maria');

-- 2
SELECT cod , nome FROM funcionario WHERE funcionario.salario > (SELECT avg(funcionario.salario) 
FROM funcionario) order by funcionario.salario DESC;

-- 3
SELECT nome, dtcontratacao FROM funcionario WHERE funcionario.coddepartamento = (SELECT funcionario.coddepartamento 
FROM funcionario WHERE funcionario.nome like '%W%');

-- 4
SELECT nome, dtcontratacao, salario FROM funcionario WHERE funcionario.salario > (SELECT avg(funcionario.salario) 
FROM funcionario);

-- 5
SELECT nome FROM funcionario AS gerente WHERE EXISTS (SELECT 8 
FROM funcionario WHERE funcionario.codgerente = gerente.cod);

-- 6
SELECT aluno.nome FROM aluno RIGHT JOIN matricula ON matricula.matriculaaluno = aluno.matricula 
WHERE matricula.cod_disciplina IN (SELECT m2.cod_disciplina 
FROM matricula m2 LEFT JOIN aluno a2 ON aluno.matricula = m2.matriculaaluno 
WHERE a2.nome LIKE 'maria') and aluno.nome <> 'maria' group by aluno.matricula;

SELECT aluno.nome FROM aluno RIGHT JOIN matricula ON matricula.matriculaaluno = aluno.matricula 
WHERE EXISTS (SELECT m2.cod_disciplina FROM matricula m2 LEFT JOIN aluno a2 ON aluno.matricula = m2.matriculaaluno 
WHERE a2.nome LIKE 'maria') and aluno.nome <> 'maria' group by aluno.nome;




