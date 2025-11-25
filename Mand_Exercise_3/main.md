# Mandatory Exercise 3 INF250

## Part 1 - Data Exploration

### Introduction
The images is taken from a drone above the field, and it is out task to detect
the rumex in this field. The picture varies in brightness, background and
filter. I have chosen to not choose any pictures that have been filtered only
focusing on raw drone footage.

### Challenges 

#### Contrast
The contrast makes it hard to objectify rumex. The pictures I have choosen
doesen't contain ripe rumex, therefore the background and the foreground blends
into one since both the plants and the ground is green. The problem worsens in the images that contains large shadows. If the picture is well lit the rumex can be more easily distinguished from the background with the help of
shadows from the plant, and reflection on top of the plant from the sun. 

### Variation 
The Rumex has some variation in size and form, therefore it can get hard for the
machine to conclude these are the same object. This has also caused issues when
labeling since it is hard to find all the small rumex.

### Clusters
This is when rumex is so tightly packed that is becomes very hard to destinguis
one ruumex from it's neighbours. When is comes to clusters you can take a few seperate approaches, you can either
label the whole cluster with another label or you can try to label them
individually. I have chosen to try and ignore pictures with large clusters and
focus on individual rumex's.

## Part 2 - Preprocessing & Labeling

### Preprocessing
I didn't preprocess the images. Contrast could be a useful preprocessing
technique, this is because the background and the foreground has very low
contrast. Therefore a bit more contrast would help destinguish the rumex from
the grass. 

### Labeling 
I labeled the images via Robotstudio. I chose to label few pictures and then
make a model that could be used to label the rest of the images. I started by
labeling 15 pictures. After getting the model I used this to autolabel 100
images to train a model to. 

## Part 3 - Model Training
```Python
from ultralytics import YOLO

# Load a pretrained YOLO11s model
model = YOLO("yolo11s.pt")

results = model.train(
    data="final_dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=4,
    device=0,  # Use GPU if available
    degrees=180
)
```
```YAML
train: ../train/images
val: ../valid/images
test: ../test/images

nc: 1
names: ['Rumex']

roboflow:
  workspace: in250-mandatory-3
  project: inf250-part2-v7tii
  version: 1
  license: Private
  url: https://app.roboflow.com/in250-mandatory-3/inf250-part2-v7tii/1

```
I used a yolo11 small version. I chose this because of a combination of time
efficiency without giving up to much accuracy. I use 100 epochs to save time,
batch equal to four is needed to not use up memory. I use GPU for efficiency, I
have a Nvidia graphic card so I downloaded Cuda for improved training. I have
set degrees to 180 to improve accuracy. This rotates the picture so that the
model can train on recognizing the object from different angles.

## Part 4 - Evaluation & Competition

### Testing
I run validation on the test folder to test the performance. I do this because
the model has not seen the test folder when training, so the images are unknown
to the model.

```Python
from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")

# Validate with a custom dataset
metrics = model.val(data="final_dataset/data.yaml", split='test', project="results")
print(metrics.box.map)  # map50-95
```
This code gives feedback on model performance for the test folder. The results
can be found under `results/testfolder_val`

### Result
The model is alright. It manages to detect the large rumex's with around 50%
certainty, but is much worse at detecting smaller rumex. All the model graphs
and results are in the folder result.

### Discussion 
I have labeled few pictures with not alot of variation, most of the pictures
containing large rumex's. Therefore the simulation isn't very good at detecting
smaller rumex. The model haven't seen many small rumex and is therefore much
worse at detecting them.  

### Conclusion 
The task was to create a model that could detect rumex in a field. I chose to
train a small model first to do the labeling for me. Since the first dataset
lacked both quantity and variation the model wasn't very good at detecting
different kinds of rumex. The rumex the final model finds have accuracy of about
50%, but the model misses alot of rumex to depending on the image. 
