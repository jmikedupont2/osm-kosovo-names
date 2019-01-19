split streetnames-al.csv  streetnames-al- -l 5000
head -1 streetnames-al.csv  > header.txt
for x in streetnames-al-a[b-z]; do echo $x; cat header.txt $x > $x.csv; done
mv streetnames-al-aa streetnames-al-aa.csv
