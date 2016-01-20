use dbBasics
use JProCo
SELECT * FROM Employee

-- coding an error message

RAISERROR('Your bad!', 16, 1)

-- Another Example

THROW 50000, 'Your bad!', 1


-- Try catch block

BEGIN TRY
	INSERT INTO PayRates (EmpID, YearlySalary, MonthlySalary, HourlyRate, Selector, Estimate, BonusPay)
	VALUES (1, 50000, Null, Null, 1, 50000, 0)
	PRINT 'After First Insert'
END TRY
BEGIN CATCH
	PRINT 'What is the error?'
	PRINT ERROR_MESSAGE()
END CATCH;


SELECT * FROM Employee
SELECT * FROM PayRates
GO

CREATE PROC InsertYearlyPay @EmpID INT, @YrSalary MONEY
AS
	BEGIN TRY
		INSERT INTO [dbo].[PayRates] (EmpID, YearlySalary, MonthlySalary, HourlyRate, Selector, Estimator, BonusPay)
		VALUES (@EmpID, @YrSalary, Null, Null, 1, @YrSalary, 0)
			COMMIT TRAN
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
	END CATCH	
GO

-- Code below runs above query, below updated the PayRates updates table

EXEC InsertYearlyPay 20, 50000

-- adding active status for employee

UPDATE Employee
SET [Status] = 'Active'
WHERE EmpID = 20



-- example of stored procedure

CREATE PROC MakeYearlyEmployeePay @EmpID INT, @YrSalary MONEY
AS

	BEGIN TRY
		BEGIN TRAN
			UPDATE EMPLOYEE
			SET [Status] = 'Active'
			WHERE EmpID = @EmpID
			
			EXEC InsertYearlyPay @EmpID	@YrSalary
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT ERROR_MESSAGE()
	END CATCH
GO

-- exec command for above

EXEC MakeYearlyEmployeePay 21, 51000