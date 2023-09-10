use company_teste;

select * from employee join departament on Ssn = Mgr_ssn;

select Fname, Lname, Address, Dno, Dnumber
from(employee join departament on Dno = Dnumber)
where Dname = 'Research';

select * from departament;
select * from dept_locations;
select Dname as Departament ,Dlocation as Location, departament.Dnumber as Number_Departament, Dept_create_date as Create_Date 
	from departament 
    join dept_locations on departament.Dnumber = dept_locations.Dnumber
	order by Dept_create_date desc;