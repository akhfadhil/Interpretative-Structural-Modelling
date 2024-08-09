import copy
import sys
from ISM import outputISM, varResiko

FuzzyS = {10: (9, 10, 10), 9: (8, 9, 10), 8: (7, 8, 9), 7: (6, 7, 8), 6: (5, 6, 7), 5: (4, 5, 6), 4: (3, 4, 5), 3: (2, 3, 4), 2: (1, 2, 3), 1: (1, 1, 2)}
FuzzyO = {10: (8, 9, 10, 10), 9: (8, 9, 10, 10), 8: (6, 7, 8, 9), 7: (6, 7, 8, 9), 6: (3, 4, 6, 7), 5: (3, 4, 6, 7), 4: (3, 4, 6, 7), 3: (1, 2, 3, 4), 2: (1, 2, 3, 4), 1: (1, 1, 2)}
FuzzyD = {10: (9, 10, 10), 9: (8, 9, 10), 8: (7, 8, 9), 7: (6, 7, 8), 6: (5, 6, 7), 5: (4, 5, 6), 4: (3, 4, 5), 3: (2, 3, 4), 2: (1, 2, 3), 1: (1, 1, 2)}
FuzzyL = {'VL': (0, 0, 0.25), 'L': (0, 0.25, 0.5), 'M': (0.25, 0.5, 0.75), 'H': (0.5, 0.75, 1), 'VH': (0.75, 1, 1)}



result_FUZZY = {}

def create_pakar(role, weight):
    return {'role': role, 'weight': weight, 'Severity': 0, 'Occurance': 0, 'Detection': 0, 'LS': '', 'LO': '', 'LD': ''
            }

def calculate_ris(pakar_list):
    weightxS = 0
    for pakar in pakar_list:
        for number in FuzzyS[pakar['Severity']]:
            weightxS += pakar['weight'] * number
    ris = (weightxS / 100) / 3
    return round(ris, 2)

def calculate_rio(pakar_list):
    weightxO = 0
    for pakar in pakar_list:
        for number in FuzzyO[pakar['Occurance']]:
            weightxO += pakar['weight'] * number
    rio = (weightxO / 100) / 3
    return round(rio, 2)

def calculate_rid(pakar_list):
    weightxD = 0
    for pakar in pakar_list:
        for number in FuzzyD[pakar['Detection']]:
            weightxD += pakar['weight'] * number
    rid = (weightxD / 100) / 3
    return round(rid, 2)

def WSeverity(listPakar):
    weightxS = 0
    for pakar in listPakar:
        if pakar['LS'] == '':
            return 0
        for number in FuzzyL[pakar['LS']]:
            weightxS += pakar['weight'] * number
    S = (weightxS / 100) / 3
    return round(S, 2)

def WOccurance(listPakar):
    weightxS = 0
    for pakar in listPakar:
        if pakar['LS'] == '':
            return 0
        for number in FuzzyL[pakar['LO']]:
            weightxS += pakar['weight'] * number
    S = (weightxS / 100) / 3
    return round(S, 2)

def WDetection(listPakar):
    weightxS = 0
    for pakar in listPakar:
        if pakar['LS'] == '':
            return 0
        for number in FuzzyL[pakar['LD']]:
            weightxS += pakar['weight'] * number
    S = (weightxS / 100) / 3
    return round(S, 2)

def WTotal(S, O, D):
    return round(S + O + D, 3)

def calculate_rank(vector):
    a = {}
    rank = 1
    for num in sorted(vector, reverse=True):
        if num not in a:
            a[num] = rank
            rank += 1
    return [a[i] for i in vector]

def matrix_to_string(matrix):
    flattened = [str(element) for row in matrix for element in row]
    matrix_str = ' '.join(flattened)
    return matrix_str

# START 
sys.argv = [0, 1]  # SIMULATED

if len(sys.argv) > 1:
    # Extract Linkage & Independent to listCode
    listCode = outputISM['linkage'] + outputISM['independent']

    # Sort
    listCode.sort()
    for i in range(len(listCode)):
        if int(listCode[1][1:]) > int(listCode[-1][1:]):
            listCode.insert(len(listCode), listCode.pop(1))

    # SIMULATE LIST CODE
    listCode = ['E9', 'E11', 'E19']

    # Initiate Pakar
    listPakar = [create_pakar('Akademisi', 40), create_pakar('UMKM1', 30), create_pakar('UMKM2', 30)]

    # Initiate Risk
    listResiko = []
    for code in listCode:
        risk = {'riskCode': code, 'riskName': varResiko[code][1], 'listPakar': copy.deepcopy(listPakar)}
        listResiko.append(risk)

    # SIMULATE INPUT SOD & LINGUISTIK
    simulated_input_pakar1 = [
        [8, 9, 2],  # Risk 1
        [10, 9, 4],  # Risk 2  [S, O, D]
        [7, 6, 2]  # Risk 3
    ]
    simulated_input_pakar2 = [
        [8, 10, 2],  # Risk 1
        [9, 10, 3],  # Risk 2  [S, O, D]
        [10, 2, 2]  # Risk 3
    ]
    simulated_input_pakar3 = [
        [7, 9, 3],  # Risk 1
        [9, 9, 4],  # Risk 2 [S, O, D]
        [10, 7, 2]  #
    ]
    simulated_input = [simulated_input_pakar1, simulated_input_pakar2, simulated_input_pakar3]

    P1L = ['H', 'H', 'L']
    P2L = ['VH', 'M','L']
    P3L = ['H', 'VH', 'L']
    simulated_language = [P1L, P2L, P3L] # [Pakar 1, Pakar 2, Pakar 3]
    """
        DELETE
    """

    # Input SOD
    # Mapping each sublist to the corresponding dictionary keys
    for i, pakar_list in enumerate(simulated_input):
        for j, values in enumerate(pakar_list):
            listResiko[j]['listPakar'][i]['Severity'] = values[0]
            listResiko[j]['listPakar'][i]['Occurance'] = values[1]
            listResiko[j]['listPakar'][i]['Detection'] = values[2]

    # Mapping simulated_language to listRisk
    for i in range(len(listResiko)):
        for j, pakar in enumerate(listResiko[i]['listPakar']):
            pakar['LS'] = simulated_language[j][0]
            pakar['LO'] = simulated_language[j][1]
            pakar['LD'] = simulated_language[j][2]
    
    for i, values in enumerate(listPakar):
        values['LS'] = simulated_language[i][0]
        values['LO'] = simulated_language[i][1]
        values['LD'] = simulated_language[i][2]
    
    # RIS, RIO, RID
    for risk in listResiko:
        risk['ris'] = calculate_ris(risk['listPakar'])
        risk['rio'] = calculate_rio(risk['listPakar'])
        risk['rid'] = calculate_rid(risk['listPakar'])
    
    # Agregat Bobot Kepentingan S
    WS = round(WSeverity(listPakar)/WTotal(WSeverity(listPakar), WOccurance(listPakar), WDetection(listPakar)), 3)

    # Agregat Bobot Kepentingan O
    WO = round(WOccurance(listPakar)/WTotal(WSeverity(listPakar), WOccurance(listPakar), WDetection(listPakar)), 3)

    # Agregat Bobot Kepentingan D
    WD = round(WDetection(listPakar)/WTotal(WSeverity(listPakar), WOccurance(listPakar), WDetection(listPakar)), 3)



    # outputFuzzy
    outputFuzzy = []
    for risk in listResiko:
        dictjson = {}
        dictjson['kode_resiko'] = risk['riskCode']
        dictjson['komponen_resiko'] = risk['riskName']
        dictjson['data_s'] = round(risk['ris']**WS, 3)
        dictjson['data_o'] = round(risk['rio']**WO, 3)
        dictjson['data_d'] = round(risk['rid']**WD, 3)
        dictjson['frpn'] = round(dictjson['data_s']*dictjson['data_o']*dictjson['data_d'], 3)
        outputFuzzy.append(dictjson)
    # Rank
    listRank = []
    for row in outputFuzzy:
        listRank.append(row['frpn'])
    rank = calculate_rank(listRank)
    i = 0
    for row in outputFuzzy:
        row['rank'] = rank[i]
        i = i + 1




    # RESULT FUZZY
    data_input = simulated_input

    # SOD
    result_FUZZY["data_sod"] = {}
    for i in range(len(data_input)):
        result_FUZZY["data_sod"]["risk"+str(i+1)] = [listCode[i], varResiko[listCode[i]][1], data_input[0][i]+data_input[1][i]+data_input[2][i]]

    # Linguistik
    result_FUZZY["data_linguistik"] = matrix_to_string(simulated_language)

    # Output fuzzy
    result_FUZZY["output_fuzzy"] = outputFuzzy

    print(result_FUZZY)