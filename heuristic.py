import math
import pandas as pd


class Nodes:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.neighbors = {}

def calculate_distance(node1, node2):
    x1, y1 = node1.coordinates
    x2, y2 = node2.coordinates
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def get_neighbors(node):
    return node.neighbors.keys()

def a_star(start, goal):
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: calculate_distance(start, goal)}

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path

        open_set.remove(current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + calculate_distance(current, neighbor)

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + calculate_distance(neighbor, goal)

                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None


def initialize(start,end):
    # Membuat node objek wisata
    node={}
    data=pd.read_csv("test.csv")
    for i in data.iterrows():
        node[i[1]["nama lokasi/perempatan jalan"].strip()] = Nodes(i[1]["nama lokasi/perempatan jalan"], (float(i[1]["x"]),float( i[1]["y"])))
    # Menentukan tetangga-tetangga setiap node
    for i in data.iterrows():
        for z in [x.strip() for x in i[1]["jalan terhubung"].split(",")]:
            node[i[1]["nama lokasi/perempatan jalan"].strip()].neighbors[node[z]]=calculate_distance(node[i[1]["nama lokasi/perempatan jalan"].strip()],node[z])
    # Menggunakan algoritma A* untuk mencari rute terpendek
    start_node = node[start]
    goal_node = node[end]
    shortest_path = a_star(start_node, goal_node)

    # Menampilkan hasil
    if shortest_path:
        print("Rute terpendek:")
        for node in shortest_path:
            print(node.name)
    else:
        print("Tidak ada rute yang tersedia.")

initialize("sangeh monkey forest","pantai kuta")