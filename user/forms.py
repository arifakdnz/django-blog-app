from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Kullanıcı Adı")
    password =  forms.CharField(max_length=20, label = "Parola",widget = forms.PasswordInput) #Parola alanı gibi görünmesi için
    confirm = forms.CharField(max_length=20, label= "Parolayı Doğrula", widget = forms.PasswordInput)
    
    def clean(self): #django da böyle yapılıyor.
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:

            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values ={
            "username": username, #fonskiyonun yapııs gereği values değerini sözlük olarak döndürüyoruz.
            "password": password,
        }
        return values 

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola", widget = forms.PasswordInput)