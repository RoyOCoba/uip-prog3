## Programa que sume los numeros pares desde 10 hasta 5000 sin sumar 100 y 1000.
n=10
p=0
while n<=5000:
    if n%2==0:
        p+=n
    n+=1
print("La suma de todos los pares es igual a", p-1100)
