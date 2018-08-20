# MNIST Section

This section studies the Capsnet network behavior with MNIST dataset. 
There are two notebooks:
- Capsules_vMNIST.ipynb: This is an implementation in TensorFlow of the Capsnet model. 
- Baseline_CNN_Hinton_Paper.ipynb: This is an implementation in Keras of the Baseline CNN model. 

## Data

### Description

Both models are trained with the original training MNIST dataset. There is no data-augmentation technic used. 
Both models are tested with 5 versions of the testing MNIST dataset:
- Basic
- BackGround Img
- RandomBackGround
- Rotated MNIST
- Rotated MNIST + BackGround

### Source

[LISA MNIST webpage](http://www.iro.umontreal.ca/~lisa/twiki/bin/view.cgi/Public/MnistVariations) 

The data are saved in the folder: data_transfo

## Installing

Requiered packages:
- TensorFlow
- TensorBoard
- Keras
- Numpy
- Scikit-Learn 

## Running the notebooks

Both notebooks requiere heavy computation power. It is advisable to use GPU for computation. 

## Main results

TBD 

## Interesting observations 

TBD 

## Further work

TBD 

## Thanks to

Special thanks to **Aurélien Geron** [ageron](https://github.com/ageron)
The MNIST Capsnet implementation is based on the amazing git: https://github.com/ageron/handson-ml/blob/master/extra_capsnets.ipynb

## Authors

* **Maxime Allard** [Allma079](https://github.com/Allma079)
* **Selim Amrouni** [selimamrouni](https://github.com/selimamrouni)
* **Thibault Duplay** 
* **Phillipe Mizrahi** [pcamizrahi](https://github.com/pcamizrahi)
