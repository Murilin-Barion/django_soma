from django.shortcuts import render, HttpResponse

# Create your views here.

def sum(request, num1, num2):

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        return HttpResponse("<h3>Não foi possível fazer a conta, favor preencher com apenas números</h3>")

    result = num1 + num2

    # for number in numbers:
    #     result += number
    
    return HttpResponse(f"<h3>Soma: {result}</h3>")
