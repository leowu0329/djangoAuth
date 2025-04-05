from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser

# ------------------- CustomUser Admin (擴展 User 模型) -------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):  # 繼承 UserAdmin 和 ImportExportModelAdmin
    list_display = ("username", "email", "birthday", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email", "birthday")
    
    # 修改 fieldsets，加入 birthday 欄位
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("birthday",)}),
    )
    
    # 新增用戶時的表單欄位
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("birthday",)}),
    )
