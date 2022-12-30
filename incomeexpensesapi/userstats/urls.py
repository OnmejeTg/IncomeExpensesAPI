from . views import ExpenseSummaryStats
from django.urls import path

urlpatterns=[
    path('expenses-summary-data', ExpenseSummaryStats.as_view(), name='expsnes-summary-data'),
]