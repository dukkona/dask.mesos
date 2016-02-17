from dask_mesos.mesos import get
from dask_mesos.imperative import mesos
from dask import set_options
from dask.imperative import do

@do
def inc(x):
    return x+1

@mesos(cpus=1)
def add(x, y):
    return x+y

@mesos(mem=64)
def mul(x, y):
    return x*y


with set_options(get=get):
    x = inc(666)
    y = mul(666, 777)
    print add(y, x).compute()
