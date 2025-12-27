class BasicTools:


    @staticmethod
    def sum_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        s = 0
        for x in args:

            s = s+ x
        return s

    @staticmethod
    def factorial_b(number):
        if number == None:
            raise ValueError("number cannot be None")
        if number < 0:
            raise ValueError("number must be equal or greater than 0")
        if type(number) != int:
            raise TypeError("number must be an int")

        k = number-1
        for x in range(number-1):
            number *= k
            k -=1
        return number


    @staticmethod
    def pow_b(a,b):
        if a ==None or b == None or a == None and b ==None:
            raise ValueError("a or b or both cannot be None")
        return a**b

    @staticmethod
    def root_b(a,b):
        if a ==None or b == None:
            raise ValueError("a or b or both cannot be None")
        if a<0 or b<0 or a<0 and b<0:
            raise ValueError("a or b or both cannot be lower than 0")
        if type(b) != int:
            raise TypeError("number must be an int")

        return a**(1/b)









