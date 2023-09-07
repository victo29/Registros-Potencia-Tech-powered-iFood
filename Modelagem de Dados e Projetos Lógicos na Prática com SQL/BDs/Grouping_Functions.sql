-- funções e clausulas de agrupamento
use company_teste;
select * from employee;
select * from departament;
select count(*) from employee;

select count(*) from employee, departament 
	where Dno = Dnumber and Dname = 'Research';
    
select Dno, count(*) as amount , round(avg(salary),2) as media_salary from employee
	group by Dno;

select Pnumber,Pname, count(*)
	from project, works_on
    where Pnumber = Pno
    group by Pnumber, Pname;
    
    select Pnumber,Pname, count(*) as Number_of_register, round(avg(Salary),2) as Salary
	from project, works_on, employee
    where Pnumber = Pno and Ssn =Essn
    group by Pnumber, Pname
    order by Salary desc;

select count(distinct Salary) from employee;
select sum(Salary) as Total_Salary, max(Salary) as Max_Salary, min(Salary) as Min_salary, avg(Salary) as Media_Salary from employee;