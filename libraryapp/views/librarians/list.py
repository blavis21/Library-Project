import sqlite3
from django.shortcuts import render
from libraryapp.models import Librarian
# from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def list_librarians(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.location_id,
                l.user_id,
                u.first_name,
                u.last_name,
                u.email
            from libraryapp_librarian l
            join auth_user u on l.user_id = u.id
            """)

            # librarian_list = []
            all_librarians = db_cursor.fetchall()

            # for row in dataset:
            #     librarian = Librarian()
            #     librarian.id = row['id']
            #     librarian.location_id = row['location_id']
            #     librarian.user_id = row['user_id']

        template_name = 'librarians/list.html'
        # context = {
        #     'librarian_list': librarian_list
        # }

        return render(request, template_name, {'all_librarians': all_librarians})