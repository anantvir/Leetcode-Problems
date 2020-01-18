import queue
import math

class Vertex:
    def __init__(self,info):
        self.info = info
        self.color = None
        self.parent = None
        self.d = 0

    def get_info(self):
        return self.info
    def __hash__(self):
        return hash(id(self))       # make hashable so that can be used in a hashmap as keys in hashmap should be hashable

class Edge:
    def __init__(self,u,v,info):
        self.origin = u
        self.destination = v
        self.info = info

    def endpoints(self):
        return (self.origin,self.destination)
    
    def opposite(self,u):
        return self.destination if u is self.origin else self.destination
    
    def get_info(self):
        return self.info
    
    def __hash__(self):
        return hash((self.origin,self.destination))

class Graph:
    def __init__(self,directed = False):
        self.outgoing = {}
        self.incoming = {} if directed == True else self.outgoing
    
    def is_directed(self):
        return self.outgoing is not self.incoming

    def vertex_count(self):
        return len(self.outgoing)
    
    def vertices(self):
        return self.outgoing.keys()

    def edge_count(self):
        edges = set()
        for eachDict in self.outgoing.values():
            edges.add(eachDict.values())
        return edges
    
    def get_edge(self,u,v):
        return self.outgoing[u].get(v)      # get() used because it returns None if v is not present and doesnt give KeyError
            
    def degree(self,v):
        return len(self.outgoing[v])
    
    def incident_edges(self,v):
        dic = self.outgoing
        for edge in dic[v].values():
            yield edge
    
    def insert_vertex(self,v):
        v = Vertex(v)
        self.outgoing[v] = {}
        return v
    
    def insert_edge(self,u,v,info = None):
        e = Edge(u,v,info)
        self.outgoing[u][v] = e
        self.outgoing[v][u] = e
    
    def get_vertex_dict(self):
        return self.outgoing

def Breadth_First_Search(G,s):
    vertex_list = G.vertices()
    vertex_list.remove(s)
    for v in vertex_list:
        v.color = 'WHITE'
        v.d = math.inf
        v.parent = None
    s.color = 'GRAY'
    s.d = 0
    s.parent = None
    vertex_dict = G.get_vertex_dict()
    Q = queue.Queue(len(vertex_list))
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in vertex_dict[u].keys():
            if v.color == 'WHITE':
                v.color = 'GRAY'
                v.d = u.d + 1
                v.parent = u
                Q.put(v)
        u.color = 'BLACK'