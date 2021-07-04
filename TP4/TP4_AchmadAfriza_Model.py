from TP4_AchmadAfriza_Model_Specifications import EAN13Specs as Specs


class Barcode(Specs):
    def __init__(self, code):
        if not int(code): raise ValueError
        if len(code) != super().LENGTH_WITHOUT_CHECKSUM: raise IndexError

        self.__code = code + super().getCheckSum(code)
        self.__bitsEncoded = ''
        self.generateBarcode(code)

    def __addBits(self, bits):
        self.__bitsEncoded = self.__bitsEncoded + bits

    def generateBarcode(self, s):
        encoding = super().getEncoding(s[0])
        code = self.__code[1:]

        self.__addBits(super().SIDE_GUARD)
        for i in range(len(encoding)):
            if i == super().MIDDLE_GUARD_INDEX:
                self.__addBits(super().MIDDLE_GUARD)
            self.__addBits(super().getBits(encoding[i], code[i]))
        self.__addBits(super().SIDE_GUARD)

    def getCode(self):
        return self.__code

    def getBarcode(self):
        return self.__bitsEncoded