from django.shortcuts import render, get_object_or_404, redirect
from .models import Seller, Buyer, Transaction
from .forms import SellerForm, BuyerForm
from .forms import TransactionForm
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.contrib import messages

def home(request):
    return render(request, 'home.html')


def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def seller_detail(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    transactions = Transaction.objects.filter(seller=seller).order_by('date')
    total_pending_amount = transactions.filter(status='pending').aggregate(Sum('payment'))['payment__sum'] or 0
    return render(request, 'seller_detail.html', {'seller': seller, 'transactions': transactions,'total_pending_amount': total_pending_amount,})

def seller_add(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm()
    return render(request, 'seller_form.html', {'form': form})

def seller_edit(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'seller_form.html', {'form': form})

def seller_delete(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    if request.method == 'POST':
        seller.delete()
        return redirect('seller_list')
    return render(request, 'seller_confirm_delete.html', {'seller': seller})

def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyer_list.html', {'buyers': buyers})

def buyer_detail(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)
    transactions = Transaction.objects.filter(buyer=buyer).order_by('date')
    total_pending_amount = transactions.filter(status='pending').aggregate(Sum('payment'))['payment__sum'] or 0
    return render(request, 'buyer_detail.html', {'buyer': buyer, 'transactions': transactions,'total_pending_amount': total_pending_amount,})

def buyer_add(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer_list')
    else:
        form = BuyerForm()
    return render(request, 'buyer_form.html', {'form': form})

def buyer_edit(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)
    if request.method == 'POST':
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('buyer_list')
    else:
        form = BuyerForm(instance=buyer)
    return render(request, 'buyer_form.html', {'form': form})

def buyer_delete(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)
    if request.method == 'POST':
        buyer.delete()
        return redirect('buyer_list')
    return render(request, 'buyer_confirm_delete.html', {'buyer': buyer})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Seller, Buyer, Transaction

def add_transaction(request):
    if request.method == "POST":
        mobile_number = request.POST.get('mobile_number')
        seller = Seller.objects.filter(mobile=mobile_number).first()
        buyer = Buyer.objects.filter(mobile=mobile_number).first()

        if not seller and not buyer:
            messages.error(request, "This mobile number is not registered as either a Seller or a Buyer.")
            return redirect('add_transaction')

        transaction_type = request.POST.get('transaction_type')

        if seller and transaction_type == "buy":
            messages.error(request, "This mobile number belongs to a seller, not a buyer. Please select the correct transaction type.")
            return redirect('add_transaction')
        elif buyer and transaction_type == "sell":  
            messages.error(request, "This mobile number belongs to a buyer, not a seller. Please select the correct transaction type.")
            return redirect('add_transaction')

        litres = request.POST.get('litres')
        date = request.POST.get('date')
        payment = request.POST.get('payment')
        status = request.POST.get('status')

        seller_instance = seller if seller else None
        buyer_instance = buyer if buyer else None

        transaction = Transaction(
            seller=seller_instance,
            buyer=buyer_instance,
            date=date,
            litres=litres,
            transaction_type=transaction_type,
            payment=payment,
            status=status
        )
        transaction.save()

        messages.success(request, "Transaction added successfully!")
        return redirect('transaction_list')

    return render(request, 'add_transaction.html')

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_form.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == "POST":
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transaction_confirm_delete.html', {'transaction': transaction})
