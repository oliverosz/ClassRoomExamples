from collections import deque
import random


class Graph():
    def __init__(self, n=None, m=None, matrix=None):
        if matrix:
            self.adj_list = {i: set(neighbors) for i, neighbors in enumerate(matrix)} #ha adott a szomszedsagi lista
        elif n is not None and m is not None:
            self.adj_list = self._generate_random(n, m)
        else:
            self.adj_list = []

    def _generate_random(self, n, m):
        adj_list = {i:set() for i in range(n)}
        possible= [(i, j) for i in range(n) for j in range(i+1,n)]  #lehetseges elek

        if m > len(possible):
            raise ValueError("Túl sok él")
        
        edges = random.sample(possible, m)

        for u, v in edges:
            adj_list[u].add(v)      #elek hozzaadasa szomszedsagi listahoz
            adj_list[v].add(u)

        return adj_list

    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj_list.values()) // 2
    
    def vertex_count(self) -> int:
        return len(self.adj_list)
    
    def neighbors_of(self, v:int) -> set[int]:
        return self.adj_list.get(v, set())
    
    def cluster(self,v):
        #return self.neighbors_of(v)
        visited = set()
        queue = deque([v])

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                neighbors_visit = self.adj_list.get(current, set()) - visited
                queue.extend(neighbors_visit)
        return visited
    
    def shortest_path(self, source, destination):
        if source == destination:
            return [source]
        
        visited = {source}
        queue = deque([(source, [source])])

        while queue:
            current, path = queue.popleft()
            for neighbor in self.adj_list.get(current, []):
                if neighbor == destination:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []
    
    """def save_dot_file(self, filename="graph.dot"):
        with open(filename, "w") as file:
            file.write("graph G {\n")
            for node, neighbors in self.adj_list.items():
                for neighbor in neighbors:
                    if node < neighbor:  #minden el csak egyszer
                        file.write(f"    {node} -- {neighbor};\n")
            file.write("}\n")
        print(f"save graf: {filename}")"""

@staticmethod
def random_graph(n, m):
    return Graph(n=n, m=m)

#if __name__ == "__main__":
    #g = Graph(n=12, m=15)
    #print("Adj list:", g.adj_list)
    #print("Edge count:", g.edge_count())
    #print("Vertex:", g.vertex_count())
    #print("Neighbors of 0:", g.neighbors_of(0))
    #print("Cluster:", g.cluster(2))
    #print("Shortest path:", g.shortest_path(0,4))
    #g.save_dot_file("graph.dot")