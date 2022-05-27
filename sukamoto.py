x_suhu1 = input ("masukan nilai suhu1 =")
x_ketinggian1 = input ("masukan nilai ketingggian1 =")

suhu = int (x_suhu1)
ketinggian = int (x_ketinggian1)

#menghitung suhu
if suhu<= 27 :
    value_sedikitA = 1
    value_banyakA = 0
if suhu > 30 and suhu < 100 :
    value_sedikitA = (100- suhu)/(100 - 30)
    value_banyakA = (suhu - 300)/(100 - 30)
if suhu >= 100 :
    value_sedikitA = 0
    value_banyakA= 1

print ('suhu')

print ('suhu', value_sedikitA)
print ('suhu', value_banyakA)



#menghitung ketinggian air

if ketinggian <= 25 :
    value_sedikitB = 1
    value_banyakB = 0
if ketinggian > 30 and ketinggian < 50 :
    value_sedikitB = (50- ketinggian)/(50 - 30)
    value_banyakB = (ketinggian - 30)/(50 - 30)
if ketinggian >= 50 :
    value_sedikitB = 0
    value_banyakB= 1


print ('ketinggian')
print ('ketinggian', value_sedikitB)
print ('ketinggian', value_banyakB)


#proses inferensi 
#proses buzzer
speed=[]
def fungsiinferensiterbuka (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 100])

def fungsiinferensitertutup (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 10])
#proses led hijau
speed=[]
def fungsiinferensiterbuka (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 30])

def fungsiinferensitertutup (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 10])
#proses led orange
speed=[]
def fungsiinferensiterbuka (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 70])

def fungsiinferensitertutup (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian,)
                speed.append([hasil_output, 30])
#proses led merah
speed=[]
def fungsiinferensiterbuka (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 100])

def fungsiinferensitertutup (variabel_suhu, variabel_ketinggian) :
    if variabel_suhu != 0:
        if variabel_ketinggian != 0:
                hasil_output = min (variabel_suhu, variabel_ketinggian)
                speed.append([hasil_output, 70])


fungsiinferensiterbuka (value_sedikitA, value_banyakB)
fungsiinferensiterbuka (value_sedikitA, value_sedikitB)
fungsiinferensiterbuka (value_banyakA, value_sedikitB)
fungsiinferensiterbuka (value_sedikitA, value_banyakB)
fungsiinferensiterbuka (value_banyakA, value_banyakB)
fungsiinferensitertutup (value_sedikitA, value_sedikitB)

#print ('maka speed adalah', speed)

#proses defuzzyfikasi

perkalian_new = 0
pembagian_new = 0

for j in range (0, len(speed)):
    perkalian = speed[j][0]*speed[j][1]
    pembagian = speed[j][0]
    perkalian_new = perkalian_new + perkalian
    pembagian_new = pembagian_new + pembagian

z = perkalian_new/pembagian_new

print ('persentasi air (z) = ', z, '[%]')
