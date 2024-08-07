import numpy as np
import pandas as pd
import dask.dataframe as dd
from dask import delayed
import dask 




def main():
    data_dict = {
        'a': np.arange(5000),
        'b': np.random.randn(5000),
        'c': np.random.choice(['a', 'b', 'c'], 5000)
    }
    
    df: pd.DataFrame = pd.DataFrame(data_dict)


    ddf: Unknown| Array | any = dd.from_pandas(df, npartitions=10)
    

    # ddf.partitions[1].compute() # has been called only second partition and printed - because of compute function, result is pandasDataframe


    sum_df = ddf.groupby('c').sum()
    # print(sum_df.compute())

    mean_df: Unknown | any = ddf.groupby('c').mean() +10 
    
    #mean_df.visualize()

    @dask.delayed
    def increment(x: int) -> int:
        return x + 1
    

    @dask.delayed
    def add(x:int, y:int) -> int:
        return x + y
    

    a: Unknown | Delayed = increment(1)
    b: Unknown | Delayed = increment(2)

    c: Unknown | Delayed = add(a, b)

    c: Unknown = c.compute()

    print(c)



                



    












if __name__ == "__main__":
    main()