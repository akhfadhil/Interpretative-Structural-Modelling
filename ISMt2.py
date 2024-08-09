varResiko = {
   'A1' : ['Kualitas', 'Kualitas sesuai dengan spesifikasi'],
   'A2' : ['Kualitas', 'Persentase bahan baku reject'],
   'F2' : ['Fleksibilitas', 'Fleksibilitas dalam perubahan jumlah pesanan'],
   'F3' : ['Fleksibilitas', 'Fleksibilitas dalam pengiriman bahan baku'],
   'A3' : ['Kualitas', 'Konsistensi kualitas bahan baku'],
   'B1' : ['Pengiriman', 'Kecepatan pengiriman'],
   'B2' : ['Pengiriman', 'Ketepatan waktu pengiriman'],
   'E1' : ['Harga', 'Harga bahan baku'],
   'E2' : ['Harga', 'Harga tidak berfluktuasi'],
   'E3' : ['Harga', 'Memiliki potongan harga'],
   'E4' : ['Harga', 'Cara Pembayaran'],
   'B3' : ['Pengiriman', 'Ketepatan kuantitas bahan baku yang dikirim'],
   'C1' : ['Riwayat Performa Supplier', 'Ketersediaan bahan baku'],
   'C2' : ['Riwayat Performa Supplier', 'Kecepatan menanggapi permintaan pesanan'],
   'C3' : ['Riwayat Performa Supplier', 'Memiliki kerja sama jangka panjang'],
   'D1' : ['Pelayanan', 'Responsif'],
   'D2' : ['Pelayanan', 'Ketersediaan dalam mengganti kerugian akibat bahan baku yang rusak'],
   'F1' : ['Fleksibilitas', 'Fleksibilitas dalam penawaran harga']
}

result_ISM = {}

def sort_custom(lst):
    def custom_key(item):
        # Find the point where the letters end and the numbers start
        for i, char in enumerate(item):
            if char.isdigit():
                # Return a tuple with the alphabetical part and the numerical part as an integer
                return (item[:i], int(item[i:]))
    
    # Use the custom key for sorting
    return sorted(lst, key=custom_key)

def sort_dict_keys(d, order_list):
    # Ensure that all keys in the order_list are present in the dictionary
    if not all(key in d for key in order_list):
        raise ValueError("Order list contains keys not present in the dictionary")

    # Create a new dictionary with keys sorted according to order_list
    sorted_dict = {key: d[key] for key in order_list}
    
    return sorted_dict

def create_matrix(ordo, string_data):
    matrix = [['' for _ in range(ordo)] for _ in range(ordo)]
    pattern_index = 0
    
    for i in range(ordo):
        matrix[i][ordo - 1 - i] = 'X'
        for j in range(ordo - 1 - i):
            matrix[i][j] = string_data[pattern_index]
            pattern_index = (pattern_index + 1) % len(string_data)
    
    return matrix

def input_to_mirror(string_data, ordo):
    list_data = string_data.split()
    # list_data = list(string_data)
    index = 0

    # Mengisi segitiga atas matrix
    matrix = create_matrix(ordo, list_data)

    # Mengisi segitiga bawah matrix otomatis
    for i in range(ordo-1):
        for j in range(ordo):
            if matrix[i][j] == 'V':
                matrix[ordo - 1 - j][ordo - 1 - i] = 'A'
            elif matrix[i][j] == 'A':
                matrix[ordo - 1 - j][ordo - 1 - i] = 'V'
            elif matrix[i][j] == 'X':
                matrix[ordo - 1 - j][ordo - 1 - i] = 'X'
            elif matrix[i][j] == 'O':
                matrix[ordo - 1 - j][ordo - 1 - i] = 'O'

            if j == [ordo - 1 - i]:
                break
    
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

def reverse_ranks(ranks):
    max_rank = max(ranks)
    reversed_ranks = [max_rank - rank + 1 for rank in ranks]
    return reversed_ranks

def create_level_dict(codes, ranks):
    # Create a list of (code, rank) pairs
    code_rank_pairs = list(zip(codes, reverse_ranks(ranks)))
    
    # Sort pairs by rank (ascending order)
    sorted_pairs = sorted(code_rank_pairs, key=lambda x: x[1])
    
    # Create the dictionary with levels
    level_dict = {}
    for code, rank in sorted_pairs:
        level = 'Level ' + str(rank)  # Level is determined by rank
        if level not in level_dict:
            level_dict[level] = []
        level_dict[level].append(code)
    
    return level_dict

# Rearrange code
list_key = varResiko.keys()
list_key = sort_custom(list_key)

varResiko = sort_dict_keys(varResiko, list_key)

# START 
import sys
sys.argv = [0,1] # SIMULATED

if len(sys.argv) > 1:
    ''' INPUT ORDO'''
    ordo = len(varResiko)
    ''' DELETE HERE '''
    
    

    ''' ISM INPUT '''
    # Input ISM
    data_input = ["O O O O O O X V O V O O O O O V V O O O O V O O V O V O O O O O V O O O O O O O O O V O O O O O A O O O O O O O X V A A O A A A O A O O O O A V A A O X X O O O O O O V V O A X X V V O X O O O V O O O O O O O O A X X V V V X V O O A V X X X O O O O A O O O O V O O O O V V X X O O V O O O O A A O O O O O O",
                  "O O O O O O X V O V O O O O O V V O O O O V O O V O V O O O O O V O O O O O O O O O V O O O O O A O O O O O O O X V A A O A A A O A O O O O A V A A O X X O O O O O O V V O A X X V V O X O O O V O O O O O O O O A X X V V V X V O O A V X X X O O O O A O O O O V O O O O V V X X O O V O O O O A A O O O O O O",
                  "O O O O O O X V O V O O O O O V V O O O O V O O V O V O O O O O V O O O O O O O O O V O O O O O A O O O O O O O X V A A O A A A O A O O O O A V A A O X X O O O O O O V V O A X X V V O X O O O V O O O O O O O O A X X V V V X V O O A V X X X O O O O A O O O O V O O O O V V X X O O V O O O O A A O O O O O O"
    ]
    ''' DELETE HERE '''

    result_ISM["data_input"] = data_input

    # Input to mirror
    result_ISM["data_mirror"] = []
    for data in result_ISM["data_input"]:
        result_ISM["data_mirror"].append(input_to_mirror(data, ordo))

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
        DrP.append(value)                   # Driven Power
        value = 0
        for k in range(len(matrix[i])):
            if matrix[k][i] == '1':
                value = value + 1
        DeP.append(value)                   # Dependence Power

    # Sort the data in descending order and remove duplicates
    sorted_unique = sorted(set(DrP), reverse=True)

    # Create a dictionary that maps each number to its reverse dense rank
    rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_unique)}

    # Assign reverse ranks based on the dictionary
    ranks = [rank_dict[value] for value in DrP]


    result_ISM["Level"] = create_level_dict(list_key, ranks)

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