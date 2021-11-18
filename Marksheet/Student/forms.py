from django.forms import ModelForm
from .models import Enter_Detail


class Enter_DetailForm(ModelForm):
	class Meta:
		model = Enter_Detail
		fields = ['reg']