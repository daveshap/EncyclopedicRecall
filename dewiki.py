import re
from ast import literal_eval



with open('wiki.txt', 'r', encoding='utf-8') as infile:
    #body = infile.read()
    body = literal_eval(f'"""{infile.read()}"""')


replacements = [
('&lt;','<'),
('&gt;','>'),
('&quot;','"'),
("'''",' = '),
("'{2,}",''),
('\n',' '),
(r'\n',' '),
('\\n',' '),
('r\\n',' '),
('<ref.*?>',''),
('</ref>',''),
('http.*?\s',''),
('\s+',' '),
]


def basic_replacements(text):
    text = text.replace('\\n',' ')
    for r in replacements:
        #text = text.replace(r[0], r[1])
        text = re.sub(r[0], r[1], text)
    return text

body = basic_replacements(body)


def remove_double_curly(text):
    while True:
        before = len(text)
        text = re.sub('{{[^{]*?}}', '', text) 
        after = len(text)
        if before == after:
            return text
    

body = remove_double_curly(body)

def remove_double_brackets(text):
    while True:
        before = len(text)
        double_brackets = re.findall('\[\[.*?\]\]', text)
        for db in double_brackets:
            if '|' in db:
                new = db.split('|')[-1].strip(']')
                text = text.replace(db, new)
            else:
                new = db.strip('[').strip(']')
                text = text.replace(db, new)
        after = len(text)
        if before == after:
            return text

body = remove_double_brackets(body)
body = remove_double_brackets(body)



print(body)