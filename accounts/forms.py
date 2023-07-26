from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

	class Meta():
		fields = ('username','email','password1','password2')
		model = get_user_model()

	def __init__(self,*arg,**kwarg):
		super().__init__(*arg,**kwarg)
		self.fields['username'].label = 'Enter Name'
		self.fields['email'].label = 'Email Address'
		self.fields['password2'].label = 'Confirm Password'