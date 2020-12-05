# Very simple script to parse the html description of problems, in order to add them to each solutions documentation.
import re
with open('description.txt', 'r') as infile:
    original_text_list = infile.readlines()
original_text = ''.join(original_text_list)
print(re.sub('<.+?>', '', original_text))

