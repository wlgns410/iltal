import os 
import django 
import csv 
import sys 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","iltal.settings")
django.setup()
from users.models    import User, Host
from products.models import Category, Subcategory, Product
from books.models    import BookStatus
CSV_PATH_CATEGORY    = 'csv/category.csv'
CSV_PATH_SUBCATEGORY = 'csv/subcategory.csv'
CSV_PATH_PRODUCT     = 'csv/product.csv'
CSV_PATH_BOOKSTATUS  = 'csv/bookstatus.csv'
def insert_category():
    with open(CSV_PATH_CATEGORY) as in_file:
        data_reader = csv.reader(in_file)
        # 첫번째 줄 빼고 출력
        next(data_reader, None)
        for row in data_reader:
            category_name               = row[0]
            Category.objects.create(name=category_name)     
def insert_subcategory():
    with open(CSV_PATH_SUBCATEGORY) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                category_id = row[0]
            if row[1]:
                subcategory_id = row[1]
                category__id = Category.objects.get(id=category_id)
                Subcategory.objects.create(category=category__id,name=subcategory_id)
def insert_product():
    with open(CSV_PATH_PRODUCT) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            subcategory_id = row[0]
            host_id = row[1]
            title = row[2]
            region = row[3]
            price = row[4]
            is_group = row[5]
            background_url = row[6]
            Product.objects.create(subcategory_id=subcategory_id, host_id=host_id, title=title, region=region, price=price, is_group=is_group,background_url=background_url)
def insert_bookstatus():
    with open(CSV_PATH_BOOKSTATUS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            status               = row[0]
            BookStatus.objects.create(status=status)             
# insert_category()
# insert_subcategory()
# insert_product()
# insert_bookstatus()