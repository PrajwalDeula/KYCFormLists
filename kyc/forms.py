from django import forms
from .models import KYCModel
from nepali_datetime_field.forms import NepaliDateInput

class KYCForm(forms.ModelForm):

    class Meta:
        model = KYCModel
        exclude = ['created_date', 'updated_date'] 
        fields = '__all__'
        ordering = ['-created_date']
        widgets = {
            'dob_bs': NepaliDateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD (B.S.)',
                'autocomplete': 'off'}),
            'salutation': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'given-name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control','required': False}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'family-name'}),
            'nep_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'nationality': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth_ad': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place':forms.TextInput(attrs={'class': 'form-control'}),
            'address_nepali': forms.TextInput(attrs={'class': 'form-control'}),
            'risk_category': forms.Select(attrs={'class': 'form-select'}),
            'document_issued_date_bs': NepaliDateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD (B.S.)'
            }),
            'document_issued_date_bs': NepaliDateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD (B.S.)'
            }),
            'document_issued_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'qualification': forms.Select(attrs={'class': 'form-select'}),
             'profession': forms.Select(attrs={'class': 'form-select'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nep_father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'grand_father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'grandfather_in_law_name': forms.TextInput(attrs={'class': 'form-control'}),
            'spouse_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_in_law_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'son_name': forms.TextInput(attrs={'class': 'form-control'}),
            'daughter_name': forms.TextInput(attrs={'class': 'form-control'}),
            'daughter_in_law_name': forms.TextInput(attrs={'class': 'form-control'}),
            'proposer_full_name': forms.TextInput(attrs={'class': 'form-control'}),

            'age_proof_doc': forms.Select(attrs={'class': 'form-select'}),
            'document_number': forms.TextInput(attrs={'class': 'form-control'}),
            'document_issued_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'document_issued_date_bs': NepaliDateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD (B.S.)',
                'autocomplete': 'off'}),
            'issued_place': forms.Select(attrs={'class': 'form-select'}),

            'is_politically_involved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_family_politically_involved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'temporary_address': forms.TextInput(attrs={'class': 'form-control'}),
            'temporary_district': forms.TextInput(attrs={'class': 'form-control'}),  # or Select if choices added
            'ward_no': forms.TextInput(attrs={'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'local_unit': forms.Select(attrs={'class': 'form-select'}),
            'structure': forms.Select(attrs={'class': 'form-select'}),

            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),

            'income_mode': forms.Select(attrs={'class': 'form-select'}),
            'income_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'pan_no': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_ac_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_ac_no': forms.TextInput(attrs={'class': 'form-control'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control'}),
            'firm_name': forms.TextInput(attrs={'class': 'form-control'}),

            'is_aml_crime': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_family_aml_crime': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['middle_name'].required = False
        self.fields['dob_bs'].required = False
        self.fields['document_number'].required = True
        self.fields['document_number'].widget.attrs['required'] = 'required'
        self.fields['document_number'].error_messages = {
            'required': 'Document number is required'
        }
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields

