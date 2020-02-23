# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:11:47 2020

@author: jm.rivera@uniandes.edu.co
This script generates an array with the shape of the sound wave used in the startle and prepulse trials
"""
a=[[      1,   30051,     100,       0],
       [      2,   50021,      75,      30],
       [      1,   85051,     100,       0],
       [      2,  104021,      75,      30],
       [      2,  129951,      75,     100],
       [      2,  150021,      75,      30],
       [      1,  181051,     100,       0],
       [      1,  202051,     100,       0],
       [      2,  223021,      85,      30],
       [      2,  250021,      85,      30],
       [      2,  271951,      85,     100],
       [      1,  293051,     100,       0],
       [      1,  315051,     100,       0],
       [      2,  334951,      75,     100],
       [      2,  358051,     100,       0],
       [      2,  381951,      85,     100],
       [      1,  411051,     100,       0],
       [      2,  437951,      75,     100],
       [      2,  459021,      85,      30],
       [      2,  479951,      85,     100],
       [      1,  502051,     100,       0],
       [      1,  528051,     100,       0],
       [      2,  558021,      85,      30],
       [      2,  586951,      75,     100],
       [      2,  609021,      75,      30],
       [      1,  639051,     100,       0],
       [      1,  661051,     100,       0],
       [      2,  686951,      75,     100],
       [      2,  706951,      85,     100],
       [      2,  736951,      85,     100],
       [      2,  757021,      85,      30],
       [      1,  785051,     100,       0],
       [      1,  814051,     100,       0],
       [      2,  839021,      75,      30],
       [      1,  869051,     100,       0],
       [      2,  894951,      85,     100],
       [      2,  930051,     100,       0],
       [      2,  950021,      75,      30],
       [      1,  985051,     100,       0],
       [      2, 1004021,      75,      30],
       [      2, 1029951,      75,     100],
       [      2, 1050021,      75,      30],
       [      1, 1081051,     100,       0],
       [      1, 1102051,     100,       0],
       [      2, 1123021,      85,      30],
       [      2, 1150021,      85,      30],
       [      2, 1171951,      85,     100],
       [      1, 1193051,     100,       0],
       [      1, 1215051,     100,       0],
       [      2, 1234951,      75,     100],
       [      2, 1258051,     100,       0],
       [      2, 1281951,      85,     100],
       [      1, 1311051,     100,       0],
       [      2, 1337951,      75,     100],
       [      2, 1359021,      85,      30],
       [      2, 1379951,      85,     100],
       [      1, 1402051,     100,       0],
       [      1, 1428051,     100,       0],
       [      2, 1458021,      85,      30],
       [      2, 1486951,      75,     100],
       [      2, 1509021,      75,      30],
       [      1, 1539051,     100,       0],
       [      1, 1561051,     100,       0],
       [      2, 1586951,      75,     100],
       [      2, 1606951,      85,     100],
       [      2, 1636951,      85,     100],
       [      2, 1657021,      85,      30],
       [      1, 1685051,     100,       0],
       [      1, 1714051,     100,       0],
       [      2, 1739021,      75,      30],
       [      1, 1769051,     100,       0],
       [      2, 1794951,      85,     100]]
z=[[0, 0],
 [30050, 0],
 [30051, 100],
 [30071, 100],
 [30072, 0],
 [50020, 0],
 [50021, 75],
 [50025, 75],
 [50026, 0],
 [50050, 0],
 [50051, 100],
 [50071, 100],
 [50072, 0],
 [85050, 0],
 [85051, 100],
 [85071, 100],
 [85072, 0],
 [104020, 0],
 [104021, 75],
 [104025, 75],
 [104026, 0],
 [104050, 0],
 [104051, 100],
 [104071, 100],
 [104072, 0],
 [129950, 0],
 [129951, 75],
 [129955, 75],
 [129956, 0],
 [130050, 0],
 [130051, 100],
 [130071, 100],
 [130072, 0],
 [150020, 0],
 [150021, 75],
 [150025, 75],
 [150026, 0],
 [150050, 0],
 [150051, 100],
 [150071, 100],
 [150072, 0],
 [181050, 0],
 [181051, 100],
 [181071, 100],
 [181072, 0],
 [202050, 0],
 [202051, 100],
 [202071, 100],
 [202072, 0],
 [223020, 0],
 [223021, 85],
 [223025, 85],
 [223026, 0],
 [223050, 0],
 [223051, 100],
 [223071, 100],
 [223072, 0],
 [250020, 0],
 [250021, 85],
 [250025, 85],
 [250026, 0],
 [250050, 0],
 [250051, 100],
 [250071, 100],
 [250072, 0],
 [271950, 0],
 [271951, 85],
 [271955, 85],
 [271956, 0],
 [272050, 0],
 [272051, 100],
 [272071, 100],
 [272072, 0],
 [293050, 0],
 [293051, 100],
 [293071, 100],
 [293072, 0],
 [315050, 0],
 [315051, 100],
 [315071, 100],
 [315072, 0],
 [334950, 0],
 [334951, 75],
 [334955, 75],
 [334956, 0],
 [335050, 0],
 [335051, 100],
 [335071, 100],
 [335072, 0],
 [358050, 0],
 [358051, 100],
 [358055, 100],
 [358056, 0],
 [358050, 0],
 [358051, 100],
 [358071, 100],
 [358072, 0],
 [381950, 0],
 [381951, 85],
 [381955, 85],
 [381956, 0],
 [382050, 0],
 [382051, 100],
 [382071, 100],
 [382072, 0],
 [411050, 0],
 [411051, 100],
 [411071, 100],
 [411072, 0],
 [437950, 0],
 [437951, 75],
 [437955, 75],
 [437956, 0],
 [438050, 0],
 [438051, 100],
 [438071, 100],
 [438072, 0],
 [459020, 0],
 [459021, 85],
 [459025, 85],
 [459026, 0],
 [459050, 0],
 [459051, 100],
 [459071, 100],
 [459072, 0],
 [479950, 0],
 [479951, 85],
 [479955, 85],
 [479956, 0],
 [480050, 0],
 [480051, 100],
 [480071, 100],
 [480072, 0],
 [502050, 0],
 [502051, 100],
 [502071, 100],
 [502072, 0],
 [528050, 0],
 [528051, 100],
 [528071, 100],
 [528072, 0],
 [558020, 0],
 [558021, 85],
 [558025, 85],
 [558026, 0],
 [558050, 0],
 [558051, 100],
 [558071, 100],
 [558072, 0],
 [586950, 0],
 [586951, 75],
 [586955, 75],
 [586956, 0],
 [587050, 0],
 [587051, 100],
 [587071, 100],
 [587072, 0],
 [609020, 0],
 [609021, 75],
 [609025, 75],
 [609026, 0],
 [609050, 0],
 [609051, 100],
 [609071, 100],
 [609072, 0],
 [639050, 0],
 [639051, 100],
 [639071, 100],
 [639072, 0],
 [661050, 0],
 [661051, 100],
 [661071, 100],
 [661072, 0],
 [686950, 0],
 [686951, 75],
 [686955, 75],
 [686956, 0],
 [687050, 0],
 [687051, 100],
 [687071, 100],
 [687072, 0],
 [706950, 0],
 [706951, 85],
 [706955, 85],
 [706956, 0],
 [707050, 0],
 [707051, 100],
 [707071, 100],
 [707072, 0],
 [736950, 0],
 [736951, 85],
 [736955, 85],
 [736956, 0],
 [737050, 0],
 [737051, 100],
 [737071, 100],
 [737072, 0],
 [757020, 0],
 [757021, 85],
 [757025, 85],
 [757026, 0],
 [757050, 0],
 [757051, 100],
 [757071, 100],
 [757072, 0],
 [785050, 0],
 [785051, 100],
 [785071, 100],
 [785072, 0],
 [814050, 0],
 [814051, 100],
 [814071, 100],
 [814072, 0],
 [839020, 0],
 [839021, 75],
 [839025, 75],
 [839026, 0],
 [839050, 0],
 [839051, 100],
 [839071, 100],
 [839072, 0],
 [869050, 0],
 [869051, 100],
 [869071, 100],
 [869072, 0],
 [894950, 0],
 [894951, 85],
 [894955, 85],
 [894956, 0],
 [895050, 0],
 [895051, 100],
 [895071, 100],
 [895072, 0],
 [930050, 0],
 [930051, 100],
 [930055, 100],
 [930056, 0],
 [930050, 0],
 [930051, 100],
 [930071, 100],
 [930072, 0],
 [950020, 0],
 [950021, 75],
 [950025, 75],
 [950026, 0],
 [950050, 0],
 [950051, 100],
 [950071, 100],
 [950072, 0],
 [985050, 0],
 [985051, 100],
 [985071, 100],
 [985072, 0],
 [1004020, 0],
 [1004021, 75],
 [1004025, 75],
 [1004026, 0],
 [1004050, 0],
 [1004051, 100],
 [1004071, 100],
 [1004072, 0],
 [1029950, 0],
 [1029951, 75],
 [1029955, 75],
 [1029956, 0],
 [1030050, 0],
 [1030051, 100],
 [1030071, 100],
 [1030072, 0],
 [1050020, 0],
 [1050021, 75],
 [1050025, 75],
 [1050026, 0],
 [1050050, 0],
 [1050051, 100],
 [1050071, 100],
 [1050072, 0],
 [1081050, 0],
 [1081051, 100],
 [1081071, 100],
 [1081072, 0],
 [1102050, 0],
 [1102051, 100],
 [1102071, 100],
 [1102072, 0],
 [1123020, 0],
 [1123021, 85],
 [1123025, 85],
 [1123026, 0],
 [1123050, 0],
 [1123051, 100],
 [1123071, 100],
 [1123072, 0],
 [1150020, 0],
 [1150021, 85],
 [1150025, 85],
 [1150026, 0],
 [1150050, 0],
 [1150051, 100],
 [1150071, 100],
 [1150072, 0],
 [1171950, 0],
 [1171951, 85],
 [1171955, 85],
 [1171956, 0],
 [1172050, 0],
 [1172051, 100],
 [1172071, 100],
 [1172072, 0],
 [1193050, 0],
 [1193051, 100],
 [1193071, 100],
 [1193072, 0],
 [1215050, 0],
 [1215051, 100],
 [1215071, 100],
 [1215072, 0],
 [1234950, 0],
 [1234951, 75],
 [1234955, 75],
 [1234956, 0],
 [1235050, 0],
 [1235051, 100],
 [1235071, 100],
 [1235072, 0],
 [1258050, 0],
 [1258051, 100],
 [1258055, 100],
 [1258056, 0],
 [1258050, 0],
 [1258051, 100],
 [1258071, 100],
 [1258072, 0],
 [1281950, 0],
 [1281951, 85],
 [1281955, 85],
 [1281956, 0],
 [1282050, 0],
 [1282051, 100],
 [1282071, 100],
 [1282072, 0],
 [1311050, 0],
 [1311051, 100],
 [1311071, 100],
 [1311072, 0],
 [1337950, 0],
 [1337951, 75],
 [1337955, 75],
 [1337956, 0],
 [1338050, 0],
 [1338051, 100],
 [1338071, 100],
 [1338072, 0],
 [1359020, 0],
 [1359021, 85],
 [1359025, 85],
 [1359026, 0],
 [1359050, 0],
 [1359051, 100],
 [1359071, 100],
 [1359072, 0],
 [1379950, 0],
 [1379951, 85],
 [1379955, 85],
 [1379956, 0],
 [1380050, 0],
 [1380051, 100],
 [1380071, 100],
 [1380072, 0],
 [1402050, 0],
 [1402051, 100],
 [1402071, 100],
 [1402072, 0],
 [1428050, 0],
 [1428051, 100],
 [1428071, 100],
 [1428072, 0],
 [1458020, 0],
 [1458021, 85],
 [1458025, 85],
 [1458026, 0],
 [1458050, 0],
 [1458051, 100],
 [1458071, 100],
 [1458072, 0],
 [1486950, 0],
 [1486951, 75],
 [1486955, 75],
 [1486956, 0],
 [1487050, 0],
 [1487051, 100],
 [1487071, 100],
 [1487072, 0],
 [1509020, 0],
 [1509021, 75],
 [1509025, 75],
 [1509026, 0],
 [1509050, 0],
 [1509051, 100],
 [1509071, 100],
 [1509072, 0],
 [1539050, 0],
 [1539051, 100],
 [1539071, 100],
 [1539072, 0],
 [1561050, 0],
 [1561051, 100],
 [1561071, 100],
 [1561072, 0],
 [1586950, 0],
 [1586951, 75],
 [1586955, 75],
 [1586956, 0],
 [1587050, 0],
 [1587051, 100],
 [1587071, 100],
 [1587072, 0],
 [1606950, 0],
 [1606951, 85],
 [1606955, 85],
 [1606956, 0],
 [1607050, 0],
 [1607051, 100],
 [1607071, 100],
 [1607072, 0],
 [1636950, 0],
 [1636951, 85],
 [1636955, 85],
 [1636956, 0],
 [1637050, 0],
 [1637051, 100],
 [1637071, 100],
 [1637072, 0],
 [1657020, 0],
 [1657021, 85],
 [1657025, 85],
 [1657026, 0],
 [1657050, 0],
 [1657051, 100],
 [1657071, 100],
 [1657072, 0],
 [1685050, 0],
 [1685051, 100],
 [1685071, 100],
 [1685072, 0],
 [1714050, 0],
 [1714051, 100],
 [1714071, 100],
 [1714072, 0],
 [1739020, 0],
 [1739021, 75],
 [1739025, 75],
 [1739026, 0],
 [1739050, 0],
 [1739051, 100],
 [1739071, 100],
 [1739072, 0],
 [1769050, 0],
 [1769051, 100],
 [1769071, 100],
 [1769072, 0],
 [1794950, 0],
 [1794951, 85],
 [1794955, 85],
 [1794956, 0],
 [1795050, 0],
 [1795051, 100],
 [1795071, 100],
 [1795072, 0],
 [1800072, 0]]

def soundWave():
    z=[]
    for i in range(len(a)):
        x=a[i]
        y=x[0]
        if y==1:
            z.append([x[1]-1,0])
            z.append([x[1],x[2]])
            z.append([x[1]+20,x[2]])
            z.append([x[1]+21,0])
        else:
            z.append([x[1]-1,0])
            z.append([x[1],x[2]])
            z.append([x[1]+4,x[2]])
            z.append([x[1]+5,0])
    
            z.append([x[1]+x[3]-1,0])
            z.append([x[1]+x[3],100])
            z.append([x[1]+x[3]+20,100])
            z.append([x[1]+x[3]+21,0])
    
    return z