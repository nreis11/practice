# import re

# filepath = "/Users/admin/Downloads/channel/%s.txt"
# num = "90052"
# comments = []

# while True:
#     file = open(filepath % num)
#     # regex = r'nothing is (\d+)'
#     regex = r'\A#.+'
#     match = re.search(regex, file.read())
#     comment = file.comment.decode("utf-8")
#     print(comment)
#     # comments.append(file.getinfo().comment.decode("utf-8"))
#     print(file.getinfo)
#     if match == None:
#         break
#     # print(match.group(0))
#     num = match.group(1)

import re

a = [1, 11, 21, 1211, 111221]
regex = r'(\d)(\1*)'

match = re.findall(regex, "111221")
print(match)







