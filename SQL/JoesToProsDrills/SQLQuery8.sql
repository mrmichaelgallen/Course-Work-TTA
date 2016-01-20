SELECT E.FirstName,E.FirstName,E.LastName,E.LocationID,G.GrantName,G.Amount
From [Grant] G INNER JOIN Employee E
ON G.EmpID = e.EmpID
WHERE LocationID = 2

Update Location
SET Street = '111 1st Ave'
Where LocationID = 1

Update G set Amount = 20000
From [Grant] G INNER JOIN Employee E
ON G.EmpID = e.EmpID
WHERE LocationID = 2
