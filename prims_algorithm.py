from collections import defaultdict
import bisect

graph = [
    [-1, 2, 3, 3, -1, -1, -1],
    [2, -1, 4, -1, 3, -1, -1],
    [3, 4, -1, 5, 1, 6, -1],
    [3, -1, 5, -1, -1, 7, -1],
    [-1, 3, 1, -1, -1, 8, -1],
    [-1, -1, 6, 7, 8, -1, 9],
    [-1, -1, -1, -1, -1, 9, -1],
]

numbers_to_letters = ["A", "B", "C", "D", "E", "F", "G"]

class PrimsAlgorithm:
    def __init__(self, graph):
        self.graph = graph # 2D list which represents the Adjacency Matrix of the input graph


    def output_edges(self):

        num_nodes = len(self.graph[0])
        edges = defaultdict(set)

        # start with a random node
        
        available_edges = defaultdict(set)
        for index in range(len(self.graph[0])):
            if self.graph[0][index] != -1:
                available_edges[self.graph[0][index]].add((0, index))

        mst = []
        visited_nodes = {0}
        sorted_available_weights = list(sorted(available_edges.keys()))
        while len(visited_nodes) < num_nodes:
            for weight_index, edge_weight in enumerate(sorted_available_weights):
                shortest_edge_weight = edge_weight
                old_node, new_node = None, None
                for edge_start, edge_end in available_edges[edge_weight]:
                    if edge_start in visited_nodes and edge_end in visited_nodes:
                        continue
                    if edge_start not in visited_nodes:
                        new_node = edge_start
                        old_node = edge_end
                        break
                    elif edge_end not in visited_nodes:
                        new_node = edge_end
                        old_node = edge_start
                        break
                if new_node:
                    break

            available_edges[edge_weight].remove((edge_start, edge_end))
            if len(available_edges[edge_weight]) == 0:
                sorted_available_weights = sorted_available_weights[:weight_index] + sorted_available_weights[weight_index + 1:]

            mst.append((new_node, old_node, shortest_edge_weight))
            visited_nodes.add(new_node)
            for index in range(len(self.graph[new_node])):
                if self.graph[new_node][index] != -1:
                    available_edges[self.graph[new_node][index]].add((new_node, index))
                    bisect.insort(sorted_available_weights, self.graph[new_node][index])

        for start_node, end_node, weight in mst:
            print(f"{numbers_to_letters[start_node]} -> {numbers_to_letters[end_node]} ({weight})")


PrimsAlgorithm(graph).output_edges()
