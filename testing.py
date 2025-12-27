from sorting import Sorting
from stats import Statistics
from basic_tools import BasicTools
import random
import math
import statistics

class Generator:
    @staticmethod
    def gen_one():
        return random.uniform(1,100)

    @staticmethod
    def gen_more():
        x = []
        for i in range(random.randint(2,5)):
            x.append(random.uniform(1,5))
        return x

    @staticmethod
    def gen_int():
        return random.randint(1, 5)


def test():
    a, b = Generator.gen_one(), Generator.gen_one()
    c = Generator.gen_more()
    d = Generator.gen_int()
    return statistics.mean([BasicTools.sum_b(*c)/sum(c), BasicTools.factorial_b(d)/math.factorial(d), BasicTools.pow_b(a,b)/pow(a,b), BasicTools.root_b(a,d)/a**1/d, Statistics.mean_b(*c)/statistics.median(c), Statistics.mean_b(*c)/statistics.mean(c), Statistics.standard_deviation_b(*c)/statistics.stdev(c), Sorting.min_b(*c)/min(c), Sorting.max_b(*c)/max(c)])

def run():
    print(f"Avarage correctness : {test()}")


if __name__ == "__main__":
    run()



