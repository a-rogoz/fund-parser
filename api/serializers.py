from rest_framework import serializers

from funds.models import Fund


class FundSerializer(serializers.ModelSerializer):
    """
    Serializes Fund data for API responses and validates incoming data.
    """

    aum = serializers.IntegerField(allow_null=True, required=False)
    inception_date = serializers.DateField(allow_null=True, required=False)

    class Meta:
        model = Fund
        fields = "__all__"
