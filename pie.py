import json

data = [{
    "values": [10, 25, 30],
    "labels": ['Debug', 'Confused', 'Rest'],
    "type": 'pie'
}]

layout = {
    "height": 500,
    "width": 500
}

examples = {
    "kind": {
        "plotly": True
    },
    "data": data,
    "layout": layout
}

visualized = json.dumps(examples)

print(visualized)