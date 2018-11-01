# flower-classifier
Image classifier using Python TensorFlow trained using a modified set of flower images from Kaggle.

## Dataset
Our dataset originally comes from [Kaggle](https://www.kaggle.com/alxmamaev/flowers-recognition), though
we've removed some images that were incorrectly labeled and images that were poor examples
of the flowers they were supposed to represent.

We then scaled and cropped the images using `scale-and-crop-images.py` so they were all 240x240px.

## Using `scale-and-crop-images.py`
Assuming you're working with the same Kaggle dataset, extract the images to a directory such as `flowers-raw/`
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
with the same structure as `flowers-raw/`, but where the images are all exactly 240x240px in size.

Note that the `flowers-scaled/` directory in this repository does not contain the scaled versions of all
images from the original Kaggle dataset, as we removed some that were either improperly labeled or were
poor examples.
