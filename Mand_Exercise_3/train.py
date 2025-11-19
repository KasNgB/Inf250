from ultralytics import YOLO

# Load a pretrained YOLO11s model
model = YOLO("yolo11s.pt")

# Train the model on COCO8
results = model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    device=0,  # Use GPU if available
    degrees=180
)
