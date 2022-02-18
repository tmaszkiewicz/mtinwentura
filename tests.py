from django.test import TestCase,Client
from .models import indeks_bazowy

# Create your tests here.
class mtinw_pc2(TestCase):
    def setUp(self):
        indeks_bazowy.objects.create(barcode="70105037")
    

    def test_mtinw_pc2(self):
        c = Client()
        resp = c.post('/mtinwentura/mtinw_pc2/',{})
        self.assertEqual(resp.status_code,200)

class przeslij_zlicz(TestCase):
    def test_przeslij_zlicz(self):
        c = Client()
        resp = c.post('/mtinwentura/przeslij_zlicz/',{'barcode':'123','skaner':'mt1','ilosc':'1','nazwa':'sdfsdf',})
        self.assertEqual(resp.status_code,200)

class przeslij_inw(TestCase):
    def test_przeslij_inw(self):
        bar = "70105032"
        indeks_bazowy.objects.create(barcode=bar)
        c = Client()
        resp = c.post('/mtinwentura/przeslij_inw/',{'barcode':bar,'skaner':'mt1','ilosc':'1',})
        #resp = c.post('/mtinwentura/przeslij_inw/',{'barcode':'123','skaner':'mt1','ilosc':'1'})
        self.assertEqual(resp.status_code,200)
