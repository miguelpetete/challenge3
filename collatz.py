import time

dictionary = {}

def collatz(num,cache=None):
    sequence = []
    sequence.append(num)
    while sequence[-1] != 1: 
        n = sequence[-1]
        if cache is not None: 
            if n in cache:
                sequence = sequence + cache[n]
                break
        if(n%2):
            n = 3*n + 1
            sequence.append(n)
        else: 
            n = n//2
            sequence.append(n)
    if cache is not None:
        cache[num] = sequence
    print(cache)
    return sequence

"""
n = int(input('Please, give a number: '))
seq = collatz(n,dictionary)
print(seq)
"""

def first_of_n(n,cache=None):
    l = 0
    x = 0
    for i in range(n): 
        sequence = collatz(n,cache)
        if len(sequence) > l: 
            l = len(sequence)
            x = i
        
    #print(f"{x} gives largest sequence with a length of: {l}")


t1 = time.time()
first_of_n(25, dictionary)
t2 = time.time()
#first_of_n(5000, dictionary)
t3 = time.time()

t4 = time.time()
#first_of_n(500)
t5 = time.time()
#first_of_n(5000)
t6 = time.time()

time1 = t2 - t1
time2 = t3 - t2

time3 = t5 - t4
time4 = t6 - t5

#print(f"Function 1 with cache took {time1} to complete")
#print(f"Function 1 without cache took {time3} to complete")
#print(f"Function 2 with cache took {time2} to complete")
#print(f"Function 2 without cache took {time4} to complete")

speedup1 = time3/time1
speedup2 = time4/time2

#print(f"Speedup funcion 1 = {speedup1}")
#print(f"Speedup funcion 2 = {speedup2}")

#print(dictionary)