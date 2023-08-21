from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.forms import MyCollectionForm, DeleteRecordForm
from app1.models import MyCollection
import uuid
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
import cv2
import os
import numpy as np
from django.http import HttpResponse
import face_recognition
import pymongo
import gridfs
import face_recognition
import glob
from django.core.mail import EmailMessage


@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def Record_Management(request):
    return render(request,'Record_Management.html')

def Crud(request):
    return render(request,'Crud.html')

def RecordManag(request):
    return render(request,'Crud.html')

def add_record(request):
    if request.method == 'POST':
        form = MyCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.file = request.FILES['CriminalPic']

            instance.record_id = str(uuid.uuid4())

            instance.save()
            messages.success(request, "Record added successfully!")
            return render(request, 'add_record.html', {'form': form})
    else:
        form = MyCollectionForm()
    return render(request, 'add_record.html', {'form': form})

def show_records(request):
    records = MyCollection.objects.all()
    return render(request, 'Crud.html', {'records': records})


def success(request):
    return HttpResponse("Record added successfully!")


def delete_record(request):
    form = DeleteRecordForm()
    success_message = None

    if request.method == 'POST':
        form = DeleteRecordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_id = data['record_id'].id
            try:
                record = MyCollection.objects.get(pk=record_id)
                record.delete()
                success_message = "Record deleted successfully."
            except MyCollection.DoesNotExist:
                error_message = "No record found with the given ID!"

    return render(request, 'delete_record.html', {'form': form, 'success_message': success_message})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:    
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        pin = request.POST.get('pin')

        if pin == '1234': # replace 1234 with your desired static PIN
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('Record_Management')
            else:
                messages.error(request, 'Invalid username or password.')
        elif pin == '':
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid PIN.')

    return render(request, 'login.html')


def mycollection(request):
    records = MyCollection.objects.all()
    context = {
        'records': records
    }
    return render(request, 'mycollection.html', context)


# This is working (Vertical) without Email

# def recognize_face(request):
#     def findEncodings(images):
#         encodeList = []
#         for img in images:
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             face_locations = face_recognition.face_locations(img)
#             if len(face_locations) > 0:
#                 encode = face_recognition.face_encodings(img, face_locations)[0]
#                 encodeList.append(encode)
#             else:
#                 print("No faces found in image")
#         return encodeList

#     # Load images from the database
#     records = MyCollection.objects.all()
#     images = [cv2.imread(str(record.CriminalPic.path)) for record in records]

#     encodeListKnown = findEncodings(images)

#     cap = cv2.VideoCapture(0)
#     # cap = cv2.VideoCapture('http://192.168.43.39/video')

#     while True:
#         success, img = cap.read()
#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

#         facesCurFrame = face_recognition.face_locations(imgS)
#         encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#         for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#             matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#             faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#             if len(faceDis) > 0:  # check if face distance array is not empty
#                 matchIndex = faceDis.argmin()
#                 if matches[matchIndex]:
#                     y1, x2, y2, x1 = faceLoc
#                     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Set the color to red
#                     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 250, 0), cv2.FILLED)

#                     # Fetch record related to the recognized face
#                     record = records[int(matchIndex)]
#                     criminal_name = record.CriminalName
#                     age = record.Age
#                     criminality = record.Criminality

#                     # Display text vertically
#                     text_lines = [criminal_name, f"Age: {age}", f"Criminality: {criminality}"]
#                     text_y = y2 - 6
#                     for line in text_lines:
#                         cv2.putText(img, line, (x1 + 6, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
#                         text_y -= 30

#                 else:
#                     x1, y1, x2, y2 = 0, 0, 0, 0  # Assign default values when no matches are found
#                     cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                                 (255, 255, 255), 2)


#         cv2.imshow('webcam', img)
#         if cv2.waitKey(10) == ord('s') or cv2.waitKey(10) == ord('S'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     return render(request, 'home.html')


# With Email but not EPS32



# UNI TRY

def recognize_face(request):
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(img)
            if len(face_locations) > 0:
                encode = face_recognition.face_encodings(img, face_locations)[0]
                encodeList.append(encode)
            else:
                print("No faces found in image")
        return encodeList

    # Load images from the database
    records = MyCollection.objects.all()
    images = [cv2.imread(str(record.CriminalPic.path)) for record in records]

    encodeListKnown = findEncodings(images)

    cap = cv2.VideoCapture(0)
    
    # cap = cv2.VideoCapture('http://192.168.18.168:81/stream')


    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        x1, y1, x2, y2 = 0, 0, 0, 0  # Initialize variables with default values

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            if len(faceDis) > 0:  # check if face distance array is not empty
                matchIndex = faceDis.argmin()
                if matches[matchIndex] and not request.session.get('email_sent', False):
                    # Only proceed if email hasn't been sent yet
                    # Fetch record related to the recognized face
                    record = records[int(matchIndex)]
                    criminal_name = record.CriminalName
                    age = record.Age
                    criminality = record.Criminality
                    CriminalPic = record.CriminalPic
                    # Send email alert
                    subject = 'Criminal Face Detected'
                    message = f"A criminal face has been detected.\n\nCriminal Name: {criminal_name}\nAge: {age}\nCriminality: {criminality}"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.user.email]  # Send email to the logged-in user's email address

                    email = EmailMessage(subject, message, email_from, recipient_list)
                    
                    image_path = os.path.join(settings.MEDIA_ROOT, str(CriminalPic))
                    # Attach the image to the email
                    with open(image_path, 'rb') as f:
                        email.attach_file(image_path, 'uploads/jpg')
                        
                    try:
                        email.send()
                        request.session['email_sent'] = True  # Set the flag in the session
                    except Exception as e:
                        print(f"An error occurred while sending the email: {str(e)}")


                    # Display text vertically
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Set the color to red
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 250, 0), cv2.FILLED)

                    # Display text vertically
                    text_lines = [criminal_name, f"Age: {age}", f"Criminality: {criminality}"]
                    text_y = y2 - 6
                    for line in text_lines:
                        cv2.putText(img, line, (x1 + 6, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1,
                                    cv2.LINE_AA)
                        text_y -= 30

                else:
                    cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 2)

        cv2.imshow('webcam', img)
        if cv2.waitKey(10) == ord('s') or cv2.waitKey(10) == ord('S'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'home.html')



def success(request):
    return HttpResponse("Record added successfully!")

def LogoutPage(request):    
    logout(request)
    return redirect('login')