from django.shortcuts import render_to_response
from django.template.context import RequestContext

#from django.shortcuts import render_to_response# Create your views here.

#def index(request):
	#droughts = Drought.objects.filter(D3D4__gte=5)

		#return render_to_response('index.html', {'drought': droughts})

	#from dateutil.relativedelta import relativedelta

    def render_chart(request):
            if request.method == "GET":

                    # Get a point in time we want to render chart from
                    #series_age = date.today() - relativedelta(months=3)

                    # Create a fairly advanced QuerySet using:
                    #  - filter() to get records newer than 'series_age'
                    #  - extra() to cast a PostgreSQL 'timestampz' to 'date' which translates to a pyton date object
                    #  - values() to extract fields of interest
                    #  - annotate() to group aggregate Count into 'id__count'
                    #  - order_by() to make the aggregate work
                    #qset = Spam.gcharts.filter(cdt__gt=series_age).extra(select={"date": "cdt::date"}) \
                                               #.values("date").annotate(Count("id")).order_by()

                    # Call the qset.to_json() method to output the data in json
                    #  - labels is a dict which sets labels and the correct javascript data type for
                    #    fields in the QuerySet. The javascript data types are automatically set, 
                    #    except for extra fields, which needs to be specified in a dict as:
                    #       {'extra_name': {'javascript data type': 'label for field'}}
                    #  - order is an iterable which sets the column order in which the data should be
                    #    rendered
                    #  - formatting is a dict {'field_name': 'expression'}, where expression is a 
                    #    valid string.format() expression.
                    drought_json = qset.to_json(labels={"D3D4": "Drought percentage", "date": {"date": "Date"}},
                                             order=("date", "D3D4"), 
                                             formatting={"D3D4": "{0:d} units of spam"})

                    return render_to_response("sales_overviews/spamreport.html, {"drought_data": drought_json},
                                              context_instance=RequestContext(request))