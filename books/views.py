from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class BookcollectionListView(ListView):
	model = models.Book

class BookcollectionDetailView(DetailView):
	model = models.Book

class BookcollectionUpdateView(UpdateView):
    model = models.Book
    ## fields = ['description'] jos haluaa vain päivittää yhden tai osan tietueista
    fields = "__all__"

class BookcollectionCreateView(CreateView):
	model = models.Book
	fields = "__all__"
	success_url = "/bookcollection/"

class BookcollectionDeleteView(DeleteView):
    model = models.Book
    success_url = "/bookcollection/"
