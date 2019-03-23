import re
tonoi = ('αά', 'εέ', 'ηή', 'ιί', 'οό', 'ύυ', 'ωώ')
*var* = '****.txt'
try:
    with open(*var*, 'r', encoding = 'utf-8') as f:
        *var2* = f.read()
        print(*var2*)
except IOError as e:
    print(e)
while True:
    phrase = input('Δώσε λέξη-κλειδί:')
    if phrase == '': break
    n_phrase = ''
    for c in phrase:
        char = c
        for t in tonoi:
            if c in t: char = '['+t+']'
        n_phrase += char
    print(n_phrase)
    pattern = '.*'+n_phrase+'.*'
    w =re.findall(pattern, works, re.I)
    print(w)
