import numpy as np
import pandas as pd
import copy
import sys
import json 

ordo = 22
matrix = np.diag(np.full(ordo,'X'))

# processed_data = sys.argv[1]
string_data = "V	V	O	O	V	O	V	V	V	V	O	O	O	O	O	O	O	O	O	V	O   O	O	O	O	O	O	V	O	V	O	O	O	O	O	O	O	O	O	V	O   O	O	O	O	O	O	O	V	O	O	O	O	O	O	V	O	V	O	V   O	O	O	O	O	O	O	O	O	V	O	O	O	O	V	V	V	O   O	O	O	O	V	O	O	O	O	O	O	O	O	O	O	V	O   O	O	V	O	O	O	O	O	O	O	O	O	O	O	O	O   O	O	O	O	O	O	O	O	O	O	O	V	O	O	O   O	O	O	O	O	O	O	O	O	O	O	O	V	O   O	V	O	O	O	O	O	O	O	V	O	V	O   V	O	O	O	O	O	O	V	O	V	V	O   V	O	V	V	O	O	O	O	V	V	O   V	O	O	V	O	O	V	V	V	O   O	O	V	O	O	O	V	O	O   O	V	O	O	O	O	V	O   V	O	O	O	V	O	O   O	O	O	O	V	O   O	O	V	O	O   O	V	O	O   V	V	V   V	O   V"
string_data1 = "OOVOVOVOVVVOVOVOVOVOVOVOOOVOVOVOVOVOVOVOVOVOVOOVVOOVVOVOVOVOVOVOVVVOVOVOVOVOVOVOVOVVOVOVOOOVOVVVVOOOVOOVOVOOOOVOVOVVOOOOVOVOVVVOOVVOVOOVVVOOVVOOVVOOVVVOVOVOVOOOVVOVOVOVOVVVOVOVOVOOVOVOVVOVOOVOVOVOVOVOVOVOVOVOVOVOVOVOOOOVVVVOVOVOVOO"
string_data2 = "VOVOVOVOVVVOVOVOOVOVOVOVOOVOVOVOVOVOVOVOVOVVOVOVOVOVOVOVOVOVOVOVOVOOOVOVOOOOOOOOOOOOOOOVVVVVVVVVVVVVVVVVVVOOVOVOVOOOOOOOOOOOOOOOVOVOVOVOOVOVOVOOOOOOOOOOOOOVVVVVVVVVVVVVVVVVVVVVOVOOOVOVOVOVOVOVOVOVOVOVOVVVVVVVVOVOVOVOVOVOVOVOVOOVOVO"
string_data3 = "OOOOOOOOOOOOOOVOVOVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOVOVOOVVOOVOVOVOVOVOOVOOOVOOVOVOVOVVOOVOVOVOVVOVOVOVOVOVOVOVOOVOVOVVOOVOVOVVOVOVOOVOVOVOVOVVOVOOVOVOVOVVOVOVOOVOVOVVOVOVOOVOVOVOVOVOVOVOVOVOVOVOVOVOVVOVOVVOOVOOVOVOVOVOVOVOVOVOVOVOOVO"
list_data = string_data.split()
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

dataset = pd.DataFrame(matrix)

# Membuat kolom drive power
dataset["Dr P"] = dataset.apply(lambda row: sum(row[0:ordo]=='1') ,axis=1)

# Membuat kolom dependence power
lst = []
for column in range(len(dataset)):
    DeP = dataset[column].value_counts()['1']
    lst.append(DeP)

dataset['De P'] = lst

# Klasifikasi Output
outputISM = {'Independent':[], 'Linkage':[], 'Autonomous':[], 'Dependent':[]}
for row in range(len(dataset)):
    if dataset['Dr P'][row] > dataset["Dr P"].mean() and dataset['De P'][row] < dataset["De P"].mean():
        outputISM['Independent'].append('E' + str(row+1))
    elif dataset['Dr P'][row] > dataset["Dr P"].mean() and dataset['De P'][row] > dataset["De P"].mean():
        outputISM['Linkage'].append('E' + str(row+1))
    elif dataset['Dr P'][row] < dataset["Dr P"].mean() and dataset['De P'][row] > dataset["De P"].mean():
        outputISM['Dependent'].append('E' + str(row+1))
    elif dataset['Dr P'][row] < dataset["Dr P"].mean() and dataset['De P'][row] < dataset["De P"].mean():
        outputISM['Autonomous'].append('E' + str(row+1))

listCode = outputISM['Linkage'] + outputISM['Independent']

# Sort
listCode.sort()
for i in range(len(listCode)):
    if int(listCode[1][1:])>int(listCode[-1][1:]):
        listCode.insert(len(listCode), listCode.pop(1))

FuzzyS = {10 : (9,10,10), 9 : (8,9,10), 8 : (7,8,9), 7 : (6,7,8), 6 : (5,6,7), 5 : (4,5,6), 4 : (3,4,5), 3 : (2,3,4), 2 : (1,2,3), 1 : (1,1,2)}
FuzzyO = {10 : (8,9,10,10), 9 : (8,9,10,10), 8 : (6,7,8,9), 7 : (6,7,8,9), 6 : (3,4,6,7), 5 : (3,4,6,7), 4 : (3,4,6,7), 3 : (1,2,3,4), 2 : (1,2,3,4), 1 : (1,1,2)}
FuzzyD = {10 : (9,10,10), 9 : (8,9,10), 8 : (7,8,9), 7 : (6,7,8), 6 : (5,6,7), 5 : (4,5,6), 4 : (3,4,5), 3 : (2,3,4),  2 : (1,2,3), 1 : (1,1,2)}
FuzzyL = {'VL' : (0, 0, 0.25), 'L' : (0, 0.25, 0.5), 'M' : (0.25, 0.5, 0.75), 'H' : (0.5, 0.75, 1), 'VH' : (0.75, 1, 1)}
varResiko = {
                'E1':'Perencanaan yang tidak tepat akibat perubahan iklim',
                'E2':'Target penanaman yang tidak sesuai',
                'E3':'Kualitas yang tidak sesuai',
                'E4':'Kurangnya tenaga kerja',
                'E5':'Harga pupuk yang fluktuatif',
                'E6':'Ketersediaan air tidak memadai',
                'E7':'Tenaga kerja kurang terampil',
                'E8':'Terdapat hama',
                'E9':'Pemanenan tidak serentak ',
                'E10':'Kualitas buah kopi yang tidak sesuai dengan standar',
                'E11':'Biji kopi kualitas rendah',
                'E12':'Mesin yang digunakan tidak stabil',
                'E13':'Pekerja kesulitan mengoperasikan mesin',
                'E14':'Terbuangnya kopi akibat tidak tersangrai dengan sempurna',
                'E15':'Terdapat kerikil pada biji kopi yang telah disangrai',
                'E16':'Kurang memadainya peralatan ',
                'E17':'Kurang menariknya kemasan yang digunakan',
                'E18':'Kebersihan tempat penyimpanan kurang',
                'E19':'Terjadi keterlambatan pengiriman',
                'E20':'Rendahnya tingkat kepuasan konsumen',
                'E21':'Profit yang dihasilkan tidak stabil',
                'E22':'Pemutusan kerjasama antar pemasok dengan distributor',
            }

class Pakar:
    Severity = 0
    Occurance = 0
    Detection = 0
    LS = ''
    LO = ''
    LD = ''

    def __init__(self, role, weight):
        self.role = role
        self.weight = weight

    def RPN(self):
        return self.Severity*self.Occurance*self.Detection

class Risk:
    def __init__(self, riskCode, riskName, listPakar):
        self.riskCode = riskCode
        self.riskName = riskName
        self.listPakar = listPakar

    def RIS(self):
        weightxS = 0
        for pakar in self.listPakar:
            for number in FuzzyS[pakar.Severity]:
                weightxS = weightxS + pakar.weight*number
        ris = (weightxS/100)/3
        return round(ris, 2)

    def RIO(self):
        weightxO = 0
        for pakar in self.listPakar:
            for number in FuzzyO[pakar.Occurance]:
                weightxO = weightxO + pakar.weight*number
        rio = (weightxO/100)/3
        return round(rio, 2)

    def RID(self):
        weightxD = 0
        for pakar in self.listPakar:
            for number in FuzzyD[pakar.Detection]:
                weightxD = weightxD + pakar.weight*number
        rid = (weightxD/100)/3
        return round(rid, 2)
    
listPakar = [Pakar('Akademisi', 40), Pakar('UMKM1', 30), Pakar('UMKM2', 30)]

listResiko = []

for i in range(len(listCode)):
    risk = Risk(listCode[i], varResiko[listCode[i]], copy.deepcopy(listPakar))
    listResiko.append(risk)

# Simulate input for testing purposes (replace with actual input in production)
simulated_input = [
    [7, 7, 7],
    [6, 6, 6],
    [5, 5, 5]
]

# Input SOD (simulated)
for risk in listResiko:
    for pakar in risk.listPakar:
        pakar.Severity = simulated_input[0][0]
        pakar.Occurance = simulated_input[0][1]
        pakar.Detection = simulated_input[0][2]

# Input Linguistik (simulated)
for pakar in listPakar:
    pakar.LS = 'L'
    pakar.LO = 'M'
    pakar.LD = 'H'

# Copy Linguistik Value to all risk
for risk in listResiko:
    for i in range(len(risk.listPakar)):
        risk.listPakar[i].LS = listPakar[i].LS
        risk.listPakar[i].LO = listPakar[i].LO
        risk.listPakar[i].LD = listPakar[i].LD

def Severity():
    weightxS = 0
    for pakar in listPakar:
        if pakar.LS == '':
            return 0
        for number in FuzzyL[pakar.LS]:
            weightxS = weightxS + pakar.weight*number
    S = (weightxS/100)/3
    return round(S, 2)

def Occurance():
    weightxS = 0
    for pakar in listPakar:
        if pakar.LS == '':
            return 0
        for number in FuzzyL[pakar.LO]:
            weightxS = weightxS + pakar.weight*number
    S = (weightxS/100)/3
    return round(S, 2)

def Detection():
    weightxS = 0
    for pakar in listPakar:
        if pakar.LS == '':
            return 0
        for number in FuzzyL[pakar.LD]:
            weightxS = weightxS + pakar.weight*number
    S = (weightxS/100)/3
    return round(S, 2)

def WTotal(S,O,D):
    return round(S+O+D, 3)

# Agregat Bobot Kepentingan S
WS = round(Severity()/WTotal(Severity(), Occurance(), Detection()), 3)

# Agregat Bobot Kepentingan O
WO = round(Occurance()/WTotal(Severity(), Occurance(), Detection()), 3)

# Agregat Bobot Kepentingan D
WD = round(Detection()/WTotal(Severity(), Occurance(), Detection()), 3)






listjson = []
for risk in listResiko:
    dictjson = {}
    dictjson['Komponen Resiko'] = risk.riskCode
    dictjson['Kode Resiko'] = risk.riskName
    dictjson['S^(WS/(WS+WO+WD))'] = risk.RIS()**WS
    dictjson['O^(WO/(WS+WO+WD))'] = risk.RIS()**WS
    dictjson['D^(WD/(WS+WO+WD))'] = risk.RID()**WD

    tot = (risk.RIS()**WS)*(risk.RIS()**WS)*(risk.RID()**WD)
    dictjson['FRPN'] = tot
    listjson.append(dictjson)

print(listjson)

# Membuat Dataframe
# data = pd.DataFrame()

# # Data Value
# Kode = []
# Komponen = []
# WSev = []
# WOcc = []
# WDet = []

# for risk in listResiko:
#     Kode.append(risk.riskCode)
#     Komponen.append(risk.riskName)
#     WSev.append(risk.RIS()**WS)
#     WOcc.append(risk.RIO()**WO)
#     WDet.append(risk.RID()**WD)

# data['Kode Resiko'] = Kode
# data['Komponen Resiko'] = Komponen
# data['S^(WS/(WS+WO+WD))'] = WSev
# data['O^(WO/(WS+WO+WD))'] = WOcc
# data['D^(WD/(WS+WO+WD))'] = WDet

# # Perhitungan FRPN
# FRPN = []
# for i in range(len(data)):
#     tot = WSev[i]*WOcc[i]*WDet[i]
#     FRPN.append(tot)
# data['FRPN'] = FRPN

# # Ranking
# data['Rank'] = data['FRPN'].rank(ascending=False)

# json_data = data.to_json(orient='records', lines=True)

# # Mencetak JSON data
# print(json_data)