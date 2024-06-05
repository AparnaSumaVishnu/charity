from django.db import models

class tbl_donor(models.Model):
    name=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=100,default='')
    dob=models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=100,default='')
    status= models.CharField(max_length=100,default='')
    utype=models.CharField(max_length=100,default='')
    
class tbl_receiver(models.Model):
    name = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    dob = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100,default='')
    gender = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=128,default='')
    phone = models.CharField(max_length=15,default='')
    id_card = models.CharField(max_length=20,default='')
    img = models.ImageField(upload_to='user_images/')
    donor_id = models.ForeignKey(tbl_donor, on_delete=models.CASCADE, blank=True, null=True) 
    account_detail = models.CharField(max_length=100,default='')
    status= models.CharField(max_length=100,default='')

    
class tbl_FoodDonation(models.Model):
    donor_id = models.ForeignKey(tbl_donor, on_delete=models.CASCADE, blank=True, null=True) 
    name = models.CharField(max_length=100,default='')
    expire = models.CharField(max_length=100,default='')
    quantity = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100,default='')
    fd_status=models.CharField(max_length=100,default='')
 
    
    
class tbl_funding(models.Model):
    name = models.CharField(max_length=100,default='')
    donor_id = models.ForeignKey(tbl_donor, on_delete=models.CASCADE, blank=True, null=True) 
    amount = models.IntegerField(max_length=100, default='')
    date = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100,default='')
    fund_status=models.CharField(max_length=100,default='')

    
    
class tbl_Medicine(models.Model):
    donor_id = models.ForeignKey(tbl_donor, on_delete=models.CASCADE, blank=True, null=True) 
    name = models.CharField(max_length=100,default='')
    quantity = models.IntegerField(max_length=100,default='')
    expire = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100,default='')
    med_status=models.CharField(max_length=100,default='')


    
    
class tbl_message(models.Model):
    receiver_id = models.ForeignKey(tbl_receiver, on_delete=models.CASCADE, blank=True, null=True) 
    msg=models.CharField(max_length=100,default='')
    
    


class tbl_buyProduct(models.Model):
    receiver_id = models.ForeignKey(tbl_receiver, on_delete=models.CASCADE, blank=True, null=True) 
    food_id = models.ForeignKey(tbl_FoodDonation, on_delete=models.CASCADE, blank=True, null=True) 
    medicine_id = models.ForeignKey(tbl_Medicine, on_delete=models.CASCADE, blank=True, null=True) 
    fund_id = models.ForeignKey(tbl_funding, on_delete=models.CASCADE, blank=True, null=True) 
    donor_id= models.ForeignKey(tbl_donor, on_delete=models.CASCADE, blank=True, null=True) 
    quantity = models.IntegerField(max_length=100,default='')
    status = models.CharField(max_length=100,default='pending')
    
    
class tbl_deliverer(models.Model):
    name = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    dob = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    status = models.CharField(max_length=100,default='')
    # receiver_id = models.ForeignKey(tbl_receiver, on_delete=models.CASCADE, blank=True, null=True) 


class tbl_contact(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    msg=models.CharField(max_length=100,default='')

class DeliverRequest(models.Model):
    deliverer_id = models.ForeignKey(tbl_deliverer, on_delete=models.CASCADE, blank=True, null=True)
    receiver_id = models.ForeignKey(tbl_receiver, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=100,default='')

    




    
    
 

    
    

    
    
   

# class tbl_admin(models.Model):
#     email = models.CharField(max_length=100,default='')
#     password = models.CharField(max_length=128,default='')




