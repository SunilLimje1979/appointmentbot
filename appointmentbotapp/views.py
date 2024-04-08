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
from collections import defaultdict
from datetime import datetime

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

    resArray = []

    if Script_Code == 0:
        Script_Code = 1

    if not Script_Code:
        res = {'message_code': 999, 'message_text': 'Script code is required'}
    elif not Location_token:
        res = {'message_code': 999, 'message_text': 'Location token is required'}
    # elif not User_Id:
    #     res = {'message_code': 999, 'message_text': 'User Id is required'}
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
            

            if Script_Option_Id != 0:
                script_option_action_script_ids = tblScriptOptions.objects.filter(
                Script_Option_Langauge=Script_Option_Langauge,
                Script_Option_Id=Script_Option_Id,
                Location_token=Location_token,
                Script_Code=Script_Code
                ).values_list('Script_Option_Action_Script_Id', flat=True)
                
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    Script_Code__in=script_option_action_script_ids
                )
            else:
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    Script_Code=Script_Code
                )

            # print(script_option_action_script_ids)
            if chat_scripts.exists():
                chat_scripts_data = []
                for chat_script in chat_scripts:
                    start = 0

                    serializer = tblChatScriptsSerializer(chat_script)
                    chat_script_data = serializer.data
                    # last_query = connection.queries[-1]['sql']
                    # print(last_query)
                    
                    chat_script.Script_Options = []  # Script_Options field as an empty list

                    script_options = tblScriptOptions.objects.filter(
                    Script_Option_Langauge=Script_Option_Langauge,
                    Location_token=Location_token,
                    Script_Code=chat_script.Script_Code
                )

                serializer_scriptoptions = tblScriptOptionsSerializer(script_options, many=True)

                if serializer.data:
                    chat_script.Script_Options = serializer_scriptoptions.data
                    chat_script_data['Script_Options'] = serializer_scriptoptions.data

                chat_scripts_data.append(chat_script_data)

                # # from date get day logic
                # # Assuming the date format is mm/dd/yyyy
                # date_format = "%d/%m/%Y"
                # if (body.get('Script_Action_Input') and datetime.strptime(body.get('Script_Action_Input'), date_format)):

                #     # Get the Location_token
                #     Script_Action_Input = body.get('Script_Action_Input')
                #     date_string = Script_Action_Input
                # else:
                #     date_string = ""

                # print(date_string)
                # # Parse the date string into a datetime object
                # if date_string:
                #     date_object = datetime.strptime(date_string, '%d/%m/%Y')

                #     # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
                #     day_of_week = date_object.weekday()
                # else:
                #     day_of_week=""

                # # Dictionary mapping day of the week to its name
                
                # day_mapping = {
                #     1: "Monday",
                #     2: "Tuesday",
                #     3: "Wednesday",
                #     4: "Thursday",
                #     5: "Friday",
                #     6: "Saturday",
                #     7: "Sunday"
                # }

                # if date_string:
                #     # Get the name of the day from the dictionary
                #     day_name = day_mapping[day_of_week]
                # print(day_name)

                                
                # Get the Script_Action_Input field from the request body
                day_mapping = {
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday",
                    7: "Sunday"
                }
                if body.get('Script_Action_Input'):
                    script_action_input = body.get('Script_Action_Input')
                else:
                    script_action_input =""
                
                day_of_week =""
                # Define the expected date format
                date_format = "%d/%m/%Y"

                # Check if Script_Action_Input is present and if it matches the expected format
                if script_action_input:
                    try:
                        # Parse the date string into a datetime object
                        date_object = datetime.strptime(script_action_input, date_format)

                        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
                        day_mapping = {
                            0: "Monday",
                            1: "Tuesday",
                            2: "Wednesday",
                            3: "Thursday",
                            4: "Friday",
                            5: "Saturday",
                            6: "Sunday"
                        }
                        day_of_week = date_object.weekday()

                       

                        # Get the name of the day from the dictionary
                        day_name = day_mapping[day_of_week]
                        print("Day of the week:", day_name)

                    except ValueError:
                        day_name=""
                else:
                    day_name=""


                time_slots = []
                day_availability = defaultdict(list)
                for chat_script in chat_scripts_data:
                    if 'Script_Options' in chat_script:
                        script_options = chat_script['Script_Options']
                        for option in script_options:
                            if 'Script_Option_Text' in option and '{TIME_SLOTS}' in option['Script_Option_Text']:
                                # Assuming Location_token is available in chat_script chat_script['Location_token']
                                doctorlocations = Tbldoctorlocations.objects.filter(location_token="test_token2")
                                if doctorlocations.exists():
                                    # Assuming DoctorLocationSerializer is properly defined
                                    serializer_doctorlocation = DoctorLocationSerializer(doctorlocations, many=True)
                                    for data_item in serializer_doctorlocation.data:
                                        doctor_location_id = data_item.get('doctor_location_id')

                                        doctorlocationavailability = Tbldoctorlocationavailability.objects.filter(doctor_location_id=doctor_location_id)
                                        if doctorlocationavailability.exists():
                                            # Assuming DoctorLocationSerializer is properly defined
                                            serializer_doctorlocationavailability = DoctorLocationAvailabilitySerializer(doctorlocationavailability, many=True)
                                            
                                            # print(serializer_doctorlocationavailability.data)
                                            for data_item in serializer_doctorlocationavailability.data:
                                                availability_day = data_item.get('availability_day')
                                                day_of_week = day_mapping.get(availability_day)


                                                
                                                # availability_starttime = data_item.get('availability_starttime')
                                                # availability_endtime = data_item.get('availability_endtime')

                                                # availability_info = f"{day_of_week}: {availability_starttime} - {availability_endtime}"
                                                availability_day = data_item.get('availability_day')
                                                day_of_week = day_mapping.get(availability_day)

                                                availability_starttime = data_item.get('availability_starttime')
                                                availability_endtime = data_item.get('availability_endtime')

                                                availability_info = f"{availability_starttime} - {availability_endtime}"

                                                # Append the availability info to the corresponding day's list
                                                day_availability[day_of_week].append(availability_info)

                                            # Now `day_availability` dictionary will have availability info for each day
                                            # Print or process this dictionary as needed
                                            # for day, availability_info in day_availability.items():
                                            #     print(f"{day}: {', '.join(availability_info)}")
                                            #     # # Append the availability info to the time_slots list
                                            #     if day==day_name:
                                            #         time_slots+={', '.join(availability_info)}  #.append(availability_info)

                                            #         # Join the time slots list with <br/> to create the final string
                                            #         time_slot_text = "<br/>".join(time_slots)

                                            #         # Replace {TIME_SLOTS} in the option text with the concatenated time slots
                                            #         option['Script_Option_Text'] = option['Script_Option_Text'].replace("{TIME_SLOTS}", time_slot_text)
                                            #     else:
                                            #         option['Script_Option_Text'] = option['Script_Option_Text'].replace("{TIME_SLOTS}", "Please select another date")
                                            for day, availability_info in day_availability.items():
                                                if day_name == day:
                                                    # print(f"{day}: {', '.join(availability_info)}")
                                                    # updated_availability_info = []
                                                    # for info in availability_info:
                                                    #     start_time, end_time = info.split(" - ")
                                                    #     start_hour = int(start_time.split(":")[0])
                                                    #     end_hour = int(end_time.split(":")[0])
                                                    #     start_time_period = "AM" if start_hour < 12 else "PM"
                                                    #     end_time_period = "AM" if end_hour < 12 else "PM"

                                                    #     # Adjust end time period based on whether it's the next day
                                                    #     if start_hour > end_hour or (start_hour == end_hour and int(start_time.split(":")[1]) > int(end_time.split(":")[1])):
                                                    #         end_time_period = "AM" if end_hour < 12 else "PM"

                                                    #     updated_info = f"{start_hour if start_hour <= 12 else start_hour - 12} {start_time_period} - {end_hour if end_hour <= 12 else end_hour - 12} {end_time_period}"
                                                    #     updated_availability_info.append(updated_info)

                                                    # # Append the availability info to the time_slots list
                                                    # time_slots.extend(updated_availability_info)
                                                    # time_slot_text = "<br/>".join(time_slots)
                                                    # option['Script_Option_Text'] = option['Script_Option_Text'].replace("{TIME_SLOTS}", time_slot_text)
                                                    print(f"{day}: {', '.join(availability_info)}")
                                                    updated_availability_info = []
                                                    for info in availability_info:
                                                        start_time, end_time = info.split(" - ")
                                                        start_hour = int(start_time.split(":")[0])
                                                        end_hour = int(end_time.split(":")[0])
                                                        start_time_period = "AM" if start_hour < 12 else "PM"
                                                        end_time_period = "AM" if end_hour < 12 else "PM"

                                                        # Adjust end time period based on whether it's the next day
                                                        if start_hour > end_hour or (start_hour == end_hour and int(start_time.split(":")[1]) > int(end_time.split(":")[1])):
                                                            end_time_period = "AM" if end_hour < 12 else "PM"

                                                        updated_info = f"{start_hour if start_hour <= 12 else start_hour - 12} {start_time_period} - {end_hour if end_hour <= 12 else end_hour - 12} {end_time_period}"
                                                        updated_availability_info.append(updated_info)

                                                    # Join the availability info with comma and space
                                                    updated_availability_info = ", ".join(updated_availability_info)

                                                    # Replace space followed by AM or PM with AM- or PM-
                                                    updated_availability_info = updated_availability_info.replace(" AM", "AM").replace(" PM", "PM")

                                                    # Replace comma followed by space with comma
                                                    updated_availability_info = updated_availability_info.replace(", ", ",")

                                                    # Replace comma with comma, space
                                                    updated_availability_info = updated_availability_info.replace(",", ", ")

                                                    # Append the availability info to the time_slots list
                                                    time_slots.append(updated_availability_info)

                                                    time_slots_individual = []

                                                    for time_slot_concatenated in time_slots:
                                                        # Split each concatenated time slot into individual parts
                                                        time_slots_individual.extend(time_slot_concatenated.split(', '))

                                                    # Now `time_slots_individual` will contain each time slot separately
                                                    # for time_slot in time_slots_individual:
                                                    # Join the time slots list with <br/> to create the final string
                                                    # time_slot_text = "<br/>".join(time_slots)
                                                    # time_slots_individual = time_slots.split(', ')
                                                    for time_slot in time_slots_individual:
                                                        script_option = {
                                                            "Script_Option_Id": 16,
                                                            "Script_Option_Type": 1,
                                                            "Script_Option_Langauge": "EN",
                                                            "Script_Option_Text": time_slot,
                                                            "Script_Option_Value": None,
                                                            "Script_Option_Action_Script_Id": 6,
                                                            "created_on": None,
                                                            "created_by": None,
                                                            "last_modified_on": None,
                                                            "last_modified_by": None,
                                                            "deleted_by": None,
                                                            "is_deleted": 0,
                                                            "Location_token": "test_token",
                                                            "Script_Code": 5
                                                        }
                                                        # Append the script option to the list
                                                        # script_options.append(script_option)
                                                        script_options.append(script_option)

                                                    chat_script['Script_Options']=""
                                                    chat_script['Script_Options']=script_options
                                                    # Replace {TIME_SLOTS} in the option text with the concatenated time slots
                                                    # option['Script_Option_Text'] = option['Script_Option_Text'].replace("{TIME_SLOTS}", str(time_slots))
                                                else:
                                                    option['Script_Option_Text'] = option['Script_Option_Text'].replace("{TIME_SLOTS}", "Please select another date")


                # for chat_script in chat_scripts_data:
                #     if 'Script_Text' in chat_script:
                #         # Define the date and time values to replace the placeholders
                #         date_value = "2024-02-20"  # Example date value
                #         time_value = "10:00 AM - 11:00 AM"  # Example time value

                #         # Replace the placeholders with the actual values
                #         formatted_script_text = chat_script["Script_Text"].format(date_value, time_value)

                #         # Update the chat_script dictionary with the formatted script text
                #         chat_script["Script_Text"] = formatted_script_text

                res = {'message_code': 1000, 'message_text': 'Response Retrieval Successfully.', 'message_data': chat_script_data, 'message_debug': [{"Debug": debug}] if debug != "" else []}
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
    location_token = body.get('location_token', "")

    try:
            
            chatscript_data = [
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Greetings,</p>\n\n<p>We appreciate your reaching out to <strong>"+str(clinic_name)+"</strong>.</p>\n\n<p>I&#39;m a <strong>Virtual Receptionist</strong>,</p>\n\n<p>To assist you more effectively, could you kindly inform me <strong>What you are looking for </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>नमस्ते,</p>\n\n<p><strong>"+str(hindi_clinic_name)+"</strong> से संपर्क करने के लिए धन्यवाद।</p>\n\n<p>मैं  एक<strong> व्हर्च्युअल रिसेप्शनिस्ट</strong> हूँ, </p>\n\n<p>आपकी अधिक प्रभावी ढंग से सहायता करने के लिए, क्या आप कृपया मुझे बता सकते हैं <strong>आप क्या खोज रहे हैं </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>नमस्कार,</p>\n\n<p><strong>"+str(marathi_clinic_name)+"</strong> ला संपर्क करण्याबद्दल आपले आभार।</p><p>मी एक <strong>व्हर्च्युअल रिसेप्शनिस्ट</strong> आहे,</p>\n\n<p>तुम्हाला अधिक प्रभावीपणे मदत करण्यासाठी, तुम्ही कृपया मला कळवू शकाल का <strong>तुम्ही काय शोधत आहात </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>"+str(dr_name)+" Profile HTML</p><br/> </strong>Would you like to book an appointment?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>"+str(hindi_dr_name)+" की प्रोफ़ाइल HTML</p><br/> </strong>क्या आप अपॉइंटमेंट बुक करना चाहेंगे?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>"+str(marathi_dr_name)+" यांचे प्रोफाइल HTML</p><br/> </strong>तुम्हाला भेटीची वेळ बुक करायची आहे का?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you<br/>If you need any more details or have any concerns you can contact "+str(dr_name)+" on <strong>+91 "+str(dr_contact_number)+"</strong></p><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "धन्यवाद<br/>यदि आपको अधिक जानकारी चाहिए या कोई चिंता है तो आप "+str(dr_name)+" से <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> पर संपर्क कर सकते हैं।", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 3, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद<br/>तुम्हाला आणखी काही तपशील हवे असल्यास किंवा काही समस्या असल्यास तुम्ही "+str(dr_name)+" यांच्याशी <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> वर संपर्क साधू शकता.", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Date</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>अपनी <strong>मुलाकात की तारीख</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 4, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची तारीख</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Time</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>अपना <strong>मिलने का समय</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 5, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची वेळ</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Who is the patient?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>रुग्ण कौन है?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 6, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>रुग्ण कोण आहे?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you, Your appointment on {2-4-0} between {2-5-0} is  confirmed. Please note your token no. <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, आपकी मुलाकात {2-5-0} के बीच {2-4-0} के लिए तय हो गई है। कृपया अपना टोकन नंबर नोट कर लें <strong></strong>। </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 7, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, तुमची {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित झाली आहे. तुमचा टोकन क्र. <strong></strong> आहे.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Please mention patient name</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का नाम बताएं</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 8, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचे नाव सांगा</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Please mention patient mobile no.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का मोबाइल नंबर बताएं।</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 9, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचा मोबाईल क्रमांक नमूद करा.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "EN", "Script_Text": "<p>Thank you,  appointment for {2-8-0} on {2-4-0} between {2-5-0} is  confirmed. Please note the token no. <strong>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, {2-8-0} के लिए {2-4-0} को {2-5-0} के बीच मिलना तय है। कृपया टोकन नंबर नोट कर लें। <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 10, "Script_Type": script_type, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, {2-8-0} साठी {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित आहे. कृपया टोकन क्र. <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
 

                
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
    # script_option_type = body.get('script_option_type', "")
    
    location_token = body.get('location_token', "")

    try:
            
            scriptoption_data = [
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": " "+str(dr_name)+" Profile", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 2, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "Book Appointment", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 4, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": " "+str(hindi_dr_name)+" की जानकारी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 2, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "बुक अपॉइंटमेंट", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 4, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": " "+str(marathi_dr_name)+" राची माहिती", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 2, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "बुक अपॉइंटमेंट", "Script_Option_Value": None, "Script_Option_Action_Script_Id":4 , "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               
               
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "Yes", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 4, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "No", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 3, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "हाँ", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 4, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "नहीं", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 3, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "होय", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 4, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 2, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "नाही", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 3, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               
               {"Script_Code": 4, "Script_Option_Type": 5, "Script_Option_Langauge": "EN", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 5, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 4, "Script_Option_Type": 5, "Script_Option_Langauge": "HI", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 5, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 4, "Script_Option_Type": 5, "Script_Option_Langauge": "MA", "Script_Option_Text": "{TENDATES}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 5, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               
               {"Script_Code": 5, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 5, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 5, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
              
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "MySelf", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 7, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "EN", "Script_Option_Text": "Family Member/Friend ", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 8, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "\nखुद के लिए", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 7, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "HI", "Script_Option_Text": "\nपरिवार के सदस्य/दोस्त के लिए", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 8, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "स्वत:साठी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 7, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 6, "Script_Option_Type": 1, "Script_Option_Langauge": "MA", "Script_Option_Text": "कुटुंबातील सदस्यांसाठी/मित्रासाठी", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 8, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               


               {"Script_Code": 8, "Script_Option_Type": 2, "Script_Option_Langauge": "EN", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 9, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 8, "Script_Option_Type": 2, "Script_Option_Langauge": "HI", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 9, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 8, "Script_Option_Type": 2, "Script_Option_Langauge": "MA", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 9, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 9, "Script_Option_Type": 3, "Script_Option_Langauge": "EN", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 10, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 9, "Script_Option_Type": 3, "Script_Option_Langauge": "HI", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 10, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 9, "Script_Option_Type": 3, "Script_Option_Langauge": "MA", "Script_Option_Text": "", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 10, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               

                
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