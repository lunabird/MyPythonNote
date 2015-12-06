#-*- coding:utf-8 -*-
from sys import argv
from os.path import exists
script, from_file, to_file=argv

print "Copying from %s to %s"%(from_file,to_file)

#这两句可以写成下面的一句
#in_file=open(from_file)
#indata=in_file.read()

indata=open(from_file).read()

#print "The input file is %d bytes long"%len(indata)
#print "Does the output file exists?%r"%exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()
#这两句可以写成下面的一句
#out_file=open(to_file,'w')
#out_file.write(indata)
open(to_file,'w').write(indata)
print "Alright, all done."

#out_file.close()
#in_file.close()