# Dynamic Routing between Capsules: A Study of Digit Recognition and Application to Time-Serie Classification Problem in Finance.

In November 2017, G. Hinton et al. realeased a paper called [Dynamic Routing Between Capsules](https://arxiv.org/abs/1710.09829). This paper promises a breakthrough in the deep learning community. 
This new type of neural network (CapsNet) is based on the so-called "Capsules".

CapsNet enables new applications, especially, it can overcome the main drawback of CNNs. CapsNet is not sensible to linear operations, i.e., unlike CNNs, it can recognize objet with no-dependency on view angles. Moreover, unlike CNNs, CapsNet can take into account orientations and spatial relationships between features. 

The project aims to reproduice the original Hinton team's experiments in digits recognition with the MNIST dataset . In second part, the project aims to go further with one potential application in finance: the time-series bi-labels classification problem. For each problem, the performance of the CapsNet network is compared to a baseline CNN network.

Both parts are develloped in this folder:
- MNIST: Folder with all the Digit Recognition experiments 
- Finance: Folder with all the time-series classification experiments
- Dynamic Routine between Capsules - Presentation.pdf: The PPT presentation of the project 

## MNIST: Digits Recognition

### Description

In this part, results of the paper are reproduced. The Capsnet is implemented, trained and tested with the original MNIST dataset. Then, the reconstruction part of images is highlighted and the Capsnet capacity to identify over-lapped digits is also tested. 
Thus, the project goes further by training CapsNet and a the Hinton baseline CNN with the original MNIST. Then, these networks are tested with the [LISA lab](http://www.iro.umontreal.ca/~lisa/) variations of the MNIST. 

### Experiment & Results

Capsnet reached almost 98% of accuracy on the MNIST test dataset with only one epoch of training. 
The reconstruction of input image was a success. 
Capsnet demonstrated the capacity to identify overlapped digits. 
LISA CNN/Capsnet: TBD: This part has to be done in order to have a Baseline for Capsnet network

## Finance: Time-series bi-labels classification problem

### Description

In finance, and especially in time-series problems, the time is an important component to take into account. Because of the Capsnet's capacity to consider spatial relationships between features. The project aimes to explore the application of Capsules for time-series classification problem.
The goal of the algorithm is to predict, for a given stock, the sign of the next day return. 

### Experiment & Results

The architecture of the network is modified because of the nature of the input and output and also to reduce the observed CapsNet tendency to overfit.
The project introduces the usage of dropout in CapsNet, still in order to reduce overfitting.
Among the 470+ tried stocks, CNN and Capsnet perform slightly in a comparative effective way. 
The overall performance is of the order of 55% of accuracy which is 5% better than a random choice.
On the basis if these findings, it is not possible to assert CapsNet performs better than CNNs. 

## Further work

### Finance

The experiment was run with auto-regressive entry. It is not taking into account the relations between the different stocks. Exploring this way should lead to better results. It should be interesting because of the CapsNet capacity to identify orientation and spatial relations.  

## Thanks to

Special thanks to **Aurélien Geron** [ageron](https://github.com/ageron)
The two Capsnet implementations are based on the amazing git: https://github.com/ageron/handson-ml/blob/master/extra_capsnets.ipynb

Special thanks to **Alex Gonchar** [Rachnog](https://github.com/Rachnog)
The Baseline CNN implementation is based on the amazing git: https://github.com/Rachnog/Deep-Trading/tree/master/simple_forecasting

## Authors

* **Maxime Allard** [Allma079](https://github.com/Allma079)
* **Selim Amrouni** [selimamrouni](https://github.com/selimamrouni)
* **Thibault Duplay** 
* **Phillipe Mizrahi** [pcamizrahi](https://github.com/pcamizrahi)


