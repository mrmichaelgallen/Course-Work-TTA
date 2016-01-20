
-- Simple Query

SELECT *
FROM Location ORDER BY LocationID

-- Query with Analytical functions

SELECT *, CUME_DIST() OVER(ORDER BY LocationID)
FROM Location 

-- Example

SELECT *
FROM Employee
ORDER BY HireDate

-- Example

SELECT *, First_Value(HireDate) OVER(Order By HireDate)
From Employee


-- Example

SELECT *
FROM StateList
Order BY LandMass DESC
