#  1-functional-programming.ipynb

from rich import print
import asyncio
import functools
import pathlib

import numpy as np
import scipy
import cv2
import multiprocessing

from helpers import get_populations

populations = get_populations()


def answer_total_population_pacific():
    """
    sum the total population for the `pac` continent using map, filter, functools.reduce
    """
    print(
        functools.reduce(
            lambda total, x: x.population + total,
            filter(lambda c: c.continent == "pac", populations),
            0,
        )
    )


def answer_only_top_half():
    """
    Create a data processing pipeline that selects the cities that have populations greater than the average of all cities
    """

    def avg(total, nxt):
        return (total[0] + nxt[1], total[1] + 1)

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
        return acc  # acc is initialized as a dict here (see below)

    pop_cont = functools.reduce(gb, populations, {"eu": [], "pac": []})

    print(list(map(lambda kv: (kv[0], sum(kv[1]) / len(kv[1])), pop_cont.items())))


#  2-single-machine.ipynb
def cpu_compute_task(image, channel=2):
    channel = image[:, :, channel]
    transformed = scipy.signal.convolve2d(
        channel, np.random.randint(-2, 2, 4).reshape(2, 2)
    )
    scipy.fft.ifftn(channel)


def load_images(scale=2):
    images = [p for p in pathlib.Path("./assets/").iterdir() if p.suffix == ".png"]
    return [cv2.imread(str(p)) for p in images] * scale


def answer_cpu_bound_problem():
    """
    there are a few solutions here - this is the `most flat` one

    I don't think it's the fastest (?)
    """
    images = load_images()
    channels = []
    for image in images:
        for channel in range(len(image.shape)):
            channels.append((image, channel))

    with multiprocessing.Pool(4) as pool:
        pool.starmap(cpu_compute_task, channels)


async def answer_io_bound_problem():
    images = [
        "https://media.nga.gov/iiif/b1461d28-88d4-4aee-88dd-a78d368308ff/full/full/0/default.jpg?attachment_filename=a_creek_in_st._thomas_%28virgin_islands%29_1985.64.29.jpg",
        "https://media.nga.gov/iiif/b94db39d-9c08-4e31-9373-a042b662ead6/full/full/0/default.jpg?attachment_filename=the_beach_at_villerville_1963.10.4.jpg",
        "https://media.nga.gov/iiif/4a3e29f1-a598-4902-b75e-f1061d4f5543/full/full/0/default.jpg?attachment_filename=jetty_and_wharf_at_trouville_1983.1.9.jpg",
        "https://media.nga.gov/iiif/84c9243d-d667-424c-8351-c51573553083/full/full/0/default.jpg?attachment_filename=the_cradle_-_camille_with_the_artist%27s_son_jean_1983.1.25.jpg",
        "https://media.nga.gov/iiif/579777b9-33fb-493e-8e2c-89b972019854/full/full/0/default.jpg?attachment_filename=sainte-adresse_1990.59.1.jpg",
        "https://media.nga.gov/iiif/97460341-dbc0-4d49-84fa-cf52b6ca7324/full/full/0/default.jpg?attachment_filename=the_western_ramparts_at_aigues-mortes_1985.64.1.jpg",
        "https://media.nga.gov/iiif/aca3980f-d5bc-44cb-940d-791f9e8efc88/full/full/0/default.jpg?attachment_filename=madame_camus_1963.10.121.jpg",
        "https://media.nga.gov/iiif/3aabc076-e658-48c9-b48c-d6ce8a868bde/full/full/0/default.jpg?attachment_filename=coast_of_brittany_1983.1.11.jpg",
        "https://media.nga.gov/iiif/4cecf562-4ced-4cfa-92bf-b6a32ce4cff3/full/full/0/default.jpg?attachment_filename=horses_in_a_meadow_1995.11.1.jpg",
    ]

    await asyncio.gather(*[download_one_image(image_url) for image_url in images])


async def download_one_image(image_url):
    import httpx

    base = pathlib.Path("./data/images")
    base.mkdir(exist_ok=True, parents=True)
    print(f"read {image_url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)
    (base / image_url.split("/")[-1]).write_bytes(response.content)
    print(f"wrote {image_url}")


if __name__ == "__main__":
    # answer_total_population_pacific()
    # answer_only_top_half()
    # answer_average_population_continent()
    # answer_cpu_bound_problem()
    asyncio.run(answer_io_bound_problem())
