# flower-classifier
Image classifier using Python3 TensorFlow trained using a modified set of flower
images from Kaggle.

## Dependencies
The following packages are required for this project:
* `pillow`
* `matplotlib`
* `tensorflow`
* `numpy`

These dependencies can be installed via `python3 -m pip install <module-name>`.

## Dataset
Our dataset originally comes from
[Kaggle](https://www.kaggle.com/alxmamaev/flowers-recognition), though we've
removed some images that were incorrectly labeled and images that were poor
examples of the flowers they were supposed to represent.

We then scaled and cropped the images using `scale-and-crop-images.py` so they
were all 240x240px.
These images can be found in the directory `flowers-scaled-selected`.

This second step is actually unnecessary, as TensorFlow's `ImageDataGenerator` will
perform the image scaling automatically, though at the time we did not realize
that.

## InceptionV3
We're using Google's pre-trained InceptionV3 model for feature extraction.
In particular, we're using the weights from InceptionV3 mentioned in the third
section of [Google's image classification exercise](https://colab.research.google.com/github/google/eng-edu/blob/master/ml/pc/exercises/image_classification_part3.ipynb?utm_source=practicum-IC&utm_campaign=colab-external&utm_medium=referral&hl=en&utm_content=imageexercise3-colab#scrollTo=KMrbllgAFipZ),
since this project is based off of that exercise.

You can obtain a copy of the InceptionV3 weights we used with

`wget https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5`

then

`mv inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 inception_v3_weights.h5`

## Using `scale-and-crop-images.py`
Assuming you're working with the same Kaggle dataset, extract the images to a
directory such as `flowers-raw/`.
The directory structure should be as follows:
```
flowers-raw/
├── daisy
├── dandelion
├── rose
├── sunflower
└── tulip
```

Then, run `./scale-and-crop-images.py flowers-raw/` and the script will create
the directory `flowers-scaled/` with the same structure as `flowers-raw/`, but
where the images are all exactly 240x240px in size.

## Using `separate-images.py`
This script will separate each image in the provided directory into one of three
 directories:
* `training`
* `validation`
* `testing`

Each of those directories will contain a subdirectory labeling the type of flowers
in the images contained within.
For example, the `training` directory should have the following structure:
```
training/
├── daisy
├── dandelion
├── rose
├── sunflower
└── tulip
```

Images will be randomly separated between `training`, `testing`, and `validation`
groups in such a way that approximately 20% of images will be placed in `testing`,
approximately 16% into `validation`, and the remaining approximately 64% into
`training`.

This mirrors an 80/20 split between training and testing datasets, where the
training dataset is further divided into an 80/20 split between training and
validation.

Run the script with the scaled flowers directory as the argument, i.e.,
`./separate-images.py flowers-scaled/`.

## Using `train-classifier.py`
This script was not written to be very flexible.
It requires that the InceptionV3 model be saved in the working directory as
`inception_v3_weights.h5`.

Additionally, it requires that the flower images be separated in such a way as
to have the same directory structure provided when separated by `separate-images.py`
and that the directory be named `flowers-scaled`.

Finally, it saves the generated models in the directory `weights` which it will
create if it does not exist.
The saved model will be named `flower-model <timestamp>.h5` where `<timestamp>`
is in the format `YYYY-MM-DD hh:mm:ss`.

If using CPU TensorFlow, expect the training to take around one hour.
My machine has an Intel(R) Core(TM) i7-4720HQ CPU @ 2.60GHz, and training took
approximately 75 minutes per run.

## Using `classifier.py`
This script is somewhat more flexible than `train-classifier.py`, though it is
not as flexible as it should be.

It must be used as follows: `./classifier.py <model> <test-images>`
where `<model>` is generated by `train-classifier.py` and can be found as
`weights/flower-model YYYY-MM-DD hh:mm:ss.h5` and `<test-images>` is a directory
containing images of flowers the model is to classify.
Note that this script will not examine subdirectories in `<test-images>` for
flower images.

The script will print to standard output the predictions it made for each image.
