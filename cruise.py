#
# # Every year, the government lists the most popular baby names (name and count). The problem is that some names have multiple spellings and are listed separately (like "Michael" and "Mike"). Given a list of baby names with their count and a list of equivalent name pairs, write an algorithm to print a new list of the unique names and their count.
# names = [
#     ("Jen", 4),
#     ("Jenny", 5),
#     ("Michael", 2),
#     ("Mike", 3),
#     ("Sara", 4),
#     ("Sarah", 2),
#     ("David", 3),
#     ("Jennifer", 4)
# ]
#
# synonyms = [
#     ("Jen", "Jenny"),
#     ("Sara", "Sarah"),
#     ("Michael", "Mike"),
#     ("Jenny", "Jennifer")
# ]
#
# # "Jenny", 9, "Sara", 6, "Mike", 5, "David", 3
# def name_match(names,synonyms):
#     synonyms_ls = []
#     res_syn ={}
#     output = {}
#     result ={}
#     for syn in synonyms:
#         if syn[0] not in res_syn:
#             res_syn[syn[0]]= syn[1]
#             synonyms_ls.append(syn[0])
#             synonyms_ls.append((syn[1]))
#     print(res_syn)
#     for s in res_syn.keys():
#         if s not in res_syn.values():
#             output[s] = [res_syn[s]]
#         else:
#             for k,v in res_syn.items():
#                 if s == v:
#                     output[k].append(res_syn[s])
#             # print(res_syn.in([s]))
#
#     print(output)
#
#
#
#     for n in names :
#         if n[0] in output:
#             result[n[0]] = n[1]
#         elif n[0] not in synonyms_ls:
#             result[n[0]] = n[1]
#         else:
#             for k,v in output.items():
#                 for i in v:
#                     if n[0] == i:
#                         result[k] += n[1]
#
#
#     print(result)
#
#
#
#         #     result[output[n[0]]] = n[1]
#         # elif n[0] not in res_syn and n[0] not in result:
#         #     result[n[0]] = n[1]
#         # else:
#         #     result[n[0]] += n[1]
#
#
# print(name_match(names,synonyms))



class GraphNode:
    def __init__(self, name, freq):
        self.name = name
        self.frequency = freq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name, frequency):
        self.graph[name] = {'frequency': frequency, 'adjacency': []}

    def add_edge(self, name1, name2):
        if name1 in self.graph:
            self.graph[name1]['adjacency'].append(name2)
        if name2 in self.graph:
            self.graph[name2]['adjacency'].append(name1)

def truly_popular_names(names, synonyms):
    graph = construct_graph(names)
    connect_edges(graph, synonyms)

    root_names = get_true_frequencies(graph)
    return root_names

def construct_graph(names):
    graph = Graph()
    for name in names:
        graph.add_node(name, names[name])  # name and frequency
    return graph

def connect_edges(graph, synonyms):
    for pair in synonyms:
        graph.add_edge(pair[0], pair[1])

def get_true_frequencies(graph):
    """Traverses graph using BFS and returns frequencies of names."""
    frequencies = {}
    visited = set()
    for name in graph.graph:
        if name in visited:
            continue
        frequencies[name] = graph.graph[name]['frequency']
        for adjacent in graph.graph[name]['adjacency']:
            if adjacent in visited:
                continue
            visited.add(adjacent)
            if adjacent in graph.graph:
                frequencies[name] += graph.graph[adjacent]['frequency']
    return frequencies

def main():
    names = {
        'John': 15,
        'Jon': 12,
        'Chris': 13,
        'Kris': 4,
        'Christopher': 19
    }

    synonyms = [
        ('Jon', 'John'),
        ('John', 'Johnny'),
        ('Chris', 'Kris'),
        ('Chris', 'Christopher')
    ]
    print(truly_popular_names(names, synonyms))


if __name__ == '__main__':
    main()