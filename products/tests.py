from django.test import TestCase
from products.models import Product
from django.utils import timezone

# Create your tests here.
class test_Models(TestCase):
    @classmethod
    def setUp(self):
            self.product = Product()
            self.product.pub_date = timezone.datetime.now()
            self.product.title = 'Bong'
            self.product.url = 'https://kingbong.com.br/ice-bong-de-vidro-king-bong-strong-beaker.html'
            self.product.body = 'A família aumentou! Esta é mais uma das novidades da linha original King Bong. O Strong Beaker é não só muito bonito mas também muito eficiente. Seu estilo beaker é projetado especialmente parar evitar que a água chegue até a boca. Bong feito de vidro borossilicato grosso que garante alta durabilidade. Possui suporte de gelo para resfriar a fumaça e proporcionar sessões muito mais suaves e prazerosas. E, para fechar com chave de ouro, vem com elegante logo incolor da King Bong no tubo. Bong: Altura: 26cm Diâmetro da Base: 11cm Diâmetro Interno da Coluna: 3,5cm Entrada: 18mm Tubo Downstem: Comprimento: 11.5cm Encaixe: 18mm'
            self.product.hunter_id = 1
            self.product.save()

    def testTitle(self):
        title = self.product.__str__()
        self.assertTrue(isinstance(title, str))

    def testSummary(self):
        self.assertTrue(len(self.product.summary()) == 100)

    
    def tearDown(self):
        self.product.delete()