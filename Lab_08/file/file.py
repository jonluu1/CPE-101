import sys
sys.path.append("../convert")
import convert

filename = str(sys.argv[1])

try:
    f = open(filename)
except:
    print("The requested file, %s, cannot be opened..." % filename)
    exit()
i = 1
for line in f:
    try:
        value1, value2 = line.split()
        converted = convert.float_default(value1, None) + convert.float_default(value2, None)
        print(converted)
    except:
        print("ERROR!!! String on line %d cannot be converted to a float..." %i)
    i += 1
f.close()