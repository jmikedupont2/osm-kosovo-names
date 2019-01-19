import csv
import re
import char_map
import collections

report = collections.Counter()

def charmap(s):
    rs = []
    for c in s:
        if c in char_map.CHAR_MAP:
            c2 = char_map.CHAR_MAP[c]
            report[c]+=1
        else:
            c2 =c
        rs.append(c2)
    return ''.join(rs)
# print(help(csv))
LANGS = ('al',
         'sr','tr',
)

def alb(s):
    # albanian rules
    return s.replace(' E ',' e ')
    
def convert():

    for l in LANGS:
        with open("streetnames-{}.txt".format(l)) as fi:
            with open("streetnames-{}.csv".format(l),'w') as fo:
                co = csv.DictWriter(fo, fieldnames=['source','title', 'speaking'])
                co.writeheader()
                for n in fi:
                    s = n.strip()
                    if not s:
                        continue
                    if re.match('^\d+$',s):
                        continue # only numbers
                    t = alb(s.title())
                    co.writerow({ 'source': s, 'title' : t , 'speaking' : charmap(t)})
if __name__ == '__main__':
    convert()
