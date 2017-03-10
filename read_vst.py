#!/Applications/anaconda/bin/python
from pprint import pprint
import xlrd, sys, os
import numpy as np

# File, xls and sheet setups
if len(sys.argv) > 1:
    fname = sys.argv[1]
    print ("Using file argument: ", fname)
else:
    #fname = join(dirname(dirname(abspath(__file__))), 'Shares', 'Code600_combolist.plink.xls')
    fname = os.path.expanduser("~/Downloads/Code600_combolist.plink.xls")
    print ("Using file default: ", fname)

workbook = xlrd.open_workbook(fname)
sheet = workbook.sheet_by_index(0) # This sets the sheet to the first one for my work I only need one sheet

# Search Arrays
search_host = ("gs615-testdata1.gsfc.nasa.gov", "hansolo.gs698-vlab.gsfc.nasa.gov")
search_names = ("David Rancourt", "Jordan Uehara", "Paul Sweatman", "Lisa Lee", "John Sheperd")

# Results array setup
w, h = 4, 100;
results = [[0 for y in range(w)] for z in range(h)]
x=0
hosts=0
primary=8
secondary=9
reason=10
# Do work
# Gets rows for the entire sheet
for row_num in range(sheet.nrows):
    row_value = sheet.row_values(row_num)
    if row_value[0] in search_host:
        a = np.asarray(row_value)
        results[x][0]=a[hosts]
        results[x][1]=a[primary]
        results[x][2]=a[secondary]
        results[x][3]=a[reason]
        x+=1

    if row_value[7] in search_names:
        a = np.asarray(row_value)
        results[x][0]=a[hosts]
        results[x][1]=a[primary]
        results[x][2]=a[secondary]
        results[x][3]=a[reason]
        x+=1
    if row_value[8] in search_names:
        a = np.asarray(row_value)
        results[x][0]=a[hosts]
        results[x][1]=a[primary]
        results[x][2]=a[secondary]
        results[x][3]=a[reason]
        x+=1

# Remove duplicates
results_final = []
for x in results:
    if x not in results_final:
        results_final.append(x)

# Print
pprint (results_final)
