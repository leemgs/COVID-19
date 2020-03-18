# COVID-19 Detection from Chest X-Rays (PA)

> #### The Model File Uploaded in the Repository is a preliminary model and is under investigational and research use. Further the model is incrementally trained everyday with the new data images that are being uploaded by the sources.

##### 

### Dataset

+ #### COVID -19 Data [Source](https://www.sirm.org/category/senza-categoria/covid-19/)
+ #### Healthy & Pneumonia [Source](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

![](https://github.com/TerenzAI/COVID-19/Reference_Materials/Sample_image.png)

### AI Algorithm
#####The X-ray data used for the development of the AI system has been acquired from primarily two public databases namely, SIRM - Società Italiana di Radiologia Medica e Interventistica and Kaggle. Predominantly the data was acquired from three different categories i.e. Normal/ Healthy People, Pneumonia and Covid-19. The X-ray data considered in the study were from posteroanterior view where the X-ray beam enters through the posterior (back) aspect of the chest and exits out of the anterior (front) aspect, where the beam is detected. For detecting Covid-19 and classifying the data into Normal, Pneumonia and COVID-19, an AI engine leveraging Convolutional Neural Network was developed. The CNN algorithm developed performed pretty well by plotting an overall accuracy of 98.141%. Further, it was derived from the outcomes that the recall for the COVID-19 X-Rays was 100% with an AUC – ROC of 0.99.
![](https://github.com/TerenzAI/COVID-19/Reference_Materials/ROC.png)