from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")

# Validate with a custom dataset
metrics = model.val(data="final_dataset/data.yaml", split='test', project="results")
print(metrics.box.map)  # map50-95
