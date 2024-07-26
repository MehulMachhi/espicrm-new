from admin_charts.charts import AdminChart
from admin_charts.dashboards import AdminDashboard
from django.db.models import Count
from django.db.models.functions import TruncMonth

from .models import enquiry


class EnquiryByMonthChart(AdminChart):
    title = 'Enquiries by Month'
    model = enquiry
    chart_type = 'line'
    date_field = 'date_created'  # Assuming your Enquiry model has a date_created field

    def get_aggregate_data(self):
        return self.model.objects.annotate(date=TruncMonth(self.date_field)).values('date').annotate(
            y=Count('id')).order_by('date')


class MyDashboard(AdminDashboard):
    title = 'My Dashboard'
    charts = [
        EnquiryByMonthChart() ,
    ]
