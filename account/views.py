from rest_framework.decorators import api_view
from rest_framework.response import response

@api_view['GET']
def get_menu(request):
    menu =[
        {
            "name":"Margherita Pizza"
            "description":"classic Pizza with tomato sauce, and basil",
            "Price":10.30
        },
        {
            "name":"pasta Alfredo",
            "description": "creamy Alfredo sauce with fettuccicine pasta",
            "price":10.40
        }
    ]
    return response(menu)