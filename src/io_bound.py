import requests
import pathlib
from rich import print

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

if __name__ == "__main__":
    base = pathlib.Path("./data/images")
    base.mkdir(exist_ok=True, parents=True)
    for image_url in images:
        print(f"read {image_url}")
        image = requests.get(image_url)
        (base / image_url.split("/")[-1]).write_bytes(image.content)
        print(f"wrote {image_url}")
