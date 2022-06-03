from student_manager.uploader.models import Invoice
from student_manager.users.models import User
from django.db import transaction


@transaction.atomic
def create_invoice(
    *, 
    date: str, 
    amount: str,
    user: User,
    number: str,
) -> Invoice:
    amount_number = float(amount[1:])
    invoice = Invoice.objects.create(
        user=user,
        invoice_number=number,
        invoice_date=date,
        invoice_amount=amount_number,
    )
    return invoice
