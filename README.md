# Distributed Computation in Python

Two hour tutorial at Kiwi Pycon 2022 in Ōtautahi (Christchurch) New Zealand.

Covers the foundations needed to be effective with running intelligent computation across many workers.


## About Me

Senior Data Scientist @ Orkestra Energy - live in Christchurch - [LinkedIn](https://www.linkedin.com/in/adgefficiency/) - [blog](https://adgefficiency.com/).


## Outcomes

What you will get out of this tutorial:

- functional programming fundamentals,
- why & how to use `multiprocessing` and `asyncio`,
- concurrency, parallelism & asynchrony,
- understand the ecosystem for distributing compute over many machines in Python,
- know how to deploy a Dask cluster on EC2.


## Agenda

### 1. Functional programming - [run in binder](https://mybinder.org/v2/gh/ADGEfficiency/intro-to-distributed-computation-in-python/HEAD?labpath=notebooks%2F1-functional-programming.ipynb)

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

We are targeting three environments:

- `requirements.txt` = Binder (important to not install Dask),
- `requirements-coiled.txt` = Coiled + local development (everything).

Python version is important for Dask/Coiled.

```shell
$ conda create -n pycon python=3.8.13
$ make setup
```
