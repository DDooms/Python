import re

text_sample = "asd das testing        more spaces \n    \t @ ! tib!"
# text_split = re.split(r'([,\|@\|%\| \|*])', text_sample)
# print(text_split)

text_split = re.split(r'\s+|(\W)', text_sample)
print(text_split)