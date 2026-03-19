from time import time
import igraph

graph = None

def bfs(graph_size):
    global graph
    if graph is None:
        graph = igraph.Graph.Barabasi(graph_size, 10)
    # result = graph.bfs(0)
    result = graph.spanning_tree(None, False)
    # result = graph.pagerank()
    return result

def main(params):
    graph_size = params['size']

    start = time()

    data = bfs(graph_size)
    latency = time() - start
    ret_val = {}
    ret_val["delay"] = latency

    return ret_val

if __name__ == '__main__':
    params = {'size': 500000}
    main(params)