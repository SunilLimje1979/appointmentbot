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
    
]

