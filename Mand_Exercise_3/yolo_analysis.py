from ultralytics import YOLO

weights = "best.pt"
file = "final_dataset/test/images"

model = YOLO(weights)
model.predict(
    source=str(file),
    device=0,        # use GPU
    imgsz=640,       # bump to 640 if smooth
    conf=0.4,
    save=True,
    project="results/"
    )

