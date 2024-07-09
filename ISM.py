import numpy as np
import sys
import json 

def string_to_biner(string_data, ordo=22):
    matrix = np.diag(np.full(ordo,'X'))
    # list_data = string_data.split()
    list_data = list(string_data)
    index = 0

    # Mengisi segitiga atas matrix
    for i in range(ordo):
        for j in range(ordo):
            if i != j and i<j:
                matrix[i][j] = list_data[index]
                index += 1

    # Mengisi segitiga bawah matrix otomatis
    for i in range(ordo):
        for j in range(ordo):
            if i != j and i>j:  # Skip elements with the same row and column index
                if matrix[j][i] == 'V':
                    matrix[i][j] = 'A'
                elif matrix[j][i] == 'A':
                    matrix[i][j] = 'V'
                elif matrix[j][i] == 'X':
                    matrix[i][j] = 'X'
                elif matrix[j][i] == 'O':
                    matrix[i][j] = 'O'
    
    # Mengubah ke biner
    for i in range(ordo): 
        for j in range(ordo):
            if matrix[i][j] == 'V':
                matrix[i][j] = 1
            elif matrix[i][j] == 'A':
                matrix[i][j] = 0
            elif matrix[i][j] == 'X':
                matrix[i][j] = 1
            elif matrix[i][j] == 'O':
                matrix[i][j] = 0
    
    return matrix

def Average(lst): 
    return sum(lst) / len(lst) 


# START 
sys.argv = [0,1] # SIMULATED

if len(sys.argv) > 1:
    ordo = 22
    matrix = np.diag(np.full(ordo,'X'))

    # processed_data = sys.argv[1]
    # string_data = processed_data


    # Input ISM
    # string_data = "VVOOVOVVVVOOOOOOOOOVOOOOOOOVOVOOOOOOOOOVOOOOOOOOVOOOOOOVOVOVOOOOOOOOOVOOOOVVVOOOOOVOOOOOOOOOOVOOOVOOOOOOOOOOOOOOOOOOOOOOOOVOOOOOOOOOOOOOOOVOOVOOOOOOOVOVOVOOOOOOVOVVOVOVVOOOOVVOVOOVOOVVVOOOVOOOVOOOVOOOOVOVOOOVOOOOOOVOOOVOOOVOOVVVVOV"
    string_data_pakar1 = "VVOOVOVVVVOOOOOOOOOVOOOOOOOVOVOOOOOOOOOVOOOOOOOOVOOOOOOVOVOVOOOOOOOOOVOOOOVVVOOOOOVOOOOOOOOOOVOOOVOOOOOOOOOOOOOOOOOOOOOOOOVOOOOOOOOOOOOOOOVOOVOOOOOOOVOVOVOOOOOOVOVVOVOVVOOOOVVOVOOVOOVVVOOOVOOOVOOOVOOOOVOVOOOVOOOOOOVOOOVOOOVOOVVVVOV"
    string_data_pakar2 = "VVOOVOVVVVOOOOOOOOOVOOOOOOOVOVOOOOOOOOOVOOOOOOOOVOOOOOOVOVOVOOOOOOOOOVOOOOVVVOOOOOVOOOOOOOOOOVOOOVOOOOOOOOOOOOOOOOOOOOOOOOVOOOOOOOOOOOOOOOVOOVOOOOOOOVOVOVOOOOOOVOVVOVOVVOOOOVVOVOOVOOVVVOOOVOOOVOOOVOOOOVOVOOOVOOOOOOVOOOVOOOVOOVVVVOV"
    string_data_pakar3 = "VVOOVOVVVVOOOOOOOOOVOOOOOOOVOVOOOOOOOOOVOOOOOOOOVOOOOOOVOVOVOOOOOOOOOVOOOOVVVOOOOOVOOOOOOOOOOVOOOVOOOOOOOOOOOOOOOOOOOOOOOOVOOOOOOOOOOOOOOOVOOVOOOOOOOVOVOVOOOOOOVOVVOVOVVOOOOVVOVOOVOOVVVOOOVOOOVOOOVOOOOVOVOOOVOOOOOOVOOOVOOOVOOVVVVOV" 

    # Convert to biner
    matrix1 = string_to_biner(string_data_pakar1, ordo)
    matrix2 = string_to_biner(string_data_pakar2, ordo)
    matrix3 = string_to_biner(string_data_pakar3, ordo)

    # Biner conclusion
    matrix = []
    for i in range(len(matrix1)):
        lst = []
        for j in range(len(matrix1[i])):
            lst2 = [matrix1[i][j], matrix2[i][j], matrix3[i][j]]
            lst.append(max(set(lst2), key=lst2.count))
        matrix.append(lst)

    # Drive power & dependence power
    DrP = []
    DeP = []
    for i in range(len(matrix)):
        value = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                value = value + 1
        DrP.append(value)
        value = 0
        for k in range(len(matrix[i])):
            if matrix[k][i] == '1':
                value = value + 1
        DeP.append(value)

    # Average (Titik potong)
    DrPAVG = Average(DrP) # Y
    DePAVG = Average(DeP) # X

    # Klasifikasi Output
    outputISM = {'Independent':[], 'Linkage':[], 'Autonomous':[], 'Dependent':[]}
    for i in range(len(DeP)):
        if DrP[i] > DrPAVG and DeP[i] < DePAVG:
            outputISM['Independent'].append('E' + str(i+1))
        elif DrP[i] > DrPAVG and DeP[i] > DePAVG:
            outputISM['Linkage'].append('E' + str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] > DePAVG:
            outputISM['Dependent'].append('E' + str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] < DePAVG:
            outputISM['Autonomous'].append('E' + str(i+1))