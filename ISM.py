import numpy as np
import sys

varResiko = {
    'E1': ['Perencanaan produksi', 'Perencanaan yang tidak tepat akibat perubahan iklim'],
    'E2': ['Perawatan tanaman', 'Kurangnya perawatan tanaman'],
    'E3': ['Perawatan tanaman', 'Penyakit tanaman'],
    'E4': ['Ketersediaan tenaga kerja', 'Kurangnya jumlah tenaga kerja'],
    'E5': ['Pengadaan bahan baku kopi', 'Harga pupuk yang fluktuatif'],
    'E6': ['Irigasi kebun kopi', 'Ketersediaan air tidak memadai'],
    'E7': ['Pemanenan kopi', 'Tenaga kerja kurang terampil'],
    'E8': ['Pemanenan kopi', 'Terdapat hama'],
    'E9': ['Pemanenan kopi', 'Pemanenan tidak serentak'],
    'E10': ['Pemanenan kopi', 'Kualitas buah kopi yang tidak sesuai dengan standar'],
    'E11': ['Penyortiran', 'Kualitas biji kopi yang rendah'],
    'E12': ['Penyangraian', 'Mesin yang digunakan tidak stabil'],
    'E13': ['Penyangraian', 'Pekerja kesulitan mengoperasikan mesin'],
    'E14': ['Penyangraian', 'Terbuangnya kopi akibat tidak tersangrai dengan sempurna'],
    'E15': ['Pendinginan dan sortasi', 'Terdapat kerikil pada biji kopi yang telah disangrai'],
    'E16': ['Penggilingan', 'Kurang memadainya peralatan '],
    'E17': ['Pengemasan', 'Kurang menariknya kemasan yang digunakan'],
    'E18': ['Penyimpanan', 'Kebersihan tempat penyimpanan kurang'],
    'E19': ['Pengiriman', 'Terjadi keterlambatan pengiriman'],
    'E20': ['Penjualan Produk', 'Rendahnya tingkat kepuasan konsumen'],
    'E21': ['Penjualan Produk', 'Profit yang dihasilkan tidak stabil'],
    'E22': ['Pengembalian Produk', 'Pemutusan kerjasama antar pemasok dengan distributor'],
}

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

def string_to_matrix(input_string, m, n):
    if m * n != len(input_string):
        raise ValueError("The dimensions of the matrix do not match the length of the input string.")
    
    matrix = []
    for i in range(m):
        row = input_string[i * n:(i + 1) * n]
        matrix.append(row)
    
    return matrix

def string_to_list(input_string):
    return [char for char in input_string]

def matrix_to_string(matrix):
    flattened = [str(element) for row in matrix for element in row]
    matrix_str = ' '.join(flattened)
    return matrix_str

def Average(lst): 
    return sum(lst) / len(lst) 


# START 
sys.argv = [0,1] # SIMULATED

if len(sys.argv) > 1:
    ''' INPUT ORDO'''
    ordo = 22
    ''' DELETE HERE '''
    
    matrix = np.diag(np.full(ordo,'X'))

    # processed_data = sys.argv[1]
    # string_data = processed_data

    ''' ISM INPUT '''
    # Input ISM
    data_input = ["V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V",
              "V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V",
              "V V O O V O V V V V O O O O O O O O O V O O O O O O O V O V O O O O O O O O O V O O O O O O O O V O O O O O O V O V O V O O O O O O O O O V O O O O V V V O O O O O V O O O O O O O O O O V O O O V O O O O O O O O O O O O O O O O O O O O O O O O V O O O O O O O O O O O O O O O V O O V O O O O O O O V O V O V O O O O O O V O V V O V O V V O O O O V V O V O O V O O V V V O O O V O O O V O O O V O O O O V O V O O O V O O O O O O V O O O V O O O V O O V V V V O V"]
    ''' DELETE HERE '''

    result_ISM["data_input"] = data_input

    # Input to mirror
    result_ISM["data_mirror"] = []
    for data in result_ISM["data_input"]:
        result_ISM["data_mirror"].append(input_to_mirror(data))

    # Mirror to biner
    result_ISM["data_biner"] = []
    for data in result_ISM["data_mirror"]:
        result_ISM["data_biner"].append(mirror_to_biner(data))

    # Biner conclusion 1
    biner_conclusion = ""
    for i in range(len(result_ISM["data_biner"][0])):
        if i % 2 == 0:
            lst2 = [result_ISM["data_biner"][0][i], result_ISM["data_biner"][1][i], result_ISM["data_biner"][2][i]]
            biner_conclusion = biner_conclusion + (max(set(lst2), key=lst2.count)) + ' '
    result_ISM["biner_conclusion"] = biner_conclusion

    # Convert from biner string to biner matrix
    matrix = string_to_matrix(biner_conclusion.replace(" ", ""), ordo, ordo)
    for i in range(len(matrix)):
        matrix[i] = string_to_list(matrix[i])

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

    # Biner conclusion 2
        # Add DrP
    for i in range(len(matrix)):
        matrix[i].append(DrP[i])
        # Add DeP
    DeP.append(sum(DrP))
    matrix.append(DeP)
    result_ISM["biner_conclusion"] = matrix_to_string(matrix)

    print(result_ISM)
