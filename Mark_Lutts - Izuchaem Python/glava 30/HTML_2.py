from converters_2 import Uppercase

class HTMLize:
    def write(self, line):
        print("<PRE>%s</PRE>" % line.rstrip())

print(Uppercase(open("spam.txt"), HTMLize()).process())