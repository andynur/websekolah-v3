from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.utils.html import escape

def dictfetchall(cursor):
    """Mengubah semua hasil query menjadi dictionary."""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dictfetchone(cursor):
    """Mengubah satu hasil query menjadi dictionary."""
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return dict(zip(columns, row))

def siswa_list(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM siswa
            ORDER BY id DESC
        """)
        data_siswa = dictfetchall(cursor)

    # passing data dari view ke template
    search_text = "Wonosogood" 

    return render(request, 'list.html', {
        'keyword': search_text,
        'data': data_siswa
    })

def siswa_detail(request, id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM siswa
            WHERE id = %s
            """,
            [id]
        )
        siswa = dictfetchone(cursor)    

    return render(request, 'detail.html', {
        'siswa': siswa,
    })

def siswa_create(request):
    # cek request yg masuk, klo dia POST (submit)
    if request.method == 'POST':     
        # debug post data
        print("debug POST req:", request.POST.dict())

        # kumpulkan data dari request post
        nama = request.POST.get('nama', '').strip()
        umur = request.POST.get('umur', '').strip()

        # eksekusi query insert ke tabel siswa
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO siswa (nama, umur)
                VALUES (%s, %s)
                """,
                [nama, umur]
            )

        # klo berhasil maka redirect ke siswa list
        return redirect('siswa_list')

    # klo gk submit (GET)
    return render(request, 'form.html')

def siswa_update(request, id):
    html = f"""
    <html>
        <head><title>Edit Siswa</title></head>
        <body>
            <h1>Edit Siswa</h1>
            <p>Edit data siswa dengan ID: {id}</p>
        </body>
    </html>
    """
    return HttpResponse(html)

def siswa_delete(request, id):
    html = f"""
    <html>
        <head><title>Hapus Siswa</title></head>
        <body>
            <h1>Hapus Siswa</h1>
            <p>Yakin ingin menghapus siswa dengan ID: {id}?</p>
        </body>
    </html>
    """
    return HttpResponse(html)