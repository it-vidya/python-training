import re

text = 'abbaaabbbbaaaaab'

pattern='ab'

occur= len(re.findall(pattern , text))

e=0

while(occur>0):
 match = re.search(pattern,text[e:] )

 s = match.start() 
 e = match.end()
 print("occurence at (%d--%d)"%(s+e,e+e))
 occur-=1


























"""
for match in re.findall(pattern, text):
    print 'Found at "[%s,%s]"' %(match.start ,match.end)
"""