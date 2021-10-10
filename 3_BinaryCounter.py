class BinaryCounter:
    def __init__(self, value):
        if value > 15 or value < 0:
            value = 0
        self.__value = value

    def __repr__(self):
        hex_value = hex(self.__value)
        bin_value = bin(self.__value)

        ledValue = str(bin_value)[2:]
        for x in range(len(str(bin_value)[2:]), 4):
            ledValue = "0" + ledValue
        ledString = ""
        for x in range(0, 4):
            ledString += " led" + str(4-x) + ": " + ledValue[x] + " "


        
        return str(bin_value) + " " + str(self.__value) + " " + str(hex_value) + "" + ledString
        
    def increment(self):
        self.__value += 1
        if self.__value > 15:
            self.__value = 0
        return

    def decrement(self):
        self.__value -= 1
        if self.__value < 0:
            self.__value = 15
        return



binaryCounter = BinaryCounter(0)
print("__BinaryCounter__")
print(binaryCounter)

print("\n\n__Increment__")
for x in range(0, 20):
    binaryCounter.increment()
    print(binaryCounter)

print("\n\n__Decrement__")
for x in range(0, 20):
    binaryCounter.decrement()
    print(binaryCounter)

