def dijkstra(g, start):
    d = {node: float('inf') for node in g}
    d[start] = 0
    p = {node: None for node in g}

    un = list(g)

    while un:
        cn = min(un, key=lambda node: d[node])

        un.remove(cn)

        for neighbor, weight in g[cn].items():
            d = distances[cn] + weight

            # Se a nova distância for menor, atualiza-a
            if d < distances[neighbor]:
                distances[neighbor] = d
                p[neighbor] = cn


g = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 1},
    'C': {'B': 2, 'D': 3, 'R': 2},
    'D': {'C': 3, 'E': 2},
    'E': {'D': 2, 'F': 1},
    'F': {'E': 1, 'G': 3, 'L': 3},
    'G': {'F': 3, 'H': 1, 'J': 1},
    'H': {'G': 1, 'I': 2},
    'I': {'H': 2, 'K': 1, 'Q': 1},
    'J': {'G': 1, 'K': 2},
    'K': {'J': 2, 'I': 1},
    'L': {'F': 3, 'M': 1},
    'M': {'L': 1, 'N': 1},
    'N': {'M': 1, 'O': 1, 'T': 1},
    'O': {'N': 1, 'P': 2},
    'P': {'O': 2, 'Q': 1},
    'Q': {'P': 1, 'I': 1},
    'R': {'C': 2, 'S': 1},
    'S': {'R': 1, 'T': 1},
    'T': {'S': 1, 'N': 1}
}


start_node = 'A'
distances, predecessors = dijkstra(g, start_node)

for node in g:
    path = []
    cn = node
    while cn is not None:
        path.insert(0, cn)
        cn = predecessors[cn]
    print(f'Caminho mais curto de {start_node} para {node}: {path}, Distância: {distances[node]}')
