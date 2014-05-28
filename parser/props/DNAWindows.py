import struct

import DNAGroup


class DNAWindows(DNAGroup.DNAGroup):
    PROP_CODE = 11

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)

        self.code = ''
        self.color = (1, 1, 1, 1)
        self.windowCount = 1

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def getWindowCount(self):
        return self.windowCount

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def setWindowCount(self, count):
        self.windowCount = count

    def debug(self, message):
        if self.verbose:
            print 'DNAWindows:', message

    def traverse(self, recursive=True, verbose=False):
        data = DNAGroup.DNAGroup.traverse(self, recursive=False, verbose=verbose)

        code = self.getCode()
        data += struct.pack('>B', len(code))  # Code length
        self.debug('packing... code length: {0}'.format(len(code)))
        data += code  # Code
        self.debug('packing... code: {0}'.format(code))

        for component in self.getColor():
            data += struct.pack('f', component)  # Color
            self.debug('packing... color: {0}'.format(component))

        data += struct.pack('>B', self.getWindowCount())  # Window count
        self.debug('packing... window count: {0}'.format(self.getWindowCount()))

        return data