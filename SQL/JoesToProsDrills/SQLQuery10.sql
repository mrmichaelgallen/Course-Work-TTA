Create PROC GetProductListByCategory @Category Varchar(50)
AS
	SELECT Cur.ProductID, Cur.ProductName, Cur.RetailPrice
	FROM CurrentProducts AS Cur
	WHERE Cur.Category = @Category 



Create PROC GetGrantsByEmployee @LastName varchar (50)
AS
	SELECT g.GrantID, g.Amount, e.EmpID, e.firstname, e.lastname
	FROM [Grant] as G
	INNER JOIN Employee AS E
	ON G.EmpID = E.EmpID
	WHERE e.lastname = @lastname
	
	SELECT * FROM Employee
	
	SELECT * FROM [grant]
