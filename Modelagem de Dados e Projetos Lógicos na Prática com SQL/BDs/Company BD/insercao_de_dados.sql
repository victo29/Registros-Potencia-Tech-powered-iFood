
use company_teste;
show tables;

insert into employee values('John','B','Souza',123456789, '1965-01-09', '731-salvador-bahia', 'M', 300000,null,5 );
insert into employee values('Fernando','C','Souza',234567890, '1964-02-09', '734-Carnaiba-Rio de janeiro', 'M', 300080,123456789,4 ), 
('Ricardo','C','Borges',345678901, '1966-02-09', '789-Pidinga-Rio de janeiro', 'M', 300001,234567890,5 ),
('Hoberto','U','Zacarias',456789012, '1969-06-09', '782-Piroquiase-São Paulo', 'F', 350000,345678901,5 );
insert into employee values('Valdirene','A','Souza',567890123, '1965-01-09', '731-Salvador-bahia', 'F', 400000,null,5 ); 

insert into dependent values (234567890, 'Alice', 'F', '1986-04-05', 'Daughter'),
							 (234567890, 'Theodore', 'M', '1983-10-25', 'Son'),
                             (234567890, 'Joy', 'F', '1958-05-03', 'Spouse'),
                             (345678901, 'Abner', 'M', '1942-02-28', 'Spouse'),
                             (123456789, 'Michael', 'M', '1988-01-04', 'Son'),
                             (123456789, 'Alice', 'F', '1988-12-30', 'Daughter'),
                             (123456789, 'Elizabeth', 'F', '1967-05-05', 'Spouse');

insert into departament values ('Research', 5, 123456789, '1988-05-22','1986-05-22'),
							   ('Administration', 4, 345678901, '1995-01-01','1994-01-01'),
                               ('Headquarters', 1, 567890123,'1981-06-19','1980-06-19');
                               
insert into dept_locations values (1, 'Houston'),
								 (4, 'Stafford'),
                                 (5, 'Bellaire'),
                                 (5, 'Sugarland'),
                                 (5, 'Houston');

insert into project values ('ProductX', 1, 'Bellaire', 5),
						   ('ProductY', 2, 'Sugarland', 5),
						   ('ProductZ', 3, 'Houston', 5),
                           ('Computerization', 10, 'Stafford', 4),
                           ('Reorganization', 20, 'Houston', 1),
                           ('Newbenefits', 30, 'Stafford', 4)
;

insert into works_on values (123456789, 1, 32.5),
							(123456789, 2, 7.5),
                            (234567890, 1, 20.0),
                            (234567890, 2, 20.0),
                            (567890123, 2, 10.0),
                            (567890123, 3, 10.0),
                            (567890123, 10, 10.0),
                            (567890123, 20, 10.0),
                            (456789012, 30, 30.0),
                            (456789012, 10, 10.0),
                            (456789012, 20, 15.0),
                            (345678901, 20, 0.0);

-- Requisições

-- gerente e seu departamento 
select Ssn, Fname, Dname from employee e, departament d where(e.Ssn = d.Mgr_ssn);
-- Empregado e seus dependentes
select Fname, Dependent_name, Relationship from employee, dependent where Essn = Ssn;

-- Ano de nascimenoe endereço de um empregado específico
select Bdate, Address from employee where Fname = 'John' and Minit = 'B';

-- Departamento específico
Select * from departament where Dname = 'Research';

--
select Fname, Lname, Address from employee, departament where Dname = 'Research' and Dnumber = Dno;