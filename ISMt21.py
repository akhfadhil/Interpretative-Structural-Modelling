'''
    VARIABLE RESIKO
'''

varResiko = {
   '1': 'Kualitas sesuai dengan spesifikasi',
   '2': 'Persentase bahan baku reject',
   '3': 'Konsistensi kualitas bahan baku',
   '4': 'Kecepatan pengiriman',
   '5': 'Ketepatan waktu pengiriman',
   '6': 'Ketepatan kuantitas bahan baku yang dikirim',
   '7': 'Ketersediaan bahan baku',
   '8': 'Kecepatan menanggapi permintaan pesanan', 
   '9': 'Memiliki kerja sama jangka panjang', 
   '10': 'Responsif', 
   '11': 'Ketersediaan dalam mengganti kerugian akibat bahan baku yang rusak', 
   '12': 'Harga bahan baku',
   '13': 'Harga tidak berfluktuasi',
   '14': 'Memiliki potongan harga',
   '15': 'Cara Pembayaran',
   '16': 'Fleksibilitas dalam penawaran harga',
   '17': 'Fleksibilitas dalam perubahan jumlah pesanan',
   '18': 'Fleksibilitas dalam pengiriman bahan baku'
}


'''
    DELETE HERE
'''

result_ISM = {}

result_ISM["resiko"] = varResiko

def create_matrix(n):
    # Create an n x n matrix filled with None or any other default value
    matrix = [['' for _ in range(n)] for _ in range(n)]
    
    # Fill the diagonal with the specified value
    for i in range(n):
        matrix[i][i] = 'X'
    
    return matrix

def input_to_mirror(string_data, ordo):
    matrix = create_matrix(ordo)
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
        level = 'level ' + str(rank)  # Level is determined by rank
        if level not in level_dict:
            level_dict[level] = []
        level_dict[level].append(code)
    
    return level_dict

# START 
import sys
sys.argv = [0,1] # SIMULATED

if len(sys.argv) > 1:



    ''' INPUT ORDO'''
    ordo = len(varResiko)
    ''' DELETE HERE '''
    
    

    ''' ISM INPUT '''
    # Input ISM
    data_input = [
        'V V O O O O O V O V X O O O O O O V O O O O O V O V O O V O O O O O O O O O V O O O O O O O O O A O A A V X O O O O O O O A O A A V A O O O O A O A A A O V V O O O O O O X X O V O O O X O V V X X X X A O O O O O O O V A O O V X V V V A O O O O X X X O O V O O O O X X V V O O O O V O O A A O O O O O O O O ',
        'V V O O O O O V O V X O O O O O O V O O O O O V O V O O V O O O O O O O O O V O O O O O O O O O A O A A V X O O O O O O O A O A A V A O O O O A O A A A O V V O O O O O O X X O V O O O X O V V X X X X A O O O O O O O V A O O V X V V V A O O O O X X X O O V O O O O X X V V O O O O V O O A A O O O O O O O O ',
        'V V O O O O O V O V X O O O O O O V O O O O O V O V O O V O O O O O O O O O V O O O O O O O O O A O A A V X O O O O O O O A O A A V A O O O O A O A A A O V V O O O O O O X X O V O O O X O V V X X X X A O O O O O O O V A O O V X V V V A O O O O X X X O O V O O O O X X V V O O O O V O O A A O O O O O O O O '
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



    # RANKING / LEVEL
    # Sort the data in descending order and remove duplicates
    sorted_unique = sorted(set(DrP), reverse=True)
    # Create a dictionary that maps each number to its reverse dense rank
    rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
    # Assign reverse ranks based on the dictionary
    ranks = [rank_dict[value] for value in DrP]
    result_ISM["level"] = create_level_dict(varResiko.keys(), ranks)



    # Average (Titik potong)
    DrPAVG = Average(DrP) # Y
    DePAVG = Average(DeP) # X



    # Klasifikasi Output
    outputISM = {'independent':[], 'linkage':[], 'autonomous':[], 'dependent':[]}
    for i in range(len(DeP)):
        if DrP[i] > DrPAVG and DeP[i] < DePAVG:
            outputISM['independent'].append(str(i+1))
        elif DrP[i] > DrPAVG and DeP[i] > DePAVG:
            outputISM['linkage'].append(str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] > DePAVG:
            outputISM['dependent'].append(str(i+1))
        elif DrP[i] < DrPAVG and DeP[i] < DePAVG:
            outputISM['autonomous'].append(str(i+1))
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
