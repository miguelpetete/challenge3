dictionary = {}

def collatz(n):
    sequence = []
    sequence.append(n)
    while n > 1:
        if (n % 2):
            n = 3*n + 1
            sequence.append(n)
        else:
            n = n//2
            sequence.append(n)
    return sequence
 
 
n = int(input('Enter n: '))
seq = collatz(n)
print(seq)

def recorrido(n):
    l=0
    x=0
    s=[]
    for i in range(n):
        sequence = collatz(i)
        if len(sequence)>l:
            l = len(sequence)
            x = i
            s = sequence
    return[l,x,s]

var = recorrido(500)
print(f"Secuencia más larga proveniente de {var[1]} con longitud {var[0]}")
print(var[2])