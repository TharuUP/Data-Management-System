from django import forms
from .models import Complaint
from .models import ClassChange

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        exclude = ['reporter', 'complaint_no', 'date']
        widgets = {
            'complaint_type': forms.Select(choices=Complaint.COMPLAINT_TYPES),
            'status': forms.Select(choices=Complaint.STATUS_CHOICES),
        }


class ClassChangeForm(forms.ModelForm):
    class Meta:
        model = ClassChange
        exclude = ['updated_by']
        widgets = {
            'change_class': forms.Select(choices=ClassChange.CLASS_CHOICES),
            'approved_by': forms.Select(choices=ClassChange.APPROVED_CHOICES),
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}
            ),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}
            ),
        }
