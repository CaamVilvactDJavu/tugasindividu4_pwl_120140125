# Tugas Individu 4 Pemrograman Web Lanjut

- Nama : Ilham Fadhlur Rahman
- Nim : 120140125
- Program Studi : Teknik Informatika
- Kelas : Pemrograman Web Lanjut

## Cara menjalankan aplikasi

1. Clone repository ini 

```
git clone https://github.com/CaamVilvactDJavu/tugasindividu4_pwl_120140125.git
```

2. Ganti ke directory pada repository ini

```
cd tugasindividu4_pwl_120140125 
```

3. Install Virtual Environment

```
python3 -m venv env
```

4. Aktifkan Virtual Environment

```
env\Scripts\activate
```

5. Install dependencies

```
env\Scripts\python -m pip install -e .
```

dan update pip

```
env\Scripts\python -m pip install --upgrade pip setuptools
```

6. Buat database

```
Buat database (mysql) dengan nama tugasindividu4_pwl_120140125
```

7. Migrate database 

```
env\Scripts\alembic -c development.ini revision --autogenerate
```

dan

```
env\Scripts\alembic -c development.ini upgrade head
```

8. Muat database

```
env\Scripts\initialize_tugasindividu4_pwl_120140125_db development.ini
```

9. Jalankan test aplikasi

```
pytest
```

10. Jalankan aplikasi

```
env\Scripts\pserve development.ini
```

## Screenshot

1. Register
![register](./public/register.png)

2. Login 
![login](./public/login.png)

3. Logout
![logout](./public/logout.png)

