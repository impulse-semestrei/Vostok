from django.test import TestCase
from django.urls import reverse
from .forms import CrearMaterial
from .models import Material
from django.db.utils import IntegrityError


######## TESTS US36 ########


class CrearMaterialTestCase(TestCase):
    def test_url_correct(self):
        """
        Regresar un codigo 200
        """
        response = self.client.get(reverse('material:crear'))
        self.assertEqual(response.status_code, 200)

    def test_form_correct(self):
        """
        La forma es valida para guardarse en la bd
        """
        data = {
            'nombre': 'curita',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertTrue(form.is_valid())

    def test_form_incorrect(self):
        """
        La forma no es valida
        """
        data = {
            'nombre': '',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())

    def test_form_not_unique(self):
        """
        la forma no es valida, porque el nombre no es unico
        """
        Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        data = {
            'nombre': 'curita',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())

    def test_model_correct(self):
        """
        Se crea un material nuevo
        """
        Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        self.assertEqual(Material.objects.first().nombre, 'curita')

    def test_model_not_unique(self):
        """
        No se crea un material porque el material no es unico
        """
        Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        sent_exception = False
        try:
            Material.objects.create(nombre='curita', descripcion='duplicado')
        except IntegrityError:
            sent_exception = True
        self.assertEqual(Material.objects.find(nombre='curita').count(), 1)
        self.assertTrue(sent_exception)


######## TESTS US36 ########
