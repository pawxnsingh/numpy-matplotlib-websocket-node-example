import matplotlib.pyplot as plt
import json

def analyze_data(data):
    numbers = data.get("numbers", [])
    
    if not numbers:
        return {"error": "No numbers provided for analysis"}

    average = sum(numbers) / len(numbers)
    
    result = {
        "average": average,
        "category": "High" if average > 50 else "Low",
        "input_size": len(numbers),
    }
    return result

def visualize_analysis(result, filename="./output/analysis_visualization.png"):
    # Extract values
    average = result["average"]
    category = result["category"]
    input_size = result["input_size"]
        
    # Visualization
    plt.figure(figsize=(8, 5))
    
    # Bar chart for numeric values
    metrics = ["Average", "Input Size"]
    values = [average, input_size]
    colors = ["blue", "green"]
    
    plt.bar(metrics, values, color=colors, alpha=0.7)
    
    # Add titles and labels
    plt.title(f"Data Analysis Visualization(METACALL)\nCategory: {category}", fontsize=14, pad=15)
    plt.xlabel("Metrics", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    
    # Add value labels on top of bars
    for i, value in enumerate(values):
        plt.text(i, value + 1, f"{value:.2f}", ha="center", va="bottom", fontsize=10)
    
    # Grid for better readability
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Save the plot to a file
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
