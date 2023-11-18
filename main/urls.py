from django.urls import path
from main.views import show_main,show_xml,show_xml_by_id,show_json,show_json_by_id,\
            register, login_user, logout_user,add_amount,sub_amount,delete_amount,\
            get_items_json,add_items_ajax, get_all_amount, delete_items_ajax, add_item,create_item_flutter

app_name = "main"

urlpatterns = [
    path("", show_main, name = "show_main"),
    path("add-item",add_item, name="add_item"),
    path("xml",show_xml, name="show_xml"),
    path("xml/<int:id>/",show_xml_by_id, name="show_xml_by_id"),
    path("json",show_json, name="show_json"),
    path("json/<int:id>/",show_json_by_id, name="show_json_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    path("add-amount/<int:id>/",add_amount, name='add_amount'),
    path("sub-amount/<int:id>/",sub_amount, name='sub_amount'),
    path("delete-amount/<int:id>/",delete_amount, name='delete_amount'),
    # path('edit-product/<int:id>', edit_product, name='edit_product'),

    path('get-items/', get_items_json, name='get_items_json'),
    path('create-ajax/', add_items_ajax, name='add_items_ajax'),
    path('get-all-amount/',get_all_amount,name='get_all_amount'),
    path("delete-item-ajax/<int:id>/",delete_items_ajax, name='delete_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]