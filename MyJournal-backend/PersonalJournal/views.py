from django.http import JsonResponse
import json
from django.http import JsonResponse
from .models import PersonalJournal
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

''' 
GET: a list of dictionairies, one dictionary with journal posts 
POST: using request's body to create instance of PersonalJournal
DELETE: using ID for filtering and removal of instance
PUT: using ID to update correct instance with user entered field values
'''

@csrf_exempt
def journals_api(request): 
    if request.method=='GET':
        return JsonResponse({
            'journalPosts': [
                PersonalJournal.to_dict()
                for PersonalJournal in PersonalJournal.objects.all()
            ]
        })
    if request.method=='POST':
        response = json.loads(request.body)    
        header = response.get('journalheader')
        moodrating = response.get('journalmoodrating')
        content = response.get('journalcontent')
        water = response.get('dailyWaterIntake')
        fruits = response.get('dailyFruitsHad')
        journal_post = PersonalJournal(JournalHeader = header, JournalMoodRating = moodrating,
        JournalContent = content, JournalDailyWaterIntake = water, JournalDailyFruits = fruits)        
        journal_post.save()
        return JsonResponse({
            'new':[journal_post.to_dict()]
        })
        
    if request.method=='DELETE':
        response = json.loads(request.body)
        journal_id = response.get('journalid')
        PersonalJournal.objects.filter(id=journal_id).delete()
        return JsonResponse({
            'new':'deleted'
        })
    if request.method=='PUT':
        response = json.loads(request.body)    
        journal_id = response.get('journalid')
        header = response.get('journalheader')
        moodrating = response.get('journalmoodrating')
        content = response.get('journalcontent')
        water = response.get('dailyWaterIntake')
        fruits = response.get('dailyFruitsHad')
        PersonalJournal.objects.filter(id=journal_id).update(JournalHeader = header, 
        JournalMoodRating = moodrating, JournalContent = content, JournalDailyWaterIntake = water,
        JournalDailyFruits = fruits, LastModified = timezone.now())
        return JsonResponse({
            'new':'updated'
        })