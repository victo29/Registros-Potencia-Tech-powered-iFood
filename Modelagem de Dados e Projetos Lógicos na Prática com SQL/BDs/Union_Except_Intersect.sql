-- Union, Except, and Intersect
create database teste1;
use teste1;
create table R(
A char(2)
);
create table S(
A char(2)
);

insert into R(A) values ('a1'),('a2'),('a2'),('a3');
insert into S(A) values ('a1'),('a1'),('a2'),('a2'),('a2'),('a3'),('a4'),('a5');
-- Except
select * from S WHERE A NOT IN (select A from R);

-- Intersect
select distinct R.A from R where R.A IN (select S.A from S);

-- Union
(select R.A from R) union (Select S.A from S);