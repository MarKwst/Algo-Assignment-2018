import argparse

parser = argparse.ArgumentParser() #eisagwgh parametrwn apo to xrhsth.
parser.add_argument("filename", help="name of input file")
parser.add_argument("b", help="bias_parameter", type=float)
parser.add_argument("s", help="start_node")
parser.add_argument("t", help="end_node")

args = parser.parse_args()

def read_weighted_graph(filename, directed=True):#dimiourgia graphou kai varwn.
    g = {}
    weights  = {}
    with open(filename) as input_file:
        for line in input_file:
            parts = line.split()
            [n1, n2, w] = line.split()
            if n1 not in g:
                g[n1] = []
            if n2 not in g:
                g[n2] = []
            g[n1].append(n2)
            weights[(n1, n2)] = int(w)
    return (g, weights)

g, w = read_weighted_graph(args.filename)

paths=[] #arxikopoihsh path,paths,visited gia thn allsimplepaths
path=[]
visited={}
for i in g.keys():
    visited[i]=False

def AllSimplePaths(g,s,t):#upologismos olwn twn monopatiwn apo to s sto t.
    visited[s]=True
    path.append(s)
    if s==t:
        paths.append(path.copy())
    else:
        for u in g[s]:
            if (visited[u]==False):
                AllSimplePaths(g,u,t)
    path.pop()
    visited[s]=False
    return paths

allpaths = AllSimplePaths(g,args.s,args.t)

#dist: key-thesi tou kathe monopatiou sthn allpaths,
#value-pragmatiko kostos tou kathe monopatiou pou antistoixei sth thesh key.
dist={}

for path in allpaths:
    #xreisimopoiw to k,thesi tou i sto allpaths,
    #giati to dist[allpaths.index(i)] mou evgaze invalid syntax.
    #thelw th thesi ws key giati etsi tha borw na vrw mesa apo thn allpaths
    #se poio monopati anaferete to value diladi to kostos.
    k = allpaths.index(path)
    dist[k]=0

def TrueCost(allpaths,w): #upologismos pragmatikou kostous twn monopatiwn.
    for path in allpaths:
        k = allpaths.index(path)
        for j in range(len(path)):
            if j==(len(path)-1):
                dist[k] = dist[k]
            else:
                dist[k] = dist[k] + w.get((path[j],path[j+1]), 0)
    return dist

dist = TrueCost(allpaths,w)

#evresi monopatiou me to min pragmatiko kostos.
minim = 500 #minim: to min kostos
minpath = 0 #minpath: h thesi sthn opoia vriskete to monopati me to min kostos sto allpaths.
for i in dist:
    if dist[i]<minim:
        minim=dist[i]
        minpath = i
print(allpaths[minpath],minim)

terminal = args.t
start = args.s
bestpath = [start] # lista me to veltisto bias monopati

while start != terminal: #upologismos biascost
    min=10000
    paths=[] #arxikopoihsh path,paths,visited gia thn allsimplepaths
    path=[]
    visited={}
    for i in g.keys():
        visited[i]=False
    newpaths = AllSimplePaths(g,start,terminal) #evresi olwn twn path metaksi NEOU start kai terminal
    for path in newpaths:
        cost=0
        for j in path:
            k = path.index(j)
            if j == start: #metaksi tou start kai twn geitwnwn vazw oloklhro ro baros
                cost = cost + w.get((path[k],path[k+1]), 0)
            elif j==path[-1]: #an ftasw ston komvo termatismou den prosthetw tpt
                cost = cost
            else: #gia kathe sundesmo pou den einai metaksi tou start kai twn geitwnwn
                cost = cost + w.get((path[k],path[k+1]), 0)*args.b
        if cost<min:
            min = cost #vrika neo veltisto path
            next = path[1] #pernw to deftero komvo tou path o opoios einai o neos start
    start = next
    bestpath.append(start)

for i in allpaths: #vriskw poio einai to pragmatiko kostos tou biaspath
    if i == bestpath:
        biascost = dist[allpaths.index(bestpath)]

print(bestpath,biascost)
