def read_matrix_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
       
        n, k = map(int, file.readline().strip().split())
        
        matrix = [list(map(float, file.readline().strip().split())) for _ in range(n)]
    return n, k, matrix

def write_matrix_to_file(filename, matrix):
    with open(filename, 'w', encoding='utf-8') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def modify_matrix(n, k, matrix):
    k -= 1  
    diagonal_element = matrix[k][k]
    
    if diagonal_element == 0:
        raise ValueError("Диагональный элемент равен нулю, деление невозможно.")
    
    for j in range(n):
        matrix[k][j] /= diagonal_element
    
    return matrix


input_filename = 'Егор_Y-244_vvod.txt'
output_filename = 'Егор_Y-244_vivod.txt'

try:
    
    n, k, matrix = read_matrix_from_file(input_filename)
    
    
    modified_matrix = modify_matrix(n, k, matrix)
    
    
    write_matrix_to_file(output_filename, modified_matrix)
    
    print("Операция выполнена успешно. Результаты записаны в файл:", output_filename)
except Exception as e:
    print("Произошла ошибка:", e)
