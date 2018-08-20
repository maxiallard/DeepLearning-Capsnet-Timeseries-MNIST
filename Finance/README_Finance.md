# FINANCE Section

This section studies the Capsnet network behavior with financial data. 
There are three notebooks:
- pre_processing_finance.ipynb: This is an implementation of pre-processing pipeline to get readable inputs for the model.
- Capsules_finance.ipynb: This is an implementation in TensorFlow of the Capsnet model. 
- Baseline_CNN_finance.ipynb: This is an implementation in Keras of the Baseline CNN model.
- utils.py: This python script contains several functions used in the notebooks. They are grouped here for better convenience.
- Evaluate_ACC.ipynb: This notebooks is made with the purpose to evaluate and compare the performances of the two models (CNN vs CapsNet). 

## Data

### Description

Both models are trained with S&P500 daily data (starting date: 2013-02-08).
Using the Open, High, Low, Close and Volume data of each stock, the pipeline transforms the time series into a serie of (30, 5) matrices. 
The data are divided into Training, Validation and Test sets with respect to the time span.

### Source

[Kaggle](https://www.kaggle.com/camnugent/sandp500) 

There are several folders containing data:
- The data are stored in the folder: sandp500
- Each individual stocks data are stored in the folder: individual_stocks_5yr
- Each individual transformed matrices (after the pre-processing) are saved into the folder: data_out_autoreg
- All the results for each stocks after the CNN and after the Capsnet programs (pickle files of dictionnaries of results): Visualization

## Installing

Requiered packages:
- TensorFlow
- TensorBoard
- Keras
- Numpy
- Scikit-Learn 
- Pickle 
- Tqdm
- Matplotlib

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
The Finance Capsnet implementation is based on the MNIST Capsnet based on the amazing git: https://github.com/ageron/handson-ml/blob/master/extra_capsnets.ipynb

Special thanks to **Alex Gonchar** [Rachnog](https://github.com/Rachnog)
The Baseline CNN implementation is based on the amazing git: https://github.com/Rachnog/Deep-Trading/tree/master/simple_forecasting

## Authors

* **Maxime Allard** [Allma079](https://github.com/Allma079)
* **Selim Amrouni** [selimamrouni](https://github.com/selimamrouni)
* **Thibault Duplay** 
* **Phillipe Mizrahi** [pcamizrahi](https://github.com/pcamizrahi)


