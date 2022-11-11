import time
dictionary = {}

def collatz(n,cache=None):
    sequence = []
    sequence.append(n)
    while n > 1:
        if (n % 2):
            n = 3*n + 1
            if cache != None:
                if n in cache.keys(): 
                    sequence = sequence + cache[n]
                    return sequence
            else:
                sequence.append(n)
        else:
            n = n//2
            if cache != None:
                if n in cache.keys(): 
                    sequence = sequence + cache[n]
                    return sequence
            else:
                sequence.append(n)
    return sequence

def recorrido_opt(n,cache=None):
    l=0
    x=0
    s=[]
    for i in range(n):
        sequence = collatz(i,cache)
        if not cache == None:
            if i not in cache.keys():
                cache[i] = sequence
        if len(sequence)>l:
            l = len(sequence)
            x = i
            s = sequence
    return[l,x,s]

n = int(input('Please, give a number, we will give you the collatz sequece: '))
seq = collatz(n) 
print(seq)

t1 = time.time()
n1 = recorrido_opt(500)
t2 = time.time()
n2 = recorrido_opt(5000)
t3 = time.time()
n3 = recorrido_opt(500,dictionary)
t4 = time.time()
n4 = recorrido_opt(5000,dictionary)
t5 = time.time()

p1 = t2 - t1
p2 = t3 - t2
p3 = t4 - t3
p4 = t5 - t4

print(f"Without optimitation and n = 500, time: {p1}")
print(f"Without optimitation and n = 5000, time: {p2}")
print(f"With optimitation and n = 500, time: {p3}")
print(f"With optimitation and n = 5000, time: {p4}")

speedup1 = p3/p1
speedup2 = p4/p2

print(f"Speedup in case of n = 500 -> {speedup1}")
print(f"Speedup in case of n = 5000 -> {speedup2}")
