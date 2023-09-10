use company_teste;
select concat(Fname, ' ', Lname) as Comlplete_name, Dno as DeptNumber, Pname as ProjectName, Pno as ProjectNumber, Plocation as Location
	from employee
	inner join works_on on Ssn = Essn
    inner join project on Pno = Pnumber
    order by Pnumber;
    
    
    select concat(Fname, ' ', Lname) as Comlplete_name, Dno as DeptNumber, Pname as ProjectName, Pno as ProjectNumber, Plocation as Location
	from employee
	inner join works_on on Ssn = Essn
    inner join project on Pno = Pnumber
    where Plocation like 's%'
    order by Pnumber;
    
    select concat(Fname, ' ', Lname) as Comlplete_name, Dno as DeptNumber, Pname as ProjectName, Pno as ProjectNumber, Plocation as Location
	from employee
	inner join works_on on Ssn = Essn
    inner join project on Pno = Pnumber
    where Pname like 'Product%'
    order by Pnumber;
    
    
    select Dnumber , Dname, concat(Fname, ' ', Lname) as Manager, Salary from departament
    inner join dept_locations using(Dnumber)
    inner join (dependent inner join employee on Ssn = Essn) on SSn = Mgr_ssn
    group by  Dnumber;
    
;
select * from employee where Ssn != Super_ssn;
select * from employee where  Super_ssn = NULL;

desc employee;
select * from employee;