from django.urls import path
from food.views import *

app_name= 'food'
urlpatterns = [
    path('home/', home_page, name="homepage"),
    path("data/", get_data, name='alldata'),
    path("detail/<int:item_id>", detail, name="detail"),
    # add item
    path("add", create_item, name="create_item"),

    #update item
    path("update/<int:id>/", update_item, name="update_item"),

    # delete item
    path("delete/<int:item_id>/", delete_item, name="delete_item"),

]