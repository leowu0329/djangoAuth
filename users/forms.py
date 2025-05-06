from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
	birthday = forms.DateField(
		widget=forms.DateInput(attrs={'type': 'date'}),
		required=False,
		label='生日'
	)

	def __init__(self, *args, **kwargs):
		user = kwargs.get('instance')
		super().__init__(*args, **kwargs)
		
		# 如果不是管理員，禁用權限選擇
		if user and not user.is_staff:
			self.fields['role'].disabled = True
			self.fields['role'].help_text = '只有管理員可以修改權限'

	class Meta:
		model = CustomUser
		fields = [
			'role', 'identity_id', 'birthday', 'phone', 'mobile',
			'county', 'district', 'village', 'neighborhood',
			'street', 'section', 'lane', 'alley', 'number', 'floor',
			'work_area', 'identity_type'
		]
		widgets = {
			'role': forms.Select(attrs={
				'class': 'form-select',
			}),
			'identity_id': forms.TextInput(attrs={'class': 'form-control'}),
			'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '02-12345678'}),
			'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0912345678'}),
			'county': forms.TextInput(attrs={'class': 'form-control'}),
			'district': forms.TextInput(attrs={'class': 'form-control'}),
			'village': forms.TextInput(attrs={'class': 'form-control'}),
			'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
			'street': forms.TextInput(attrs={'class': 'form-control'}),
			'section': forms.TextInput(attrs={'class': 'form-control'}),
			'lane': forms.TextInput(attrs={'class': 'form-control'}),
			'alley': forms.TextInput(attrs={'class': 'form-control'}),
			'number': forms.TextInput(attrs={'class': 'form-control'}),
			'floor': forms.TextInput(attrs={'class': 'form-control'}),
			'work_area': forms.Select(attrs={'class': 'form-select'}),
			'identity_type': forms.Select(attrs={'class': 'form-select'}),
		}
		help_texts = {
			'role': '設置用戶的權限等級',
			'work_area': '選擇工作的主要區域',
			'identity_type': '選擇身分類型',
			'identity_id': '請輸入有效的身分證號',
			'phone': '格式：02-12345678',
			'mobile': '格式：0912345678',
		}
