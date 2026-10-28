from collections import deque
class City:
    def __init__(self, name, population = 0):
        self.name = name
        self.population = population
        self.neighbors = []

    def connect(self, other):
        if other is not self and other not in self.neighbors:
            self.neighbors.append(other)
            other.neighbors.append(self)

def build_graph(population_file, road_file):
    cities = {}
    with open(population_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, pop = line.rsplit(":", 1)
            name = name.strip()
            if name in cities:
                continue
            cities[name] = City(name, int(pop))
 
    with open(road_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b = (s.strip() for s in line.split(":", 1))
            for n in (a, b):
                if n not in cities:
                    cities[n] = City(n, 0)
            cities[a].connect(cities[b])
    return cities
 
 
def components(cities):
    seen = set()
    all_components = []

    for start in cities:
        if start in seen:
            continue
        seen.add(start)
        comp, queue = [], deque([start])
        while queue:
            c = queue.popleft()
            comp.append(c)
            for nb in c.neighbors:
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)

        all_components.append(comp)
    return all_components
 
 

def count_islands(cities):
    return sum(1 for _ in components(cities))

def island_populations(cities):
    return [sum(c.population for c in comp) for comp in components(cities)]
 
 
def min_highways(src, dst):
    if src is dst:
        return 0
    
    dist = {src: 0}
    queue = deque([src])
    while queue:
        c = queue.popleft()
        for nb in c.neighbors:
            if nb not in dist:
                dist[nb] = dist[c] + 1
                if nb is dst:
                    return dist[nb]
                queue.append(nb)
    return -1

graph = build_graph("city_population.txt", "road_network.txt")
cities = list(graph.values())
print("Cities:", len(cities))
print("Islands:", count_islands(cities))
populations = island_populations(cities)
print("Island populations:", populations)
a, b = cities[0], cities[1]
print(f"Highways {a.name} -> {b.name}:", min_highways(a, b))