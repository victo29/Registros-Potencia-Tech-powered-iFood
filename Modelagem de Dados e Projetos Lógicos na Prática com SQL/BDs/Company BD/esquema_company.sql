create schema if not exists company_teste;
use company_teste;
create table employee(
	Fname varchar(15) not null,
	Minit char,
	Lname varchar(15) not null,
	Ssn char(9) not null,
	bdate date,
	Address varchar(30),
	sex char,
	Salary decimal(10,2),
	Super_ssn char(9),
	Dno int not null,
    constraint chk_salary_emp check (Salary>2000.0),
    constraint pk_employee primary key(Ssn)
);

alter table employee
	add constraint fk_employee
    foreign key(Super_ssn) references employee(Ssn)
    on delete set null
    on update cascade;
    
create table departament(
	Dname varchar(15) not null,
    Dnumber int not null,
    Mgr_ssn char(9),
    Mgr_start_date date,
    Dept_create_date date,
    constraint  chk_date_dpt check(Dept_create_date < Mgr_start_date ),
    constraint pk_Dpt primary key(Dnumber),
    constraint unique_name_dept unique (Dname),
    foreign key(Mgr_ssn) references employee(Ssn)
);
alter table departament drop departament_ibfk_1;
alter table departament
	add constraint fk_dpt foreign key(Mgr_ssn) references employee(Ssn)
    on update cascade;

create table dept_locations(
	Dnumber int not null,
    Dlocation varchar(15) not null,
    constraint pk_dpt_locations primary key(Dnumber, Dlocation),
    constraint fk_dpt_locations foreign key (Dnumber) references departament(Dnumber)
    
);
alter table dept_locations drop constraint fk_dpt_locations;
alter table dept_locations
	add constraint fk_dpt_locations foreign key (Dnumber) references departament(Dnumber)
    on delete cascade
    on update cascade;

create table project(
	Pname varchar(15) not null,
    Pnumber int not null,
    Plocation varchar(15),
    Dnum int not null,
    primary key(Pnumber),
    constraint unique_project unique(Pname),
    constraint fk_project foreign key(Dnum) references departament(Dnumber)
    
);

create table works_on(
	Essn char(9) not null,
	Pno int not null,
	Hours decimal(3,1) not null,
	primary key(Essn,Pno),
	constraint fk_employee_works_on foreign key (Essn) references employee(Ssn),
	constraint fk_project_works_on foreign key(Pno) references project(Pnumber) 
);

create table dependent(
	Essn char(9) not null,
    Dependent_name varchar(15) not null,
    Sex char,
    Bdate date,
    Relationship varchar(8),
    Age int not null,
    constraint chk_age_dependent check (Age < 21),
    primary key(Essn,Dependent_name),
	constraint fk_dependent foreign key (Essn) references employee(Ssn)
);

alter table dependent drop Age;

select * from information_schema.table_constraints
	where constraint_schema = 'company_teste';
    
    show tables;