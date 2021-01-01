
class Calculator:
    def __init__(self, number):
        self.number= number

    def __add__(self,other):
        if isinstance(self.number, float) or isinstance(other.number, float):
            value = float(self.number)+ float(other.number)
            return value

        return self.number + other.number
    
    def subtract(self,other):
        pass
    
    def multiply(self,other):
        return self.number * other.number

    def divide(self,other):
        try:
            return self.number / other.number
        except ZeroDivisionError:
            print('You can not divide by ZERO')



#Testing the Calculator functionality
# num1= Calculator(8)
# num2= Calculator(4)
# num3= Calculator(3)

# num1= Calculator(num1+num2)
# print(num1.multiply(num3))
