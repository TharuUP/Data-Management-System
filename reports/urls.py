from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('complaint/add/', views.add_complaint, name='add_complaint'),
    path('class-change/add/', views.add_class_change, name='add_class_change'),
    path('complaints/', views.complaint_list, name='complaint_list'),
    path('class-changes/', views.class_change_list, name='class_change_list'),
    path('complaints/export-pdf/', views.export_complaints_pdf, name='export_complaints_pdf'),
    path('complaints/<int:pk>/edit/', views.edit_complaint, name='edit_complaint'),
    path('classchange/edit/<int:pk>/', views.edit_class_change, name='edit_class_change'),
    path('class-changes/export-pdf/', views.export_classchange_pdf, name='export_classchange_pdf'),
    path('export/complaints/excel/', views.export_complaints_excel, name='export_complaints_excel'),
    path('complaints/<int:pk>/delete/', views.delete_complaint, name='delete_complaint'),
    path('export/classchange/excel/', views.export_classchange_excel, name='export_classchange_excel'),
    path('classchange/delete/<int:pk>/', views.delete_class_change, name='delete_class_change'),





]
