from django.db import models
from nepali_datetime_field.models import NepaliDateField
from django.utils import timezone
from django.conf import settings 
import datetime

# Common choices (keep these at the top to avoid duplication)
SALUTATION_CHOICES = [('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')]
NATIONALITY_CHOICES = [('Nepalese','Nepalese'), ('Indian','Indian'), ('Other','Other')]
GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
AGE_PROOF_DOC_CHOICES = [
    ('Citizenship', 'Citizenship'),
    ('Passport', 'Passport'),
    ('Birth Certificate', 'Birth Certificate'),
    ('Other', 'Other'),
]
INCOME_MODE_CHOICES = [
    ('Salary', 'Salary'),
    ('Business', 'Business'),
    ('Investment', 'Investment'),
    ('Other', 'Other'),
]
QUALIFICATION_CHOICES = [('SLC', 'SLC'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Other', 'Other')]
ISSUED_PLACE_CHOICES = [('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur')]
PROFESSION_CHOICES = [('Service', 'Service'), ('Business', 'Business'), ('Other', 'Other')]
STRUCTURE_CHOICES = [
    ('Metropolitan City', 'Metropolitan City'),
    ('Sub-Metropolitan City', 'Sub-Metropolitan City'),
    ('Municipality', 'Municipality'),
    ('Rural Municipality', 'Rural Municipality'),
    ('Ward', 'Ward'),
]
LOCAL_UNIT_CHOICES = [
    ('Kathmandu Metropolitan City', 'Kathmandu Metropolitan City'),
    ('Pokhara Metropolitan City', 'Pokhara Metropolitan City'),
    ('Lalitpur Metropolitan City', 'Lalitpur Metropolitan City'),
    ('Biratnagar Metropolitan City', 'Biratnagar Metropolitan City'),
    ('Bharatpur Metropolitan City', 'Bharatpur Metropolitan City'),
    ('Birgunj Metropolitan City', 'Birgunj Metropolitan City'),
]
RISK_CHOICES = [('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')]

class KYCModel(models.Model):
    """Comprehensive KYC information model with detailed personal data"""
    kyc_id = models.AutoField(primary_key=True)
    
    # Personal Information
    salutation = models.CharField(max_length=10, choices=SALUTATION_CHOICES, default='Mr')
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    nep_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default='Nepalese')
    date_of_birth_ad = models.DateField(blank=True, null=True, default=datetime.date.today)
    dob_bs = NepaliDateField(blank=True, null=True)
    
    # Family Information
    father_name = models.CharField(max_length=100, blank=True, null=True)
    nep_father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    grand_father_name = models.CharField(max_length=100, blank=True, null=True)
    grandfather_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    father_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    father_mother_name = models.CharField(max_length=100, blank=True, null=True)
    son_name = models.CharField(max_length=100, blank=True, null=True)
    daughter_name = models.CharField(max_length=100, blank=True, null=True)
    daughter_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    proposer_full_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Identification Documents
    age_proof_doc = models.CharField(max_length=50, choices=AGE_PROOF_DOC_CHOICES, default='Citizenship')
    document_number = models.CharField(max_length=100, verbose_name="Document Number", blank=False)
    document_issued_date_bs = NepaliDateField(verbose_name="Document Issued Date (B.S.)")
    document_issued_date = models.DateField(verbose_name="Document Issued Date (A.D.)")
    issued_place = models.CharField(max_length=100, choices=ISSUED_PLACE_CHOICES, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    
    # Address Information
    address = models.CharField(max_length=255, blank=True, null=True)
    address_nepali = models.CharField(max_length=255, blank=True, null=True)
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    temporary_address = models.CharField(max_length=255, blank=True, null=True)
    temporary_district = models.CharField(max_length=100, blank=True, null=True)
    ward_no = models.CharField(max_length=10, blank=True, null=True)
    house_no = models.CharField(max_length=10, blank=True, null=True, default='0')
    local_unit = models.CharField(max_length=50, choices=LOCAL_UNIT_CHOICES, default='Municipality')
    structure = models.CharField(max_length=50, choices=STRUCTURE_CHOICES, default='Metropolitan City')
    
    # Contact Information
    email = models.EmailField(blank=True, null=True, default='test@example.com')
    mobile = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    
    # Professional Information
    qualification = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES, blank=True, null=True)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, default='Service')
    income_mode = models.CharField(max_length=50, choices=INCOME_MODE_CHOICES, default='Salary')
    income_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.00)
    pan_no = models.CharField(max_length=20, blank=True, null=True)
    bank_ac_name = models.CharField(max_length=100, blank=True, null=True)
    bank_ac_no = models.CharField(max_length=50, blank=True, null=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)
    firm_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Risk Assessment
    risk_category = models.CharField(max_length=10, choices=RISK_CHOICES, default='LOW', verbose_name="Risk Category")
    is_politically_involved = models.BooleanField(default=False)
    is_aml_crime = models.BooleanField(default=False)
    is_family_politically_involved = models.BooleanField(default=False)
    is_family_aml_crime = models.BooleanField(default=False)
    
    # System Fields
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'KYC Detail'
        verbose_name_plural = 'KYC Details'

    def __str__(self):
        return f"{self.client_no} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()

class KYCList(models.Model):
    """Simplified tracking system for client numbers and policy status"""
    
    client_no = models.CharField(max_length=50, null=False, blank=False, default=0,verbose_name='Client Number')
    new_client_no = models.CharField(max_length=50, blank=True, null=True, verbose_name='New Client Number')
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    mobile_no = models.CharField(max_length=20, verbose_name='Mobile Number')
    is_policy_issued = models.BooleanField(default=False, verbose_name='Policy Issued Status')
    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,  # Changed from SET_NULL for data integrity
    null=False,
    blank=False,
    default=1,
    verbose_name='Created By',
    help_text='User who created this record',
    related_name='created_kyc_records')
    created_date = models.DateField(auto_now_add=True, verbose_name='Created Date')
    
    # Link to detailed KYC information
    kyc_detail = models.OneToOneField(
        KYCModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='kyc_list_entry'
    )
    
    class Meta:
        verbose_name = 'KYC List Entry'
        verbose_name_plural = 'KYC List Entries'
    
    def __str__(self):
        return f"{self.client_no} - {self.full_name}"