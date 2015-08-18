"""The program should take name of zip file as first argument and files to add as rest of the arguments. """


import sys
import zipfile
zip_file=sys.argv[1]
z=zipfile.ZipFile('zip_file','w')
for i in range(2,len(sys.argv)):
    z.write(sys.argv[i])
