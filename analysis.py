import numpy as np
import matplotlib.pyplot as plt
import json

def analyze_data(data):
    numbers = data.get("numbers", [])
    if not numbers:
        return {"error": "No numbers provided"}

    arr = np.array(numbers)
    mean = arr.mean()
    median = np.median(arr)
    std_dev = arr.std()
    # Possibly detect outliers
    outliers = arr[np.abs(arr - mean) > 2 * std_dev]

    return {
        "mean": mean,
        "median": median,
        "std_dev": std_dev,
        "outliers": outliers.tolist()
    }

def visualize_analysis(result, filename="./output/analysis_visualization.png"):
    mean = result["mean"]
    std_dev = result["std_dev"]
    outliers = result["outliers"]

    fig, ax = plt.subplots(2, 1, figsize=(8, 8))

    # Top subplot: bar chart
    metrics = ["Mean", "Standard Deviation"]
    values = [mean, std_dev]
    ax[0].bar(metrics, values, color=["blue", "red"])
    ax[0].set_title("Basic Statistics", fontsize=14)

    # Bottom subplot: outliers
    ax[1].bar(range(len(outliers)), outliers, color="orange")
    ax[1].set_title("Detected Outliers", fontsize=14)

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Visualization saved as {filename}")



def process_message(message):
    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format"})

    result = analyze_data(data)
    # now visualize this data
    
    visualize_analysis(result)

    # convert py object -> json
    return json.dumps(result)
