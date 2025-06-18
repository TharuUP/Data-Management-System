import django_filters
from .models import Complaint, ClassChange
from django import forms

class ComplaintFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500'
        })
    )
    class Meta:
        model = Complaint
        fields = ['center','date', 'complaint_no', 'vin', 'complaint_type']



class ClassChangeFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500'
        })
    )

    class Meta:  # <-- make sure this line is correctly indented (no extra tab or space)
        model = ClassChange
        fields = ['date', 'vin', 'previous_class', 'change_class']
