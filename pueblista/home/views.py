from django.shortcuts import render

# Create your views here.
def home(request):
    texto_ayuntamiento = """El Ayuntamiento de Villanueva de las Cruces es el alma de un municipio lleno de encanto, historia y tradiciones. Con eventos como la “Candela” en honor a San Sebastián y una deliciosa gastronomía que incluye el potaje de gurumelos, este pintoresco pueblo de casas blancas invita a vecinos y visitantes a disfrutar de su cultura y sentirse como un Cruceño más.
    """
    texto_pueblista = """ Pueblista es un equipo de cinco estudiantes de Ingeniería Informática de Sevilla. Apasionados por la vida en los pueblos, trabajamos para mejorar la vida rural mediante herramientas tecnológicas que fomenten el desarrollo y la conexión entre comunidades.\n Gracias a Pueblista, podrás disfrutar de tu pueblo como nunca antes habías imaginado.""" 
    return render(request, 'home.html', {"ayuntamiento": texto_ayuntamiento, "pueblista": texto_pueblista})