#I am using
from zoomus import ZoomClient
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import ZoomMeeting
from main.models import StudyGroup
from django.contrib.auth.models import User



load_dotenv()  # take environment variables from .env


ACCOUNT_ID=os.environ.get("ACCOUNT_ID")
CLIENT_ID=os.environ.get("CLIENT_ID")
CLIENT_SECRET=os.environ.get("CLIENT_SECRET")


def create_zoom_meeting(payload):
    """Go to zoom documentation https://developers.zoom.us/docs/meeting-sdk/apis/#operation/meetingCreate"""
    client = ZoomClient(CLIENT_ID, CLIENT_SECRET,   api_account_id=ACCOUNT_ID)
    response = client.meeting.create(**payload)
    return response.json()



def create_zoom_meeting_view(request:HttpRequest,user_id, group_id):
    #create the meeting
    if request.method == 'POST':
        topic = request.POST["topic"]
        agenda = request.POST["agenda"]
        start_time = request.POST["start_time"].replace("T", " ")
        password = request.POST["password"]

        #ensure the all required values are valid and formated as per zoom documentation
        data = {
            'topic': topic,
            'agenda': agenda,
            'start_time': datetime.strptime(start_time, "%Y-%m-%d %H:%M"),
            'type': 2,
            'password' : password,
            'timezone' : "Asia/Riyadh",
            'user_id': "me",
        }

        try:
            response = create_zoom_meeting(data)

        except TypeError as e:
            print("حدث خطأ:", e)

        start_url = response.get("start_url", "")
        join_url = response.get("join_url", "")

        user = User.objects.get(pk=user_id)
        group = StudyGroup.objects.get(pk=group_id)

        try:
            session = ZoomMeeting(
                topic = topic,
                agenda = agenda,
                start_time = start_time,
                password = password,
                user = user,
                study_group =group,
                start_url = start_url,
                join_url = join_url
            )
            session.save()
        except Exception as e:
            print(e)
    return render(request, "zoom/schedule_session.html")
      

    
        # return render(request, "zoom/schedule_session.html", {
        #     'start_url': start_url,
        #     'join_url': join_url,
        # })






