#Automatization for test gender models in deepstream-app

First, we have to download the epoch of the model we want to test from the Digits port.
This model will be in .tar.gz format, then we have to extract the model and we will have
a ton of file for deployment. We just need to focus in 3 of them:

1. deploy.prototxt
2. snap_xxx.caffemodel
3. labels.txt

We have to do the following changes:
1. We have to change the name of snap_xxx.caffemodel to modelgender.caffemodel
2. Then we have to edit the labels file to format the content to DS. Example:
labels.txt original:
```
female
male
```
DS format labels.txt:
```
female; male
```

We move the model folder to gender_portal insisde the docker in the configs section od the DS app.
After that we excecute the python file to edit configs according to our model.



