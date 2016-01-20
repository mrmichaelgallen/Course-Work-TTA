use dbBasics
use JProCo

SELECT * FROM Employee

DECLARE @SQL NVARCHAR(200) = 'SELECT * FROM Employee'
EXEC (@SQL)  

DECLARE @spSQL NVARCHAR(200) = 'SELECT * FROM Employee'
EXEC sp_ExecuteSql @spSQL

-- Finding last name of a given employee

-- Base example before modifying to dynamic

SELECT * FROM Employee WHERE lastname = 'smith'

-- Example with dynamic
-- The declaration is part of the parameter being passed in on the last line

DECLARE @SQL NVARCHAR(200)
SET @SQL = 'SELECT * FROM Employee Where LastName = @EmpLastName'
EXEC sp_ExecuteSQL @SQL, N'@EmpLastName NVARCHAR(50)', @EmpLastName = 'smith' -- The variable is smith

-- Between

DECLARE @MIN MONEY = 20000
DECLARE @Max MONEY = 25000
SELECT * FROM [Grant] WHERE Amount BETWEEN @Min AND @Max

-- Making it dynamic

DECLARE @SQL NVARCHAR(200)
SET @SQL = 'SELECT * FROM [Grant] WHERE Amount BETWEEN @Min AND @Max'
EXEC sp_ExecuteSQL @SQL, N'@Min MONEY, @Max MONEY', @MIN = 15000, @Max = 25000

-- Lab 2.3: sp_executesql - Skill Check #1

DECLARE @ClassTime INT = 12
SELECT * FROM MgmtTraining WHERE ClassDurationHours > @ClassTime

-- Dynamic version below

DECLARE @SQL NVARCHAR(200)
SET @SQL = 'SELECT * FROM MgmtTraining WHERE ClassDurationHours > @ClassTime'
EXEC sp_ExecuteSQL @SQL, N'@ClassTime INT', @ClassTime = 12

-- Lab 2.3: sp_executesql - Skill Check #2

DECLARE @MgrID INT = 11
DECLARE @Pay MONEY = 25000
SELECT em.*, pr.YearlySalary
FROM Employee AS em
INNER JOIN PayRates AS pr
ON em.EmpID = pr.EmpID
WHERE em.ManagerID = @MgrID
AND pr.YearlySalary > @Pay

-- Dynamic version below

DECLARE @SQL NVARCHAR(200)
SET @SQL = 'SELECT em.*, pr.YearlySalary FROM Employee AS em INNER JOIN PayRates AS pr ON em.EmpID = pr.EmpID WHERE em.ManagerID = @MgrID AND pr.YearlySalary > @Pay'
EXEC sp_ExecuteSQL @SQL, N'@MgrID INT, @Pay MONEY', @MgrID = 11, @Pay = 25000

