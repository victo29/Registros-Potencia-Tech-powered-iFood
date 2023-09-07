-- Cláusulas e funções de ordenação
use company_teste;
select * from employee;

select * from employee order by Dno;
select * from employee order by Fname;
select * from employee order by Fname, Lname;

select distinct d.Dname, concat(e.Fname, ' ', e.Lname) as Manager, Address
from departament as d, employee e, works_on as w, project as p 
where d.Dnumber = e.Dno  and e.Ssn = d.Mgr_ssn and w.Pno = p.Pnumber
order by D.dname ; 

-- Recupero todos os empregados e seus projetos em andamento
select distinct d.Dname as Departament, concat(e.Fname, ' ', e.Lname) as Employee, Address, p.Pname as project_Name
	from departament as d, employee as e, works_on as w, project as p
    where (d.dnumber = e.Dno and e.Ssn = w.Essn and w.Pno = p.Pnumber)
    order by d.Dname desc, p.Pname asc;