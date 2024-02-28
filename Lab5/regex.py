import re

# 1
def match_ab(s):
    pattern = r'^ab*'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"

# 2
def match_abb(s):
    pattern = r'^ab{2,3}'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"

# 3
def find_sequences(s):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, s)

# 4
def find_uppercase_sequences(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)

# 5
def match_a_anything_b(s):
    pattern = r'^a.*b$'
    if re.match(pattern, s):
        return "Match found"
    else:
        return "Match not found"

# 6
def replace_with_colon(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

# 7
def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase

# 8
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res

# 9 
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

# 10
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res
