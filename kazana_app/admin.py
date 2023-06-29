from django.contrib import admin
from .models import User_Detail, Category, Products, Product_images, Product_documents, Blog_management, About_us, Contact_us, Upload_document

# Register your models here.
@admin.register(User_Detail)
class User_DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_birth', 'amount_invested', 'phone_no')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'enable_category')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'payment_type', 'enable_product')

@admin.register(Product_images)
class Product_imagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'add_images')

@admin.register(Product_documents)
class Product_documentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'add_documents')

@admin.register(Blog_management)
class Blog_managementAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'blog_url', 'published_date')

@admin.register(About_us)
class About_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_title', 'description')

@admin.register(Contact_us)
class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email_address', 'subject')

@admin.register(Upload_document)
class Upload_documentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_title', 'document')