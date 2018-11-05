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

## Using `separate-images.py`
Assuming you've already modified your dataset with `scale-and-crop-images.py`,
then for each subdirectory in `flowers-scaled/` (e.g., `rose`, `daisy`) run
`./separate-images.py <dir>` (e.g., `./separate-images.py flowers-scaled/rose`).

This will proportionally separate each image in the given subdirectory into three
subdirectories, `<dir>/training`, `<dir>/validation`, and `<dir>/testing`.
We use these directories as our training datasets, validation datasets, and testing
datasets respectively.

## InceptionV3
We're using Google's pre-trained InceptionV3 model for feature extraction.
In particular, we're using the weights from InceptionV3 mentioned in the third
section of [Google's image classification exercise](https://colab.research.google.com/github/google/eng-edu/blob/master/ml/pc/exercises/image_classification_part3.ipynb?utm_source=practicum-IC&utm_campaign=colab-external&utm_medium=referral&hl=en&utm_content=imageexercise3-colab#scrollTo=KMrbllgAFipZ),
since this project is based off of that exercise.

You can obtain a copy of the InceptionV3 weights we used with

`wget https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5`

then

`mv inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 inception_v3_weights.h5`
