from sys import argv


script, args = argv[0], argv[1:]

print ("The script is called: ", script)
for i, arg in enumerate(args):
    print ("Args{0:d}: {1:s}".format(i,arg))


if len(argv) < 4:
    print ("usage: {0:s} <bike> <car> <bus>".format(script))
    raise SystemExit(-1)

script, bike, car, bus = argv

print ("The script is called:", script)
print ("The first variable is:", bike)
print ("The second variable is:", car)
print ("The third variable is:", bus)
