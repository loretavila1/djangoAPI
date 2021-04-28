# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Cellphones, Companies

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Gran Kanán" })


def vista2(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'dos.html', {'title': "Gran Kanán" })  


def cellphones(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Cellphones.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def cellphonesAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newCellphone = Cellphones(name=json_object['phone_name'], brand=json_object['brand_name'], color=json_object['phone_color'], company=json_object['phone_company_id'])
            #INSERT INTO dogs (name, type_id,color,size) values ('Solovino',4,'black','big')
            newCellphone.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Cellphone inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def cellphoneDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Cellphones.objects.get(id=json_object["phone_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The phone_id its not valid'
                return JsonResponse(responseData, status=400)
            Cellphones.objects.filter(id=json_object["phone_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The Phone has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def cellphonesGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Cellphones.objects.get(id=json_object["phone_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The phone_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['brand'] = one_entry.brand
            responseData['data']['color'] = one_entry.color
            responseData['data']['company'] = one_entry.company

            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def cellphonesGetId(request, phoneid):

    if request.method == 'GET':
       
        try:
            one_entry = Cellphones.objects.get(id=phoneid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The phone_id its not valid'
            return JsonResponse(responseData, status=400)
        
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['brand'] = one_entry.brand
        responseData['data']['color'] = one_entry.color
        responseData['data']['company'] = one_entry.company

        return JsonResponse(responseData, status=200)
      
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def cellphonesUpdate(request, phoneid):

    if request.method == 'POST':
        try:
            one_entry = Cellphones.objects.get(id=phoneid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The phone_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            #AQUI VA EL CODIGO DEL UPDATE
            try:
                value = json_object["phone_name"]
                Cellphones.objects.filter(id=phoneid).update(name=json_object["phone_name"])
                contador = contador + 1  
            except KeyError:
                responseData = {}

            try:
                value = json_object["brand_name"]
                Cellphones.objects.filter(id=phoneid).update(brand=json_object["brand_name"])
                contador = contador + 1  
            except KeyError:
                responseData = {}
                
            try:
                value = json_object["phone_color"]
                Cellphones.objects.filter(id=phoneid).update(color=json_object["phone_color"])
                contador = contador + 1  
            except KeyError:
                responseData = {}

            try:
                value = json_object["phone_company_id"]
                Cellphones.objects.filter(id=phoneid).update(company=json_object["phone_company_id"])
                contador = contador + 1  
            except KeyError:
                responseData = {}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Datos actualizados'
                return JsonResponse(responseData, status=200)
                
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
      
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def companies(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Companies.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

