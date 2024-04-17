from django.urls import path

from myapp import views

urlpatterns=[



    path('login/',views.login),
    path('login_post/',views.login_post),
    path('Admin_home/',views.Admin_home),
    path('Change_Password/',views.Change_Password),
    path('Change_Password_post/',views.Change_Password_post),
    path('Recycle_Verify/',views.Recycle_Verify),
    path('Recycle_Verify_post/',views.Recycle_Verify_post),
    path('Approve_rec_unit/<id>',views.Approve_rec_unit),
    path('Reject_rec_unit/<id>', views.Reject_rec_unit),
    path('View_Approved_unit/',views.View_Approved_unit),
    path('View_Approved_unit_post/',views.View_Approved_unit_post),
    path('View_Rejected_unit/',views.View_Rejected_unit),
    path('View_Rejected_unit_post/',views.View_Rejected_unit_post),
    path('Reject_again_rec_unit/<id>',views.Reject_again_rec_unit),
    path('Waste_Rate/',views.Waste_Rate),
    path('Waste_Rate_post/',views.Waste_Rate_post),
    path('Add_waste/', views.Add_waste),
    path('Add_waste_post/', views.Add_waste_post),
    path('View_waste/', views.View_waste),
    path('View_waste_post/', views.View_waste_post),
    path('delete_waste/<id>', views.delete_waste),
    path('Update_waste/<id>', views.Update_waste),
    path('Update_waste_post/', views.Update_waste_post),

    path('Worker_Verify/',views.Worker_Verify),
    path('Worker_Verify_post/',views.Worker_Verify_post),
    path('Approve_worker/<id>',views.Approve_worker),
    path('Reject_worker/<id>',views.Reject_worker),

    path('Pickup_Verify/',views.Pickup_Verify),
    path('Pickup_Verify_post/',views.Pickup_Verify_post),
    path('Approve_Pickup/<id>',views.Approve_pickup),
    path('Reject_Pickup/<id>', views.Reject_pickup),
    path('View_Approved_Pickup/',views.View_Approved_pickup),
    path('View_Approved_Pickup_post/',views.View_Approved_pickup_post),
    path('View_Rejected_Pickup/',views.View_Rejected_pickup),
    path('View_Rejected_Pickup_post/',views.View_Rejected_pickup_post),
    path('Approve_again_pickup/<id>',views.Approve_again_pickup),
    path('Reject_again_pickup/<id>',views.Reject_again_pickup),

    path('View_Rejected_worker/',views.View_Rejected_worker),
    path('View_Rejected_worker_post/',views.View_Rejected_worker_post),
    path('View_Approved_worker/',views.View_Approved_worker),
    path('View_Approved_worker_post/',views.View_Approved_worker_post),
    path('Approve_again_worker/<id>',views.Approve_again_worker),
    path('Reject_again_worker/<id>',views.Reject_again_worker),

    path('Approve_again_rec_unit/<id>',views.Approve_again_rec_unit),
    path('View_Area/',views.View_Area),
    path('View_Area_post/',views.View_Area_post),
    path('delete_Area/<id>', views.delete_Area),
    path('Add_Area/',views.Add_Area),
    path('Add_Area_post/',views.Add_Area_post),
    path('Update_Area/<id>',views.Update_Area),
    path('Update_Area_post/',views.Update_Area_post),
    path('View_Alloc/',views.View_Alloc),
    path('View_Alloc_post/',views.View_Alloc_post),
    path('delete_Alloc/<id>', views.delete_Alloc),
    path('Allocate/<id>',views.Allocate),
    path('Allocate_post/',views.Allocate_post),
    path('View_User/',views.View_User),
    path('View_User_post/',views.View_User_post),
    path('Add_Category/',views.Add_Category),
    path('Add_Category_post/',views.Add_Category_post),
    path('View_Category/',views.view_cat),
    path('View_Category_post/',views.View_Category_post),
    path('delete_category/<id>', views.delete_category),
    path('Update_Category/<id>',views.Update_Category),
    path('Update_Category_post/',views.Update_Category_post),
    path('View_Complaint/',views.View_Complaint),
    path('View_Complaint_post/',views.View_Complaint_post),
    path('Send_Reply/<id>',views.Send_Reply),
    path('Send_Reply_post/',views.Send_Reply_post),
    path('Feedback/',views.Feedback),
    path('Feedback_post/',views.Feedback_post),
# _______________________________________________________________________________________________________________________
    path('Recycle_Signup/',views.Recycle_Signup),
    path('Recycle_Signup_post/',views.Recycle_Signup_post),

    path('recycle_home/',views.recycle_home),

    path('recycle_Change_Password/',views.recycle_Change_Password),
    path('recycle_Change_Password_post/',views.recycle_Change_Password_post),

    path('View_Profile/',views.View_Profile),
 #   path('View_Profile_post/',views.View_Profile_post),

    path('Edit_Profile/<id>',views.Edit_Profile),
    path('Edit_Profile_post/',views.Edit_Profile_post),

    path('View_Req/',views.View_Req),
    path('View_Req_post/',views.View_Req_post),

    path('Add_Product/',views.Add_Product),
    path('Add_Product_post/',views.Add_Product_post),

    path('View_Product/',views.View_Product),
    path('View_Product_post/',views.View_Product_post),

    path('Update_Product/<id>',views.Update_Product),
    path('Update_Product_post/',views.Update_Product_post),

    path('delete_Product/<id>',views.delete_Product),

    path('Profit_Donation/',views.Profit_Donation),
    path('Profit_Donation_post/',views.Profit_Donation_post),

    path('View_Donation/',views.View_Donation),
    path('View_Donation_post/',views.View_Donation_post),

    path('View_Product_Order/',views.View_Product_Order),
    path('View_Product_Order_post/',views.View_Product_Order_post),


##############################################3worker


    path('Worker_Signup/',views.Worker_Signup),
    path('and_Login/',views.and_Login),
    path('Worker_Profile/',views.Worker_Profile),
    path('pickup_changepass/', views.pickup_changepass),
    path('Edit_Worker_Profile/',views.Edit_Worker_Profile),
    path('View_User_rqst/',views.View_User_rqst),
    path('View_Alloc_Area/',views.View_Alloc_Area),
    path('view_category/',views.view_category),
    path('worker_view_user_waste_request/',views.worker_view_user_waste_request),
    path('worker_add_qntty/',views.worker_add_qntty),

###########################################################user


    path('User_signup/',views.User_signup),
    path('User_Login/',views.User_Login),
    path('User_Change_Password/',views.User_Change_Password),
    path('View_profile/',views.View_profile),
    path('User_edit_Profile/', views.User_edit_Profile),
    path('User_complaint/',views.User_complaint),
    path('view_Reply/',views.view_Reply),
    path('User_feedbacks/',views.User_feedbacks),
    path('View_wrk_category/',views.View_wrk_category),
    path('user_work_request/',views.user_work_request),
    path('user_view_product/',views.user_view_product),
    path('Cart/',views.Cart_),
    # path('View_cart/',views.View_cart),
    path('delete_Cart/',views.delete_Cart),
    path('View_worker_ntfy/',views.View_worker_ntfy),
    path('u_add_to_cart/',views.u_add_to_cart),
    path('view_cart/',views.view_cart),
    path('remove_cart/',views.remove_cart),
    path('user_payment/',views.user_payment),
    path('view_notification/',views.view_notification),
    path('View_order_status/',views.View_order_status),
    path('View_order_sub_status/',views.View_order_sub_status),


###########################################################pickup

    path('pickup_signup/', views.pickup_signup),
    path('pickup_changepass/', views.pickup_changepass),
    path('Pickup_Profile/', views.Pickup_Profile),
    path('pickup_edit_Profile/', views.pickup_edit_Profile),
    path('view_Waste_collect/', views.view_Waste_collect),
    path('view_user_waste/', views.view_user_waste),
    path('view_user_waste_request/', views.view_user_waste_request),
    path('user_waste_request/', views.user_waste_request),



    path('pickup_add_qntty/', views.pickup_add_qntty),
    path('user_make_payment/', views.user_make_payment),



]