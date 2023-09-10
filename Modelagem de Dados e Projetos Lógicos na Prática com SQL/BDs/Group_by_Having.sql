-- Group by e having
   select Pnumber,Pname, count(*) as Number_of_register, round(avg(Salary),2) as Salary
	from project, works_on, employee
    where Pnumber = Pno and Ssn =Essn
    group by Pnumber, Pname
	having count(*) > 2
    order by Salary desc;
    
select Dno , count(*) from employee
	where Salary > 300000 and Dno in (select Dno from employee 
										group by Dno
                                        having count(*)>2)
	group by Dno;