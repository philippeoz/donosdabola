from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.contrib.auth.forms import User
from django.contrib.auth.forms import AuthenticationForm


class CadastroClienteForm(forms.ModelForm):
    """
    Formulário de cadastro
    """
    nome = forms.CharField(widget=forms.TextInput,label="Nome", required=True)
    email = forms.EmailField(widget=forms.TextInput,label="Email", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (novamente)", required=True)
    cpf_cnpj = forms.CharField(max_length=15, label="CPF/CNPJ", required=True)

    telefone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Utilize este padrão para o telefone: '+999999999'. Tamanho máximo de 15 dígitos.")

    telefone = forms.CharField(validators=[telefone_regex], max_length=15) # validators precisam ser listas


    class Meta:
        model = Cliente
        fields = ("nome",
                    "cpf_cnpj",
                    "telefone", "email",
                    "password1", "password2",)

    def clean(self):
        """
        Verifica se o que foi colocado nos campos passdword está correto

        Os erros irão aparecer em ``non_field_errors()`` pois foi aplicado em mais de um field.
        """
        cleaned_data = super(CadastroClienteForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(CadastroClienteForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user_p = User.objects.create_user(
            self.cleaned_data['nome'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'])
        user_p.save()
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.ModelForm):
    """
    Formulário de Login
    """
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['email', 'password']

    def get_user(self):
       try:
          return Cliente.objects.get(email=self.cleaned_data.get('email'))
       except Cliente.DoesNotExist:
          return None

class CadastroCampoForm(forms.ModelForm):
    nome = forms.CharField(required=True,max_length=20)
    descricao = forms.TextInput()
    horario_disponivel_de = forms.DateTimeInput()
    horario_disponivel_ate = forms.DateTimeInput()
    valor_hora = forms.FloatField()

    class Meta:
        model = Campo
        fields = ['nome', 'descricao',
                'horario_disponivel_de',
                'horario_disponivel_ate',
                'valor_hora',]

class CadastroReservaForm(forms.ModelForm):
    campo = forms.CharField(required=True,max_length=20)
    cliente = forms.CharField(required=True)
    reservado_de = forms.DateTimeInput()
    reservado_ate = forms.DateTimeInput()
    valor = forms.FloatField()

    class Meta:
        model = Reserva
        fields = ['campo', 'cliente',
                'reservado_de',
                'reservado_ate',
                'valor',]