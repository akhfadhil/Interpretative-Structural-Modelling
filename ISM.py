import numpy as np
import sys
import json 

result_ISM = {}

def input_to_mirror(string_data, ordo=22):
    matrix = np.diag(np.full(ordo,'X'))
    list_data = string_data.split()
    # list_data = list(string_data)
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
    
    full_str = ''
    for i in range(len(matrix)):
        full_str = full_str + ' '.join(matrix[i]) + ' '
    
    return full_str

def mirror_to_biner(string_data):
    new_str = ""
    for i in range(len(string_data)):
        if string_data[i] == 'V':
            new_str = new_str + '1'
        elif string_data[i] == 'A':
            new_str = new_str + '0'
        elif string_data[i] == 'X':
            new_str = new_str + '1'
        elif string_data[i] == 'O':
            new_str = new_str + '0'
        else:
            new_str = new_str + string_data[i]
    
    return new_str

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
    data_input = ["V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V",
              "V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V",
              "V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V"]
    result_ISM["data_input"] = data_input


    # Input to mirror
    result_ISM["data_mirror"] = []
    for data in result_ISM["data_input"]:
        result_ISM["data_mirror"].append(input_to_mirror(data))

    # Mirror to biner
    result_ISM["data_biner"] = []
    for data in result_ISM["data_mirror"]:
        result_ISM["data_biner"].append(mirror_to_biner(data))

    # Biner conclusion
    biner_conclusion = ""
    for i in range(len(result_ISM["data_biner"][0])):
        if i % 2 == 0:
            lst2 = [result_ISM["data_biner"][0][i], result_ISM["data_biner"][1][i], result_ISM["data_biner"][2][i]]
            biner_conclusion = biner_conclusion + (max(set(lst2), key=lst2.count)) + ' '
    result_ISM["biner_conclusion"] = biner_conclusion

    # Convert from biner string to biner matrix
    even = 0
    matrix_str = ""
    for i in range(len(biner_conclusion)):
        matrix_str = matrix_str + biner_conclusion[i]
        if i % 2 == 0:
            even = even + 1
            if even % 22 == 0:
                matrix_str = matrix_str + ';'
    matrix = np.matrix(matrix_str[:-2])
    matrix = matrix.tolist()
    matrix_new = []
    for row in matrix:
        matrix_new.append(list(map(str, row)))
    matrix = matrix_new

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
    outputISM = {'independent':[], 'linkage':[], 'autonomous':[], 'dependent':[]}
    for i in range(len(DeP)):
        if DrP[i] > DrPAVG and DeP[i] < DePAVG:
            outputISM['independent'].append('E' + str(i+1))
        elif DrP[i] > DrPAVG and DeP[i] > DePAVG:
            outputISM['linkage'].append('E' + str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] > DePAVG:
            outputISM['dependent'].append('E' + str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] < DePAVG:
            outputISM['autonomous'].append('E' + str(i+1))
    result_ISM["outputISM"] = outputISM
    print(result_ISM)
