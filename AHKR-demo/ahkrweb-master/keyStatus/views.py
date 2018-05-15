from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import KeyStatus
from .forms import KeyStatusForm
from django.utils import timezone
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
 
#To get the logged user information
def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return HttpResponseRedirect('/articles/all')

    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form 

    return render_to_response('create_article.html', args)

def get_username(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username



#To save the status of the key
@require_http_methods(["GET", "POST"])
def saveKeyStatus(request):
        company = request.GET['company']
        branch = request.GET['branch']
        product_id = request.GET['product_id']
        box_id = request.GET['box_id']
        key_status = request.GET['key_status']
        createdby = request.GET['createdby']
        #createdat = timezone.localtime(timezone.now())
        createdat = datetime.datetime.now()
        key = KeyStatus(company= company,branch= branch,product_id= product_id ,box_id= box_id,key_status= key_status,createdby= createdby,createdat= createdat)
        key.save()
        return HttpResponse("Successfully saved!")

