from django.shortcuts import render
from.models import*
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from charityapp.models import tbl_donor  # Import your Donor model
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg = request.POST['msg']
        tbl_contact(name=name,email=email,phone=phone,msg=msg).save()
        return render(request,'index.html')
    else:
        return render(request,'contact.html')




    
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        var= tbl_donor.objects.all().filter(email=email, password=password,utype='user',status='approved')
        var2=tbl_receiver.objects.all().filter(email=email, password=password,status='approved')
        var3=tbl_donor.objects.all().filter(email=email,password=password,utype='admin')
        var4=tbl_deliverer.objects.all().filter(email=email,password=password)
        if var:
            for i in var:
                request.session['id'] = i.id
            return render(request,'donor/donor_home.html')

        elif var2:
            for i in var2:
                request.session['id'] = i.id
            return render(request,'receiver/receiver_home.html')
        
        elif var3:
            for i in var3:
                request.session['id'] = i.id
            return render(request,'admin/admin_home.html')
        
        elif var4:
            for i in var4:
                request.session['id'] = i.id
            return render(request,'deliverer/deliverer_home.html')
        else:
            txt = """<script>alert("Invalid user Credentials....");window.location='/';</script>"""
            return HttpResponse(txt)
           
    else:
        return render(request, 'login.html')

    
def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
        return render(request,'index.html')



    
    
    
    
    # ..........donor............
    

    
def donor_home(request):
        return render(request, 'donor/donor_home.html')


def donor_reg(request):
    registration_success = False 
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password = request.POST['password']
        tbl_donor(name=name, email=email, address=address, gender=gender, phone=phone, dob=dob, password=password, status='pending', utype='user').save()
        registration_success = True
    return render(request, 'donor_reg.html', {'registration_success': registration_success})
    
def donor_profile(request):
    id = request.session['id']
    data = tbl_donor.objects.all().filter(id=id)
    return render(request,'donor/donor_profile.html',{'data':data})


def edit_donorprofile(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        tbl_donor.objects.all().filter(id=id).update(name=name,email=email,address=address,gender=gender,phone=phone,dob=dob,password=password)
        return HttpResponseRedirect('/donor_profile/')
    else:
        nvar=tbl_donor.objects.all().filter(id=id)
        return render(request,'donor/edit_donorprofile.html',{'nvar':nvar})
    
    
def donor_food(request):
    registration_success=False
    if request.method == "POST":
        id = request.session['id']
        name=request.POST['name']
        if name == "Other":
            name = request.POST.get("otherfoodname")
        quantity=request.POST['quantity']
        expire=request.POST['expire']
        instance=tbl_donor.objects.get(id=id)
        tbl_FoodDonation(donor_id=instance,name=name,quantity=quantity,expire=expire,status='Available',fd_status='Pending').save()
        registration_success=True
        return render(request,'donor/donor_food.html',{'registration_success':registration_success})
    return render(request,'donor/donor_food.html',{'registration_success':registration_success})


def donor_funding(request):
    registration_success=False
    if request.method == "POST":
        id = request.session['id']
        name = request.POST['name']
        amount = request.POST['amount']
        date = request.POST['date']
        instance = tbl_donor.objects.get(id=id)
        tbl_funding(donor_id=instance,name=name,amount=amount,date=date,status='Available',fund_status='pending').save()
        registration_success=True
        return render(request,'donor/donor_funding.html',{'registration_success': registration_success})
    return render(request,'donor/donor_funding.html',{'registration_success': registration_success})


def donor_medicine(request):
    registration_success=False
    if request.method == "POST":
        id = request.session['id']
        name = request.POST['name']
        if name == "Other":
            name = request.POST.get('othermedicinename')
        quantity=request.POST['quantity']
        expire=request.POST['expire']
        instance = tbl_donor.objects.get(id=id)
        tbl_Medicine(donor_id=instance,name=name,quantity=quantity,expire=expire,status='Available',med_status='pending').save()
        registration_success=True
        return render(request,'donor/donor_medicine.html',{'registration_success': registration_success})
    return render(request,'donor/donor_medicine.html',{'registration_success': registration_success})


def donor_viewMessage(request):
    data = tbl_message.objects.order_by('-id').all()
    return render(request, 'donor/donor_viewMessage.html', {'data': data})



def donor_viewReceiverNeed(request):
    id = request.session['id']
    data=tbl_buyProduct.objects.all().filter(donor_id=id, status="pending").select_related('receiver_id','food_id','medicine_id','fund_id')
    return render(request,'donor/donor_viewReceiverNeed.html',{'data':data})

     
def admin_viewReceiverNeed(request):
    data=tbl_buyProduct.objects.all().select_related('receiver_id','food_id','medicine_id','fund_id')
    return render(request,'admin/admin_viewReceiverNeed.html',{'data':data})

        

        
        

    

        

       
    



# ......receiver.......



def receiver_home(request):
        return render(request,'receiver/receiver_home.html')


def receiver_reg(request):
    registration_success = False  # Initialize the variable

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password = request.POST['password']
        img = request.FILES['file']
        id_card = request.POST['id_card']
        account_detail = request.POST['account_detail']
        tbl_receiver(name=name, email=email, address=address, gender=gender, phone=phone, dob=dob, password=password, img=img, id_card=id_card, account_detail=account_detail, status='pending').save()
        registration_success = True
    return render(request, 'receiver_reg.html', {'registration_success': registration_success})
    
    
def receiver_profile(request):
        id=request.session['id']
        data=tbl_receiver.objects.all().filter(id=id)
        print("receiver...",data)
        return render(request,'receiver/receiver_profile.html',{'data':data}) 
    

def edit_receiverprofile(request,id):
    if request.method == 'POST':
                name=request.POST['name']
                email=request.POST['email']
                address=request.POST['address']
                gender=request.POST['gender']
                phone=request.POST['phone']
                dob=request.POST['dob']
                password=request.POST['password']
                id_card=request.POST['id_card']
                account_detail=request.POST['account_detail']
                try:
                    img_c = request.FILES['img']
                    fs = FileSystemStorage()
                    file = fs.save(img_c.name, img_c)
                except MultiValueDictKeyError:
                    file = tbl_receiver.objects.get(id=id).img

                tbl_receiver.objects.all().filter(id=id).update(name=name,email=email,address=address,gender=gender,phone=phone,dob=dob,password=password,img=file,id_card=id_card,account_detail=account_detail)
                return HttpResponseRedirect('/receiver_profile/')
    else:
        var=tbl_receiver.objects.all().filter(id=id)
        return render(request,'receiver/edit_receiverprofile.html',{'var':var})
    
def receiver_addmessage(request):
   
    if request.method == "POST":
        id = request.session['id']
        msg = request.POST['msg']
        instance = tbl_receiver.objects.get(id=id)
        tbl_message(receiver_id=instance,msg=msg).save()
        registration_success = True
        return render(request,'receiver/receiver_home.html')
    return render(request,'receiver/receiver_addmessage.html')

def receiver_viewFood(request):
    data=tbl_FoodDonation.objects.all().filter(fd_status="approved", status="Available")
    return render(request,'receiver/receiver_viewFood.html',{'data':data})  

def receiver_viewFund(request):
    data=tbl_funding.objects.all().filter(fund_status="approved", status="Available")
    return render(request,'receiver/receiver_viewFund.html',{'data':data})

def receiver_viewMedicine(request):
    data=tbl_Medicine.objects.all().filter(med_status="approved", status="Available")
    return render(request,'receiver/receiver_viewMedicine.html',{'data':data})
     
    
def receiver_getFood(request):
    id=request.GET['id']
    data=tbl_FoodDonation.objects.all().filter(id=id)
    return render(request,'receiver/receiver_buyFood.html',{'data':data})
        
        
        
def receiver_buyFood(request):
    if request.method == 'POST':
        try:
            id = request.session.get('id')
            idd = request.POST.get('id')
            dd = request.POST.get('donor_id')
            uid = tbl_receiver.objects.get(id=id)
            fid = tbl_FoodDonation.objects.get(id=idd)
            did = tbl_donor.objects.get(id=dd)
            quantity = int(request.POST['quantity'])
            
            if quantity > int(fid.quantity):  # Cast fid.quantity to int
                alert_message = 'Required quantity not available'
                return render(request, 'receiver/receiver_buyFood.html', {'alert_message': alert_message})

            # Deduct the purchased quantity from the available quantity
            fid.quantity = int(fid.quantity) - quantity  # Cast fid.quantity to int
            if fid.quantity == 0:
                fid.status = 'Unavailable'
            fid.save()

            # Save the purchase transaction
            tbl_buyProduct.objects.create(receiver_id=uid, donor_id=did, food_id=fid, quantity=quantity)
            
            # Alert message for successful purchase
            alert_message = 'Food bought successfully'
            return render(request, 'receiver/receiver_buyFood.html', {'alert_message': alert_message})
        except Exception as e:
            alert_message = 'An error occurred: ' + str(e)
            return render(request, 'receiver/receiver_buyFood.html', {'alert_message': alert_message})
    else:
        return render(request, 'receiver/receiver_buyFood.html')




       
def receiver_getMedicine(request):
    id=request.GET['id']
    data=tbl_Medicine.objects.all().filter(id=id)
    return render(request,'receiver/receiver_buyMedicine.html',{'data':data})



def receiver_buyMedicine(request):
    if request.method == 'POST':
        try:
            id = request.session.get('id')
            idd = request.POST.get('id')
            dd = request.POST.get('donor_id')
            quantity = int(request.POST['quantity'])
            
            uid = tbl_receiver.objects.get(id=id)
            fid = tbl_Medicine.objects.get(id=idd)
            did = tbl_donor.objects.get(id=dd)
            
            if quantity > fid.quantity:
                alert_message = 'Required quantity not available'
                return render(request, 'receiver/receiver_buyMedicine.html', {'alert_message': alert_message})

            # Update the quantity of medicine in the database
            fid.quantity -= quantity
            if fid.quantity == 0:
                fid.status = 'Unavailable'
            fid.save()

            # Save the purchase transaction
            tbl_buyProduct(receiver_id=uid, medicine_id=fid, donor_id=did, quantity=quantity).save()
            alert_message = 'Medicine bought successfully'
            return render(request, 'receiver/receiver_buyMedicine.html', {'alert_message': alert_message})
        except Exception as e:
            alert_message = 'An error occurred: ' + str(e)
            return render(request, 'receiver/receiver_buyMedicine.html', {'alert_message': alert_message})
    else:
        return render(request, 'receiver/receiver_buyMedicine.html')
    
    
    
def receiver_getFund(request):
    id=request.GET['id']
    data=tbl_funding.objects.all().filter(id=id)
    return render(request,'receiver/receiver_buyFund.html',{'data':data})


from django.shortcuts import render, redirect

def receiver_buyFund(request):
    if request.method == 'POST':
        # Check if 'id' key is present in the session
        if 'id' in request.session:
            id = request.session['id']
            print(id)
            f_id = request.POST.get('fund_id')
            dd = request.POST.get('donor_id')
            uid = tbl_receiver.objects.get(id=id)
            fid = tbl_funding.objects.get(id=f_id)
            did = tbl_donor.objects.get(id=dd)
            fid.status = 'Unavailable'
            quantity = fid.amount
            fid.save()
            tbl_buyProduct(receiver_id=uid, donor_id=did, fund_id=fid, quantity=quantity,status='pending').save()
            # tbl_FoodDonation.objects.filter(donor_id=id).update(status='Unavailable')

            return render(request, 'receiver/receiver_home.html')
        else:
            # Redirect to some page or handle the case where 'id' is not present in the session
            return render(request, 'receiver/receiver_home.html')  # You should replace 'login' with the actual URL for login
    else:
        return render(request, 'receiver/receiver_buyMedicine.html')

    
    
def receiver_ViewDelivery(request):
    data=tbl_deliverer.objects.all().filter(status='pending')
    return render(request,'receiver/receiver_ViewDelivery.html',{'data':data})


def receiver_needDeliverer(request):
    try:
        ii = request.GET.get('id')
        u_id = request.session.get('id')

        # Update tbl_deliverer
        tbl_deliverer.objects.filter(id=ii).update(status='pendings')

        # Create a new DeliverRequest
        DeliverRequest.objects.create(deliverer_id_id=ii, receiver_id_id=u_id, status='pending')

        print("New DeliverRequest created successfully.")
    except Exception as e:
        print(f"Error creating new DeliverRequest: {str(e)}")

    return redirect('/receiver_ViewDelivery/')
    
# def receiver_viewProcessedDeliverer(request):
#     r_id = request.session.get('id')
#     data=tbl_deliverer.objects.filter(status="started")
#     return render(request,'receiver/receiver_viewProcessedDeliverer.html',{'data':data})


def receiver_viewProcessedDeliverer(request):
    r_id = request.session.get('id')
    data = DeliverRequest.objects.filter(receiver_id__id=r_id) 
    return render(request, 'receiver/receiver_viewProcessedDeliverer.html', {'data': data})





    
    
    



    



    # ..........Admin............
    
    
def admin_home(request):
    return render(request,'admin/admin_home.html')


def admin_viewDonor(request):
    data = tbl_donor.objects.all().filter(status='pending')
    return render(request,'admin/admin_viewDonor.html',{'data':data})

def admin_viewReceiver(request):
    data = tbl_receiver.objects.all().filter(status='pending')
    return render(request,'admin/admin_viewReceiver.html',{'data':data})

def admin_approve_Donor(request):
    ii = request.GET['id']
    var = tbl_donor.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/admin_viewDonor/')


def admin_complete(request):
    ii = request.GET['id']
    var = tbl_buyProduct.objects.all().filter(id=ii).update(status='completed')
    return HttpResponseRedirect('/admin_viewReceiverNeed/')

def admin_reject_Donor(request):
    ii = request.GET['id']
    tbl_donor.objects.all().filter(id=ii).update(status='Rejected')
    return HttpResponseRedirect('/admin_viewDonor/')


def admin_approve_receiver(request):
    ii = request.GET['id']
    tbl_receiver.objects.all().filter(id=ii).update(status='approved')
    return HttpResponseRedirect('/admin_viewReceiver/')

def admin_reject_receiver(request):
    ii = request.GET['id']
    tbl_receiver.objects.all().filter(id=ii).update(status='Rejected')
    return HttpResponseRedirect('/admin_viewReceiver/')



def admin_viewFood(request):
    data=tbl_FoodDonation.objects.all().filter(fd_status='pending').select_related('donor_id')
    return render(request,'admin/admin_viewFood.html',{'data':data})

def admin_approve_food(request):
    ii = request.GET['id']
    tbl_FoodDonation.objects.all().filter(id=ii).update(fd_status='approved')
    return HttpResponseRedirect('/admin_viewFood/')

def admin_reject_food(request):
    ii = request.GET['id']
    tbl_FoodDonation.objects.all().filter(id=ii).update(fd_status='Rejected')
    return HttpResponseRedirect('/admin_viewFood/')


def admin_approve_fund(request):
    ii = request.GET['id']
    tbl_funding.objects.all().filter(id=ii).update(fund_status='approved')
    return HttpResponseRedirect('/admin_viewFund/')


def admin_reject_fund(request):
    ii = request.GET['id']
    tbl_funding.objects.all().filter(id=ii).update(fund_status='Rejected')
    return HttpResponseRedirect('/admin_viewFund/')


def admin_approve_medicine(request):
    ii = request.GET['id']
    tbl_Medicine.objects.all().filter(id=ii).update(med_status='approved')
    return HttpResponseRedirect('/admin_viewMedicine/')

def admin_reject_medicine(request):
    ii = request.GET['id']
    tbl_Medicine.objects.all().filter(id=ii).update(med_status='Rejected')
    return HttpResponseRedirect('/admin_viewMedicine/')

        
    
def admin_viewFund(request):
    data=tbl_funding.objects.all().filter(fund_status='pending').select_related('donor_id')
    return render(request,'admin/admin_viewFund.html',{'data':data})

def admin_viewMedicine(request):
    data=tbl_Medicine.objects.all().filter(med_status='pending').select_related('donor_id')
    return render(request,'admin/admin_viewMedicine.html',{'data':data})



def admin_deliverer(request):
    registration_success = False
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password = request.POST['password']
        
        tbl_deliverer(name=name, email=email, address=address, phone=phone, dob=dob, password=password,status='pending').save()
        registration_success = True
        
        # Redirect to a different page after successful registration
        return render(request, 'admin/admin_deliverer.html', {'registration_success': registration_success}) # Replace with the correct URL name

    return render(request, 'admin/admin_deliverer.html', {'registration_success': registration_success})
def admin_delete_deliverer(request, d_id):
    data = tbl_deliverer.objects.all().filter(id=d_id)
    data.delete()
    return render(request,'admin/admin_view_deliverers.html',{'data':data})
    
# def admin_receiverDelivery(request):
#     data = tbl_receiver.objects.all().filter(status='pending')
#     return HttpResponseRedirect('/admin_receiverDelivery/')




def admin_pendingDeliverer(request):
    # Retrieve all deliver requests with associated deliverer and receiver data
    deliver_requests_data = []
    for deliver_request in DeliverRequest.objects.all().filter(status='pending'):
        deliver_requests_data.append({
            'deliver_request': deliver_request,
            'deliverer_instance': deliver_request.deliverer_id,
            'receiver_instance': deliver_request.receiver_id,
        })

    return render(request, 'admin/admin_pendingDeliverer.html', {'user_data': deliver_requests_data})
    
# def admin_pendingDeliverer(request):
#     # Fetch tbl_deliverer data with 'pendings' status
#     deliverer_data = tbl_deliverer.objects.filter(status='pendings')

#     # Fetch user details who made DeliverRequest
#     user_data = []
#     for deliverer_instance in deliverer_data:
#         # Filter DeliverRequest instances matching the current deliverer_instance
#         deliver_requests = DeliverRequest.objects.filter(deliverer_id=deliverer_instance)

#         # Only consider the first matching DeliverRequest, if any
#         deliver_request = deliver_requests.first()

#         user_data.append({
#             'deliverer_instance': deliverer_instance,
#             'receiver_instance': deliver_request.receiver_id if deliver_request else None,
#         })

#     return render(request, 'admin/admin_pendingDeliverer.html', {'user_data': user_data})



# def admin_alocateDeliverer(request):
#     ii = request.GET['id']
#     tbl_deliverer.objects.all().filter(id=ii).update(status='started')
#     return HttpResponseRedirect('/admin_pendingDeliverer/')
def admin_alocateDeliverer(request):
    deliverer_id = request.GET.get('id')

    # Fetch the tbl_deliverer instance
    deliverer_instance = get_object_or_404(tbl_deliverer, id=deliverer_id)

    # Update status of tbl_deliverer
    deliverer_instance.status = 'started'
    deliverer_instance.save()

    # Fetch the associated DeliverRequest
    try:
        deliver_request = DeliverRequest.objects.filter(deliverer_id=deliverer_instance).first()
    except MultipleObjectsReturned:
        # Handle the case where multiple DeliverRequest instances are found
        deliver_request = None

    if deliver_request:
        # Update status of DeliverRequest
        deliver_request.status = 'started'
        deliver_request.save()

    # Additional logic if needed

    return redirect('admin_pendingDeliverer')

def admin_viewprocessedList(request):
    data = tbl_deliverer.objects.all().filter(status='started')
    return render(request,'admin/admin_viewprocessedList.html',{'data':data})


def admin_completeDeliverer(request):
    ii = request.GET['id']
    tbl_deliverer.objects.all().filter(id=ii).update(status='pending')
    return HttpResponseRedirect('/admin_viewprocessedList/')

def admin_viewDcompletedlist(request):
    data = tbl_deliverer.objects.all().filter(status='completed')
    return render(request,'admin/admin_viewDcompletedlist.html',{'data':data})

def admin_view_deliverers(request):
    data = tbl_deliverer.objects.all()
    return render(request,'admin/admin_view_deliverers.html',{'data':data})


def deliverer_home(request):
        return render(request, 'deliverer/deliverer_home.html')
    
def deliverer_pendingDeliveries(request):
    d_id = request.session.get('id')
    
    # Fetch all DeliverRequest instances for the current deliverer with 'pending' status
    deliver_requests = DeliverRequest.objects.filter(deliverer_id=d_id, status="pending")

    # Get the corresponding deliverer instance
    deliverer_instance = tbl_deliverer.objects.get(id=d_id)

    # Create a list of dictionaries containing deliverer and receiver instances
    user_data = [{'deliverer_instance': deliverer_instance, 'receiver_instance': deliver_request.receiver_id}
                 for deliver_request in deliver_requests]

    return render(request, 'deliverer/deliverer_pendingDeliveries.html', {'user_data': user_data})



    




    

    
    

