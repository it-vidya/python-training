import re
pattern = 'a*'
text = 'welcome to aba'
match = re.search(pattern, text)
if match!=None:
    s=match.start()
    e=match.end()
    p=match.re.pattern
    print("found match: {} for pattern: {} ".format(text[s:e],p))
