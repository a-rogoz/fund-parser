from django.test import TestCase
from django.urls import reverse

from .serializers import FundSerializer
from funds.models import Fund


class FundSerializerTest(TestCase):
    def test_valid_fund_serializer(self):
        """
        Test that valid data is correctly serialized.
        """

        data = {
            "name": "Fund Name",
            "strategy": "global macro",
            "aum": 100000000,
            "inception_date": "2024-01-01"
        }
        serializer = FundSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_aum(self):
        """
        Test that an invalid AUM value raises a validation error.
        """

        data = {
            "name": "Invalid Fund",
            "strategy": "arbitrage",
            "aum": "invalid"
        }
        serializer = FundSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("aum", serializer.errors)


class FundListViewTest(TestCase):
    def setUp(self):
        self.fund = Fund.objects.create(
            name="Test Fund", strategy="arbitrage")

    def test_fund_list_view(self):
        """
        Test that the Fund list page returns a 200 response and contains the Fund name.
        """

        response = self.client.get(reverse("api:funds_list"))
        self.assertEqual(response.status_code, 200)


class FundDetailViewTest(TestCase):
    def setUp(self):
        self.fund = Fund.objects.create(
            name="Detail Fund", strategy="long/short equity")

    def test_fund_detail_view(self):
        """
        Test that the Fund detail page loads correctly.
        """

        response = self.client.get(reverse("api:funds_detail", args=[self.fund.id]))
        self.assertEqual(response.status_code, 200)
