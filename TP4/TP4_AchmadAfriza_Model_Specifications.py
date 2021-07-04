class EAN13Specs:
    SIDE_GUARD = '101'
    MIDDLE_GUARD = '01010'
    MIDDLE_GUARD_INDEX = 6
    LENGTH_WITHOUT_CHECKSUM = 12

    __ENCODING = {
        '0': 'llllllrrrrrr',
        '1': 'llglggrrrrrr',
        '2': 'llgglgrrrrrr',
        '3': 'llggglrrrrrr',
        '4': 'lgllggrrrrrr',
        '5': 'lggllgrrrrrr',
        '6': 'lgggllrrrrrr',
        '7': 'lglglgrrrrrr',
        '8': 'lglgglrrrrrr',
        '9': 'lgglglrrrrrr'
    }

    __LCODE = {
        '0': '0001101',
        '1': '0011001',
        '2': '0010011',
        '3': '0111101',
        '4': '0100011',
        '5': '0110001',
        '6': '0101111',
        '7': '0111011',
        '8': '0110111',
        '9': '0001011'
    }

    __GCODE = {
        '0': '0100111',
        '1': '0110011',
        '2': '0011011',
        '3': '0100001',
        '4': '0011101',
        '5': '0111001',
        '6': '0000101',
        '7': '0010001',
        '8': '0001001',
        '9': '0010111'
    }

    def getBits(self, code, number):
        if code == 'l':
            return self.__LCODE[number]
        elif code == 'g':
            return self.__GCODE[number]
        elif code == 'r':
            return self.__GCODE[number][::-1]
        else:
            raise SyntaxError

    def getCheckSum(self, code):
        checksum = 0
        for i in code[0::2]:
            checksum += int(i)
        for i in code[1::2]:
            checksum += int(i) * 3

        return str((10 - checksum%10)%10)

    def getEncoding(self, number):
        return self.__ENCODING[number]