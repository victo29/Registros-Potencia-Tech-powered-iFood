show databases;
create database first_example;
use first_example;
CREATE table person(
	person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	gender enum("M", "F"),
	birth_date date,
	street varchar(20),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
    constraint pk_person primary key(person_id)
);
desc person;

create table favorite_food(
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key(person_id, food),
    constraint fk_favorite_food_person_id foreign key(person_id)
    references person(person_id)
);
desc favorite_food;
show databases;

desc person;
insert into person values('2', 'Victor', 'Souza', 'M', '2000-02-06', 'rua tal', 'Cidade J', 'RJ', 'Brasil', '26054-89'),
('3', 'Victor', 'Souza', 'M', '2000-02-06', 'rua tal', 'Cidade J', 'RJ', 'Brasil', '26054-89') ;
select * from person;

delete from person where person_id = 2;

insert into favorite_food values('1', 'Hot-Dog'), ('3', 'Feijão') ;

select * from favorite_food;
