from ISM import outputISM
import numpy as np
import copy
import sys
import json 

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

def calculate_rank(vector):
  a={}
  rank=1
  for num in sorted(vector,reverse=True):
    if num not in a:
      a[num]=rank
      rank=rank+1
  return[a[i] for i in vector]

# START 
sys.argv = [0,1] # SIMULATED

if len(sys.argv) > 1:

    # Extract Linkage & Independent to listCode
    listCode = outputISM['Linkage'] + outputISM['Independent']

    # Sort
    listCode.sort()
    for i in range(len(listCode)):
        if int(listCode[1][1:])>int(listCode[-1][1:]):
            listCode.insert(len(listCode), listCode.pop(1))


    """
        SIMULATE LIST CODE
    """
    listCode = ['E9', 'E11', 'E19']

    """
        DELETE
    """



    # Initiate Pakar
    listPakar = [Pakar('Akademisi', 40), Pakar('UMKM1', 30), Pakar('UMKM2', 30)]

    # Initiate Risk
    listResiko = []
    for i in range(len(listCode)):
        risk = Risk(listCode[i], varResiko[listCode[i]], copy.deepcopy(listPakar))
        listResiko.append(risk)





    """
        SIMULATE INPUT SOD & LINGUISTIK
    """
    simulated_input_pakar1 = [
        [8, 9, 2], # Risk 1
        [10, 9, 4], # Risk 2  [S, O, D]
        [7, 6, 2] # Risk 3
    ]
    simulated_input_pakar2 = [
        [8, 10, 2], # Risk 1
        [9, 10, 3], # Risk 2  [S, O, D]
        [10, 2, 2] # Risk 3
    ]
    simulated_input_pakar3 = [
        [7, 9, 3], # Risk 1
        [9, 9, 4], # Risk 2 [S, O, D]
        [10, 7, 2] # Risk 3
    ]
    simulated_input = [simulated_input_pakar1, simulated_input_pakar2, simulated_input_pakar3]

    P1L = ['H', 'H', 'L']
    P2L = ['VH', 'M','L']
    P3L = ['H', 'VH', 'L']
    simulated_language = [P1L, P2L, P3L]
    """
        DELETE
    """






    # Input SOD
    j = 0
    for risk in listResiko:
            i = 0
            for pakar in risk.listPakar:
                pakar.Severity = simulated_input[i][j][0]
                pakar.Occurance = simulated_input[i][j][1]
                pakar.Detection = simulated_input[i][j][2]
                i = i + 1
            j = j + 1

    # Input Linguistik
    i = 0
    for pakar in listPakar:
            pakar.LS = simulated_language[i][0]
            pakar.LO = simulated_language[i][1]
            pakar.LD = simulated_language[i][2]

    # Copy Linguistik Value to all risk
    for risk in listResiko:
        for i in range(len(risk.listPakar)):
            risk.listPakar[i].LS = listPakar[i].LS
            risk.listPakar[i].LO = listPakar[i].LO
            risk.listPakar[i].LD = listPakar[i].LD

    # Agregat Bobot Kepentingan S
    WS = round(Severity()/WTotal(Severity(), Occurance(), Detection()), 3)

    # Agregat Bobot Kepentingan O
    WO = round(Occurance()/WTotal(Severity(), Occurance(), Detection()), 3)

    # Agregat Bobot Kepentingan D
    WD = round(Detection()/WTotal(Severity(), Occurance(), Detection()), 3)
    


    # DATA JSON
    listjson = []
    for risk in listResiko:
        dictjson = {}
        dictjson['Komponen Resiko'] = risk.riskName
        dictjson['Kode Resiko'] = risk.riskCode
        dictjson['S^(WS/(WS+WO+WD))'] = risk.RIS()**WS
        dictjson['O^(WO/(WS+WO+WD))'] = risk.RIS()**WS
        dictjson['D^(WD/(WS+WO+WD))'] = risk.RID()**WD

        tot = (risk.RIS()**WS)*(risk.RIO()**WO)*(risk.RID()**WD)
        dictjson['FRPN'] = tot
        listjson.append(dictjson)
    # Rank
    listRank = []
    for row in listjson:
        listRank.append(row['FRPN'])
    rank = calculate_rank(listRank)
    i = 0
    for row in listjson:
        row['Rank'] = rank[i]
        i = i + 1

    print(listjson)
else :
    processed_data = ""
