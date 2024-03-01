from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import JsonResponse
import json

from medicify_project.models import * 
from medicify_project.serializers import *



@api_view(['POST'])
def fi_insert_chatscripts(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
    # Extract data from request
    Script_Code = request.data.get('Script_Code', '')
    Location_token = request.data.get('Location_token', '')
    Script_Type = request.data.get('Script_Type', '')
    Script_Language = request.data.get('Script_Language', '')
    Script_Text = request.data.get('Script_Text', '')
    S1 = request.data.get('S1', '')
    S2 = request.data.get('S2', '')

    # Validate appointment_id
    if not Script_Code:
        res = {'message_code': 999,'message_text': 'Script code is required'}
    elif not Location_token:
        res = {'message_code': 999,'message_text': 'Location token is required'}
    elif not Script_Type:
        res = {'message_code': 999,'message_text': 'Script type is required'}
    elif not Script_Language:
        res = {'message_code': 999,'message_text': 'Script language is required'}
    elif not Script_Text:
        res = {'message_code': 999,'message_text': 'Script text is required'}
    elif not S1:
        res = {'message_code': 999,'message_text': 'S1 is required'}
    elif not S2:
        res = {'message_code': 999,'message_text': 'S2 is required'}
    else:
        try:
            
            chatscript_data = {
                'Script_Code':Script_Code,
                'Location_token':Location_token,
                'Script_Type':Script_Type,
                'Script_Language':Script_Language,
                'Script_Text':Script_Text,
                'S1':S1,
                'S2':S2

            }

            ChatScriptsSerializer = tblChatScriptsSerializer(data=chatscript_data)
            if ChatScriptsSerializer.is_valid():
                instance = ChatScriptsSerializer.save()
                last_Script_id_id = instance.Script_id
                serialized_data = tblChatScriptsSerializer(instance).data

                res = {
                    'message_code': 1000,
                    'message_text': 'Chat script inserted successfully',
                    'message_data': serialized_data,
                    'message_debug': debug if debug else []
                }
            else:
                res = {
                    'message_code': 2000,
                    'message_text': 'Validation Error',
                    'message_errors': ChatScriptsSerializer.errors
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def fi_insert_scriptoptions(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
    # Extract data from request
    Script_Code = request.data.get('Script_Code', '')
    Location_token = request.data.get('Location_token', '')
    Script_Option_Type = request.data.get('Script_Option_Type', '')
    Script_Option_Langauge = request.data.get('Script_Option_Langauge', '')
    Script_Option_Text = request.data.get('Script_Option_Text', '')
    Script_Option_Value = request.data.get('Script_Option_Value', '')
    Script_Option_Action_Script_Id = request.data.get('Script_Option_Action_Script_Id', '')

    # Validate appointment_id
    if not Location_token:
        res = {'message_code': 999,'message_text': 'Location token is required'}
    elif not Script_Code:
        res = {'message_code': 999,'message_text': 'Script code is required'}
    elif not Script_Option_Type:
        res = {'message_code': 999,'message_text': 'Script option type is required'}
    elif not Script_Option_Langauge:
        res = {'message_code': 999,'message_text': 'Script option language is required'}
    elif not Script_Option_Text:
        res = {'message_code': 999,'message_text': 'Script option text is required'}
    elif not Script_Option_Value:
        res = {'message_code': 999,'message_text': 'Script option value is required'}
    else:
        try:
            
            ScriptOption_data = {
                'Location_token':Location_token,
                'Script_Code':Script_Code,
                'Script_Option_Type':Script_Option_Type,
                'Script_Option_Langauge':Script_Option_Langauge,
                'Script_Option_Text':Script_Option_Text,
                'Script_Option_Value':Script_Option_Value,
                'Script_Option_Action_Script_Id':Script_Option_Action_Script_Id

            }

            ScriptOptionSerializer = tblScriptOptionsSerializer(data=ScriptOption_data)
            if ScriptOptionSerializer.is_valid():
                instance = ScriptOptionSerializer.save()
                serialized_data = tblScriptOptionsSerializer(instance).data

                res = {
                    'message_code': 1000,
                    'message_text': 'Script option inserted successfully',
                    'message_data': serialized_data,
                    'message_debug': debug if debug else []
                }
            else:
                res = {
                    'message_code': 2000,
                    'message_text': 'Validation Error',
                    'message_errors': ScriptOptionSerializer.errors
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(res, status=status.HTTP_200_OK)



@api_view(['POST'])
def fi_insert_useractions(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
     
    # Extract data from request
    Location_token = request.data.get('Location_token', '')
    User_Id = request.data.get('User_Id', '')
    Script_Code = request.data.get('Script_Code', '')
    Script_Option_Id = request.data.get('Script_Option_Id', '')
    Script_Option_Langauge = request.data.get('Script_Option_Langauge', '')
    Script_Action_Input = request.data.get('Script_Action_Input', '')
    Script_Option_Value = request.data.get('Script_Option_Value', '')

    # Validate appointment_id
    if not Location_token:
        res = {'message_code': 999,'message_text': 'Location token is required'}
    elif not Script_Code:
        res = {'message_code': 999,'message_text': 'Script code is required'}
    elif not User_Id:
        res = {'message_code': 999,'message_text': 'User id is required'}
    elif not Script_Option_Id:
        res = {'message_code': 999,'message_text': 'Script option id is required'}
    elif not Script_Option_Langauge:
        res = {'message_code': 999,'message_text': 'Script option langauge is required'}
    elif not Script_Action_Input:
        res = {'message_code': 999,'message_text': 'Script action input is required'}
    else:
        try:
            
            UserAction_data = {
                'Location_token':Location_token,
                'Script_Code':Script_Code,
                'User_Id':User_Id,
                'Script_Option_Id':Script_Option_Id,
                'Script_Option_Langauge':Script_Option_Langauge,
                'Script_Action_Input':Script_Action_Input,
                'Script_Option_Value':Script_Option_Value

            }

            UserActionSerializer = tblUserActionsSerializer(data=UserAction_data)
            if UserActionSerializer.is_valid():
                instance = UserActionSerializer.save()
                serialized_data = tblUserActionsSerializer(instance).data

                res = {
                    'message_code': 1000,
                    'message_text': 'User action inserted successfully',
                    'message_data': serialized_data,
                    'message_debug': debug if debug else []
                }
            else:
                res = {
                    'message_code': 2000,
                    'message_text': 'Validation Error',
                    'message_errors': UserActionSerializer.errors
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(res, status=status.HTTP_200_OK)



@api_view(['POST'])
def fi_get_useraction_by_locationtoken_userid(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
        

    Location_token = request.data.get('Location_token', '')
    User_Id = request.data.get('User_Id', '')

    if not Location_token:
        res = {'message_code': 999, 'message_text': 'Location token is required.'}
    elif not User_Id:
        res = {'message_code': 999, 'message_text': 'User id is required.'}
    else:
        try:
            
            # Fetch data using Django ORM
            UserActions = tblUserActions.objects.filter(
                Q(Location_token=Location_token,User_Id=User_Id,is_deleted=0)
            )

            # Serialize the data
            serializer = tblUserActionsSerializer(UserActions, many=True)
            result = serializer.data

            if result:
                res = {
                    'message_code': 1000,
                    'message_text': "User action retrieved successfully.",
                    'message_data': result,
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }
            else:
                res = {
                    'message_code': 999,
                    'message_text': "User action for this Location_token,User_Id not found.",
                    'message_data': [],
                    'message_debug': [{"Debug": debug}] if debug != "" else []
                }

        except Exception as e:
            res = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(res, status=status.HTTP_200_OK)
