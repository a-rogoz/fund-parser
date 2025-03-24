from django.test import TestCase

from .forms import FundDataForm
from .models import Fund


class FundModelTest(TestCase):
    def test_create_fund(self):
        """
        Test that a Fund object can be created successfully.
        """

        fund = Fund.objects.create(
            name="Test Fund Name",
            strategy="long/short equity",
            aum=500000000,
            inception_date="2024-01-01"
        )
        self.assertEqual(str(fund), f"{fund.name} data")


class FundDataFormTest(TestCase):
    def test_invalid_file_type(self):
        """
        Test that a non-CSV file is rejected.
        """

        form = FundDataForm(files={"file": None})
        self.assertFalse(form.is_valid())
        self.assertIn("file", form.errors)
