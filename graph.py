from json import dumps
from random import randint

graph = {
    "kind": {"graph": True},
    "nodes": [
        # example data
        # {"id": "1", "label": "1"}
    ],
    "edges": []
}

for i in range(2,25):
    # add a node
    id = str(i)
    # connects the node to a random edge
    targetId = str(randint(1, i - 1))
    graph["nodes"].append({"id": id, "label": id})
    graph["edges"].append({"from": id, "to": targetId})
    
    json_graph = dumps(graph)
    
    print(graph['nodes'][i-2])
    print(graph['edges'][i-2])
    print('-------------')