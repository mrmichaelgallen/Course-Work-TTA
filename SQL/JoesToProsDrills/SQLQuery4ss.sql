CREATE PROCEDURE GetNOWWashingtonEmployees
AS
	SELECT E.firstname, E.lastname, L.city, L.[state]
	FROM Employee AS E
	INNER JOIN Location AS L
	ON E.LocationID = L.LocationID
	WHERE L.[state] != 'WA'
