from django.test import TestCase
from django.urls import reverse
from .forms import CrearMaterial
from .models import Material
from django.db import IntegrityError, transaction


######## TESTS US36 ########


class CrearMaterialTestCase(TestCase):
    def setUp(self):
        Material.objects.create(nombre='curita', descripcion='proteccion de herida', cantidad=4)

    def test_url_correct(self):
        """
        Regresar un codigo 200
        """
        response = self.client.get(reverse('material:crear'))
        self.assertEqual(response.status_code, 302)

    def test_form_correct(self):
        """
        La forma es valida para guardarse en la bd
        """
        data = {
            'codigo': 'codigo1',
            'nombre': 'alcohol',
            'descripcion': 'desinfección',
            'cantidad': 4,
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
            'cantidad': '',
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())

    def test_form_not_unique(self):
        """
        la forma no es valida, porque el nombre no es unico
        """
        data = {
            'nombre': 'curita',
            'descripcion': 'proteccion de herida',
            'cantidad': 10
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())

    def test_model_correct(self):
        """
        Se crea un material nuevo
        """
        self.assertEqual(Material.objects.first().nombre, 'curita')

    def test_model_not_unique(self):
        """
        No se crea un material porque el material no es unico
        """
        sent_exception = False
        try:
            with transaction.atomic():
                Material.objects.create(nombre='curita', descripcion='duplicado', cantidad= 10)
        except IntegrityError:
            sent_exception = True
        self.assertEqual(Material.objects.filter(nombre='curita').count(), 1)
        self.assertTrue(sent_exception)

######## TESTS US36 ########


######## TESTS US38 ########
class VerMaterialTestCase(TestCase):
    def test_verMaterialURL(self):
        response = self.client.get(reverse('material:ver_material'))
        self.assertEqual(response.status_code, 302)

######## TESTS US38 ########


# ------- TESTS US 34 -------

class EditarMaterialTests(TestCase):
    def test_editarMaterialName(self):
        Material.objects.create(nombre='Test', descripcion='Material for test', cantidad = 5)
        self.client.get('material:editar_material',)

