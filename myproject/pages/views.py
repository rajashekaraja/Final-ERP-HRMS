from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
from django.conf import settings

import json

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def save_employee(request):
    if request.method == 'POST':
        # Extract form data
        firstname = request.POST.get('firstname')
        midname = request.POST.get('midname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        dob=request.POST.get('dob')
        doj=request.POST.get('doj')
        employment_type=request.POST.get('employment_type')
        create_user=request.POST.get('create_user')
        offerdate=request.POST.get('offerdate')
        confirmationdate=request.POST.get('confirmationdate')
        contractenddate=request.POST.get('contractenddate')
        dateofretirement=request.POST.get('dateofretirement')
        notice=request.POST.get('notice')
        company=request.POST.get('company')
        designation=request.POST.get('designation')
        branch=request.POST.get('branch')
        department=request.POST.get('department')
        reports_to=request.POST.get('reports_to')
        grade=request.POST.get('grade')
        annual_leave=request.POST.get('annual_leave')
        sick_leave=request.POST.get('sick_leave')
        maternity_leave=request.POST.get('maternity_leave')
        paternity_leave=request.POST.get('paternity_leave')
        other_leave=request.POST.get('other_leave')
        salary_amount=request.POST.get('salary_amount')
        salary_payment_mode=request.POST.get('salary_payment_mode')
        mobile_number=request.POST.get('mobile_number')
        current_address=request.POST.get('current_address')
        permanent_address=request.POST.get('permanent_address')
        personal_email=request.POST.get('personal_email')
        company_email=request.POST.get('company_email')
        preferred_email=request.POST.get('preferred_email')
        parent_name=request.POST.get('parent_name')
        parent_occupation=request.POST.get('parent_occupation')
        spouse_name=request.POST.get('spouse_name')
        spouse_occupation=request.POST.get('spouse_occupation')
        children_names=request.POST.get('children_names')
        passport_issue_date=request.POST.get('passport_issue_date')
        passport_place_of_issue=request.POST.get('passport_place_of_issue')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        allergies=request.POST.get('allergies')
        medical_concerns=request.POST.get('medical_concerns')
        exit_status=request.POST.get('exit_status')
        relieving=request.POST.get('relieving')  
        resignation=request.POST.get('resignation')
        exit_interview=request.POST.get('exit_interview')
        leave_encashment=request.POST.get('leave_encashment')
        emergency_contact=request.POST.get('emergency_contact')
        health_insurance=request.POST.get('health_insurance')
        personal_bio=request.POST.get('personal_bio')
        company_history=request.POST.get('company_history')

        educational_details_json=request.POST.get('educational_details')
        educational_details=json.loads(educational_details_json) if educational_details_json else []

        workExperience_details_json=request.POST.get('workExperience_details')
        workExperience_details=json.loads(workExperience_details_json) if workExperience_details_json else []
        
        # Extract other form fields similarly
        
        # Connect to MongoDB
        client = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
        db = client[settings.MONGO_DB_NAME]
        collection = db['employees']
        
        # Insert data into MongoDB
        employee_data = {
            'first_name': firstname,
            'middle_name': midname,
            'last_name': lastname,
            'gender': gender,
            'date_of_birth' : dob,
            'date_of_joining' : doj,
            'employment_type' : employment_type,
            'create_user' : create_user,
            'offer_date' : offerdate,
            'confirmation_date' : confirmationdate,
            'contract_end_date' : contractenddate,
            'date_of_retirement' : dateofretirement,
            'notice' : notice,
            'company' : company,
            'designation' : designation,
            'branch' : branch,
            'department' : department,
            'reports_to' : reports_to,
            'grade' : grade,
            'annual_leave' : annual_leave,
            'sick_leave' : sick_leave,
            'maternity_leave' : maternity_leave,
            'paternity_leave' : paternity_leave,
            'other_leave' : other_leave,
            'salary_amount' : salary_amount,
            'salary_payment_mode' : salary_payment_mode,
            'mobile_number' : mobile_number,
            'current_address' : current_address,
            'permanent_address' : permanent_address,
            'personal_email' : personal_email,
            'company_email' : company_email,
            'preferred_email' : preferred_email,
            'parent_name' : parent_name,
            'parent_occupation' : parent_occupation,
            'spouse_name' : spouse_name,
            'spouse_occupation' : spouse_occupation,
            'children_names' : children_names,
            'passport_issue_date' : passport_issue_date,
            'passport_place_of_issue' : passport_place_of_issue,
            'height' : height,
            'weight' : weight,
            'allergies' : allergies,
            'medical_concerns' : medical_concerns,
            'exit_status' : exit_status,
            'relieving' : relieving,
            'resignation' : resignation,
            'exit_interview' : exit_interview,
            'leave_encashment' : leave_encashment,
            'emergency_contact' : emergency_contact,
            'health_insurance' : health_insurance,
            'personal_bio' : personal_bio,
            'company_history' : company_history,

            'educational_details' : educational_details,
            'workExperience_details' : workExperience_details,
            # Add other fields here
        }
        result = collection.insert_one(employee_data)
        
        if result.inserted_id:
            return HttpResponse('Employee saved successfully')
        else:
            return HttpResponse('Failed to save employee')
    else:
        return HttpResponse('Invalid request method')