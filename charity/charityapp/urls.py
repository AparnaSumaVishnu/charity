from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.index),
    path('donor_reg/',views.donor_reg),
    path('receiver_reg/',views.receiver_reg),
    path('login/',views.login),
    path('logout/',views.logout),
    path('contact/',views.contact),
    
    
    
    path('donor_home/',views.donor_home),
    path('donor_profile/',views.donor_profile),
    path('edit_donorprofile/<int:id>/',views.edit_donorprofile,name="edit_donorprofile"),
    path('donor_food/',views.donor_food),
    path('donor_funding/',views.donor_funding),
    path('donor_medicine/',views.donor_medicine),
    path('donor_viewMessage/',views.donor_viewMessage),
    path('donor_viewReceiverNeed/',views.donor_viewReceiverNeed),
    
    
    path('receiver_home/',views.receiver_home),
    path('receiver_profile/',views.receiver_profile),
    path('edit_receiverprofile/<int:id>/',views.edit_receiverprofile,name="edit_receiverprofile"),
    path('receiver_addmessage/',views.receiver_addmessage),
    path('receiver_viewFood/',views.receiver_viewFood),
    path('receiver_viewFund/',views.receiver_viewFund),
    path('receiver_viewMedicine/',views.receiver_viewMedicine),
    path('receiver_getFood/',views.receiver_getFood),
    path('receiver_buyFood/',views.receiver_buyFood),
    path('receiver_getMedicine/',views.receiver_getMedicine,name='receiver_getMedicine'),
    path('receiver_buyMedicine/',views.receiver_buyMedicine),
    path('receiver_getFund/',views.receiver_getFund),
    path('receiver_buyFund/',views.receiver_buyFund),
    path('receiver_ViewDelivery/',views.receiver_ViewDelivery),
    path('receiver_needDeliverer/',views.receiver_needDeliverer),
    path('receiver_viewProcessedDeliverer/',views.receiver_viewProcessedDeliverer),

    
    
    
    path('admin_home/',views.admin_home),
    path('admin_viewDonor/',views.admin_viewDonor),
    path('admin_viewReceiver/',views.admin_viewReceiver),
    path('admin_approve_Donor/',views.admin_approve_Donor),
    path('admin_approve_receiver/',views.admin_approve_receiver),
    path('admin_viewFood/',views.admin_viewFood),
    path('admin_viewFund/',views.admin_viewFund),
    path('admin_viewMedicine/',views.admin_viewMedicine),
    path('admin_deliverer/',views.admin_deliverer),
    path('admin_view_deliverers/',views.admin_view_deliverers,name="admin_view_deliverers"),
    path('admin_delete_deliverer/<int:d_id>/',views.admin_delete_deliverer),
    path('admin_pendingDeliverer/',views.admin_pendingDeliverer,name='admin_pendingDeliverer'),
    path('admin_alocateDeliverer/',views.admin_alocateDeliverer),
    path('admin_viewprocessedList/',views.admin_viewprocessedList),
    path('admin_completeDeliverer/',views.admin_completeDeliverer),
    path('admin_viewDcompletedlist/',views.admin_viewDcompletedlist),
    path('admin_reject_Donor/',views. admin_reject_Donor),
    path('admin_reject_receiver/',views.admin_reject_receiver),
    path('admin_approve_food/',views.admin_approve_food),
    path('admin_reject_food/',views.admin_reject_food),
    path('admin_approve_fund/',views.admin_approve_fund),
    path('admin_reject_fund/',views.admin_reject_fund),
    path('admin_approve_medicine/',views.admin_approve_medicine),
    path('admin_reject_medicine/',views.admin_reject_medicine),
    path('admin_viewReceiverNeed/',views.admin_viewReceiverNeed),
    path('admin_complete/',views.admin_complete),


    path('deliverer_home/',views.deliverer_home),
     path('deliverer_pendingDeliveries/',views.deliverer_pendingDeliveries),



    

   
]
    

