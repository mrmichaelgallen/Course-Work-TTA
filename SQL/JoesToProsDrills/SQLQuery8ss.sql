CREATE PROC GetEmployeesFromBoston
AS
	SELECT Emp.firstname, emp.lastname, loc.city, Loc.[state]
	FROM Employee AS emp
	INNER JOIN Location as Loc
	ON emp.LocationID = Loc.LocationID
	WHERE Loc.city = 'Boston'
