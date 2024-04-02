from django.urls import path
from .views import *

urlpatterns = [    
    #################################tblChatScripts#########################################
    path('insert_chatscripts/', fi_insert_chatscripts, name='fi_insert_chatscripts'),

    #################################tblScriptOptions#########################################
    path('insert_scriptoptions/', fi_insert_scriptoptions, name='fi_insert_scriptoptions'),

    # #################################tblUserActions#########################################
    path('insert_useractions/', fi_insert_useractions, name='fi_insert_useractions'),
    path("get_useraction_by_locationtoken_userid/",fi_get_useraction_by_locationtoken_userid, name='fi_get_useraction_by_locationtoken_userid'),
    

    path("check_replacement/",fi_check_replacement, name='fi_check_replacement'),
    path("get_chat_action/",fi_get_chat_action, name='fi_get_chat_action'),

    
    path("insert_chatscripts_bulk_record_withparam/",fi_insert_chatscripts_bulk_record_withparam, name='fi_insert_chatscripts_bulk_record_withparam'),


    path("insert_scriptoptions_bulk_record_withparam/",fi_insert_scriptoptions_bulk_record_withparam, name='fi_insert_scriptoptions_bulk_record_withparam'),

     path("get_chat/",fi_get_chat, name='fi_get_chat'),

   
]

