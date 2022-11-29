import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from sede.models import Sede

class SedeTestCase(TestCase):
    def setUp(self):
        Sede.objects.create(name="Cordoba", cod=123, tel=1231553)
        Sede.objects.create(name="BuenosAires", cod=222,tel= 3123132)

        sede_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(sede_test_num)
        ]
        self.mock_cods = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(sede_test_num)
        ]
        self.mock_tels = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(sede_test_num)
        ]
        

        for mock_name, mock_cod, mock_tel in zip(self.mock_names, self.mock_cods, self.mock_tels):
            Sede.objects.create(name=mock_name, cod=mock_cod,tel=mock_tel)

    def test_sede_model(self):
        
        Cordoba_sede = Sede.objects.get(name="Cordoba")
        BuenosAires_sede = Sede.objects.get(name="BuenosAires")
        self.assertEqual(Cordoba_sede.cod,123)
        self.assertEqual(BuenosAires_sede.cod,222)
        self.assertEqual(Cordoba_sede.tel,1231553)
        self.assertEqual(BuenosAires_sede.tel,3123132)
      

    def test_sede_list(self):
        for mock_name, mock_cod, mock_tel in zip(self.mock_names, self.mock_cods, self.mock_tels):
            sede_test = Sede.objects.get(name=mock_name)
            self.assertEqual(sede_test.cod, mock_cod)
            self.assertEqual(sede_test.tel, mock_tel)
            
