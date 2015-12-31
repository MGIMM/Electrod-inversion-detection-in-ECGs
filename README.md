# Electrod-inversion-detection-in-ECGs
Electrod-inversion-detection-in-ECGs

* ####reference : 
https://challengedata.ens.fr/en/challenge/11/electrod_inversion_detection_in_ecgs.html

* ####data :
The data could be downloaded from the site above, and they are supposed to be put in the folder called "raw data". Attention! input_train and input_test are .zip format files.

##Schedule ：

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

### Back to the start:


During the blackbox exploration, we found some bizzare problems of feature collection :

* A relatively unstable benchmark for feature selection :
we could not find the stable error rate curve even with a large number of features.
* "good" performance when number of feature is very small.

It's reasonable, because we didn't use the physic background of the problem : it's a test ! It aims to find out the aberrant electrode(s), which we don't know how to locate. And that is why we've never got a result with a better performance than 83% with cv : we are using wrong features !

So, next step, we are going to work on how to find out the inverted channel(s), with an "unsupervised" method.

### 29-12-2015
* add cut the wave (not finished)
* Feature analysis(precisely)

### 30-12-2015
* start working on action potential extraction

### 31-12-2015
* finish period extractor !!! with violent method(see PeriodSpliter in ECG functions)
