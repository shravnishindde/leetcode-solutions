# Write your MySQL query statement below
select d.name as Department,e.name as Employee, e.salary as Salary 
from Employee  e 
Join Department  d
on e.departmentid=d.id
where e.salary=(
    Select max(salary)
    From employee
    where departmentId=e.departmentId
);