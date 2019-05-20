from streams_2 import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

f = open("spam.txt", "w")
f.write("spam")

if __name__ == "__main__":
    import sys
    obj = Uppercase(open("spam.txt"), sys.stdout)
    obj.process()


