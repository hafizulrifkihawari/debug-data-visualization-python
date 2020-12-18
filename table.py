import csv, json

def visualize_table():
    with open('test-data.csv') as csv_file:
        dataset = csv.reader(csv_file, delimiter=',')

        plotter = {
            "kind": { "table": True },
            "rows": [
                # examples
                # { "userId": 1, "country": "us", "amount": 2 },
                # { "userId": 2, "amount": 1 },
                # { "userId": 2, "country": "de", "amount": 1 },
                # { "userId": 1, "country": "us" }
            ]
        }

        headers = next(dataset)
        visualized = json.dumps(plotter)
        for row, data in enumerate(dataset):
            _input = {}
            for idx, key in enumerate(headers):
                _input[key] = data[idx]

            plotter['rows'].append(_input)
            visualized = json.dumps(plotter)

        visualized = json.dumps(plotter) # variable visualize
        return
        
visualize_table()