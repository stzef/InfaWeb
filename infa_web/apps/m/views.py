from django.shortcuts import render

def mDashboard(request):
	return render(request, 'm/m_dashboard.html')