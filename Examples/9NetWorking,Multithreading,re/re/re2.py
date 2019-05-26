import re

pattern = 'this'
text = 'Does this text this match this the this pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Found "%s" in "%s" from %d to %d ("%s")' %(match.re.pattern, match.string, s, e, text[s:e])
input()