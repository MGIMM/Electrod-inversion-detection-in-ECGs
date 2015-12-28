# Electrod-inversion-detection-in-ECGs
Electrod-inversion-detection-in-ECGs

* ####reference : 
https://challengedata.ens.fr/en/challenge/11/electrod_inversion_detection_in_ecgs.html

* ####data :
The data could be downloaded from the site above, and they are supposed to be put in the folder called "raw data". Attention! input_train and input_test are .zip format files.

##schedule ：

### 24-12-2015
* add preliminary analysis
* add function package for data importing and sampling
* add "naive" fft transformation(blackbox)
* add "naive" wt transformation(blackbox)
* add plot confusion matrix function to function package

### 25-12-2015
* change wavelet package, try cwt with "mexican hat"
* finish violent black box method
* start trying white box method
* tried MLP with less features(12 features) and failed(found in whitebox exploration)

### 26-12-2015
* add sign to the 12 features, failed
* add fft transformation after wt transformation in Naive WT, a little bit better performance
* fix the feature selection over estimate bug

### 28-12-2015
* finish MLP
* found out main problem for feature collection !



