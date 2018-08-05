import sys
import pprint

# oi times <list of values> antistoixoun stis theseis tou pinaka alla se arithmous grey,
# diladi to 8(1000) einai to 12(0011) se grey arithmo kai ara dixnei sth sydetagmenh:
# 00: grammi(CD) 0 kai 11: stili(AB) 2 k.o.k.

list_of_values=[]
if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        if i > 0:
            n = int(sys.argv[i])
            list_of_values.append(n)

if len(sys.argv) == 17 :
    print('F = 1')

list_of_gray=[]
for i in list_of_values:
    #len = bit_len(i)
    #print(len)
    ab = bin(i >> 2)
    cd = bin(i & 0b0011)
    a = bin((i>>2)>>1)
    b = bin((i>>2) & 0b01)
    c = bin((i & 0b0011)>>1)
    d = bin((i & 0b0011) & 0b01)
    list_of_gray.append([a,b,c,d,i])

teams=[0,0,0,0]
team_row = [] # oles oi grammes me 1
team_col = [] # oles oi stiles me 1
solo_ones = []
team_r = {}
team_c = {}
visited=[]
for b1 in list_of_gray:
    for b2 in list_of_gray:
        if b1[3] == b2[2] and b2 not in team_col and b1 != b2: # gia na einai to y epomeno tou x: b1[D] == b2[C]
            if (b1[0],b1[1]) == (b2[0],b2[1]): # vriskontai sthn idia stili (b1[A],b1[B])==(b2[A],b2[B])
                if (b1[0],b1[1]) not in team_c.keys():
                    team_c[(b1[0],b1[1])] = [b1,b2]
                    team_col.append(b1)
                    team_col.append(b2)
                else:
                    team_c[(b1[0],b1[1])].append(b2)
                    team_col.append(b2)

        if b1[1] == b2[0] and b2 not in team_row and b1 != b2: # gia na einai to y epomeno tou x: b1[B] == b2[B]
            if (b1[2],b1[3]) == (b2[2],b2[3]): # vriskontai sthn idia seira
                if (b1[2],b1[3]) not in team_r.keys():
                    team_r[(b1[2],b1[3])] = [b1,b2]
                    team_row.append(b1)
                    team_row.append(b2)
                else:
                    team_r[(b1[2],b1[3])].append(b2)
                    team_row.append(b2)
for b in list_of_gray:
    if b not in team_col and b not in team_row:
        solo_ones.append(b)

grammes = list(team_r.keys())
stiles = list(team_c.keys())
visited=[[],[]]
omades = [] # omades grammwn omadopoihmenes ana plithos stoixeiwn
group = []
mikos = 4
plithos = 0
while plithos <= len(grammes)+len(stiles):
    plithos +=1
    list_grammwn = []
    list_stilwn = []
    for x in grammes:
        for y in grammes:
            if x[1] == y[0]: # vriskontai sthn amesws epomenh grammi
                if len(team_r[x]) == len(team_r[y]) == mikos:
                    if all(i[0]==j[0] and i[1]==j[1] for i,j in zip(team_r[x], team_r[y])): # tha preprei n vriskontai sthn idia stili A kai B
                        if y not in list_grammwn:
                            list_grammwn.append(y)
                            visited[0].append(y)

    if len(list_grammwn) != 0:
        if len(list_grammwn)!=3:
            if list_grammwn not in omades:
                omades.append(list_grammwn)
        else:
            if (i[2] != j[2] and i[3] != j[3] for x in list_grammwn for y in list_grammwn for x in team_r[i] for y in team_r[j]):
                list_grammwn.remove(y)
                omades.append(list_grammwn)

    for x in stiles:
        for y in stiles:
                if x[1] == y[0]:
                    if len(team_c[x]) == len(team_c[y]) == mikos:
                        if all(i[2]==j[2] and i[3]==j[3] for i,j in zip(team_c[x], team_c[y])):
                            if y not in list_stilwn:
                                list_stilwn.append(y)
                                visited[1].append(y)
    if len(list_stilwn) != 0:
        if list_stilwn not in group:
            group.append(list_stilwn)
    mikos = int(mikos/2)

solo_row=[]
solo_col=[]
m = 4
while m <=1:
    for x in grammes:
        if x not in visited[0] and len(team_r(x))==m:
            solo_row.append(team_r[x])
    for y in stiles:
        if y not in visited[1] and len(team_c(y))==m:
            solo_col.append(team_c[y])
    m = int(m/2)

def find_numbers(team):
    numbers=[]
    for number in team: # arxika pernw ta noumera tou kathe gray aritmou ths stilis
        numbers.append(number[4])
    return numbers

def bitwise_and(k,n):
    return(k&n)

def bitwise_or(k,n):
    return(k|n)

def find_what_letter_has_1_or_0_(i):
    letters_with_1=[]
    letters_with_0_or_1=[0,0,0,0]
    a = bin((i>>2)>>1)
    b = bin((i>>2) & 0b01)
    c = bin((i & 0b0011)>>1)
    d = bin((i & 0b0011) & 0b01)
    if a == '0b1': # A
        letters_with_0_or_1[0] = (1)

    if b == '0b1': # B
        letters_with_0_or_1[1] = (1)

    if c == '0b1': # C
        letters_with_0_or_1[2] = (1)

    if d == '0b1': # D
        letters_with_0_or_1[3] = (1)

    return (letters_with_0_or_1)

def answerPerGroup(results):
    AnswerPerGroup=''
    for i in results:
        if i[0][0] == 1:
            AnswerPerGroup += 'A'
        if i[0][1] == 1:
            AnswerPerGroup += 'B'
        if i[0][2] == 1:
            AnswerPerGroup += 'C'
        if i[0][3] == 1:
            AnswerPerGroup += 'D'
        if i[1][0] == 0:
            AnswerPerGroup += '~A'
        if i[1][1] == 0:
            AnswerPerGroup += '~B'
        if i[1][2] == 0:
            AnswerPerGroup += '~C'
        if i[1][3] == 0:
            AnswerPerGroup += '~D'
    return(AnswerPerGroup)

results=[]
numbers_of_each_col=[]
for i in group: # gia kathe omada stis omades stilwn
    aces = 15
    zeros = 0
    for j in i: # kathe stili sthn omada
        numbers_of_each_col += find_numbers(team_c[j]) # arxika pernw ta noumera tou kathe gray aritmou ths stilis
    for i in numbers_of_each_col:
     # arxika that ta kanw logiko and & gia na mou emfanistoun ta koina 1
     # kai logiko or | gia na vrw ta koina 0 se afth tnn omada
        aces = bitwise_and(aces,i)
        zeros = bitwise_or(zeros,i)
    # spaw ta apo telesmata zeros, aces se A,B,C,D
    results.append([find_what_letter_has_1_or_0_(aces),find_what_letter_has_1_or_0_(zeros)])

result=[]
numbers_of_each_row = []
for i in omades: # gia kathe omada stis omades grammwn
    aces = 15
    zeros = 0
    for j in i: # kathe stili sthn omada
        numbers_of_each_row += find_numbers(team_r[j]) # arxika pernw ta noumera tou kathe gray aritmou ths stilis
    for i in numbers_of_each_row:
     # arxika that ta kanw logiko and & gia na mou emfanistoun ta koina 1
     # kai logiko or | gia na vrw ta koina 0 se afth tnn omada
        aces = bitwise_and(aces,i)
        zeros = bitwise_or(zeros,i)
    # spaw ta apo telesmata zeros, aces se A,B,C,D
    result.append([find_what_letter_has_1_or_0_(aces),find_what_letter_has_1_or_0_(zeros)])

res=[]
if len(solo_row) != 0 :
    res=[] # gia monaxikes grammes
    numbers=[s]
    aces = 15
    zeros = 0
    for i in solo_row: # kathe stili sthn omada
        numbers += find_numbers(solo_row[j]) # arxika pernw ta noumera tou kathe gray aritmou ths stilis
    for i in numbers:
     # arxika that ta kanw logiko and & gia na mou emfanistoun ta koina 1
     # kai logiko or | gia na vrw ta koina 0 se afth tnn omada
        aces = bitwise_and(aces,i)
        zeros = bitwise_or(zeros,i)
    # spaw ta apo telesmata zeros, aces se A,B,C,D
    res.append([find_what_letter_has_1_or_0_(aces),find_what_letter_has_1_or_0_(zeros)])

r=[]
if len(solo_col) != 0 :
    numbers =[]
    r=[] # gia monaxikes stiles
    aces = 15
    zeros = 0
    for i in solo_col: # kathe stili sthn omada
        print(i)
        print(solo_col[i])
        numbers += find_numbers(solo_col[j]) # arxika pernw ta noumera tou kathe gray aritmou ths stilis
    for i in numbers:
     # arxika that ta kanw logiko and & gia na mou emfanistoun ta koina 1
     # kai logiko or | gia na vrw ta koina 0 se afth tnn omada
        aces = bitwise_and(aces,i)
        zeros = bitwise_or(zeros,i)
        print(bin(aces),bin(zeros))
    # spaw ta apo telesmata zeros, aces se A,B,C,D
    r.append([find_what_letter_has_1_or_0_(aces),find_what_letter_has_1_or_0_(zeros)])
    
k=0
F=''
if answerPerGroup(results) not in F:
    k += 1
    F = F + answerPerGroup(results)
if answerPerGroup(result) not in F:
    k += 1
    F = F + " V " + answerPerGroup(result)
if answerPerGroup(res) not in F:
    k += 1
    F = F + " V " + answerPerGroup(res)
if answerPerGroup(r) not in F:
    k += 1
    F = F + " V " + answerPerGroup(r)
print('F =',F,k)
