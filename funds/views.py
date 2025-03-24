from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import View

from .forms import FundDataForm
from .models import Fund
from .utils import process_fund_csv


def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page.
    """

    return render(request, "home.html")


def funds(request: HttpRequest) -> HttpResponse:
    """
    Render the funds page with a list of all Funds.
    """

    funds = Fund.objects.all()
    fund_data = Fund.objects.aggregate(
        total_aum=Sum("aum"),
        num_of_funds=Sum(1)
    )

    return render(request, "funds.html", {
        "funds": funds,
        "strategy_choices": Fund.STRATEGY_CHOICES,
        "num_of_funds": fund_data["num_of_funds"] or 0,
        "total_aum": fund_data["total_aum"] or 0,
    })


class FundDataUpload(View):
    """
    Handles the upload and processing of a CSV file containing Fund data.
    """

    def get(self, *args, **kwargs) -> HttpResponse:
        return render(self.request, "funds-upload.html", {
            "FundDataForm": FundDataForm
            }
        )
    
    def post(self, *args, **kwargs) -> HttpResponseRedirect:
        form = FundDataForm(self.request.POST, self.request.FILES)
    
        if form.is_valid():
            fund_data_file = form.cleaned_data["file"]

            # Process the file.
            valid_funds, errors = process_fund_csv(fund_data_file)

            # Save valid Funds.
            Fund.objects.bulk_create([Fund(**fund) for fund in valid_funds])

            if errors:
                messages.error(self.request, f"Some rows contained errors: {errors}")
            else:
                messages.success(self.request, "File uploaded and processed successfully.")

            return redirect("funds:funds_all")
        else:
            messages.error(self.request, "Invalid file. Please check and try again.")
            return redirect("funds:funds_upload")
