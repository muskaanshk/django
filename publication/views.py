from django.shortcuts import render
from .models import Publication

# publication=[
# 	{'title':'Java',
# 	 'file': 'https://gking.harvard.edu/files/paperspub.pdf',
# 	 'year': '2020'
	
# 	},
# 	{
# 	'title':'Python',
# 	 'file': 'http://www.icmje.org/icmje-recommendations.pdf',
# 	 'year': '2018'

# 	}
# ]

def home(request):
	context={'publication':Publication.objects.all()}


	return render(request ,'publication/home.html',context)

# Create your views here.
