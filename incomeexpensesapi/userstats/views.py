from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expense
from rest_framework. response import Response
from rest_framework import status
# Create your views here.


class ExpenseSummaryStats(APIView):

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount

        return {'amount':str(amount)}
    

    def get_category(self, expenses):
        return expenses.category

    def get(self, request):
        today_date = datetime.date.today()
        ayear_agor = today_date-datetime.timedelta(days=30*12)
        expenses = Expense.objects.filter(owner=request.user, date__gte=ayear_agor)

        final  = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expenses, category)

        return Response({'category_data':final}, status=status.HTTP_200_OK)
         


         
