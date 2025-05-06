from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from import_export.admin import ImportExportModelAdmin

@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = [field.name for field in CustomUser._meta.fields]
	list_filter = ['role', 'work_area', 'identity_type', 'is_staff', 'is_active']
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('個人資訊', {'fields': (
			'email', 'identity_id', 'birthday', 'phone', 'mobile',
			'role', 'work_area', 'identity_type'
		)}),
		('地址資訊', {'fields': (
			'county', 'district', 'village', 'neighborhood',
			'street', 'section', 'lane', 'alley', 'number', 'floor'
		)}),
		('權限', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
		('重要日期', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
	)
	readonly_fields = ['created_at', 'updated_at', 'last_login', 'date_joined']
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': (
				'username', 'email', 'password1', 'password2',
				'role', 'work_area', 'identity_type', 'is_staff', 'is_active'
			)
		}),
	)
	search_fields = ['username', 'email', 'identity_id', 'phone', 'mobile']
	ordering = ['username']
