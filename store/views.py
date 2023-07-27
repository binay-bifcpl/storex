from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import UsageForm
from .forms import StoreEntryForm
from .models import StoreEntry
import pandas as pd
from django.http import HttpResponse
from io import BytesIO
from .models import Usage
from django.shortcuts import render, redirect, get_object_or_404


@staff_member_required
def add_store_entry(request, entry_id=None):
    if entry_id:
        entry = get_object_or_404(StoreEntry, pk=entry_id)
    else:
        entry = None

    if request.method == 'POST':
        form = StoreEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('all_entries')
    else:
        form = StoreEntryForm(instance=entry)

    return render(request, 'store/add_store_entry.html', {'form': form})



@login_required
def all_entries(request):
    entries = StoreEntry.objects.all()
    return render(request, 'store/all_entries.html', {'entries': entries})



@staff_member_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(StoreEntry, pk=entry_id)
    return add_store_entry(request, entry_id=entry_id)
@staff_member_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(StoreEntry, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('all_entries')

    return render(request, 'store/delete_entry.html', {'entry': entry})



@staff_member_required
def add_usage(request):
    if request.method == 'POST':
        form = UsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_usage')  # Replace 'all_usage' with the URL name of the view to display all usage data.
    else:
        form = UsageForm()

    return render(request, 'store/add_usage.html', {'form': form})




@login_required
def all_usage(request):
    usages = Usage.objects.all()
    return render(request, 'store/all_usage.html', {'usages': usages})



@staff_member_required
def edit_usage(request, usage_id):
    usage = get_object_or_404(Usage, pk=usage_id)
    if request.method == 'POST':
        form = UsageForm(request.POST, instance=usage)
        if form.is_valid():
            form.save()
            return redirect('all_usage')
    else:
        form = UsageForm(instance=usage)

    return render(request, 'store/add_usage.html', {'form': form})

@staff_member_required
def delete_usage(request, usage_id):
    usage = get_object_or_404(Usage, pk=usage_id)
    if request.method == 'POST':
        usage.delete()
        return redirect('all_usage')

    return render(request, 'store/delete_usage.html', {'usage': usage})


@login_required

def download_usage_as_excel(request):
    # Query all usage data from the database
    usages = Usage.objects.all()

    # Create a DataFrame from the usage data
    data = {
        'SL No': [usage.sl_no for usage in usages],
        'Date': [usage.date for usage in usages],
        'Product': [usage.product.name for usage in usages],
        'Location': [usage.location for usage in usages],
        'Given By': [usage.given_by for usage in usages],
        'Taken By': [usage.taken_by for usage in usages],
        'Quantity': [usage.quantity for usage in usages],
        'Remarks': [usage.remarks for usage in usages],
    }
    df = pd.DataFrame(data)

    # Create an Excel file in memory using pandas and openpyxl engine
    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Usage Data')

    # Prepare the response to download the Excel file
    response = HttpResponse(excel_file.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=usage_data.xlsx'

    return response

# store/views.py

@login_required
def download_store_entries_as_excel(request):
    # Query all store entries from the database
    store_entries = StoreEntry.objects.all()

    # Create a DataFrame from the store entries data
    data = {
        'Name': [entry.name for entry in store_entries],
        'Type': [entry.entry_type for entry in store_entries],
        'Model': [entry.model for entry in store_entries],
        'Serial No': [entry.serial_no for entry in store_entries],
        'Date': [entry.date for entry in store_entries],
        'Quantity': [entry.quantity for entry in store_entries],
        'Remarks': [entry.remarks for entry in store_entries],
    }
    df = pd.DataFrame(data)

    # Create an Excel file in memory using pandas and openpyxl engine
    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Store Entries')

    # Prepare the response to download the Excel file
    response = HttpResponse(excel_file.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=store_entries.xlsx'

    return response
