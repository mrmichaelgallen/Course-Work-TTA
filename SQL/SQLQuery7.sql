SELECT *
FROM Employee AS E INNER JOIN PayRates AS PR
ON E.EmpID = PR.EmpID
WHERE ManagerID = 11
AND YearlySalary IS NOT NULL

UPDATE PR SET YearlySalary = YearlySalary + 10000
FROM Employee AS E INNER JOIN PayRates AS PR
ON E.EmpID = PR.EmpID
WHERE ManagerID = 11
AND YearlySalary IS NOT NULL

Update Employee
SET LastName = 'Green'
Where EmpID = 11

Update Employee
SET Status = 'External'
Where LocationID = 4

SELECT * FROM Location

Update Location
SET Street = '111 1st Ave'
Where LocationID = 1

DELETE MgmtTraining 
Where ClassDurationHours > 20

SELECT * FROM MgmtTraining