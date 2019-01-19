split streetnames-al.csv  streetnames-al -b 500K
head -1 streetnames-alaa  > header.txt
for x in streetnames-ala[b-z]; do echo $x; cat header.txt $x > $x.csv; done
mv streetnames-alaa streetnames-ala.csv
