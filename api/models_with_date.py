from django.db import models

class interviewer_dw(models.Model): #dw = datewise
    uid = models.CharField(max_length=10)
    date = models.DateField()
    slot_begining = models.IntegerField()
    slot_end = models.IntegerField()
    def __str__(self):
        return ret_str(self)

class applicant_dw(models.Model): #dw = datewise
    uid = models.CharField(max_length=10)
    date = models.DateField()
    slot_begining = models.IntegerField()
    slot_end = models.IntegerField()
    def __str__(self):
        return ret_str(self)






class interviewer(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    id_type = models.CharField(max_length=10)
    slot_begining = models.IntegerField()
    slot_end = models.IntegerField()

    def __str__(self):
        return ret_str(self)

class applicant(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    id_type = models.CharField(max_length=10)

    slot_begining = models.IntegerField()
    slot_end = models.IntegerField()

    def __str__(self):
        return ret_str(self)

def ret_str(self):
    r_data =  """ id : %(id)s , \n slot_begining" : %(slot_begining)s,\n slot_end : %(slot_end)s
                """%{"id" : self.id,
                    "slot_begining" : self.slot_begining,
                    "slot_end" : self.slot_end}
    return str(r_data)