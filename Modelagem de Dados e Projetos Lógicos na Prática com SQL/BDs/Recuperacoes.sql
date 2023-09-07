
-- como utilizar like e between nas queries
use company_teste; 
select * from employee;

select Fname, Lname,Salary, Salary * 0.011 as INSS from employee; 
select Fname, Lname,Salary, round(Salary * 0.011) as INSS from employee; 

-- definir aumento de salário oara gerentes que trabalham em um certo projeto
select * from employee e, works_on as w, project as p where (e.Ssn = w.Essn and w.Pno = p.pnumber AND p.Pname = 'ProductX');

select concat(Fname, ' ', Lname) as Complete_name, Salary, round(Salary * 1.10,2) as Aumento 
from employee as e, works_on as w, project as p where (e.Ssn = w.Essn and w.Pno = p.pnumber AND p.Pname = 'ProductX');

-- Recuperando todos os Manager que trabalham em Stafford
select Dname as Departament_Name, concat(Fname, " ", Lname) as Maneger  from departament as d, dept_locations as dept_l, employee as e  
where  d.Dnumber = dept_l.Dnumber and dept_l.Dlocation = 'Stafford' and Mgr_ssn = e.ssn ;

 -- Recuperando todos os empregados de um departamento
select concat(Fname, " ", Lname) as Employee from employee, departament where Dname = 'Administration' and Dnumber= Dno;

-- Recuperando todos os Manager
select Dname as Departament_Name, concat(Fname, " ", Lname) as Maneger , Dlocation as Departament_localization from departament as d, dept_locations as dept_l, employee as e  
where  d.Dnumber = dept_l.Dnumber and Mgr_ssn = e.ssn ;




-- Like e Between

select Fname, Lname from employee where Address like '%Pidinga-Rio de janeiro%';
select Fname, Lname from employee where Address like '%731%';
select concat(Fname ,' ', Lname ) as FullName from employee where Address like '%731%';

select Fname, Lname from employee where Bdate like '19________';
select Fname, Lname from employee where Bdate like '19__-__-__';
select Fname, Lname from employee where Bdate like '__6_-__-__';

select Fname, Lname, Bdate from employee where Bdate like '__6%';
select Fname, Lname, Bdate from employee where Bdate like '196%';

select Dno, Salary from employee;
select * from employee where (Salary between 300000 and 400000);
select * from employee where (Salary between 300000 and 400000) and Dno=5;