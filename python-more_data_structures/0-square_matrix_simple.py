def square_matrix_simple(matrix=[]):
    # Create a new matrix using list comprehension
    new_matrix = []
    for row in matrix:
        # Square each element in the row and create a new row
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
