def determinant_recursion(matrix): # Рекурсивная функция(recursive function).
    first_line = matrix[0].copy() # Берем первую строчку нашей матрицы(тоесть числа с первой строки у нас будут алгеброическими дополнениями)
    # и так будет всегда, тоесть элементы первой строки всегда будут в качестве алгеброических дополнений.

    # We take the first line of our matrix (that is, the numbers from the first line will be algebraic additions)
    # and so it will always be, that is, the elements of the first line will always be as algebraic additions.


    # Если в процессе рекурсии мы дошли до матрицы второго порядка , то по формуле просто выводим его значение.
    # If in the process of recursion we have reached the second - order matrix , then by the formula we simply output its value.
    if len(matrix)==2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


    # Тут перебираем элементы первой строки, тоесть first_line[i] - алгебраическое дополнение.
    # Here we iterate over the elements of the first line, that is, first_line[i] is an algebraic complement.
    for i in range(len(first_line)):
        if i%2==0:  # Снизу мы первый элемент матрицы умножаем на алгеброическое дополнение(from below we multiply the first element of the matrix by the algebraic complement).
            first_line[i] = first_line[i] * determinant_recursion( [matrix[j+1][:i] + matrix[j+1][i+1:] for j in range(  len(matrix[1:])  )] )
        else:       # Тут тоже самое только алгебраическое дополнение берется со знаком минус(шахматный порядок)(here, too, only the algebraic complement is taken with a minus sign (chess order)).
            first_line[i] = (-1) * first_line[i] * determinant_recursion( [matrix[j+1][:i] + matrix[j+1][i+1:] for j in range(  len(matrix[1:])  )] )
    return sum(first_line)




if __name__ == '__main__':
    a = int(input("Размер матрицы(Matrix Size): "))
    try:
        matrix = [list(map(int, input().split(' '))) for _ in range(a)] # Собираем матрицу(assembling the matrix).
    except:
        raise ValueError('Не правильно введены данные(The data is not entered correctly)')
    for x in matrix:
        if len(x) != a:
            raise ValueError('Не правильно введены данные(The data is not entered correctly)')

    determinant = determinant_recursion(matrix) # Определитель исходной матриц.
    if determinant == 0:
        raise ValueError('Матрицы у которых определитель равен 0, нет обратной матрицы')



    # 1
    # Скелет транспонированной матрицы алгеброических дополнений.
    # The skeleton of the transposed matrix of algebraic complements.
    new_matrix = [ [0] * a for _ in range(a)]
    for line in range( len(matrix) ): # Перебираем все элементы нашей матрицы(We iterate through all the elements of our matrix).
        for column in range( len(matrix[line]) ):
            # В новую пустую матрицу мы добавляем новые элементы: поочередно вырезаем строки и столбцы нашей матрицы, и находим определитель этих новый матриц.
            # We add new elements to the new empty matrix: we cut out the rows and columns of our matrix one by one, and find the determinant of these new matrices.
            new_matrix[line][column] = (-1 if (line+column)%2==1 else 1) *\
                                       determinant_recursion( [matrix[line_][:column]+matrix[line_][column+1:] for line_ in range(len(matrix)) if line_!=line] )


    # 2
    # Далее мы транспонируем нашу матрицу, однако хочу обратить ваше внимание что даннух операцию мы могли сделать в верхнем цикле,
    # просто вместо строки new_matrix[line][column], написать new_matrix[column][line].

    # Next, we transpose our matrix, but I want to draw your attention to the fact that we could do this operation in the upper cycle,
    # just instead of a string new_matrix[line][column], to write new_matrix[column][line].
    for line in range( len(matrix) ):
        for column in range( line, len(matrix[line]) ):
            new_matrix[line][column],new_matrix[column][line] = new_matrix[column][line], new_matrix[line][column]




    # 3
    # Далее мы умножаем 1/определитель на все элементы получившейся матрицы, также хочу обратить ваше внимание, что данную операцию можно было сделать в цикле где мы собираем
    # новую матриц, new_matrix[line][column] = ......... * 1/determinant.
    # Также выводит элементы матрицы(ОТВЕТ)

    # Next, we multiply 1/determinant by all the elements of the resulting matrix, I also want to draw your attention to the
    # fact that this operation could be done in a loop where we collect, new_matrix[line][column] = ......... * 1/determinant.
    # Also outputs matrix elements(ANSWER)
    for line in range( len(matrix) ):
        for column in range( len(matrix[line]) ):
            if new_matrix[line][column] % determinant == 0:
                print(new_matrix[line][column]//determinant, end=' ')
            else:
                print(str(new_matrix[line][column]) + '/' + str(determinant), end=' ')
        print()

    # ДАЛЕЕ БУДЕМ ИСПРАВЛЯТЬ ПРОБЛЕМУ НЕЦЕЛЫХ ЧИСЕЛ В ОТВЕТЕ
    # NEXT WE WILL FIX THE PROBLEM OF NON-INTEGERS IN THE ANSWER
