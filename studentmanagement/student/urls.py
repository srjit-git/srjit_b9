from django.urls import path
from student import views
urlpatterns = [
   path('stu/',views.student,name='sh'),
   path('scon/',views.contact_st,name='sc'),
   path('sab/',views.about_st,name='sa'),
   path('add/',views.add_depart,name='add'),
   path('add_stud/',views.add_studnt,name='add_stud'),
   path('view_stud/',views.view_stud,name='view_stud'),
   path('delst/<int:d>',views.del_stud,name='del_stud'),
]