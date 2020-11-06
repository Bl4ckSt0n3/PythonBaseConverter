number = int(input("enter number: "))
from_base = int(input("from base: "))
to_base = int(input("to base: "))

class Converter:

    def convert_to_decimal(self):

        self.check_valid = True
        self.digit_list = [int(digits) for digits in (sorted(set(list(str(number)))))]

        for index in self.digit_list:
            if index >= from_base:
                self.check_valid = False
    
        if self.check_valid == True:
            self.result = 0
            self.length = len(str(number)) - 1

            for num in str(number):
                self.result  += int(num) * (from_base ** self.length)
                self.length -= 1
            return self.result

        elif self.check_valid == False:
            return "invalid number"

    def convert_from_decimal(self, number1): 

        self.number1 = number1
        self.stack = []
        self.hex_dict = {10 : 'A' , 11 : 'B' , 12 : 'C' , 13 : 'D' , 14 : 'E' , 15 : 'F'}

        if self.convert_to_decimal() == "invalid number":
            print("invalid number !")

        else:

            while number1 > 0:
                self.reminder = number1 % to_base
                number1 = number1 // to_base
                self.stack.append(self.reminder)

            self.stack = self.stack[::-1]

            if to_base > 10:
                for index in range(len(self.stack)):
                    for key, value in self.hex_dict.items():
                        if self.stack[index] == key:
                            self.stack[index] = value

            print("".join([str(i) for i in self.stack]))

c = Converter()
c.convert_from_decimal(c.convert_to_decimal())

