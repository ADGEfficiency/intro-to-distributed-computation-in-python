# Distributed Computation in Python

![](./assets/lyttleton.jpg)

<div>
<center>
<i>Lyttleton Harbour, N.Z., Inside the Breakwater - John Gib - 1886</i>
<br />
<i>Photographed at the Christchurch Art Gallery in 2016</i>
</center>
<br />
</div>

---

Two hour tutorial at Kiwi Pycon 2022 in Ōtautahi (Christchurch) New Zealand - [tutorial recording](https://www.youtube.com/watch?v=x_NBHIi-Yf0).

Covers the foundations needed to be effective with running computation across many workers.


## About Me

Senior Data Scientist @ Orkestra Energy - I live in Christchurch - [LinkedIn](https://www.linkedin.com/in/adgefficiency/) - [blog](https://adgefficiency.com/).


## Outcomes Of This Tutorial

- functional programming fundamentals - `map`, `filter`, `functools.reduce`,
- CPU cores, threads & processes,
- concurrency, parallelism & asynchrony,
- why & how to use `multiprocessing` and `asyncio`,
- introduction to the ecosystem for distributing compute over many machines in Python,
- demonstration of using an EC2/Dask/Coiled/Prefect stack to deploy a Dask cluster to EC2.


## Agenda

### 1. Functional Programming - [run in binder](https://mybinder.org/v2/gh/ADGEfficiency/intro-to-distributed-computation-in-python/HEAD?labpath=notebooks%2F1-functional-programming.ipynb)

*20 min theory, 20 min practical*

Warmup session introducing functional programming in Python.


### 2. Single Machine - [run in binder](https://mybinder.org/v2/gh/ADGEfficiency/intro-to-distributed-computation-in-python/HEAD?labpath=notebooks%2F2-single-machine.ipynb)

*30 min theory, 20 min practical*

Options for distributing computation on a single machine with the Python standard library - doing many things at once on single machine.

- threads & `threading`, processes & `multiprocessing`, `asyncio`,
- why not to used threads in Python (possible but dangerous),
- `multiprocessing` for CPU bound tasks,
- `asyncio` for IO bound tasks,
- 3 short exercises & one large exercise,


### 3. Many Machines - [read in binder](https://mybinder.org/v2/gh/ADGEfficiency/intro-to-distributed-computation-in-python/HEAD?labpath=notebooks%2F3-many-machines.ipynb)

*10 min theory, 15 min demonstration, balance practical*

- options for distributing computation on the cloud (many machines) in Python, 
- demonstration of distributing compute over an AWS EC2 cluster with Dask, Coiled & Prefect,
- note that this notebook `3-many-machines` will not run in Binder - you can run locally combined with a `$ pip install -r requirements-coiled.txt`.


## Setup

As this repo targets two environments (Binder & Coiled):

- `requirements.txt` = Binder (important to not install Dask in Binder),
- `requirements-coiled.txt` = Coiled (will run on EC2 instances),
- `requirements-coiled.txt` = local development.

Python version is important for Dask/Coiled.

To setup Python locally:

```shell
$ make setup
```
