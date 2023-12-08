from django.db import models
'''
CharField for shorter header
TextField for longer journal post's content
LastModified updated when a PUT request is made
'''
class PersonalJournal(models.Model):
    JournalHeader = models.CharField(max_length=255, default='Journal Post Title', unique = False)
    JournalMoodRating = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=False)
    JournalContent = models.TextField(max_length=255, default='Journal Post Content', unique = False)
    JournalDailyWaterIntake = models.BooleanField(default=False, unique = False)
    JournalDailyFruits = models.BooleanField(default=False, unique = False)
    LastModified = models.DateTimeField(auto_now_add = True)

    # Mainly for improving view in admin page
    def __str__(self):
        modification = (self.LastModified).strftime('%m/%d/%Y %H:%M:%S')
        return '{} | {} | {} | {}'.format(modification, self.JournalHeader, self.JournalContent, self.JournalDailyWaterIntake)

    # Converting object to dictionary
    def to_dict(self):
        return {
            'id':self.id,
            'journalheader':self.JournalHeader,
            'journalmoodrating':self.JournalMoodRating,
            'journalcontent':self.JournalContent,
            'journaldailywaterintake':self.JournalDailyWaterIntake,
            'journaldailyfruits':self.JournalDailyFruits,
            'lastmodified':self.LastModified,
        }