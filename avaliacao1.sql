create database bd_p1;

-- 1

create table faixaproduto(
	cod int (6) auto_increment,
	categoria varchar (50),
	valorinicial numeric (6),
	valorfinal numeric (6),
	primary key(cod)
);

create table estado(
	cod int (3) auto_increment,
	nome varchar (50)not null,
	sigla varchar (6)not null,
	primary key(cod)
);

create table cidade(
	cod int (3) auto_increment,
	nome varchar (50)not null,
	codestado int (3)not null,
	primary key(cod),
	foreign key(codestado) references estado (cod)
);

create table fabricante(
	cod int (6) auto_increment,
	nome varchar (50) not null,
	endereco varchar (50),
	codcidade int (3) not null,
	primary key(cod),
	foreign key(codcidade) references cidade (cod)
);

create table grupo(
	cod int (6) auto_increment,
	descrição varchar (50) not null,
	codgrupopai int (6),
	primary key(cod),
	foreign key(codgrupopai) references grupo (cod)
);

create table produto(
	cod int (6) auto_increment,
	descricao varchar (500) not null,
	dtultcompra date,
	quantidade numeric (3),
	prcunit numeric (6),
	perecivel char(1) not null,
	codfabricante int (6),
	codgrupo int (6),
	primary key(cod),
	foreign key(codfabricante) references fabricante (cod),
	foreign key(codgrupo) references grupo (cod),
	check (perecivel = 's' or perecivel = 'n')
);

-- 2

insert into grupo values(null,'BEBIDAS',null);
insert into grupo values(null,'HIGIENE',null);
insert into grupo values(null,'ALIMENTO',null);
insert into grupo values(null,'LIMPEZA',null);

insert into grupo select null,'DESTILADAS',grupo.cod from grupo where grupo.descrição like 'BEBIDAS';
insert into grupo select null,'DENTARIA',grupo.cod from grupo where grupo.descrição like 'HIGIENE';
insert into grupo select null,'CAPILAR',grupo.cod from grupo where grupo.descrição like 'HIGIENE';
insert into grupo select null,'SANITARIA',grupo.cod from grupo where grupo.descrição like 'LIMPEZA';

insert into estado values(null,'Rio Grande do Sul','RS');
insert into estado values(null,'Sao Paulo','SP');
insert into estado values(null,'Rio de Janeiro','RJ');

insert into cidade select null,'Porto Alegre',estado.cod from estado where estado.sigla like 'RS';
insert into cidade select null,'Sao Paulo',estado.cod from estado where estado.sigla like 'SP';
insert into cidade select null,'Rio de Janeiro',estado.cod from estado where estado.sigla like 'RJ';

insert into fabricante select null,'FABRICANTE1','endereco 111',cidade.cod from cidade where cidade.nome like 'Porto Alegre';
insert into fabricante select null,'FABRICANTE2','endereco 222',cidade.cod from cidade where cidade.nome like 'Sao Paulo';
insert into fabricante select null,'FABRICANTE3','endereco 333',cidade.cod from cidade where cidade.nome like 'Porto Alegre';
insert into fabricante select null,'FABRICANTE4','endereco 444',cidade.cod from cidade where cidade.nome like 'Rio de Janeiro';
insert into fabricante select null,'FABRICANTE5','endereco 555',cidade.cod from cidade where cidade.nome like 'Sao Paulo';
insert into fabricante select null,'FABRICANTE6','endereco 666',cidade.cod from cidade where cidade.nome like 'Rio de Janeiro';
insert into fabricante select null,'FABRICANTE7','endereco de teste 777',cidade.cod from cidade where cidade.nome like 'Rio de Janeiro';
insert into fabricante select null,'FABRICANTE8','ENDERECO DE TESTE 888',cidade.cod from cidade where cidade.nome like 'Rio de Janeiro';

insert into produto select null,'DESINFETANTE',		'2009-05-04','2','3.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'LIMPEZA' and fabricante.nome like 'FABRICANTE1';
insert into produto select null,'DESENGORDURANTE',	'2008-05-10','1','4.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'LIMPEZA' and fabricante.nome like 'FABRICANTE6';
insert into produto select null,'CLORO',			'2009-12-31','1','5.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'SANITARIA' and fabricante.nome like 'FABRICANTE6';
insert into produto select null,'LIMPA-VIDRO',		'2009-06-06','2','2.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'LIMPEZA' and fabricante.nome like 'FABRICANTE1';

insert into produto select null,'DORITOS',		'2009-05-04','4','3.99','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE4';
insert into produto select null,'FEIJAO',		'2008-05-10','2','4.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE3';
insert into produto select null,'ARROZ',		'2009-12-31','1','25.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE4';
insert into produto select null,'CARNE',		'2009-06-06','3','7.99','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE3';

insert into produto select null,'QUEIJO',		'2009-06-06','3','9999.99','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE3';

insert into produto select null,'BOMBOM',		'2009-06-06','1','3','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'ALIMENTO' and fabricante.nome like 'FABRICANTE3';

insert into produto select null,'ENERGETICO',		'2009-05-04','2','10.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'BEBIDAS' and fabricante.nome like 'FABRICANTE4';
insert into produto select null,'VODKA',			'2008-05-10','2','15.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'DESTILADAS' and fabricante.nome like 'FABRICANTE5';
insert into produto select null,'REFRIGERANTE',		'2009-12-31','2','4.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'BEBIDAS' and fabricante.nome like 'FABRICANTE5';
insert into produto select null,'SUCO',				'2009-06-06','4','2.99','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'BEBIDAS' and fabricante.nome like 'FABRICANTE4';

insert into produto select null,'VINHO',			'2008-05-12','2','15.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'DESTILADAS' and fabricante.nome like 'FABRICANTE1';
insert into produto select null,'CACHACA',			'2008-05-01','2','15.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'DESTILADAS' and fabricante.nome like 'FABRICANTE1';

insert into produto select null,'PASTA-DE-DENTE',	'2009-05-04','1','4.99','S', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'DENTARIA' and fabricante.nome like 'FABRICANTE1';
insert into produto select null,'SHAMPOO',			'2008-05-10','1','15.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'CAPILAR' and fabricante.nome like 'FABRICANTE2';
insert into produto select null,'CONDICIONADOR',	'2009-12-31','1','16.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'CAPILAR' and fabricante.nome like 'FABRICANTE2';
insert into produto select null,'SABONETE',			'2009-06-06','4','1.99','N', fabricante.cod, grupo.cod from fabricante, grupo where grupo.descrição like 'HIGIENE' and fabricante.nome like 'FABRICANTE2';

insert into faixaproduto values(null,'C','0','5000');
insert into faixaproduto values(null,'B','5001','10000');
insert into faixaproduto values(null,'A','10001','999999');

-- 3

select fabricante.nome, estado.nome , produto.cod from fabricante right join produto on produto.codfabricante = fabricante.cod
left join cidade on cidade.cod = fabricante.codcidade 
left join estado on estado.cod = cidade.codestado 
where (estado.sigla like 'SP' or estado.sigla like 'RJ')
and produto.dtultcompra between '2009-01-01' and '2009-06-30'
order by produto.dtultcompra ASC;

-- 4

select produto.descricao , produto.prcunit*produto.quantidade as valor, fabricante.nome, (case when produto.perecivel like'S' then 'PERECIVEL' 
else 'NAO PERECIVEL' end) as perecivel from fabricante right join produto on produto.codfabricante = fabricante.cod;

-- 5

select grupo.descrição, sum(produto.prcunit*produto.quantidade) as valor from grupo right join produto on produto.codgrupo = grupo.cod 
where (select sum(produto.prcunit*produto.quantidade) from grupo g where grupo.cod = g.cod) > 10000 group by grupo.descrição order by valor DESC;

-- 6

select estado.nome from estado left join cidade on estado.cod = cidade.codestado 
right join fabricante on cidade.cod = fabricante.codcidade 
right join produto on produto.codfabricante = fabricante.cod
right join grupo on produto.codgrupo = (select grupo.cod from grupo left join grupo g on grupo.cod = g.codgrupopai where grupo.descrição like 'BEBIDAS')
where produto.dtultcompra between '2008-01-01' and '2008-12-31'
order by estado.sigla ASC;

-- 7

UPDATE fabricante SET fabricante.endereco = CONCAT(UCASE(LEFT(fabricante.endereco,1)),LCASE(SUBSTRING(fabricante.endereco,2)));

-- 8 

select produto.descricao, faixaproduto.categoria from produto, faixaproduto where (produto.prcunit*produto.quantidade) 
between faixaproduto.valorinicial and faixaproduto.valorfinal order by faixaproduto.categoria;

-- 9

select fabricante.nome, produto.descricao from fabricante left join produto on produto.codfabricante = fabricante.cod;

-- 10

select grupo.descrição as grupo, g.descrição as subgrupo from grupo left join grupo g on grupo.cod = g.codgrupopai group by grupo.descrição order by grupo.descrição;

-- 11

select produto.descricao from produto left join fabricante on fabricante.cod = produto.codfabricante where fabricante.nome like "FABRICANTE3" 
and produto.prcunit > (select avg(p.prcunit) from produto p where p.codfabricante = produto.codfabricante and fabricante.nome like "FABRICANTE3");

