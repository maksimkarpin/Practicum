print("задание 01")#Разглаживание вложенных списков
def flatten_list(x):
    while x:
        num = x.pop(0)
        if isinstance(num, list):
            x = num + x
        else:
            yield num
print(list(flatten_list([1, 2, [3, 4, [5, 6]], 7, [8]])))
print(list(flatten_list([1, [2, [3, [4, [5, [6, [7, [8,[9, [0]]]]]]]]]])))
print(list(flatten_list([1, 2, 3.14, 4, 5, 6, 7 , 8, 9] )))

print("задание 02")#По следам четных чисел:Количество четных чисел во вложенных списках
def  count_even_numbers(x):
    num=[]
    num=x
    num2=[]
    for i in num:
        if isinstance(i, list):
            num.extend(i)
        else:
            num2.append(i)
    e_nim=[]
    for j in num2:
        if j%2==0:
            e_nim.append(j)
        else:
            continue
    return len(e_nim)
print(count_even_numbers([1, 2, [3, 4, [5, 6]], 7, [8]] ))
print(count_even_numbers([1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]] ))
print(count_even_numbers([1, 2, 3.14, 4, 5, 6, 7 ] ))

print("задание 03")#Поддиагональная сумма
def sum_matrix_second_diagonal(x):
    sum_=[]
    sum1=[]
    sum_.append(x[1::1])
    for i in sum_:
        if isinstance(i,list):
            sum1.extend(i)
    a=0
    Sum = []
    for i in sum1:
        Sum.append(i[a])
        a+=1
    result = sum(Sum)
    return result
print(sum_matrix_second_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]] ))
print(sum_matrix_second_diagonal([[1, 2], [7, 8]]  ))
print(sum_matrix_second_diagonal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(sum_matrix_second_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] ))

print("задание 04")#Матричное умножение
def multiply_matrices(matrix1, matrix2):
    Zero=[]
    x1=[]
    x2=[]
    x1.extend(matrix1)
    x2.extend(matrix2)
    X1=[]
    X2=[]
    for i in x1:
        X1.extend(i)
    for i in x2:
        X2.extend(i)
    if len(X1) != len(X2):
        return Zero
    M=len(x1)
    N=len(x2)
    K=int(len(X2)/len(x2))

    result=[' '*M for _ in range(K)]



    return X1,X2,x1,x2,'!',result,'!'

print(multiply_matrices(matrix1 =  [[1, 2, 3,], [4, 5, 6]],
                        matrix2 = [[7, 8], [9, 10], [11, 12]]))
print(multiply_matrices(matrix1 =  [[1, 2, 3], [4, 5, 6]],
                        matrix2 = [[7, 8], [9, 10], [11, 12]]))
print(multiply_matrices(matrix1 =  [[1, 2], [3, 4], [5, 6]],
                        matrix2 = [[7, 8, 9], [10, 11, 12]]))