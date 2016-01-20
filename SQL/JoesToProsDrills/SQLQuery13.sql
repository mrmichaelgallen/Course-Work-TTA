SELECT * FROM [grant]

BEGIN TRAN

DELETE [Grant]
Where GrantName = 'Norman''s Outreach'

INSERT INTO [Grant]
VALUES (11,'Seasons Outreach',NULL,85000)

COMMIT TRAN

SELECT * FROM [grant]






