import dask.array as da

from dask.distributed import Client



def main() -> None:
    client: Client = Client("tcp://192.168.1.79:8786")


    x = da.random.random((40_000,40_000), chunks=(1000, 1000))
    print(da.exp(x).sum().compute())



if __name__ == "__main__":
    main()