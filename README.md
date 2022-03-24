# Cardiac Health Risk Prediction

This project uses an ML model to predict whether a person is at a higher or lower risk of a cardiovascular disease.

Try it out for yourself at https://cardiachealth.ml/.

Edit : The above link does not work anymore as we have shifted the app from AWS to Heroku. Use this link https://cardiachealth.herokuapp.com/ .

![](https://img.shields.io/badge/flask-1.1.2-brightgreen)
![](https://img.shields.io/badge/python-3.8.9-green)
![](https://img.shields.io/badge/numpy-1.19.2-yellowgreen)
![](https://img.shields.io/badge/scikit--learn-0.24.1-orange)
![](https://img.shields.io/badge/gunicorn-20.1.0-red)
![](https://img.shields.io/badge/wtforms-2.3.3-blue)

![](https://github.com/DebangshuB/CardioUIDeploy/blob/main/1.png)

## Machine Learning Model

The model is a classification model which uses gradient boosting algorithm. The model has been made using [Kaggle | Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset) made by [Svetlana Ulianova](https://www.kaggle.com/sulianova).\
The features of the dataset that we have used to train our model are as follows:

* Objective Features
  * Age
  * Height
  * Weight
  * Gender
* Examination Features
  * Systolic Blood Pressure
  * Diastolic Blood Pressure
  * Cholesterol
  * Glucose
* Subjective Features
  * Smoking
  * Alcohol Intake
  * Physical Activity
  

## Frontend

The front end of the website has been made using HTML, SCSS, Bootstrap and Javascript.


## Backend

#### Server
The project is hosted on an AWS EC2 instance.

Edit : It has been shifted to Heroku.

#### Web Backend
The project is contained in a Flask application written in python. The templating has been done using Jinja and the data collection from the user is done using WT Forms.


## Contributors

### Primary Contributors
* [@DebangshuB](https://github.com/DebangshuB)
* [@Debmalya-prog](https://github.com/Debmalya-prog)
* [@dalmeow](https://github.com/dalmeow)

#### About the Primary Contributors

The three of us are second year into our B.Tech in Computer Science and Engineering from KIIT University, Bhubaneswar, India.\
This project stemmed from our desire to put into use what we have learnt, and to make a real world application out of it.


