from django.db import models
from django.contrib.auth.models import User
from openai import OpenAI
from django.db import transaction
from django.utils.crypto import get_random_string


client= OpenAI()


# Create your models here.
class Firm(models.Model):
    root_user= models.OneToOneField(User, on_delete= models.CASCADE, related_name='firms')
    
    name= models.CharField(max_length=100)
    address= models.TextField()
    contact_number= models.CharField(max_length=12, unique=True)
    email= models.EmailField(unique=True, null=True, blank=True)
    website_url= models.URLField(unique=True, null=True, blank=True)

    members= models.ManyToManyField(User)
    assistant_id = models.CharField(max_length=40,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return self.name

    def clean(self):
        super().clean()
        self.website_url= self.website_url.lower()

    def save(self, *args, **kwargs):
        is_being_created = self._state.adding
        super().save(*args, **kwargs)

        if is_being_created:
            assistant= client.beta.assistants.create(
                name=self.name,
                instructions="",
                tools=[{"type": "file_search"}],
                model="gpt-4o"
            )
            self.assistant_id= assistant.id
            self.save(update_fields=['assistant_id'])

            def add_member():
                    self.members.add(self.root_user)

            # https://stackoverflow.com/a/78053539/13953998
            transaction.on_commit(add_member)


def create_firm_invite():
    return get_random_string(10)

class FirmInvite(models.Model):
    firm= models.ForeignKey(Firm, on_delete=models.CASCADE)
    invite_code= models.CharField(max_length=20, default=create_firm_invite)
    email= models.EmailField(null=False, blank=False)
    accepted= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.firm)



class Entity(models.Model):
    firm= models.ForeignKey(Firm, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)

    industry_type=  models.IntegerField(choices=( (1, "Trading"), (2,"Manufacturing"), (3,"Service"), (4, "Others") ))
    entity_type= models.IntegerField(choices=( (1, "Huf"), (2,"Proprietary"), (3, "Partnership"), (4, "Corporation")  ))
    gstin= models.CharField(max_length=15 ,unique=True, blank=True, null=True)
    pan_number= models.CharField(max_length=10,blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
     

    def __str__(self):
        return str(self.firm)
    
    class Meta:
         verbose_name_plural ='Entities'