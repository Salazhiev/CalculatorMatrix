def matr(matrix): # рекурсивная функция(recursive function)
    first_line = matrix[0].copy() # берем первую строчку нашей матрицы(тоесть числа с первой строки у нас будут алгеброическими дополнениями)
                                  # и так будет всегда, тоесть элементы первой строки всегда будут в качестве алгеброических дополнений

                                  # we take the first line of our matrix (that is, the numbers from the first line will be algebraic additions)
                                  # and so it will always be, that is, the elements of the first line will always be as algebraic additions


    # если в процессе рекурсии мы дошли до матрицы второго порядка , то по формуле просто выводим его значение
    # if in the process of recursion we have reached the second - order matrix , then by the formula we simply output its value
    if len(matrix)==2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


    # тут перебираем элементы первой строки, тоесть first_line[i] - алгебраическое дополнение
    # here we iterate over the elements of the first line, that is, first_line[i] is an algebraic complement
    for i in range(len(first_line)):
        if i%2==0:  # снизу мы первый элемент матрицы умножаем на алгеброическое дополнение(from below we multiply the first element of the matrix by the algebraic complement)
            first_line[i] = first_line[i] * matr( [matrix[j+1][:i] + matrix[j+1][i+1:] for j in range(  len(matrix[1:])  )] )
        else:       # тут тоже самое только алгебраическое дополнение берется со знаком минус(шахматный порядок)(here, too, only the algebraic complement is taken with a minus sign (chess order))
            first_line[i] = (-1) * first_line[i] * matr( [matrix[j+1][:i] + matrix[j+1][i+1:] for j in range(  len(matrix[1:])  )] )
    return sum(first_line)



if __name__ == '__main__':
    a = int(input("Размер матрицы(Matrix Size): "))
    try:
        matrix = [list(map(int, input().split(' '))) for _ in range(a)] # собираем матрицу(assembling the matrix)
    except:
        raise ValueError('Не правильно введены данные(The data is not entered correctly)')
    for x in matrix:
        if len(x) != a:
            raise ValueError('Не правильно введены данные(The data is not entered correctly)')


    print(matr(matrix))