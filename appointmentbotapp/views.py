from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime ,timedelta
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
import random

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


###############################################################


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
    #print("Script Location_token:",Location_token)
    #print("script action input:",Script_Action_Input)

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
                # serialized_data = tblUserActionsSerializer(instance).data
                if(Script_Code==9):
                    print("add appointment")
                     # Fetch all user actions associated with the User_Id
                    user_actions = tblUserActions.objects.filter(User_Id=User_Id)
                    doctor_location = Tbldoctorlocations.objects.get(location_token=Location_token)
                    doctor_id = doctor_location.doctor_id_id  # Accessing the doctor_id field from Tbldoctorlocations
                    print(doctor_id)
                    Input_values=[Data.Script_Action_Input for Data in user_actions]
                    appointment_date=Input_values[2]
                    appointment_time=Input_values[3]
                    appointment_name=Input_values[5]
                    appointment_mobileno=Input_values[6]
                    print(Input_values)
                    print(appointment_date,appointment_time,appointment_name,appointment_mobileno)
                
                    # Parse time slot (assuming '8 AM to 12 AM' format)
                    start_time, end_time = appointment_time.split(' to ')
                    start_hour = int(start_time.split()[0])
                    end_hour = int(end_time.split()[0])

                    day, month, year = appointment_date.split("-")

                    # Construct the datetime string in the desired format "YYYY-MM-DD HH:MM:SS"
                    date_time_str = f"{year}-{month}-{day} {start_hour:02d}:00:00"

                    # Print the formatted datetime string
                    print(date_time_str)
                 
                    # Create a dictionary with the appointment data
                    appointment_data = {
                        'doctor_id': doctor_id,
                        'appointment_mobileno': appointment_mobileno,
                        'appointment_name': appointment_name,
                        'appointment_datetime': date_time_str,
                        'appointment_status': 1,
                        'appointment_gender':'Male'
                    }
                    api_url="http://13.233.211.102/appointment/api/insert_appointment_data/"
                    response=requests.post(api_url,json=appointment_data)
                    print(response.text)

                else:
                    print("Script Code",Script_Code)
                serialized_data = UserActionSerializer.data 
                # print(serialized_data)
            else:
                # print("Validation Errors:", tblUserActionsSerializer.errors)
                print("Validation Errors:",  UserActionSerializer.errors)
            

            if Script_Option_Id != 0:
                #print("line 427 if")
                #print(Script_Option_Id,Script_Option_Langauge,Location_token,Script_Code)
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
                
                #for item in script_option_action_script_ids:
                #    print(item)  # This will print each item in the queryset

            else:
                chat_scripts = tblChatScripts.objects.filter(
                    Location_token=Location_token,
                    Script_Language=Script_Option_Langauge,
                    Script_Code=Script_Code
                )
                #print("line 447 else")
                
            # print(Location_token)
            # print(User_Id)
          

            #print("446",script_option_action_script_ids)
            if chat_scripts.exists():
                #print("line 451")
                chat_scripts_data = []
                
                for chat_script in chat_scripts:
                    start = 0
                    
                    if '{' in chat_script.Script_Text:
                        while start > -1:
                            posS = chat_script.Script_Text.find('{', start)
                            posE = chat_script.Script_Text.find('}', start)

                            if posS > -1:
                                Var = chat_script.Script_Text[posS:posE + 1]
                                debug = f"{posS} | {posE} | {Var}"
                                print("Debug:", debug)

                                Var = Var.replace("{", "").replace("}", "")
                                arr = Var.split("-")
                                print("arr:", arr)

                                iData = tblUserActions.objects.filter(
                                        Location_token=Location_token,
                                        User_Id=User_Id,
                                        Script_Code_id=arr[0]
                                
                                    ).values_list('Script_Action_Input', flat=True).first()
                                print("iData:", iData)
                                
                                chat_script.Script_Text = chat_script.Script_Text.replace(
                                                    "{" + arr[0] + "-" + arr[1] + "-" + arr[2] + "}",
                                                    iData)
                                print(chat_script.Script_Text)
                                
                                start = posE + 1
                                
                            else:
                                start=-1
                                
                    chat_script.Script_Options = []  # Script_Options field as an empty list
                    
                    serializer = tblChatScriptsSerializer(chat_script)
                    chat_script_data = serializer.data
                    # last_query = connection.queries[-1]['sql']
                    # print(last_query)
                    
                  

                    script_options = tblScriptOptions.objects.filter(
                    Script_Option_Langauge=Script_Option_Langauge,
                    Location_token=Location_token,
                    Script_Code=chat_script.Script_Code
                    )
                #print("line 468")
                
                for loop in script_options:
                    #print("Script Option type:", loop.Script_Option_Type)
                    #print("Script Option Text:", loop.Script_Option_Text)
                    #print("Script Location_token:",Location_token)
                    #print("script action input:",Script_Action_Input)
                    #print("Script_Option_Id ",loop.Script_Option_Id )
   
                    # in look check Script_Option_Type == 5 and Srcipt_Option_Text == {TENDATES}
                    if loop.Script_Option_Type == 5 and loop.Script_Option_Text == '{TENDATES}':
                        try:
                            doctor_location = Tbldoctorlocations.objects.get(location_token=Location_token)
                        except Tbldoctorlocations.DoesNotExist:
                            return Response({'error': 'Invalid location token'}, status=status.HTTP_404_NOT_FOUND)

                        doctor_id = doctor_location.doctor_id

                        # Calculate date range (current date to next 10 days)
                        current_date = datetime.now().date()
                        end_date = current_date + timedelta(days=10)

                        # Fetch doctor leave records within the specified date range
                        doctor_leaves = Tbldoctorleave.objects.filter(
                            doctor_id=doctor_id,
                            leave_date__gte=(datetime.now() - timedelta(days=1)).timestamp(),  # Include current date (considering time zone differences)
                            leave_date__lt=(datetime.now() + timedelta(days=10)).timestamp()  # Next 10 days from current date
                        )

                        # Prepare leave details with structured format
                        leave_details = []
                        valid_leave_dates = set()

                        for leave in doctor_leaves:
                            if leave.start_time != 0 and leave.end_time != 0:  # Only consider if start_time and end_time are non-zero
                                leave_date = datetime.fromtimestamp(leave.leave_date).date()
                                valid_leave_dates.add(leave_date.strftime('%d-%m-%Y'))  # Add formatted date string to the set.
                        
                        valid_leave_dates=list(valid_leave_dates)
                        print(valid_leave_dates)
                        for leave_date in valid_leave_dates:  
                                # Construct leave detail entry
                                leave_details.append({
                                    'Script_Option_Id': loop.Script_Option_Id,
                                    'Script_Option_Type':  1,
                                    'Script_Option_Language': loop.Script_Option_Langauge,
                                    'Script_Option_Text': leave_date,
                                    'Script_Option_Value': leave_date,
                                    'Script_Option_Action_Script_Id': loop.Script_Option_Action_Script_Id,
                                    
                                    'Script_Code': loop.Script_Code
                                })

                        # Generate list of all dates within the date range (including current date)
                        all_dates = [current_date + timedelta(days=i) for i in range(10)]  # 11 days including current date

                        # Prepare non-leave date details with structured format
                        nonleaved_dates_details = []
                        for date in all_dates:
                            if date not in [datetime.fromtimestamp(leave.leave_date).date() for leave in doctor_leaves]:
                                # Determine time suffix based on day of the week (Monday to Sunday)
                                day_of_week = date.weekday() + 1  # Monday is 0, so add 1 to match your day numbering
                                availability = Tbldoctorlocationavailability.objects.filter(doctor_id=doctor_id, availability_day=day_of_week).first()
                                if availability and availability.availability_starttime != 0 and availability.availability_endtime != 0:
                                     
                                    # Construct non-leave detail entry
                                    nonleaved_dates_details.append({
                                        'Script_Option_Id': loop.Script_Option_Id,
                                        'Script_Option_Type':  1,
                                        'Script_Option_Language': loop.Script_Option_Langauge,
                                        'Script_Option_Text': date.strftime('%d-%m-%Y'),
                                        'Script_Option_Value':  date.strftime('%d-%m-%Y'),
                                        'Script_Option_Action_Script_Id': loop.Script_Option_Action_Script_Id,
                                        
                                        'Script_Code': loop.Script_Code
                                    })

                        # Combine leave and non-leave date details into a single list
                        script_options = leave_details + nonleaved_dates_details
                   
                    elif(loop.Script_Option_Type == 6 and loop.Script_Option_Text == '{TIME_SLOTS}'):
                            # print(loop.Script_Option_Type)
                            # print("Script Location_token:",Location_token)
                            # print("script action input:",Script_Action_Input)
                            # print("Language",loop.Script_Option_Langauge,str(loop.Script_Option_Langauge))
                            try:
                                doctor_location = Tbldoctorlocations.objects.get(location_token=Location_token)
                            except Tbldoctorlocations.DoesNotExist:
                                return Response({'error': 'Invalid location token'}, status=status.HTTP_404_NOT_FOUND)

                            doctor_id = doctor_location.doctor_id

                            try:
                                # Parse the provided date string into a datetime object
                                # date = datetime.strptime(Script_Action_Input, "%d-%m-%Y").date()
                                # print(date,'date')
                                 # Parse the date string into a datetime object
                                date_object = datetime.strptime(Script_Action_Input, '%d-%m-%Y')
                                print(date_object)
                            except ValueError:
                                return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

                            # Convert the date to a Unix timestamp (epoch time)
                            # leave_timestamp =int(datetime.timestamp(datetime.combine(date, datetime.min.time())))
                            # print("leave_timestamp",leave_timestamp)
                            epoch_timestamp_gmt = int(date_object.timestamp())
    
                            # Calculate the epoch timestamp for the start of the day (midnight) in GMT+05:30 timezone
                            leave_timestamp = epoch_timestamp_gmt + (5 * 3600) + (30 * 60)
                            
                            print(leave_timestamp)

                            # Check if there are doctor leaves for the specified date
                            doctor_leaves = Tbldoctorleave.objects.filter(
                                doctor_id=doctor_id,
                                leave_date=leave_timestamp
                            )

                            if doctor_leaves.exists():
                                # Doctor leave details found for the date
                                leave_details = []
                                for leave in doctor_leaves:
                                    if leave.start_time != 0 and leave.end_time != 0:
                                        # Determine time suffix based on order (1: AM, 2 or 3: PM)
                                        if leave.order == 1:
                                            time_suffix = " AM"
                                        else:
                                            time_suffix = " PM"

                                        start_time_str = f"{leave.start_time}{time_suffix}"
                                        end_time_str = f"{leave.end_time}{time_suffix}"

                                        leave_details.append({
                                            'Script_Option_Id':  loop.Script_Option_Id,
                                            'Script_Option_Type': 1,
                                            'Script_Option_Language':loop.Script_Option_Langauge,
                                            'Script_Option_Text': f"{start_time_str} to {end_time_str}",
                                            'Script_Option_Value': f"{start_time_str} to {end_time_str}",
                                            'Script_Option_Action_Script_Id': loop.Script_Option_Action_Script_Id,
                                            'Script_Code':  loop.Script_Code
                                        })

                                # Prepare response data with structured format
                                script_options = leave_details

                            else:
                                # No doctor leaves found, check doctor location availability for the day of the week
                                date = datetime.strptime(Script_Action_Input, "%d-%m-%Y").date()
                                day_of_week = date.weekday() + 1  # Monday is 0, so add 1 to match your day numbering

                                availabilities = Tbldoctorlocationavailability.objects.filter(
                                    doctor_id=doctor_id,
                                    availability_day=day_of_week
                                )

                                if availabilities.exists():
                                    availability_details = []
                                    for availability in availabilities:
                                        if availability.availability_starttime != 0 and availability.availability_endtime != 0:
                                            # Determine time suffix based on order (1: AM, 2 or 3: PM)
                                            if availability.availability_order == 1:
                                                time_suffix = " AM"
                                            else:
                                                time_suffix = " PM"

                                            start_time_str = f"{availability.availability_starttime}{time_suffix}"
                                            end_time_str = f"{availability.availability_endtime}{time_suffix}"

                                            availability_details.append({
                                                'Script_Option_Id':  loop.Script_Option_Id,
                                                'Script_Option_Type': 1,
                                                'Script_Option_Language': loop.Script_Option_Langauge,
                                                'Script_Option_Text': f"{start_time_str} to {end_time_str}",
                                                'Script_Option_Value': f"{start_time_str} to {end_time_str}",
                                                'Script_Option_Action_Script_Id': loop.Script_Option_Action_Script_Id,
                                                'Script_Code':  loop.Script_Code
                                            })

                                    # Prepare response data with structured format
                                    script_options = availability_details

                    #     //Add the logic from first api here which will prepare the Script_Options Object array
                    #     Data required for that code like Location_token can be found in this api parameter posted
                        
                    # else condtion to check is Sciprt_Option_type == and script_Option_Text {TIME_SLOTS}
                    #     //Add the logic from second api here which will prepare the scriot option obejct resArray
                    #     Data required for that code like location_token can be found in this api parameter and
                    #     Date required for that can be found under Script_Option_Value parameter to this API
                        
               
                serializer_scriptoptions = tblScriptOptionsSerializer(script_options, many=True)

                if serializer_scriptoptions.data:
                #    chat_script.Script_Options = serializer_scriptoptions.data
                    chat_script_data['Script_Options'] = serializer_scriptoptions.data

                #chat_scripts_data.append(chat_script_data)

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
    # script_type = body.get('script_type', "")
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
                {"Script_Code": 1, "Script_Type": 1, "Script_Language": "EN", "Script_Text": "<p>Greetings,</p>\n\n<p>We appreciate your reaching out to <strong>"+str(clinic_name)+"</strong>.</p>\n\n<p>I&#39;m a <strong>Virtual Receptionist</strong>,</p>\n\n<p>To assist you more effectively, could you kindly inform me <strong>What you are looking for </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Type": 1, "Script_Language": "HI", "Script_Text": "<p>नमस्ते,</p>\n\n<p><strong>"+str(hindi_clinic_name)+"</strong> से संपर्क करने के लिए धन्यवाद।</p>\n\n<p>मैं  एक<strong> व्हर्च्युअल रिसेप्शनिस्ट</strong> हूँ, </p>\n\n<p>आपकी अधिक प्रभावी ढंग से सहायता करने के लिए, क्या आप कृपया मुझे बता सकते हैं <strong>आप क्या खोज रहे हैं </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 1, "Script_Type": 1, "Script_Language": "MA", "Script_Text": "<p>नमस्कार,</p>\n\n<p><strong>"+str(marathi_clinic_name)+"</strong> ला संपर्क करण्याबद्दल आपले आभार।</p><p>मी एक <strong>व्हर्च्युअल रिसेप्शनिस्ट</strong> आहे,</p>\n\n<p>तुम्हाला अधिक प्रभावीपणे मदत करण्यासाठी, तुम्ही कृपया मला कळवू शकाल का <strong>तुम्ही काय शोधत आहात </strong>?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": 1, "Script_Language": "EN", "Script_Text": "<p>"+str(dr_name)+" Profile HTML</p><br/> </strong>Would you like to book an appointment?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": 1, "Script_Language": "HI", "Script_Text": "<p>"+str(hindi_dr_name)+" की प्रोफ़ाइल HTML</p><br/> </strong>क्या आप अपॉइंटमेंट बुक करना चाहेंगे?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 2, "Script_Type": 1, "Script_Language": "MA", "Script_Text": "<p>"+str(marathi_dr_name)+" यांचे प्रोफाइल HTML</p><br/> </strong>तुम्हाला भेटीची वेळ बुक करायची आहे का?</strong><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 3, "Script_Type": 0, "Script_Language": "EN", "Script_Text": "<p>Thank you<br/>If you need any more details or have any concerns you can contact "+str(dr_name)+" on <strong>+91 "+str(dr_contact_number)+"</strong></p><br/>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 3, "Script_Type": 0, "Script_Language": "HI", "Script_Text": "धन्यवाद<br/>यदि आपको अधिक जानकारी चाहिए या कोई चिंता है तो आप "+str(dr_name)+" से <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> पर संपर्क कर सकते हैं।", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 3, "Script_Type": 0, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद<br/>तुम्हाला आणखी काही तपशील हवे असल्यास किंवा काही समस्या असल्यास तुम्ही "+str(dr_name)+" यांच्याशी <strong>+91 "+str(dr_contact_number)+"</strong></p><br/> वर संपर्क साधू शकता.", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 4, "Script_Type": 1, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Date</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 4, "Script_Type": 1, "Script_Language": "HI", "Script_Text": "<p>अपनी <strong>मुलाकात की तारीख</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 4, "Script_Type": 1, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची तारीख</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 5, "Script_Type": 1, "Script_Language": "EN", "Script_Text": "<p>Choose your <strong>Appointment Time</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 5, "Script_Type": 1, "Script_Language": "HI", "Script_Text": "<p>अपना <strong>मिलने का समय</strong></p> चुनें", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 5, "Script_Type": 1, "Script_Language": "MA", "Script_Text": "<p>तुमची <strong>भेटण्याची वेळ</strong></p> निवडा", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
            
                {"Script_Code": 6, "Script_Type": 1, "Script_Language": "EN", "Script_Text": "<p>Who is the patient?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 6, "Script_Type": 1, "Script_Language": "HI", "Script_Text": "<p>रुग्ण कौन है?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 6, "Script_Type": 1, "Script_Language": "MA", "Script_Text": "<p>रुग्ण कोण आहे?</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 7, "Script_Type": 0, "Script_Language": "EN", "Script_Text": "<p>Thank you, Your appointment on {2-4-0} between {2-5-0} is  confirmed. Please note your token no. <strong></strong> </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 7, "Script_Type": 0, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, आपकी मुलाकात {2-5-0} के बीच {2-4-0} के लिए तय हो गई है। कृपया अपना टोकन नंबर नोट कर लें <strong></strong>। </p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 7, "Script_Type": 0, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, तुमची {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित झाली आहे. तुमचा टोकन क्र. <strong></strong> आहे.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 8, "Script_Type": 2, "Script_Language": "EN", "Script_Text": "<p>Please mention patient name</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 8, "Script_Type": 2, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का नाम बताएं</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 8, "Script_Type": 2, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचे नाव सांगा</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                {"Script_Code": 9, "Script_Type": 3, "Script_Language": "EN", "Script_Text": "<p>Please mention patient mobile no.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 9, "Script_Type": 3, "Script_Language": "HI", "Script_Text": "<p>कृपया मरीज का मोबाइल नंबर बताएं।</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 9, "Script_Type": 3, "Script_Language": "MA", "Script_Text": "<p>कृपया रुग्णाचा मोबाईल क्रमांक नमूद करा.</p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},

                
                {"Script_Code": 10, "Script_Type": 0, "Script_Language": "EN", "Script_Text": "<p>Thank you,  appointment for {2-8-0} on {2-4-0} between {2-5-0} is  confirmed. Please note the token no.<strong>=TOKEN</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 10, "Script_Type": 0, "Script_Language": "HI", "Script_Text": "<p>धन्यवाद, {2-8-0} के लिए {2-4-0} को {2-5-0} के बीच मिलना तय है। कृपया टोकन नंबर नोट कर लें। <strong>=TOKEN</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
                {"Script_Code": 10, "Script_Type": 0, "Script_Language": "MA", "Script_Text": "<p>धन्यवाद, {2-8-0} साठी {2-4-0} रोजी {2-5-0} दरम्यानची भेट निश्चित आहे. कृपया टोकन क्र. <strong>=TOKEN</strong></p>", "S1": 0, "S2": 0, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
 

                
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
               
               {"Script_Code": 5, "Script_Option_Type": 6, "Script_Option_Langauge": "EN", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 5, "Script_Option_Type": 6, "Script_Option_Langauge": "HI", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
               {"Script_Code": 5, "Script_Option_Type": 6, "Script_Option_Langauge": "MA", "Script_Option_Text": "{TIME_SLOTS}", "Script_Option_Value": None, "Script_Option_Action_Script_Id": 6, "created_on": None, "created_by": None, "last_modified_on": None, "last_modified_by": None, "deleted_by": None, "is_deleted": 0, "Location_token": location_token},
              
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