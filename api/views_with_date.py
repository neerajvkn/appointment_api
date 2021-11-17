from django.shortcuts import render

from django.http import HttpResponse, response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import applicant, interviewer, interviewer_dw, applicant_dw
from . serializers import interviewerSerializer, applicantSerializer
from rest_framework import permissions

import json
from datetime import datetime


class post_slot(APIView):
    http_method_names = ['post', 'head']
    def post(self, request):
        return post(self, request)


# class post(APIView):
#     http_method_names = ['post', 'head']
#     def post(self, request):
#         return post(self, request, "applicant")


class get_slot(APIView):
    http_method_names = ['get', 'head']
    def get(self, request):
        args = request.data
        appl_obj = applicant_dw.objects.filter(uid=args['appl_id'])
        intr_obj = interviewer_dw.objects.filter(uid=args['intr_id'])

        print(appl_obj)
        print(intr_obj)
        
        # min_begin = max(appl_obj.slot_begining, intr_obj.slot_begining )
        # max_end = min(appl_obj.slot_end, intr_obj.slot_end )

        # print("applicant slot begining : " + str(appl_obj.slot_begining))
        # print("interviewer slot begining : " + str(intr_obj.slot_begining))
        # print("min being is " + str(min_begin))
        # print("max end is " + str(max_end))

        # if min_begin >= max_end:
        #     response = "No time slots available"

        # else:
        #     available_slots = []
        #     for i in range (min_begin, max_end):
        #         print(i)
        #         tup = (i, i+1)
        #         print(type(tup))
        #         available_slots.append(tup) 
        #         print(available_slots)

        # print(available_slots)
        # data = json.dumps(available_slots)
        # print(data)
        # idt = json.loads(data)
        # print(idt)
        return Response("idt,200")

#function to enter/upadate data in db
def post(self, request):
    args = request.data
    skipped = []
    if args['id_type'] == "applicant":
        applicant_dw.objects.filter(uid=args['uid']).delete() #deletes all previous entries for the user
        for i in args['slot']:
            if datetime.strptime(i, "%d/%m/%Y") < datetime.now():    #skips if the date is not today or in future
                skipped.append(i)
            else:
                #checks if time slot is valid ( if hours are between 0 to 24 hours and begining is not greater or equal to end time)
                if ((args['slot'][i]['begin'] > args['slot'][i]['end'])) \
                    or not (0 <= args['slot'][i]['begin'] <= 24) \
                    or not (0 <= args['slot'][i]['end'] <= 24) \
                    or (args['slot'][i]['begin'] == args['slot'][i]['end']) \
                    or not isinstance(args['slot'][i]['begin'], int) or not isinstance(args['slot'][i]['end'], int):
                    skipped.append(i) #skips if the time slots are not proper
                else:
                    proper_date = datetime.strptime(i, "%d/%m/%Y").strftime('%Y-%m-%d')
                    print(proper_date)
                    applicant_dw.objects.create(uid=args['uid'], date=proper_date, slot_begining = args['slot'][i]['begin'], slot_end =args['slot'][i]['end'])
        return Response( "Applicant time slots updated" )
    
    if args['id_type'] == "interviewer":
        interviewer_dw.objects.filter(uid=args['uid']).delete() #deletes all previous entries for the user
        for i in args['slot']:
            if datetime.strptime(i, "%d/%m/%Y") < datetime.now():    #skips if the date is not today or in future
                skipped.append(i)
            else:
                #checks if time slot is valid ( if hours are between 0 to 24 hours and begining is not greater or equal to end time)
                if ((args['slot'][i]['begin'] > args['slot'][i]['end'])) \
                    or not (0 <= args['slot'][i]['begin'] <= 24) \
                    or not (0 <= args['slot'][i]['end'] <= 24) \
                    or (args['slot'][i]['begin'] == args['slot'][i]['end']) \
                    or not isinstance(args['slot'][i]['begin'], int) or not isinstance(args['slot'][i]['end'], int):
                    skipped.append(i) #skips if the time slots are not proper
                else:
                    proper_date = datetime.strptime(i, "%d/%m/%Y").strftime('%Y-%m-%d')
                    interviewer_dw.objects.create(uid=args['uid'], date = proper_date, slot_begining = args['slot'][i]['begin'], slot_end =args['slot'][i]['end'])
        return Response( "Interviewer time slots updated" )



    # #checks if time slot is valid ( if hours are between 0 to 24 hours and begining is not greater or equal to end time)
    # if ((args['slot_begining'] > args['slot_end'])) \
    #     or not (0 <= args['slot_begining'] <= 24) \
    #     or not (0 <= args['slot_end'] <= 24) \
    #     or (args['slot_begining'] == args['slot_end']) \
    #     or not isinstance(args['slot_begining'], int) or not isinstance(args['slot_end'], int):
    #     return Response( "Unacceptable time slot parameters" )

    # if args['id_type'] == "applicant":

    #     #checks if the id is already in system, if it is, updates time slot else creates a new record
    #     obj, created = applicant.objects.update_or_create(
    #         id=args['id'],
    #         defaults={
    #             "id_type" : args['id_type'],
    #             "slot_begining" : args['slot_begining'],
    #             "slot_end" : args['slot_end']
    #         }
    #     )
    #     action = "created" if created else "updated"
    #     response_data = ("applicant time slot entered "  + action)

    # if args['id_type'] == "interviewer" :

    #     #checks if the id is already in system, if it is, updates time slot else creates a new record
    #     obj, created = interviewer.objects.update_or_create(
    #         id=args['id'],
    #         defaults={
    #             "id_type" : args['id_type'],
    #             "slot_begining" : args['slot_begining'],
    #             "slot_end" : args['slot_end']
    #         }
    #     )
    #     action = "created" if created else "updated"
    #     response_data = ("interviewer time slot " + action)

    return Response( "response_data" )
