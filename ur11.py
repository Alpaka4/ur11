##Array5. Дано целое число N (> 2). Сформировать и вывести целочисленный
##массив размера N, содержащий N первых элементов последовательности
##чисел Фибоначчи FK:
##F1 = 1, F2 = 1, FK = FK−2 + FK−1, K = 3, 4, . . . .
##lst=[1,1]
##n=int(input())
##for i in range(n-2):
##    size = len(lst)
##    lst.append(lst[size-1]+lst[size-2])
##print(lst)
##Array6. Даны целые числа N (> 2), A и B. Сформировать и вывести целочисленный массив размера N, первый элемент которого равен A, второй
##равен B, а каждый последующий элемент равен сумме всех предыдущих.
##lst=[]
##n=int(input())
##a=int(input())
##b=int(input())
##lst.append(a)
##lst.append(b)
##for i in range(n-2):
##    size = len(lst)
##    lst.append(lst[size-1]+lst[size-2])
##print(lst)
#Array7◦
#. Дан массив размера N. Вывести его элементы в обратном порядке
##import random
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##lst.reverse()
##print(lst)
###Array8. Дан целочисленный массив размера N. Вывести все содержащиеся в
###данном массиве нечетные числа в порядке возрастания их индексов, а
###также их количество K.
##import random
##lst=[]
##n=int(input())
##nech=0
##for i in range(n):
##    lst.append(random.randint(1,100))
##    if lst[i]%2!=0:
##        print(lst[i], end=" ")
##        nech+=1
##print( lst)
##print(nech)
##Array9. Дан целочисленный массив размера N. Вывести все содержащиеся в
##данном массиве четные числа в порядке убывания их индексов, а также
##их количество K.
##import random
##lst=[]
##n=int(input())
##ch=0
##for i in range(n):
##    lst.append(random.randint(1,100))
##    if lst[i]%2==0:
##        print(lst[i], end=" ")
##        ch+=1
##lst.reverse()
##print( )
##print( lst)
##print(ch)
###Array10. Дан целочисленный массив размера N. Вывести вначале все содержащиеся в данном массиве четные числа в порядке возрастания их индексов,
###а затем — все нечетные числа в порядке убывания их индексов.
##import random
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##    if lst[i]%2==0:
##        print(lst[i], end=" ")
##lst.reverse()
##print( )
##for i in range(n):
##    if lst[i]%2!=0:
##        print(lst[i], end=" ")
##lst.reverse()
##print( )
##print( lst)
###Array11. Дан массив A размера N и целое число K (1 ≤ K ≤ N). Вывести элементы массива с порядковыми номерами, кратными K: AK, A2·K, A3·K, . . . .
###Условный оператор не использовать.
##import random
##lst=[]
##n=int(input())
##k=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##for i in range(k,n,k):
##    print(lst[i])
##print(lst)
##Array12. Дан массив A размера N (N — четное число). Вывести его элементы
##с четными номерами в порядке возрастания номеров: A2, A4, A6, . . ., AN .
##Условный оператор не использовать.   
##import random
##print("введите ЧЁТНЫЙ  размер списка")
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##for i in range(2,n,2):
##    print(lst[i])
##print(lst)
##Array13. Дан массив A размера N (N — нечетное число). Вывести его элементы
##с нечетными номерами в порядке убывания номеров: AN , AN−2, AN−4, . . .,
##A1. Условный оператор не использовать
##import random
##print("введите НЕЧЁТНЫЙ  размер списка")
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##lst.reverse()
##for i in range(1,n,2):
##    print(lst[i])
##lst.reverse()
##print(lst)
##Array14. Дан массив A размера N. Вывести вначале его элементы с четными
##номерами (в порядке возрастания номеров), а затем — элементы с нечетными номерами (также в порядке возрастания номеров):
##A2, A4, A6, . . ., A1, A3, A5, . . . .
##Условный оператор не использовать.
##import random
##lst=[]
##n=int(input())
##for i in range(n):
##    lst.append(random.randint(1,100))
##for i in range(2,n,2):
##    print(lst[i], end=" ")
##print( )
##for i in range(1,n,2):
##    print(lst[i], end=" ")
##print( )
##print(lst)
##Array15. Дан массив A размера N. Вывести вначале его элементы с нечетными номерами в порядке возрастания номеров, а затем — элементы с четными
##номерами в порядке убывания номеров:
##A1, A3, A5, . . ., A6, A4, A2.
##Условный оператор не использовать.
##import random
##lst=[]
##n=int(input("Нечетное число - размер массива"))
##for i in range(n):
##    lst.append(random.randint(1,100))
##for i in range(1,n,2):
##    print(lst[i], end=" ")
##print( )
##for i in range(n-1,0,-2):
##    print(lst[i], end=" ")
##print( )
##print(lst)
#Array16. Дан массив A размера N. Вывести его элементы в следующем порядке:
#A1, AN , A2, AN−1, A3, AN−2, . . . .
##import random
##lst=[]
##n=int(input())
##lastindex=len(lst)-1
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(0,len(lst)//2):
##    print(lst[i])
##    print(lst[lastindex-i])
##Array17. Дан массив A размера N. Вывести его элементы в следующем порядке:
##A1, A2, AN , AN−1, A3, A4, AN−2, AN−3, . . . .
##import random
##lst=[]
##n=int(input())
##lastindex=len(lst)-1
##for i in range(n):
##    lst.append(random.randint(1,100))
##print(lst)
##for i in range(0,len(lst)//2,2):
##    print(lst[i])
##    print(lst[i+1])
##    print(lst[lastindex-i])
##    print(lst[lastindex-i-1])
##Array18. Дан массив A ненулевых целых чисел размера 10. Вывести значение
##первого из тех его элементов AK, которые удовлетворяют неравенству
##AK < A10. Если таких элементов нет, то вывести 0.
import random
lst=[]
size=len(lst)
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)
for i in range(10):
    if lst[i]<lst[size-1]:
        print(lst[i])
    elif lst[i]>lst[size-1]:
        print(0)
