from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.forms.models import inlineformset_factory
from .models import Author
from .models import Book


def manage_books(request, pk):
    author = Author.objects.get(pk=pk)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return render(request, 'main/manage_books.html', {'formset': formset, 'author': author})
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request, 'main/manage_books.html', {'formset': formset, 'author': author})