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
from django.db import connection
import time

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


###############################################################fi_check_replacement

@api_view(['POST'])
def fi_check_replacement(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}

    Location_token = request.data.get('Location_token', 0)
    User_Id = request.data.get('User_Id', 0)
    Script_Code = request.data.get('Script_Code', 1)
    Script_Option_Id = request.data.get('Script_Option_Id', 0)
    Script_Option_Langauge = request.data.get('Script_Option_Langauge', 'EN')
    Script_Action_Input = request.data.get('Script_Action_Input', '')

    if Script_Code == 0:
        Script_Code = 1

    if not Script_Code:
            res = {'message_code': 999, 'message_text': 'Script code is required'}
    elif not Location_token:
        res = {'message_code': 999, 'message_text': 'Location token is required'}
    elif not Script_Option_Langauge:
        res = {'message_code': 999, 'message_text': 'Script option language is required'}
    else:
            
            if Script_Option_Id != 0:
                
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    is_deleted = 0,
                    Script_Code__in=tblScriptOptions.objects.filter(
                        Script_Option_Langauge=Script_Option_Langauge,
                        Script_Option_Id=Script_Option_Id,
                        Location_token=Location_token,
                        Script_Code=Script_Code
                    )
                )
            else:
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    Script_Code=Script_Code
                )
            # serializer = tblChatScriptsSerializer(chat_scripts, many=True)
            # result = serializer.data
            # last_query = connection.queries[-1]['sql']
            # print(last_query)
            # print(result)
            # print(chat_scripts)
            if chat_scripts.exists():
                for chat_script in chat_scripts:
                    start = 0

                    if '{' in chat_script.Script_Text:
                        while start > -1:
                            posS = chat_script.Script_Text.find('{', start)
                            posE = chat_script.Script_Text.find('}', start)

                            if posS > -1:
                                Var = chat_script.Script_Text[posS:posE + 1]
                                debug = f"{posS} | {posE} | {Var}"

                                Var = Var.replace("{", "").replace("}", "")
                                arr = Var.split("-")

                                last_input = tblUserActions.objects.filter(
                                    Location_token=arr[0],
                                    User_Id=User_Id,
                                    Script_Code=arr[1]
                                ).values_list('Script_Action_Input', flat=True).first()

                                chat_script.Script_Text = chat_script.Script_Text.replace(
                                    "{" + arr[0] + "-" + arr[1] + "-" + arr[2] + "}",
                                    last_input
                                )

                                debug = f"{debug} | {chat_script.Script_Text}"
                                start = posE + 1

                    chat_script.Script_Options = []  # Script_Options field as empty list

                serializer = tblChatScriptsSerializer(chat_scripts, many=True)
                res = {'message_code': 1000, 'message_text': 'Response Retrieval Successfully.', 'message_data': serializer.data, 'message_debug':  [{"Debug": debug}] if debug != "" else []}
            else:
                res = {'message_code': 999, 'message_text': 'Sorry unable to understand your message. Please try again.', 'message_debug':  [{"Debug": debug}] if debug != "" else []}

    return JsonResponse(res)

##################################################fi_get_chat_action

@api_view(['POST'])
def fi_get_chat_action(request):
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}

    body = request.data

    Location_token = body.get('Location_token', 0)
    User_Id = body.get('User_Id', 0)
    Script_Code = body.get('Script_Code', 1)
    Script_Option_Id = body.get('Script_Option_Id', 0)
    Script_Option_Langauge = body.get('Script_Option_Langauge', 'EN')
    Script_Action_Input = body.get('Script_Action_Input', '')
    Script_Option_Value = body.get('Script_Option_Value', '')

    if Script_Code == 0:
        Script_Code = 1

    if not Script_Code:
        res = {'message_code': 999, 'message_text': 'Script code is required'}
    elif not Location_token:
        res = {'message_code': 999, 'message_text': 'Location token is required'}
    elif not User_Id:
        res = {'message_code': 999, 'message_text': 'User Id is required'}
    elif not Script_Option_Langauge:
        res = {'message_code': 999, 'message_text': 'Script option language is required'}
    else:
        
            user_action_data = {
                'Location_token':Location_token,
                'User_Id':User_Id,
                'Script_Code':Script_Code,
                'Script_Option_Id':Script_Option_Id,
                'Script_Option_Langauge':Script_Option_Langauge,
                'Script_Action_Input':Script_Action_Input,
                'Script_Option_Value':Script_Option_Value,
                'created_by':User_Id,
                'created_on':int(time.time()),
                'last_modified_by':User_Id,
                'last_modified_on':int(time.time())

            }
            UserActionSerializer = tblUserActionsSerializer(data=user_action_data)
            if UserActionSerializer.is_valid():
                instance = UserActionSerializer.save()
                serialized_data = tblUserActionsSerializer(instance).data
            else:
                print("Validation Errors:", tblUserActionsSerializer.errors)
            # print(int(time.time()))
            # last_query = connection.queries[-1]['sql']
            # print(last_query)


            if Script_Option_Id != 0:
                chat_scripts = tblChatScripts.objects.filter(
                Location_token=Location_token,
                Script_Language=Script_Option_Langauge,
                Script_Code__in=tblScriptOptions.objects.filter(
                    Script_Option_Langauge=Script_Option_Langauge,
                    Script_Option_Id=Script_Option_Id,
                    Location_token=Location_token,
                    Script_Code=Script_Code
                ).values('Script_Option_Action_Script_Id')
            )
            else:
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    Script_Code=Script_Code
                )

                
            if chat_scripts.exists():
                for chat_script in chat_scripts:
                    start = 0

                    if '{' in chat_script.Script_Text:
                        while start > -1:
                            posS = chat_script.Script_Text.find('{', start)
                            posE = chat_script.Script_Text.find('}', start)

                            if posS > -1:
                                Var = chat_script.Script_Text[posS:posE + 1]
                                debug = f"{posS} | {posE} | {Var}"

                                Var = Var.replace("{", "").replace("}", "")
                                arr = Var.split("-")

                                if '=' in Var:
                                    Quantity = tblUserActions.objects.filter(
                                        App_Id=App_Id,
                                        User_Id=User_Id,
                                        Script_Code=15
                                    ).values_list('Script_Action_Input', flat=True).first()

                                    url = f"https://www.vgold.co.in/dashboard/webservices/get_gold_plan_rate.php?qty={Quantity}"
                                    response = requests.get(url)
                                    details = response.json()

                                    debug = details
                                    if Var == "=BOOKING_CHARGES":
                                        lastInput = details.get("booking_charge", "")
                                    elif Var == "=BOOKING_AMOUNT":
                                        lastInput = details.get("booking_amount", "")
                                    elif Var == "=PAY_NOW":
                                        lastInput = details.get("have_to_pay", "")
                                    elif Var == "=EMI":
                                        EMI = tblUserActions.objects.filter(
                                            Location_token=Location_token,
                                            User_Id=User_Id,
                                            Script_Code=16
                                        ).values_list('Script_Option_Value', flat=True).first()

                                        arrInstallments = details.get("installments", {})
                                        lastInput = "Contact Support"
                                        for tempKey, tempValue in arrInstallments.items():
                                            if tempKey == f"{int(EMI)} Months":
                                                lastInput = f"{tempValue} for {tempKey}"
                                    
                                                chat_script.Script_Text = chat_script.Script_Text.replace(
                                                    "{" + arr[0] + "-" + arr[1] + "-" + arr[2] + "}",
                                                    lastInput
                                                )

                                                debug = f"{debug} | {chat_script.Script_Text}"
                                                start = posE + 1

                                            else:
                                                arr = Var.split("-")
                                                lastInput = tblUserActions.objects.filter(
                                                    Location_token=arr[0],
                                                    User_Id=User_Id,
                                                    Script_Code=arr[1]
                                                ).values_list('Script_Action_Input', flat=True).first()

                                                chat_script.Script_Text = chat_script.Script_Text.replace(
                                                    "{" + arr[0] + "-" + arr[1] + "-" + arr[2] + "}",
                                                    lastInput
                                                )

                                                debug = f"{debug} | {chat_script.Script_Text}"
                                                start = posE + 1

                    chat_script.Script_Options = []  # Script_Options field as an empty list

                    script_options = tblScriptOptions.objects.filter(
                    Script_Option_Langauge=Script_Option_Langauge,
                    Location_token=Location_token,
                    Script_Code=chat_script.Script_Code
                )

                serializer = tblScriptOptionsSerializer(script_options, many=True)

                if serializer.data:
                    chat_script.Script_Options = serializer.data






                # serializer = tblChatScriptsSerializer(chat_scripts, many=True)
                res = {'message_code': 1000, 'message_text': 'Response Retrieval Successfully.', 'message_data': serializer.data, 'message_debug': [{"Debug": debug}] if debug != "" else []}
            else:
                res = {'message_code': 999, 'message_text': 'Sorry unable to understand your message. Please try again.', 'message_debug': [{"Debug": debug}] if debug != "" else []}

    return JsonResponse(res)