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
from googletrans import Translator

from medicify_project.models import * 
from medicify_project.serializers import *

from django.shortcuts import render,redirect
import requests

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
                                        Location_token=Location_token,
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


def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='hi').text
    return translated_text


def translate_to_marathi(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='mr').text
    return translated_text

# fi_insert_chatscripts_bulk_record_withparam
@api_view(['POST'])
def fi_insert_chatscripts_bulk_record_withparam(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
    body = request.data

    # script_code = body.get('script_code', "")
    script_type = body.get('script_type', "")
    clinic_name = body.get('clinic_name', "") #Dr. Mohite\'s Clinic
    hindi_clinic_name = translate_to_hindi(clinic_name)
    marathi_clinic_name = translate_to_marathi(clinic_name)
    dr_name = body.get('dr_name', "")
    hindi_dr_name = translate_to_hindi(dr_name)
    marathi_dr_name = translate_to_marathi(dr_name)
    dr_contact_number = body.get('dr_contact_number', "")

    try:
            
            chatscript_data = [
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Greetings,</p>\n\n<p>We appreciate your reaching out to <strong>"+str(clinic_name)+"</strong>.</p>\n\n<p>I&#39;m a <strong>Virtual Receptionist</strong>,</p>\n\n<p>To assist you more effectively, could you kindly inform me <strong>What you are looking for </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>नमस्ते,</p>\n\n<p><strong>"+str(hindi_clinic_name)+"</strong> से संपर्क करने के लिए धन्यवाद।</p>\n\n<p>मैं  एक<strong> व्हर्च्युअल रिसेप्शनिस्ट</strong> हूँ, </p>\n\n<p>आपकी अधिक प्रभावी ढंग से सहायता करने के लिए, क्या आप कृपया मुझे बता सकते हैं <strong>आप क्या खोज रहे हैं </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>नमस्कार,</p>\n\n<p><strong>"+str(marathi_clinic_name)+"</strong> ला संपर्क करण्याबद्दल आपले आभार।</p><p>मी एक <strong>व्हर्च्युअल रिसेप्शनिस्ट</strong> आहे,</p>\n\n<p>तुम्हाला अधिक प्रभावीपणे मदत करण्यासाठी, तुम्ही कृपया मला कळवू शकाल का <strong>तुम्ही काय शोधत आहात </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>"+str(dr_name)+" Profile HTML</p><br/> </strong>Would you like to book an appointment?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>"+str(hindi_dr_name)+" की प्रोफ़ाइल HTML</p><br/> </strong>क्या आप अपॉइंटमेंट बुक करना चाहेंगे?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>"+str(marathi_dr_name)+" यांचे प्रोफाइल HTML</p><br/> </strong>तुम्हाला भेटीची वेळ बुक करायची आहे का?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
            
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you<br/>If you need any more details or have any concerns you can contact "+str(dr_name)+" on <strong>+91 "+str(dr_contact_number)+"</strong></p><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "धन्यवाद<br/>यदि आपको अधिक जानकारी चाहिए या कोई चिंता है तो आप "+str(dr_name)+" से <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> पर संपर्क कर सकते हैं।", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद<br/>तुम्हाला आणखी काही तपशील हवे असल्यास किंवा काही समस्या असल्यास तुम्ही "+str(dr_name)+" यांच्याशी <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> वर संपर्क साधू शकता.", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
            
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Date</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>अपनी <strong>मुलाकात की तारीख</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची तारीख</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
            
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Time</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>अपना <strong>मिलने का समय</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची वेळ</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
            
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Who is the patient?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>रुग्ण कौन है?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>रुग्ण कोण आहे?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},

                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you, Your appointment on {2-4-0} between {2-5-0} is  confirmed. Please note your token no. <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, आपकी मुलाकात {2-5-0} के बीच {2-4-0} के लिए तय हो गई है। कृपया अपना टोकन नंबर नोट कर लें <strong></strong>। </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, तुमची {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित झाली आहे. तुमचा टोकन क्र. <strong></strong> आहे.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},

                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Please mention patient name</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का नाम बताएं</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचे नाव सांगा</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},

                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Please mention patient mobile no.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का मोबाइल नंबर बताएं।</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचा मोबाईल क्रमांक नमूद करा.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},

                
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you,  appointment for {2-8-0} on {2-4-0} between {2-5-0} is  confirmed. Please note the token no. <strong>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, {2-8-0} के लिए {2-4-0} को {2-5-0} के बीच मिलना तय है। कृपया टोकन नंबर नोट कर लें। <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, {2-8-0} साठी {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित आहे. कृपया टोकन क्र. <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
 

                
            ]

            # print(chatscript_data)

            for data_item in chatscript_data:
                ChatScriptsSerializer = tblChatScriptsSerializer(data=data_item)
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

# fi_insert_scriptoptions_bulk_record_withparam
@api_view(['POST'])
def fi_insert_scriptoptions_bulk_record_withparam(request):
    
    debug = ""
    res = {'message_code': 999, 'message_text': 'Functional part is commented.', 'message_data': [], 'message_debug': debug}
    body = request.data

    # script_code = body.get('script_code', "")
    dr_name = body.get('dr_name', "")
    hindi_dr_name = translate_to_hindi(dr_name)
    marathi_dr_name = translate_to_marathi(dr_name)
    script_option_type = body.get('script_option_type', "")

    try:
            
            scriptoption_data = [
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": " "+str(dr_name)+" Profile", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "Book Appointment", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": " "+str(hindi_dr_name)+" की जानकारी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "बुक अपॉइंटमेंट", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": " "+str(marathi_dr_name)+" राची माहिती", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
                {"Script_Code": 1, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "बुक अपॉइंटमेंट", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               
               
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "Yes", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "No", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "हाँ", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "नहीं", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "होय", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 2, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "नाही", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               
               {"Script_Code": 4, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 4, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 4, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               
               {"Script_Code": 5, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 5, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 5, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
              
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "MySelf", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "EN", "Script_Option_Text": "Family Member/Friend ", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "\nखुद के लिए", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "HI", "Script_Option_Text": "\nपरिवार के सदस्य/दोस्त के लिए", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "स्वत:साठी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               {"Script_Code": 6, "Script_Option_Type": script_option_type, "Script_Option_Langauge": "MA", "Script_Option_Text": "कुटुंबातील सदस्यांसाठी/मित्रासाठी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": None, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": None},
               
                
            ]


            for data_item in scriptoption_data:
                ScriptOptionSerializer = tblScriptOptionsSerializer(data=data_item)
                if ScriptOptionSerializer.is_valid():
                    instance = ScriptOptionSerializer.save()
                    last_Script_Option_Id = instance.Script_Option_Id
                    serialized_data = tblScriptOptionsSerializer(instance).data

                    res = {
                        'message_code': 1000,
                        'message_text': 'script options inserted successfully',
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
def fi_get_chat(request):
    if request.method == 'POST':
        # Get the JSON data from the request body
        json_data = request.body.decode('utf-8').strip()

        url = 'http://13.233.211.102/appointmentbot/api/get_chat_action/'

        # Make a POST request using the requests library
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json_data, headers=headers)

        # Check for errors in the response
        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to fetch data from the server'}, status=500)

        # Return the response data
        return JsonResponse(response.json(), status=200)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)