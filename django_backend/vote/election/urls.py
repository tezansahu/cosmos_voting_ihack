from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('election.v1.urls'), name='v1_election'),
]
