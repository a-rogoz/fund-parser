from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import FundSerializer
from funds.models import Fund


class FundListView(ListAPIView):
    """
    Displays a list of all available Funds.
    """

    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Fund.objects.all()
        strategy = self.request.query_params.get("strategy", None)
        if strategy:
            queryset = queryset.filter(strategy=strategy)
        return queryset


class FundDetailView(RetrieveAPIView):
    """
    Displays detailed information about an individual Fund.
    """

    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    permission_classes = (permissions.AllowAny,)
