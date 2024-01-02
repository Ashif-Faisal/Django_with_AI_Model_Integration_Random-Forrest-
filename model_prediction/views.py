from django.http import HttpResponse
from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd
import joblib


# Create your views here.
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            ap_hi = request.POST.get('ap_hi')
            ap_lo = request.POST.get('ap_lo')
            cholesterol = request.POST.get('cholesterol')
            gluc = request.POST.get('gluc')
            smoke = request.POST.get('smoke')
            alco = request.POST.get('alco')
            active = request.POST.get('active')

            print(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active)


            df = pd.DataFrame({'age': [age],'gender': [gender], 'height': [height],'weight':[weight], 'ap_hi':[ap_hi], 'ap_lo':[ap_lo], 'cholesterol':[cholesterol], 'gluc':[gluc], 'smoke': [smoke], 'alco':[alco], 'active':[active]})
            print(df)
            model = joblib.load('model_prediction/rndf_model.pkl')
            news = model.predict(df)
            print(news)

            if news[0]==0:
                return HttpResponse('No')
            else:
                return HttpResponse('Yesss')
    else:
        form = PredictionForm()
    return render(request, "predict.html", {"form": form})
