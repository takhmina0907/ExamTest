import re

file = open('text.txt','r')
text = file.read()

iin = re.findall(r'([0-9]{12})', text)
print(iin)

'''
Select * from table where text
  LIKE '%[0-9]{12}%'

'''
'''
DECLARE @strNumbers VARCHAR(100) = 'I was born in 1978. I am 39 years old. Hopefully I wll make it to 40'
DECLARE @Pos SMALLINT = 0
SET @Pos = PATINDEX('%[^0-9]%', @strNumbers) --Find first character
 
WHILE (@Pos > 0)
BEGIN
	SET @strNumbers = STUFF(@strNumbers, @Pos, 1, '')
   
    -- Find next alphabet
    SET @Pos = PATINDEX('[0-9]{12}', @strNumbers)
END
SELECT @strNumbers
'''