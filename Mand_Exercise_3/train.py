from ultralytics import YOLO

# Load a pretrained YOLO11s model
model = YOLO("yolo11s.pt")

# Train the model on COCO8
results = model.train(
    data="final_dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=4,
    device=0,  # Use GPU if available
    degrees=180
)
