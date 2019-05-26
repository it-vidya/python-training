import re
pattern = 'a?'
text = 'aaa'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match!=None:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
