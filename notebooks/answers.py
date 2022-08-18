#  1-functional-programming.ipynb

import functools
from helpers import get_populations

populations = get_populations()


def answer_total_population_pacific():
    """
    sum the total population for the `pac` continent using map, filter, functools.reduce
    """
    print(
        functools.reduce(
        lambda total, x: x.population + total,
        filter(lambda c: c.continent == 'pac', populations),
        0
    )
    )


def answer_only_top_half():
    """
    Create a data processing pipeline that selects the cities that have populations greater than the average of all cities
    """

    def avg(total, nxt):
        return (total[0]+nxt[1], total[1]+1)

    total = functools.reduce(avg, populations, (0, 0))

    # total = tuple(sum, count)
    mean = total[0] / total[1]

    list(filter(lambda x: x.population > mean, populations))

    #  You can also do this in a single reduce by incrementally updating the mean
    # state = (mean, num)
    def incremental_mean(state, nxt):
        state[1] += 1
        state[0] = state[0] + (nxt.population - state[0]) / state[1]
        return state

    print(functools.reduce(incremental_mean, populations, [0, 0])[0])


def answer_average_population_continent():
    """
    Create a data processing pipeline that finds the average population for both continents:
    """
        
    def gb(acc, city):
        acc[city.continent].append(city.population)
        return acc# acc is initialized as a dict here (see below)

    pop_cont = functools.reduce(
        gb,
        populations,
        {'eu': [], 'pac': []}
    )

    print(list(map(lambda kv: (kv[0], sum(kv[1]) / len(kv[1])), pop_cont.items())))


if __name__ == '__main__':
    answer_total_population_pacific()
    answer_only_top_half()
    answer_average_population_continent()
