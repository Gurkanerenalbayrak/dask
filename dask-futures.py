from __future__ import annotations
import time 


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor #Python'da paralel yürütmeyi kolaylaştıran bir araç seti sunar.


from dask.distributed import Client

def multiply_by_two(inp: int | float ) -> int | float:
    time.sleep(1)
    return inp * 2



outputs =  []
start: float = time.time() 

for inp in range(10):
    output = multiply_by_two(inp)
    outputs.append(output)

end: float = time.time()


print(outputs)
print(f"it took {end-start:.2f}s to execute the loop.")



futures: list[Unknown] = [] # Bu kısımda bir futures listesi oluşturuyorsunuz. 
#Bu liste, daha sonra işlerin sonuçlarını saklayacak Future nesnelerini içerecek. Ayrıca, 
#işlem süresini ölçmek için start değişkenine geçerli zaman atanıyor.
start: float = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    for inp in range(10):
        future: Future[int|float] = executor.submit(multiply_by_two, inp)

        print(f"is it still runnging? {future.running()}")
        print(f"is it still runnging? {future.done()}")
        futures.append(future)
    outputs: list[Unknown] = [future.result() for future in futures]
end: float = time.time()
print(outputs)
print(f"it took {end-start:.2f}s to execute the loop.")



with ProcessPoolExecutor(max_workers=5) as executor:
    for inp in range(10):
        future: Future[int|float] = executor.submit(multiply_by_two, inp)

        print(f"is it still runnging? {future.running()}")
        print(f"is it still runnging? {future.done()}")
        futures.append(future)
    outputs: list[Unknown] = [future.result() for future in futures]
end: float = time.time()
print(outputs)
print(f"it took {end-start:.2f}s to execute the loop.")



"""
ThreadPoolExecutor: Bu, Python'un concurrent.futures modülünden bir sınıftır ve çok iş parçacıklı (multithread) 
işlerin havuz tabanlı bir sistemle yürütülmesini sağlar.
 Yani, birden fazla iş parçacığını (thread) aynı anda çalıştırabilirsiniz.

Future: Bu, bir işin (task) sonucunu temsil eden bir nesnedir. Bir Future nesnesi, işin henüz tamamlanmamış olduğunu ama tamamlandığında sonucunu döndüreceğini gösterir.
Future nesnesini kullanarak işin durumunu kontrol edebilir ve sonucunu alabilirsiniz.

"""
#--------------------------------------------
#DASK client IMPLEMENTATION 

if __name__ == "__main__":
    Client: Client = Client()

    futures = []
    start = time.time()
    for inp in range(10):
        future = client.submit(multiply_by_two, inp)
        futures.append(future)                        # map method

    outputs = [future.result() for future in futures] #gather method
    end = time.time()
    print(outputs)
    print(f"it took {end-start:.2f}s to execute the loop.")
#--------------------------------------------
# for loop yerine client map fonksiyonu ile işi çözüyoruz 

start = time.time()
inputs= list(range(10))
futures = client.map(multiply_by_two, inputs)
outputs = client.gather(futures)
end = time.time()

print(outputs)
print(f"it took {end-start:.2f}s to execute the loop.")

# if i dont want to be see in my memory,

del futures     

#--------------------------------------------


start = time.time()
inputs= list(range(10))
remote_inputs = client.scatter(multiply_by_two, inputs)
futures = client.map(multiply_by_two, remote_inputs)
outputs = client.gather(futures)
end = time.time()
print(outputs)
print(f"it took {end-start:.2f}s to execute the loop.")

del remote_futures
del future


#--------------------------------------------