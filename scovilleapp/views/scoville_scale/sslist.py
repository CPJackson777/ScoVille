import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import ScovilleScale
from ..connection import Connection
from scovilleapp.models import model_factory


def scovillescale_list(request):
    if request.method == 'GET':
        scale_list = ScovilleScale.objects.all()

        template = 'scoville_scale/sslist.html'
        context = {
            'scale_list': scale_list
        }
        return render(request, template, context)




# def scovillescale_list(request):
#     if request.method == 'GET':
      
#         all_scovillescales = ScovilleScale.objects.all()

#         pepper_name = request.GET.get('pepper_name', None)
#         # title = request.GET['title']

#         if pepper_name is not None:
#             all_scovillescales = all_scovillescales.filter(pepper_name__contains=pepper_name)

#         template = 'scovillescales/sslist.html'
#         context = {
#             'all_scovillescales': all_scovillescales
#         }

#         return render(request, template, context)
#     elif request.method == 'POST':
#         form_data = request.POST

#         # with sqlite3.connect(Connection.db_path) as conn:
#         #     db_cursor = conn.cursor()

#         #     db_cursor.execute("""
#         #     INSERT INTO scovilleapp_book
#         #     (
#         #         title, author, isbn,
#         #         year, location_id, librarian_id
#         #     )
#         #     VALUES (?, ?, ?, ?, ?, ?)
#         #     """,
#         #     (form_data['title'], form_data['author'],
#         #     form_data['isbn'], form_data['year_published'],
#         #     request.user.librarian.id, form_data["location"]))
        
#         # instantiate...
#         new_scovillescale = ScovilleScale(
#             pepper_name = form_data['pepper_name'],
#             heat_range = form_data['heat_range'],
#             image = form_data['pythonlogo.png']
#         )

#         # and then save to the db
#         # print(new_scovillescale.librarian.user.username)
#         # new_scovillescale.save()

#         # Or...
#         # Use a shortcut to do both at the same time
#         # new_book = Book.objects.create(
#         #     title = form_data['title'],
#         #     author = form_data['author'],
#         #     isbn = form_data['isbn'],
#         #     year = form_data['year_published'],
#         #     location_id = request.user.librarian.id,
#         #     librarian_id = form_data["location"]
#         # )

#         return redirect(reverse('scovilleapp:scovillescale'))