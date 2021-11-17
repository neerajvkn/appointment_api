from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import applicant, interviewer

class post_slot(APIView):
    http_method_names = ['post', 'head']
    #function to enter/upadate data in db
    def post(self, request):
        args = request.data

        # checks if time slot is valid ( if hours are between 0 to 24 hours and begining is not greater or equal to end time)
        if ((args['slot_begining'] > args['slot_end'])) \
            or not (0 <= args['slot_begining'] <= 24) \
            or not (0 <= args['slot_end'] <= 24) \
            or (args['slot_begining'] == args['slot_end']) \
            or not isinstance(args['slot_begining'], int) or not isinstance(args['slot_end'], int):
            return Response( "Unacceptable time slot parameters" )

        if args['id_type'] == "applicant":

            #checks if the id is already in system, if it is, updates time slot else creates a new record
            obj, created = applicant.objects.update_or_create(
                id=args['id'],
                defaults={
                    "id_type" : args['id_type'],
                    "slot_begining" : args['slot_begining'],
                    "slot_end" : args['slot_end']
                }
            )
            action = "created" if created else "updated"
            response_data = ("applicant time slot entered "  + action)

        if args['id_type'] == "interviewer" :

            #checks if the id is already in system, if it is, updates time slot else creates a new record
            obj, created = interviewer.objects.update_or_create(
                id=args['id'],
                defaults={
                    "id_type" : args['id_type'],
                    "slot_begining" : args['slot_begining'],
                    "slot_end" : args['slot_end']
                }
            )
            action = "created" if created else "updated"
            response_data = ("interviewer time slot " + action)

        return Response( response_data )

class get_slot(APIView):
    http_method_names = ['get', 'head']
    # function to fetch given time and find slots for interviewer / applicant pair
    def get(self, request):
        args = request.data
        appl_obj = applicant.objects.get(id=args['appl_id'])
        intr_obj = interviewer.objects.get(id=args['intr_id'])

        min_begin = max(appl_obj.slot_begining, intr_obj.slot_begining ) # earliest time the interview can begin
        max_end = min(appl_obj.slot_end, intr_obj.slot_end ) # maximum time that interview can go upto

        if min_begin >= max_end:
            return Response("No time slots available",200)

        else:
            available_slots = []
            for i in range (min_begin, max_end):
                tup = (i, i+1)
                available_slots.append(tup) 

        return Response(available_slots,200)

