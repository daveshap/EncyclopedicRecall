from ast import literal_eval


with open('wiki.txt', 'r', encoding='utf-8') as infile:
    body = infile.read()
    
print(body)

print(literal_eval(f'"""{body}"""'))