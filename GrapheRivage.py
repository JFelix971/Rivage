import matplotlib.pyplot as plt
import numpy as np
import tables
from math import pi,cos,sin,exp


# Calculer une sortie d'interet -> vecteurs des 7 sorties importantes pour les 600simulations .
# 600 simulation = 1 vecteur de 28cases
# Faire un tri sur les années départ et les scénario
# Regarder la variabilité des années départ sur un des tableau PestPerwoWeek ou l'autre
filename =  'CombinedOUTPUTS_ZONE_2_HIVERNAGE.h5'
DATA =  tables.open_file(filename, 'r')
Data = DATA.root.DATA

#--------------------------Def variables importantes-------------------------------------------
NBLIGNES = Data.nrows
NBSCENARIO = NBLIGNES/1200
# print("NBLIGNES=",NBLIGNES)
print("NBScnario=",int(NBSCENARIO))

dose_pest_apply = 6.0
PestApplyCum1 = 1417.86
PestApplyCum2 = 2160.00
Glyphosate_Z2H1 = []
Ampa_Z2H1 = []
ite_gly = 0
ite_ampa = 0
types_sol = ['INTERGRADE', 'ANDOSOL', 'NITISOL', 'FERRISOL', 'COLLUVION']

Week_per_year = 50

#-----------------------------------Verif value Data----------------------------------------------------------------
# cultures = []#OK 8 cultures
# stade = []#OK 3stades
# zones = []
# for i in range(0,Data.nrows):
#     cultures.append(Data[i][2])
#     stade.append(Data[i][16])
#     zones.append(Data[i][20])
#     if( i%50001 == 50000):
#         print("\n i --> ", i)
#
# cultures = list(set(cultures))
# stade = list(set(stade))
# zones = list(set(zones))
# print("\n cultures :", cultures)
# print("\n stade :", stade)
# print("\n zones :", zones)
#-----------------------------------Verif value Data - OK----------------------------------------------------------------


# Seperation des deux molecules - Il faut choisir le nombre de ligne totale sachant que 1200 = 1scenario.
for i in range(0,1200): #1200 pour la boucle
    if(i%2 == 0):
        Glyphosate_Z2H1.append(Data[i])
        # print("\n verif data  gly: ", i, ite_gly, Glyphosate_Z2H1[ite_gly][21], Glyphosate_Z2H1[ite_gly][13])
        ite_gly= ite_gly+1
    elif(i%2 == 1):
        Ampa_Z2H1.append(Data[ i])
        # print("\n verif data ampa: ", i, ite_ampa, Ampa_Z2H1[ite_ampa][21], Ampa_Z2H1[ite_ampa][13])
        ite_ampa=ite_ampa+1

print("\n length gly : ", len(Glyphosate_Z2H1))
print("\n length ampa : ", len(Ampa_Z2H1))

# print("\n verif data : ", Ampa_Z2H1[4][21])

Years = np.linspace(Glyphosate_Z2H1[0][0],Glyphosate_Z2H1[0][0]+31,1000)

ampa_infiltration =  0
ampa_ruissellement = 0
ampa_all = 0

glypho_infiltration =  0
glypho_ruissellement = 0
glypho_all = 0

test = []

for i in range(0,1000):
    test.append(1)


somme_buff = []
somme=0
for i in range(0,600):
    ampa_infiltration += Ampa_Z2H1[i][10]
    ampa_ruissellement += Ampa_Z2H1[i][11]


ampa_all = ampa_infiltration + ampa_ruissellement
print("\n ampa_infiltration = ", len(ampa_ruissellement))

for i in range(0,600):
    glypho_infiltration += Glyphosate_Z2H1[i][10]
    glypho_ruissellement += Glyphosate_Z2H1[i][11]

glypho_all = glypho_infiltration + glypho_ruissellement

print("\n tailles : ", len(glypho_infiltration))
mean_glypho = []
for i in range(0,1):
    mean_glypho.append(np.mean(Glyphosate_Z2H1[i][11]))

# print("\n mean_glypho = ", mean_glypho)


ite_gly = 0
ite = 1
ite_ampa = 0
buff_inf_gly = []
buff_inf_ampa = []
buff_rui_gly = []
buff_rui_ampa = []
buff_year = []
for i in range(0,1000):
    if( i%50 == 49 ):
        buff_inf_gly.append( np.mean(glypho_infiltration[ ite_gly * 50 : ( ite_gly + 1 ) * 50]))
        buff_inf_ampa.append( np.mean(ampa_infiltration[ ite_ampa * 50 : ( ite_ampa + 1 ) * 50]))
        buff_rui_gly.append( np.mean(glypho_ruissellement[ ite_gly * 50 : ( ite_gly + 1 ) * 50]))
        buff_rui_ampa.append( np.mean(ampa_ruissellement[ ite_ampa * 50 : ( ite_ampa + 1 ) * 50]))
        buff_year.append(ite*50)
        ite = ite + 1
        ite_gly = ite_gly + 1
        ite_ampa = ite_ampa + 1

# print("\n len buff inf : ", len(buff_inf_gly))
# print("\n buff inf glypho : ", buff_inf_gly)
#
# print("\n len buff ruiss : ", len(buff_rui_gly))
# print("\n  buff ruiss : ", buff_rui_gly)
# print("\n buff year : ", buff_year)

# TEST trié --- OK

# buff_old_ind = []
# buff_new_ind = []
# years_gly = []
# ntaille = 600
# for i in range(0,ntaille):
#      years_gly.append(Glyphosate_Z2H1[i][0]) # Recupère les années dans le tableau pour trier
# print("\n GLYPHO ", years_gly)
#
#
# for i in enumerate(years_gly):
#     # print(i)
#     buff_old_ind.append(i)#On recupère les anciennes indices
#
# print("\n new ind")
# for i in enumerate(sorted(years_gly)):
#     # print(i)
#     buff_new_ind.append(i) # On trie puis on recupère les nouvelles indices
#
# newGly = [0]*ntaille # Nouvelle table de glyphosate
#
# for i in range(0,len(years_gly)):
#     newGly[buff_new_ind[i][0]] = buff_new_ind[i][1] # Redistribution des données avec la nouvelle indices
#
# print("\n Ind trié : ", newGly)
#
# uniqyear = []
# uniqyear = list(set(years_gly))
# for i in range(0, len(uniqyear)):
#     print("\n  annee : ", uniqyear[i], " nb occ : ", newGly.count(uniqyear[i]))



#------------------------------------------------------Fonction tri fichier par annee--------------------------------------------------
# Fonction qui retourne la valeur de la nouvelle position
def getKey(item):
    return item[1]

def Tri_FilebyYear(glyphosate, ampa, num_scenario, pas_simulation):

    newGly = [0]*pas_simulation
    oldInd = []
    newInd = []
    years = []

    uniqyear = []
    occyear = []

    result_gly = [0]*pas_simulation # Nouvelle table de glyphosate
    result_ampa = [0]*pas_simulation # Nouvelle table ampa

    for i in range(((num_scenario-1)*pas_simulation), (num_scenario*pas_simulation)):
        years.append(glyphosate[i][0]) # Recupère les années dans le tableau pour trier

    for i in enumerate(years):
        oldInd.append(i)#On recupère les anciens indices

    for i in enumerate(sorted(oldInd, key=getKey)):
        # print("\n i : ",i)
        newInd.append(i) # On trie puis on recupère les nouvels indices

    # print("\n old indices : ", oldInd)
    # print("\n new indices : ", newInd)
    # print("\n longueur years", len(years))
    #
    # for i in range(0,25):
    #     print("\n old position : ",oldInd[i],"   new position : ",newInd[i])

    for i in range(0,len(years)):
        result_gly[i] = glyphosate[((num_scenario-1)*pas_simulation)+newInd[i][1][0]] # Redistribution des données avec la nouvelle indices
        result_ampa[i] = ampa[((num_scenario-1)*pas_simulation)+newInd[i][1][0]] # Redistribution des données avec la nouvelle indices
        newGly[i] = newInd[i][1][1]

    uniqyear = list(set(years))
    # print("\n uniqyear", uniqyear)

    for i in range(0, len(uniqyear)):
        occyear.append(newGly.count(uniqyear[i]))
        # print("\n  annee : ", uniqyear[i], " nb occ : ", occyear[i])

    return result_gly, result_ampa, occyear
#------------------------------------------------------Fonction tri fichier par annee--------------------------------------------------
GLYPHOSATE = []
AMPA = []
OCCU_YEAR = []
GLYPHOSATE, AMPA, OCCU_YEAR = Tri_FilebyYear(Glyphosate_Z2H1,Ampa_Z2H1,1,600)

# for i in range (0,25):
#     print("\nligne: ",i,"\tglypho", GLYPHOSATE[i][0], " Scenario : ", GLYPHOSATE[i][13])
# print("\n 1ere ligne ampa", AMPA[0][0])
print("\n somme occ :", sum(OCCU_YEAR[0:5]))

glypho_inf = 0
glypho_rui = 0
for i in range(0,600):
    glypho_inf += GLYPHOSATE[i][10]
    glypho_rui += GLYPHOSATE[i][11]

inf_mean_buff = []
rui_mean_buff = []
for i in range(0,600):
    inf_mean_buff.append(np.mean(glypho_inf[i]))
    rui_mean_buff.append(np.mean(glypho_rui[i]))

ite = 0
pas = 5
inf_buff = []
rui_buff = []

y = [2005,2010,2015,2020,2030]
newyears =[]
newyears.append(0)

for i in range(0,6):
    newyears.append(sum(OCCU_YEAR[i*5:(i+1)*5]))

print("\n newyears : ",newyears," len : ", len(newyears))

for i in range(0,len(newyears)-1):
    inf_buff.append(sum(glypho_inf[newyears[i]:newyears[i+1]]) / newyears[i+1])
    rui_buff.append(sum(glypho_rui[newyears[i]:newyears[i+1]]) / newyears[i+1])
    print("\n rui buff ", rui_buff[i])
#----------------------------------Ampa------------------------------------------------
plt.figure()
plt.title("Variabilite entre les années")
plt.plot(inf_buff)
plt.show()


plt.figure()
plt.title("Variabilite entre les années")
plt.plot(inf_buff)
plt.show()

plt.figure()
plt.subplot(221)
plt.title("Evolution des voies de transfert en fonction du temps - Ampa (2000-2030)")

plt.plot(Years,ampa_infiltration/600, "r", label="Infiltration ")
plt.ylabel("Quantite exportées")
plt.legend()

plt.subplot(222)
plt.title("Evolution des voies de transfert en fonction du temps - Ampa (ligne 1)(2000-2030)")
plt.plot(Years,ampa_ruissellement/600, label="Ruissellement ")
plt.plot(Years,test)
plt.xlabel("Années")
plt.ylabel("Quantite exportées")
plt.legend()

plt.subplot(212)
# plt.title("Evolution des voies de transfert en fonction du temps - Ampa (2000-2030)")
plt.plot(Years, ampa_all, label="Cumul Infiltration + Ruissellement ")
plt.xlabel("Années")
plt.ylabel("Quantité exportées")
plt.legend()
# plt.show()

#----------------------------------Glyphosate------------------------------------------------
plt.figure()
plt.subplot(221)
plt.title("Evolution des voies de transfert en fonction du temps - Glyphosate (ligne 0) (2000-2030)")
plt.plot(Years,glypho_infiltration, "r", label="Infiltration ")
plt.ylabel("Quantite exportées")
plt.legend()

plt.subplot(222)
plt.title("Evolution des voies de transfert en fonction du temps - Glyphosate (2000-2030)")
plt.plot(Years,glypho_ruissellement, label="Ruissellement ")
plt.plot(Years,test)
plt.xlabel("Années")
plt.ylabel("Quantite exportées")
plt.legend()

plt.subplot(212)
# plt.title("Evolution des voies de transfert en fonction du temps - Ampa (2000-2030)")
plt.plot(Years, glypho_all, label="Cumul Infiltration + Ruissellement ")
plt.xlabel("Années")
plt.ylabel("Quantité exportées")
plt.legend()
# plt.show()

#---------------------------------------------------
plt.figure()
plt.title("Cumul des quantités exportées du Glyphosate en fonction du temps(50vals -> 1an)")
plt.plot(buff_year, buff_inf_gly, label="Infiltration")
plt.plot(buff_year, buff_rui_gly, label="Ruissellement")
plt.xlabel("Years")
plt.ylabel("Quantité exportée")
plt.legend()
# plt.show()

plt.figure()
plt.title("Cumul des quantités exportées de l'ampa en fonction du temps(50vals -> 1an)")
plt.plot(buff_year, buff_inf_ampa, label="Infiltration")
plt.plot(buff_year, buff_rui_ampa, label="Ruissellement")
plt.xlabel("Semaines")
plt.ylabel("Quantité exportée")
plt.legend()
# plt.show()

# plt.figure()
# n, bins, patches = plt.hist(ampa_ruissellement)
# plt.show()
# plt.figure()
# plt.plot(Years,ampa_infiltration/600  , label="Infiltration ")
# plt.title("Evolution des voies de transferts - Ampa")
# plt.xlabel("Années")
# plt.ylabel("Quantite exportées(mean)")
# plt.legend()
# plt.show()


DATA.close()
