from sys import argv

if len(argv) == 4:
    script, first, second, third = argv
elif len(argv) == 3:
    script, first, second = argv
    third = raw_input("Please input your third argument: ")
elif len(argv) == 2:
    script, first = argv
    second = raw_input("Please input your second argument: ")
    third = raw_input("Please input your third argument: ")
elif len(argv) == 1:
    script = argv
    first = raw_input("Please input your first argument: ")
    second = raw_input("Please input your second argument: ")
    third = raw_input("Please input your third argument: ")
else:
    script = argv[0]
    # get more args from the user using raw_input()
    print "Error: not enough args (%d)!" % len(argv)
    print "Usage: %s [arg1] [arg2] [arg3]" % script
    exit()

print "The script is called:", script
print "Yout first variable is:", first
print "Yout second variable is:", second
print "Yout third variable is:", third
