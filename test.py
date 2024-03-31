import re

line = 'tho amar_nam = "Kamal"'
pattern = r'(tho|ar)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*"(.*?)"'

match = re.match(pattern, line)
if match:
    keyword = match.group(1)
    variable_name = match.group(2)
    value = match.group(3)
    print("Keyword:", keyword)
    print("Variable Name:", variable_name)
    print("Value:", value)
else:
    print("No match found.")
