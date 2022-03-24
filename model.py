import joblib
import numpy


def parse(form_data):
    user_data = []
    user_data.append(form_data.age.data * 365)
    user_data.append(int(form_data.sex.data))
    user_data.append(form_data.height.data)
    user_data.append(form_data.weight.data)
    user_data.append(form_data.systolic_blood_pressure.data)
    user_data.append(form_data.diastolic_blood_pressure.data)
    user_data.append(int(form_data.cholestrol.data))
    user_data.append(int(form_data.gluc_level.data))
    user_data.append(int(form_data.smoking_Status.data))
    user_data.append(int(form_data.alcohol.data))
    user_data.append(int(form_data.active.data))
    

    return user_data


def GBModel(ls_sample):
    model_loaded = joblib.load('GBmodel')
    sample = numpy.asarray(ls_sample)
    sample = sample.reshape(1, -1)
    predicted = model_loaded.predict(sample)
    return predicted
