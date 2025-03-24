from django import forms

from .validators import FileValidator, validate_file_extension


class FundDataForm(forms.Form):
    """
    Form for uploading Fund data as a CSV file.
    """

    file = forms.FileField(
        label="Upload Fund data (CSV, max 16MB)",
        required=True,
        validators=[
            FileValidator.validate_file_size,
            FileValidator.validate_file_mime_type, 
            validate_file_extension
        ],
        widget=forms.FileInput(
            attrs={ "accept": ".csv" }
        )
    )
