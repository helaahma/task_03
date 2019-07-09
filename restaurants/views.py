from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [

    {
    "restaurant_name":"five guys",
    "food_type" : "fast food"
    },
    {
    "restaurant_name":"Meat co.",
    "food_type" : "stake house"
    },
    {
    "restaurant_name" : "Dai Forni",
    "food_type" : "Italian food"
    }
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":
    {
    "restaurant_name":"five guys",
    "food_type":"fast food"
    },
    }
    return render(request, 'detail.html', context)
