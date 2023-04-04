from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    # save the user data
    def register(self):
        self.save()

    # tries to retrieve the customer using the email address
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        
        except:
            return None
    # checks if the customer does exist and returns true else returns False
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False