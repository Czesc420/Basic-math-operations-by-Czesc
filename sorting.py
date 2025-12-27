class Sorting:
    @staticmethod
    def min_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        min = args[0]
        for x in args:
            if min > x:
                min = x
        return min
    @staticmethod
    def max_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        max = args[0]
        for x in args:
            if max < x:
                max = x
        return max

    @staticmethod
    def sort_asc(*args):
        if args == None:
            raise ValueError("args cannot be None")
        arg = [*args]
        after_sort = []
        for x in  range(len(arg)):
            after_sort.append(Sorting.min_b(*arg))
            arg.remove(Sorting.min_b(*arg))
        return after_sort

    @staticmethod
    def sort_desc(*args):
        if args == None:
            raise ValueError("args cannot be None")
        arg = [*args]
        after_sort = []
        for x in range(len(arg)):
            after_sort.append(Sorting.max_b(*arg))
            arg.remove(Sorting.max_b(*arg))
        return after_sort


