from django.db import models
from firms.models import Entity

class Financial(models.Model):
    entity= models.ForeignKey(Entity, on_delete=models.CASCADE)
    balance_sheet= models.FileField()
    cashflow=
    changes_in_equity=
    
class Ledger(models.Model):
    account_name= models.CharField(max_length=100)
    acct_no= models.CharField(max_length=20) 
    month_ending= models.Dat



# Create your models here.
class Manufacturing(models.Model):
    entity= models.ForeignKey(Entity, on_delete=models.CASCADE)
    financial= models.ForeignKey(Financial, on_delete=models.CASCADE)
    general_ledger=
    trial_balance=
    fixed_assets=
    inventory_records=
    purchase_records=
    sales_records=
    tax_docs=
    payroll_records=
    bank_statements_reconcillation=
    loan_agreement_liability=
    expense_report=
    internal_audit_report=
    contract_legal_agreement=
    compliance_certificate= 