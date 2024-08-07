from __future__ import annotations
import time 
import random

import dask
from dask import delayed


import numpy


def increment(x: int | float) -> int | float:
    return x + 1


def double(x: int | float) -> int | float:
    return x * 2



def add(x: int | float, y: int | float) -> int | float: 
    return x + y



data: list[int] = [1,2,3,4,5] 

output: list[Unknown] = []



for x in data:
    a: int | float = increment(x)
    b: int | float = double(x)
    c: int | float = add(a,b)

    output.append(c)

total: int = sum(output)

print(f"{total=}")




@delayed
def delayed_increment(x: int | float) -> int | float:
    return x + 1

@delayed
def delayed_double(x: int | float) -> int | float:
    return x * 2


@delayed
def delayed_add(x: int | float, y: int | float) -> int | float: 
    return x + y



delayed_output: list[Unknown] = []

for x in data:
    a: Unknown | Delayed = delayed_increment(x)
    b: Unknown | Delayed = delayed_double(x)
    c: Unknown | Delayed = delayed_add(a,b)


    delayed_output.append(c)

delayed_total: int = delayed(sum)(delayed_output)


print(f"{delayed_total.compute()=}")


delayed_total.visualize()


#Advice

# results will be different because of the unparalelization, random sleep function converts timeline of execution of functions.
@delayed(pure=False)
def adder(x -> np.ndarray) -> np.ndarray:
    time.sleep(random.random())
    #x += 1 #DONT DO THIS
    x = x + 1
    return x

@delayed(pure=False)    
def doubler(x -> np.ndarray) -> np.ndarray:
    time.sleep(random.random())
    #x *= 2 #DONT DO THIS
    x = x * 2
    return x

results: list[Unknown] = []

for _ in range(10):
    x: np.ndarray[Unknown, Unknown] = np.ones(10)
    y: np.ndarray = doubler(x) + adder(x)
    results = append(y)


results = dask.compute(*results)
print(f"{results=}")







#advice 2

# whole function should be inclued only one job. then fuctions be able to be gathered one new function. 


@delayed
def load(filename: str) -> np.ndarray:
    return np.load(filename)

@delayed
def process(data) -> np.ndarray:
    return np.exp(data)

@delayed
def save(filename, data) -> None:
    np.save(filename, data)


#işte bu fonksiyon paralelize olabilicek şuannn !
# @delayed , no need decorator 
def good_function(filename: str) -> None:
    for _ in enumerate(filename):

        data = load(filename)
        processed = process(data)
        save(filename, processed)



    

























