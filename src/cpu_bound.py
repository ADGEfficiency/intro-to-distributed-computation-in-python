import pathlib
import numpy as np
import scipy
import cv2
import multiprocessing


def cpu_compute_task(image, channel=2):
    channel = image[:, :, channel]
    transformed = scipy.signal.convolve2d(channel, np.random.randint(-2, 2, 4).reshape(2, 2))
    scipy.fft.ifftn(channel)

   
def load_images(scale=2):
    images = [p for p in pathlib.Path("./assets/").iterdir() if p.suffix == ".png"]
    return [cv2.imread(str(p)) for p in images] * scale


if __name__ == '__main__':
    for n, image in enumerate(load_images()):
        print(f" image {n}")
        for channel in range(len(image.shape)):
            print(f" channel {channel}")
            cpu_compute_task(image, channel)
