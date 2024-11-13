from django.db import models

# Create your models here.
class Configuracion(models.Model):
    texto_ayuntamiento = models.TextField(default="""El Ayuntamiento de Villanueva de las Cruces es el
        alma de un municipio lleno de encanto, historia y tradiciones. Con eventos
        como la “Candela” en honor a San Sebastián y una deliciosa gastronomía que
        incluye el potaje de gurumelos, este pintoresco pueblo de casas blancas
        invita  a vecinos y visitantes a disfrutar de su cultura y sentirse como un
        Cruceño más.""")