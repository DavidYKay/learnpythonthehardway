from sys import argv
from os.path import exists

open(argv[2], 'w').write(open(argv[1]).read()) 

#script, from_file, to_file = argv
#indata = open(from_file).read()
#open(to_file, 'w').write(indata)

#print "Copying from %s to %s" % (from_file, to_file)

#how do we do these on one line?
#input = open(from_file)
#indata = input.read()


#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#output = open(to_file, 'w')
#output.write(indata)


#print "Alright, all done."

#output.close()
#input.close()
