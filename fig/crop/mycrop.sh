#!/bin/sh
# cd ../.

for i in *.pdf
do
	pdfcrop $i $i
done

# cd crop
mv *.pdf ../.
# 
# find . -name \*.pdf -print0 | xargs -0 -I{} pdfcrop --margins "2 2 2 2" {} {}