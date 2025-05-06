from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
	# 時間相關欄位
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')
	last_login = models.DateTimeField(null=True, blank=True, verbose_name='最後登入時間')

	# 權限和工作區域
	ROLE_CHOICES = [
		('guest', '訪客'),
		('user', '一般使用者'),
		('admin', '管理者'),
	]
	role = models.CharField(
		max_length=10,
		choices=ROLE_CHOICES,
		default='guest',
		verbose_name='權限'
	)

	AREA_CHOICES = [
		('north', '雙北桃竹苗'),
		('central', '中彰投'),
		('south', '雲嘉南'),
		('east', '高高屏'),
	]
	work_area = models.CharField(
		max_length=10,
		choices=AREA_CHOICES,
		null=True,
		blank=True,
		verbose_name='工作轄區'
	)

	# 個人資訊
	identity_id = models.CharField(max_length=20, null=True, blank=True, verbose_name='身分ID')
	birthday = models.DateField(null=True, blank=True, verbose_name='生日')
	phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='市話')
	mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name='手機')

	# 地址相關
	county = models.CharField(max_length=20, null=True, blank=True, verbose_name='縣市')
	district = models.CharField(max_length=20, null=True, blank=True, verbose_name='鄉鎮')
	village = models.CharField(max_length=20, null=True, blank=True, verbose_name='村里')
	neighborhood = models.CharField(max_length=10, null=True, blank=True, verbose_name='鄰')
	street = models.CharField(max_length=50, null=True, blank=True, verbose_name='街路')
	section = models.CharField(max_length=10, null=True, blank=True, verbose_name='段')
	lane = models.CharField(max_length=10, null=True, blank=True, verbose_name='巷')
	alley = models.CharField(max_length=10, null=True, blank=True, verbose_name='弄')
	number = models.CharField(max_length=10, null=True, blank=True, verbose_name='號')
	floor = models.CharField(max_length=10, null=True, blank=True, verbose_name='樓')

	# 身分別
	IDENTITY_CHOICES = [
		('public', '公'),
		('private', '私'),
	]
	identity_type = models.CharField(
		max_length=10,
		choices=IDENTITY_CHOICES,
		null=True,
		blank=True,
		verbose_name='身分別'
	)

	class Meta:
		verbose_name = '使用者'
		verbose_name_plural = '使用者'

	def __str__(self):
		return self.username

	def get_full_address(self):
		"""取得完整地址"""
		address_parts = [
			self.county,
			self.district,
			self.village,
			f"{self.neighborhood}鄰" if self.neighborhood else "",
			self.street,
			f"{self.section}段" if self.section else "",
			f"{self.lane}巷" if self.lane else "",
			f"{self.alley}弄" if self.alley else "",
			f"{self.number}號" if self.number else "",
			f"{self.floor}樓" if self.floor else "",
		]
		return "".join(part for part in address_parts if part)
