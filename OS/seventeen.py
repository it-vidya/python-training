import re
pattern = '[^a-z]'
text = 'abcdbcdbcbdbcbdbcbdbdxyzHelloSAdfsdfa'
temp="found match: {} for pattern: {} "
match = re.search(pattern, text)
if match:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print(s,e,temp.format(text[s:e],p))
else:
    print("No match found")
