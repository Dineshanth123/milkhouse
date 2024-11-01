
from django.shortcuts import render, get_object_or_404, redirect
from .models import Seller, Buyer, Transaction
from .forms import SellerForm, BuyerForm

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def seller_detail(request, seller_id):
    seller = get_object_or_404(Seller, id=seller_id)
    transactions = Transaction.objects.filter(seller=seller).order_by('date')
    return render(request, 'seller_detail.html', {'seller': seller, 'transactions': transactions})

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
    return render(request, 'buyer_detail.html', {'buyer': buyer, 'transactions': transactions})

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
