from django.shortcuts import render

def mDashboard(request):
	return render(request, 'm/m_dashboard.html')

def mFacChooseClient(request):
	return render(request, 'm/m_fac_choose_client.html')

def mFacSearchClient(request):
	return render(request, 'm/m_fac_search_client.html')

def mFacOrder(request):
	return render(request, 'm/m_fac_order.html')

def mFacOrder2(request):
	return render(request, 'm/m_fac_order2.html')

def mFacChooseArtice(request):
	return render(request, 'm/m_fac_choose_article.html')

def mFacPay(request):
	return render(request, 'm/m_fac_pay.html')
