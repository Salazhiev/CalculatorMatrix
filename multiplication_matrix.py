def check_true_matrix(column_, matrix_):
    for line in matrix_:
        if len(line) != column_:
            raise ValueError('Не правильно введены данные(Data entered incorrectly)')




if __name__ == '__main__':
    line_A, column_A = map(int, (input("Количество строк и столбцов матрицы A(Matrix Size A): ").split()))
    matrix_A = [ list(map(int, input(f'Введите {i+1} строку матрицы А: ').split())) for i in range(line_A) ]
    check_true_matrix(column_A, matrix_A)

    line_B, column_B = map(int, (input("Количество строк и столбцов матрицы B(Matrix Size B): ").split()))
    matrix_B = [ list(map(int, input(f'Введите {i+1} строку матрицы B: ').split())) for i in range(line_B) ]
    check_true_matrix(column_B, matrix_B)


    new_matrix_multiplication = [ [0]*column_B for _ in range(line_A) ]
    for line_first_matrix in range( line_A ):
        for column_second_matrix in range( column_B ):

            a1 = matrix_A[line_first_matrix]
            a2 = [ matrix_B[i][column_second_matrix] for i in range( line_B ) ]

            new_matrix_multiplication[line_first_matrix][column_second_matrix] = sum( a1[i]*a2[i] for i in range(len(a1)) )


    for k in new_matrix_multiplication:
        print(*k)