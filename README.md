# flower-classifier
Image classifier using Python TensorFlow trained using a set of flower images from Kaggle.

## Usage
Assuming you're working with the same Kaggle dataset, extract the images to the directory `flowers-raw/`
The directory structure should be as follows:
```
flowers-raw/
├── daisy
├── dandelion
├── rose
├── sunflower
└── tulip
```

Then, run `./scale-and-crop-images.py flowers-raw/` and the script will create the directory `flowers-scaled/`
with the same structure as `flowers-raw/`, but where the images are all exactly 240px by 240px in size.
