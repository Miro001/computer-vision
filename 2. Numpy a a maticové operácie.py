import numpy as np

import math

if __name__ == '__main__':

    A = np.array([[1, 2], [3, 4]])
    # A = np.array([(1, 2), (3, 4)])
    print("Matrix/ Matica: \n", A)

    n = 1  #skalar

    v_row = np.array([1, 2, 3, 4])
    v_row = np.array([[1, 2, 3, 4]])

    print("Row vector / Riadkovy vektor: ", v_row)

    v_column = np.array([[1, 2, 3, 4]]).T
    print("Column vector / Stlpcovy vektor: ", v_column)

    trans_2_v_row = v_column.T
    print("Transpose / Transponuje sa cez atribut T (Vymena riadkov a stlpcov): ", trans_2_v_row)

    lin_spaced_vector = np.linspace(0, 9, 10)
    print("Linearly spaced vector / Vektor s linearnym rastom:", lin_spaced_vector)

    v_empty = np.array([])
    print("Empty vector / Prazdny vector: ", v_empty)

    ########
    # Specific types of initialization
    ########
    mat_zeros = np.zeros((3, 3))  # tuple as input param
    print(mat_zeros)

    mat_ones = np.ones((2, 3, 2))
    print("Ones matrix: \n", mat_ones)

    mat_eye = np.eye(3)
    print("Diagional matrix / Diagonalna matica:\n", mat_eye)

    mat_rand = np.random.rand(2, 3)
    print("Random matrix / Matica nahodnych cisel:\n", mat_rand)

    vec = np.array([3, 2, 1])
    print("Third element of the vector / Treti prvok vektora: ", vec[2])  # Indexovanie zacina 0-tym prvkom v pythone

    ########
    # Pristup k matici
    ########

    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Acessing matrix / Pristup k matici")

    print("Accessing  element at (2,3) / Pristup k elementu (2,3)", mat[1][2])
    print("Accesing different elements through sequences:/ Dynamicky pristup k elementom matic")
    print(mat[0][:])  # vrati prvy riadok ako riadkovy vektor
    print(mat[:][1])  # vrati druhy stlpec ako riadkovy vektor !!!
    print(mat[1:3, 1:3])  # submatica zacinajuca na 2,2
    print(mat[1:, 1:])  # (2,2) + till end
    print(mat[:3, :3])  # od [] -> to index [3 3]

    print("Shape of the matrix/ Rozmery matice: ", mat.shape)
    print("Shape of the matrix/ Rozmery matice: ", mat.shape[0])
    print("Shape of the matrix/ Rozmery matice: ", mat.shape[1])

    mat_zeroes = np.zeros(mat.shape)

    ########
    # Jednoduché operácie s vektormi a maticam
    ########

    vec_a = np.array([[1, 2, 3, 4]]).T
    print(2 * vec_a)
    print(vec_a / 2)
    print(vec_a ** 3)  # umocnenie na 3

    vec_b = np.array([[1, 2, 3, 4]]).T

    print(vec_a * vec_b)
    print(vec_a / vec_b)
    print(vec_a - vec_b)
    print(np.log(vec_a))
    print(np.round(np.log(vec_a)))

    ######
    # Skalarne operacie na vektore -> vystup je skalar
    ######
    print(np.sum(vec_a))
    print(np.mean(vec_a))
    print(np.var(vec_a))
    print(np.std(vec_a))
    print(np.min(vec_a), np.max(vec_a))

    ######
    # Operacie na matici -> vystup je vektor
    ######
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.mean(mat, 0))
    print("Max of mat along axis 0: ", np.max(mat, 0))
    print("Max of mat alojng axis 1: ", np.max(mat, 1))
    print(np.max(mat))
    print(vec_a * vec_b)  # elementwise
    print(vec_a.T * vec_b)  # vektorovy sucin
    print(vec_a * vec_b.T)  # vektorovy sucin
    print(vec_a.T @ vec_b)  # skalarny sucin

    ######
    # Operacie na matici
    ######
    mat_1 = np.random.rand(3, 2)
    mat_2 = np.random.rand(2, 4)
    vec_1 = np.array([[1, 2, 3]]).T
    vec_2 = np.array([1, 2])
    print(np.matmul(mat_1, mat_2))

    print(np.matmul(vec_1.T, mat_1)) # 1x3 * 3x2 = 1x2
    print(np.matmul(mat_1, vec_2)) # 3x2 * 2x1 = 3x1

    print("Inverse matrix: \n", np.linalg.inv(np.random.rand(3, 3)))

    print("Eigen values: \n", np.linalg.eigvals(np.random.rand(3, 3)))
    ######
    # Linearna algebra
    ######
    V, D = np.linalg.eig(np.random.rand(3, 3))
    print("Eigen values: \n",V,"\n Eigen matrix\n",D)
    U, S, V = np.linalg.svd(np.random.rand(3, 3))
    print("SVD single value decomposition: \n", U,"\n Eigen matrix\n",S,"\n Eigen matrix\n",V) # a = U * S * V'

    B = np.random.rand(4, 4)
    np.linalg.det(B)
    np.sum(B)
    print(B.reshape((8,2)))
    vec_a = np.array([[1, 2, 3]])
    vec_b = np.array([[4, 5, 6]])

    vec_c = np.concatenate((vec_a, vec_b), 0)
    print(vec_c)

    vec_c = np.array((vec_a, vec_b))
    vec_c = np.squeeze(vec_c)
    print(vec_c)

    print(np.repeat(A, 2,axis=0))
    print(np.diag(B))

# https://numpy.org/doc/1.19/user/absolute_beginners.html
# https://numpy.org/doc/stable/

# Dokoncit cvicenie po stranu 10 okrem vizualizacie
#Vizualizacia sa bude preberat nma dalsom cviceni

# odovzdat na gitlabe zadanie  do strany 10