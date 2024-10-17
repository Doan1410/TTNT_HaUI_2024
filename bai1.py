graph = {"A" :{"B":2,"C":4,"F":6},
         "B":{},
         "C":{"D":2,"E":8},
         "D":{"E":2},
         "E":{},
         "F":{"G":5,"H":1},
         "G":{},
         "H":{}
         }

graph1={"A":{"B":20,"C":15,"E":80},
        "B":{"A":40,"E":10,"F":30},
        "C":{"A":20,"B":4,"F":10},
        "D":{"A":36 ,"B":18,"C":15},
        "E":{"B":90,"C":15},
        "F":{"C":45,"D":4,"E":10}
        }
def print_past_and_cost (start, goal, parent, g):
    path=[]
    current = goal
    while current!=start:
        path.append(current)
        current= parent[current]
    path.append(start)
    path.reverse()
    print("Đường đi","->".join(path))
    print("C(p)=",g[goal])

def AT(graph,start,goals):
    MO=[start]# danh sách các đỉnh chờ được duyệt
    g={start:0} # chi phí (giá trị ) tới từng đỉnh
    DONG=[] #danh sách các đỉnh đã vét qua
    parent={}#lưu trữ cha của mỗi đỉnh

    while MO:
        #lấy đỉnh n có chi phí g(n) nhỏ nhất từ tập MO
        min_cost = float('inf')
        n = None
        for vertex in MO:
            if vertex in g:
                cost = g[vertex]
            else:
                cost = float('inf')
            if cost < min_cost:
                min_cost = cost
                n = vertex

        if n in goals:
            print_past_and_cost(start,n,parent,g)
            return True
        
        MO.remove(n)
        DONG.append(n)# thêm đỉnh n vào tập đã xét

        for m in graph.get(n,{}): # duyệt qua các đỉnh kề của n
            cost = graph[n][m]# chi phí từ n đến m
            new_cost = g.get(n, float('inf'))+cost

             #nếu m đã có cha và đường đi mới ngắn nhất      
            if m in parent and new_cost<g[m]:
                  g[m]=new_cost
                  parent[m]=n     

            #nếu n chưa được duyệt
            elif m not in MO and m not in DONG :
                g[m]=new_cost
                parent[m]= n
                MO.append(m)

    return False # ko tìm thấy đường đi đến đỉnh đích

start = "A"
goals =["E","H"]
AT(graph1,start,goals)