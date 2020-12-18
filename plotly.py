import csv, json

def visualize_table():
    with open('plot.csv') as csv_file:
        dataset = csv.reader(csv_file, delimiter=',')

        plotter = {
            "kind":{ "plotly": True },
            "data":[
                # { "y": [1, 2, 4, 8, 16] },
                # { "y": [14, 3, 0, 15, 10] }
            ]
        }

        visualized = json.dumps(plotter)
        for data in dataset:
            plotter['data'].append({
                "y": data[1:],
                "name": data[0]
            })
            visualized = json.dumps(plotter)
        
visualize_table()