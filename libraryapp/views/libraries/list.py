import sqlite3
from django.shortcuts import render
from libraryapp.models import Librarian
# from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def list_libraries(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address,
                
            from libraryapp_libraries l
            """)

            all_libraries = db_cursor.fetchall()

        template_name = 'libraries/list.html'

        return render(request, template_name, {'all_libraries': all_libraries})
