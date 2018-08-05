import csv
import timeit
import pprint
import sys

total_elapsed = 0
start = timeit.default_timer()

csv.register_dialect('SkipInitialSpaces', delimiter = ',', skipinitialspace=True)
with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile, dialect='SkipInitialSpaces')
    square_input=[]
    for row in spamreader:
        square_input.append(row)

diasxiseis=[]
diasxisi=[]
rows_used = []
columns_used=[]

def euler_diasxisi(square_input,grammi,stili):# adistoixh logiki me AllSimplePaths
    rows_used.append(grammi)
    columns_used.append(stili)
    diasxisi.append(square_input[grammi][stili])
    # an eksetasa oles tis stiles tou pinaka tote exw mia diasxisi kata euler
    if (stili == len(square_input[0])-1):
        if diasxisi not in diasxiseis: # an den thn exw vrei idi
            diasxiseis.append(diasxisi.copy())
    else:
        # metakinw thn anazitisi mia stili deksia kai th psaxnw kata grammi
        # an den exw xrhsimopoihsei th grammi, th stili kai ton aritho tote:
        for row in range(len(square_input[0])):
            if row not in rows_used and (stili+1) not in columns_used:
                if square_input[row][stili+1] not in diasxisi:
                    euler_diasxisi(square_input,row,stili+1)
    diasxisi.pop()
    rows_used.pop()
    columns_used.pop()
    return diasxiseis

for row in range(len(square_input[0])): # ksekinaw apo to prwto stoixeio kathe grammis
    d = euler_diasxisi(square_input,row,0)

gr_lt_sq=[]
if len(diasxiseis) != 0:
    s={}
    for i in diasxiseis[0]: # omadopoihsh twn diasxisewn analoga me ton 1o aritho tous
        for j in diasxiseis:
            if i == j[0]:
                if i not in s.keys():
                    s[i]=[] # key: to 1o stoixieo ths diasxisis
                    s[i].append(j) # value: oles oi diasxiseis me 1o tous stoixeio to key
                else:
                    s[i].append(j)

    def find_matched(used, diasxisi): # elegxos sugroushs
        return all(u != d for i in used for u, d in zip(i, diasxisi))

    first_number = 0 # upodikniei to 1o stoixeio mias diasxiseis
    used = [] # edw apothikevw tis diasxiseis pou kataskevazoun to 2o tetragwno
    dias_tried=[] # apothikevw oses diasxiseis exw eksetasei kai eixa/exw balei sthn used apo kathe 1o arithmo
    numbers_used=[] # gia elegxo an exei bei mia mono diasxisi apo kathe 1o stoixeio
    k=0
    while len(used) < len(square_input[0]):
        l = list(s[str(first_number)]) # pernei oles tis diasxiseis pou arxizoun apo first_number se lista apo to s
        for dias in l:
            if find_matched(used,dias) and (dias not in dias_tried) and (first_number not in numbers_used):
                used.append(dias.copy())
                numbers_used.append(first_number)
                dias_tried.append(dias.copy())
        if first_number not in numbers_used: # an de vrw diasxisi me 1o stoixeio first_number paw pros ta pisw
            if len(used) != 0: # den thelw na ksexasw tis diasxiseis me 1o stoixeio to 0
                used.pop() # vgazw th diasxisi me 1o arithmo to first_number-1
                numbers_used.pop() # antistoixa vgazw kai to stoixeio first_number-1
                for i in dias_tried:
                # ean paw pros ta pisw ksexnaw ti eixa eksetasei ean o arithmos einai megaluteros apo
                # first_number-1 gia na borw na ksana dokimasw me diaforetiko sundiasmo diasxisewn sto mellon
                    if int(i[0]) > first_number-1:
                        dias_tried.remove(i)
                first_number -= 1
        else: # an vrw mia diasxisi pou na mhn sugrouetai proxwraw sto epomeno 1o stoixeio
            first_number += 1

    stiles_square_output={} # edw apothikevw poia stoixeia tha exei kathe stili tou 2ou tetragwnou
    for i in range(len(square_input[0])):
        stiles_square_output[i]=[]

    for row in range(len(square_input[0])):
        for u in used:
            for i in u:
                # h thesi tou i sto u einai h stili pou tha anoikei to i sto 2o tetragwno
                if square_input[row][u.index(i)] == i:
                    stiles_square_output[u.index(i)].append(u[0])

    square_output=[] # kataskevh tou 2ou tetragwbou
    for col in stiles_square_output.keys():
        # pernw ta stoixeia ths kathe stilis ws lista gia na borw na ta diatreksw me seira
        k = list(stiles_square_output[col])
        if col == 0:
            for i in k:
                square_output.append([i]) # dimiourgw tis listes pou apotelous tis grammes tou 2ou tetragwnou
        else:
            for i,j in zip(k,square_output):
                j.append(i) # tis sublirwnw me ola ta stoixeia pou anoikoun se kathe grammi antistoixa

    gr_lt_sq=[] # kataskevh el-lat-tetragwnou
    for row in range(len(square_input[0])):
        for column in range(len(square_input[0])):
            if column == 0: # dimiourgw tis listes pou apoteloun tis grammes tou el-lat-tetrag
                gr_lt_sq.append([(int(square_input[row][column]),int(square_output[row][column]))])
            else:
                for i in gr_lt_sq:
                    if gr_lt_sq.index(i) == row:
                    # tis sublirwnw me ta stoixeia pou vriskontai sthn idia thesi me to 1o kai 2o tetragwno
                        i.append((int(square_input[row][column]),int(square_output[row][column])))
    pprint.pprint(gr_lt_sq,width=85)
else:
    print(gr_lt_sq)
end = timeit.default_timer()
total_elapsed += end - start
print(total_elapsed,"seconds")
x = divmod(total_elapsed,60)
print(x[0],"min",x[1],"sec")
