--Concat

SELECT *, CONCAT(firstname,' ',lastname) AS FullName
From Employee

--Convert Function

SELECT *, CONVERT(NVARCHAR, HireDate, 103) AS CharDate
From Employee


-- mm = minutes while MMMM, MMM, MM, M date formats

