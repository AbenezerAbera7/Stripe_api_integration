# stripe_dashboard/views.py
import stripe
from django.conf import settings
from django.shortcuts import render
stripe.api_key = 'sk_test_51NiymQKHVQTyd5K6ORso1XHeXEtKwG4Rr2GYHigsfQugFZiWHiRTzXHcHUdLRT1D60Q8qGilFNs0kR76qmIvplfR00AA0zVowZ'

def connect_stripe():
    stripe.api_key = 'sk_test_51NiymQKHVQTyd5K6ORso1XHeXEtKwG4Rr2GYHigsfQugFZiWHiRTzXHcHUdLRT1D60Q8qGilFNs0kR76qmIvplfR00AA0zVowZ'
def customer_data():
    customers = stripe.Customer.list()
    customer_data = []
    for customer in customers.data:
        customer_data.append({
            "Customer ID": customer.id,
            "Email Address": customer.email,
            "Name": customer.name,
            # "Phone Number": customer.phone,
            # "Address": customer.address,
            # "Creation Date": customer.created
        })
    return customer_data

def subscription_data():
    subscriptions = stripe.Subscription.list()
    subscription_data = []
    for subscription in subscriptions.data:
        subscription_data.append({
            "Subscription ID": subscription.id,
            "Status": subscription.status,
            "Plan Name": subscription.plan.nickname,
            "Plan Amount": subscription.plan.amount,
            "Billing Cycle": subscription.plan.interval,
            "Start Date": subscription.start_date,
            "End Date": subscription.current_period_end,
            "Trial Period": subscription.trial_end - subscription.start_date if subscription.trial_end else None,
            "Renewal Date": subscription.current_period_end
        })    
    return subscription_data  

def payment_data():
    payments = stripe.PaymentIntent.list()
    payment_data = []
    for payment in payments.data:
        payment_data.append({
            "Payment ID": payment.id,
            "Amount": payment.amount,
            "Currency": payment.currency,
            "Payment Method": payment.payment_method,
            "Status": payment.status,
            "Payment Date": payment.created
        })
    return payment_data

def invoice_data():
    invoices = stripe.Invoice.list()
    invoice_data = []
    for invoice in invoices.data:
        invoice_data.append({
            "Invoice ID": invoice.id,
            "Customer ID": invoice.customer,
            "Amount Due": invoice.amount_due,
            "Amount Paid": invoice.amount_paid,
            "Due Date": invoice.due_date,
            "Status": invoice.status,
            "Invoice Date": invoice.created
        })
    return invoice_data

def event_data():
    events = stripe.Event.list()
    event_data = []
    for event in events.data:
        event_data.append({
            "Event ID": event.id,
            "Type": event.type,
            "Created Date": event.created,
            "Data Payload": event.data.object
        })
    return event_data

def dashboard(request):
    context = {
        'customers': customer_data(),
        'subscriptions': subscription_data(),
        'payments': payment_data(),
        'invoices': invoice_data(),
        'events': event_data(),
    }
    return render(request, 'stripe_dashboard/dashboard.html', context)