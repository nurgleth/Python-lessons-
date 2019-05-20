"""
Ещё раз об обработке потоков
"""
def processor1(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data:
            break
        data = converter(data)
        writer.write(data)
"""
Однако вместо простой функции мы могли бы реализовать обработку в виде
класса, который использует прием композиции, чтобы обеспечить поддержку
наследования и более удобную конструкцию программного кода.
"""
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.wrire(data)
    def converter(self, data):
        assert False, "converter must be defined" # Или возбудить исключение
