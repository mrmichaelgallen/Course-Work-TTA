SELECT * FROM tblMovie

Update tblMovie
SET m_Title = 'A-List Explorers'
Where m_id = 1

Update tblMovie
SET m_Title = 'Dare the World to Try'
Where m_id = 4

Update tblMovie
SET m_Title = 'Eeee-Ghads'
Where m_id = 5

DELETE tblMovie 
Where m_runtime > 90

DELETE tblMovie 
Where m_rating = 'G'
