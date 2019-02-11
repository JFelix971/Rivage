import tables    #Librairie PyTables
import numpy as np

from tables import *

tablepath="CombinedOUTPUTS_ZONE_2_HIVERNAGE.h5"
DATA = tables.open_file(tablepath, 'r') # en lecture
Data = DATA.root.DATA

print("DATA=",DATA)

# Data est de type Table
print("Data=",Data)

# Data est de type Table
# Colonne 1
#print("Data[1]=",Data[1])
print("Data[1][0]=",Data[1][0])
print("Data[1][9]=",Data[1][1])
print("Data[2][0]=",Data[2][0])
print("Data[3][0]=",Data[3][0])


NBLIGNES = Data.nrows
print("NBLIGNES=",NBLIGNES)

#for x is 0 to NBLIGNES:
#   print(x, "AnneeDepart=",Data[1][x])


#afficher la liste des colonnes
print("\n Data Colonnes : ",Data.colnames)

print("\n Data Description : ",Data.description)

print("\n Data Colonnes avec type : ",Data.coltypes)
print("\n Data NBCOLONNES : ",Data.cols)
#print("\n Data Cols[0]: ",Data.cols[0])
print("\n Data.colnames[0]: ",Data.colnames[0])

#print("\n", Data.colnames[10], " : Data.cols[0][10]: ",Data.cols[0][10])
print("\n ----------------------------------AnneeDepart------------------------------------------------")
AnneeDepart = Data.cols[0][0]
print("\n AnneeDepart : ",AnneeDepart)

print("\n ----------------------------------PestPercoWeek------------------------------------------------")
testpercoWeek = []

testpercoWeek.append(Data.cols[0][10][0])
testpercoWeek.append(Data.cols[1][10])
print("\ntestpercoweek \n", np.mean(testpercoWeek[0]))

test = []
test.append(Data[0])
test.append(Data[1])
print("\n test : ",test[1][8])
print("\n lentest : ",len(test))

# pestPercoWeek = Data.cols[0][10]
# print("\n PestPercoWeek[0]: ",pestPercoWeek[0])
# print("\n PestPercoWeek Size",pestPercoWeek.size)
# print("\n PestPercoWeek Min",pestPercoWeek.min())
# print("\n PestPercoWeek Max",pestPercoWeek.max())
# print("\n Moyenne PestPercoWeek ",sum(pestPercoWeek)/1000)

print("\n ----------------------------------PestRunoffWeek------------------------------------------------")
# pestRunoffWeek = Data.cols[0][11]
# print("\n PestRunoffWeek Size",pestRunoffWeek.size)
# print("\n pestRunoffWeek Min",pestRunoffWeek.min())
# print("\n pestRunoffWeek Max",pestRunoffWeek.max())
# print("\n Moyenne pestRunoffWeek ",sum(pestRunoffWeek)/1000)


DATA.close()
