import basic_tools

class Statistics:
    @staticmethod
    def mean_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        return float(basic_tools.BasicTools.sum_b(*args))/len(args)


    @staticmethod
    def median_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        return args[int(len(args) / 2)] if len(args) % 2 != 0 and len(args) != 1 else (args[int(len(args) / 2) - 1] +args[-int(len(args) / 2)]) / 2 if len(args) % 2 == 0 and len(args) != 2 else args[0] if len(args) == 1 else sum(args) / 2

    @staticmethod
    def standard_deviation_b(*args):
        if args == None:
            raise ValueError("args cannot be None")
        results = []
        mean = Statistics.mean_b(*args)
        for x in args:
            results.append(basic_tools.BasicTools.pow_b(x-mean,2))
        return basic_tools.BasicTools.root_b(Statistics.mean_b(*results), 2)



