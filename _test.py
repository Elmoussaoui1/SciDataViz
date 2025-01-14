import re

# Original command
command = 'iris["new_column"]=iris["sepal_width"] + iris["petal_width"]'

# Pattern for replacing the first occurrence of an identifier followed by '[something]=' with the same identifier followed by a space
pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\['

# Perform the substitution
pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\['

replace = r'\1 ['

result = re.sub(pattern, replace, command, count=1)

original_regex = r'[a-zA-Z_][a-zA-Z0-9_]*?\[.*?\]'

replacement_pattern = r'(\g<0>)'

result = re.sub(original_regex, replacement_pattern, result)

# Print the result
print(result)
