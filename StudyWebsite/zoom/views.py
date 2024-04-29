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
from django.contrib import messages



load_dotenv()  # take environment variables from .env


ACCOUNT_ID=os.environ.get("ACCOUNT_ID")
CLIENT_ID=os.environ.get("CLIENT_ID")
CLIENT_SECRET=os.environ.get("CLIENT_SECRET")


def create_zoom_meeting(payload):
    """Go to zoom documentation https://developers.zoom.us/docs/meeting-sdk/apis/#operation/meetingCreate"""
    client = ZoomClient(CLIENT_ID, CLIENT_SECRET,   api_account_id=ACCOUNT_ID)
    response = client.meeting.create(**payload)
    return response.json()




def create_zoom_meeting_view(request: HttpRequest, user_id, group_id):
    
    if request.method == 'POST':
        topic = request.POST["topic"]
        agenda = request.POST["agenda"]
        start_time = request.POST["start_time"].replace("T", " ")
        password = request.POST["password"]

        data = {
            'topic': topic,
            'agenda': agenda,
            'start_time': datetime.strptime(start_time, "%Y-%m-%d %H:%M"),
            'type': 2,
            'password': password,
            'timezone': "Asia/Riyadh",
            'user_id': "me",
        }

        try:
            response = create_zoom_meeting(data)
            start_url = response.get("start_url", "")
            join_url = response.get("join_url", "")

            user = User.objects.get(pk=user_id)
            group = StudyGroup.objects.get(pk=group_id)

            
            ZoomMeeting.objects.create(
                topic=topic,
                agenda=agenda,
                start_time=start_time,
                password=password,
                user=user,
                study_group=group,
                start_url=start_url,
                join_url=join_url
            )

            
            messages.success(request, "تم إنشاء الاجتماع بنجاح!")
           
            return redirect('main:group_dashboard_view', group_id=group_id, user_id=user_id)

        except Exception as e:
            messages.error(request, f"حدث خطأ: {e}")
            
            return redirect('main:not_found')  

    
    return render(request, "zoom/schedule_session.html", {"group_id" : group_id})

      

    
        # return render(request, "zoom/schedule_session.html", {
        #     'start_url': start_url,
        #     'join_url': join_url,
        # })






