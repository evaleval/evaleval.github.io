import requests
import json

url = "https://huggingface.co/api/datasets/evaleval/EEE_datastore/tree/main?recursive=true"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    print(f"Type of data: {type(data)}")
    if isinstance(data, list):
        print(f"Number of items: {len(data)}")
        if len(data) > 0:
            print(f"First item: {data[0]}")
            
        # simulating the logic
        benchmarks = set()
        models = set()
        file_count = 0
        
        for item in data:
            path = item.get('path', '')
            if path.startswith('data/'):
                parts = path.split('/')
                # Structure: data/{benchmark}/{developer}/{model}
                
                # Benchmark (index 1)
                if len(parts) >= 2 and parts[1]:
                    benchmarks.add(parts[1])
                
                # Model (index 2 and 3 -> developer/model)
                if len(parts) >= 4 and parts[2] and parts[3]:
                    models.add(f"{parts[2]}/{parts[3]}")
                
                # Count files (evaluations)
                if item.get('type') == 'file':
                     file_count += 1
                     
        print(f"Benchmarks: {len(benchmarks)}")
        print(f"Models: {len(models)}")
        print(f"Files (Evals): {file_count}")

except Exception as e:
    print(f"Error: {e}")
