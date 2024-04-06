import json

bullish = 0
bearish = 0

with open('files/json_files_prediction-Direction_Prediction-2024-03-31T16_17_57.613885Z_predictions_00006.jsonl', 'r') as f:
    for line in f:
        data = json.loads(line)
        
        if data["prediction"]["displayNames"][0] == "Bearish":
          bearish = bearish + 1
        else:
          bullish = bullish + 1
        #print("Age:", data['age'])

print(f"Bearish = {bearish} | Bullish = {bullish}")