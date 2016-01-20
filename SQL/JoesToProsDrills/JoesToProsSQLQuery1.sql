Select * FROM tblMovie

ALTER TABLE tblMovie
ADD m_Description Varchar(100) NULL

INSERT INTO tblMovie
VALUES (6,'Fire Shaft',75,'R','Cool Pic about..')

INSERT INTO tblMovie
VALUES (2,'Bonker Bonzo',96,'G',NULL),
(5,'EeeeGhads',88,'G',NULL)

sp_rename 'tblMovie.m_description', 'm_Teaser'

sp_rename 'tblMovie', 'Movie'

Select * FROM Movie

ALTER TABLE Movie
ADD m_Releases Varchar(2000) NOT NULL
Default 2000

DELETE FROM Movie
Where m_ID = 6

ALTER TABLE Movie
DROP COLUMN m_Releases

