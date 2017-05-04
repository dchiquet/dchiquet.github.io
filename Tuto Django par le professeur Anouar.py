"""
    Concrètement Django fonctionne en apps et projets.
    
    Un projet Django est un site à proprement parler, une app peut-être plus ou moins tout ce qu'on veut.
    Une app contient:
        - Des vues (views.py)
        - Des modèles (models.py)
        - BASIC MVC
        - Des URL (urls.py)
        
    Disons que rageux que nous sommes, nous voulons recomposer Megaupload, un upload gratuit et libre et on se tape de ce qu'ils envoient.
    
    La structure nécessite qu'une app qui sera notre site.
    
    On installe Django (pip install Django sur la commande, pip étant le package manager de Python). Ensuite:
    
    django-admin startproject megakernel
    
    ça va créer un projet dans le dossier megakernel (bon, jusque là c'est plutôt normal non ?).
    
    Notre arbore(sse, désolé le modo)scence sera la suivante: 
        - megakernel/
        | - megakernel/
        . | - settings.py (Fichier qui contient la configuration du site)
        . | - urls.py (Le "routing" du site)
        . | - wsgi.py (on y fait pas attention pour l'instant)
        | - manage.py
        
    Normalement à ce stage, on crée une app à l'aide de la commande python manage.py startapp "Nom de l'App". Mais comme c'est un site pas très compliqué on va dire, on     va se contenter de faire une app pour le site.
    
    On va faire tout ça manuellement, on crée déjà le fichier apps.py dans le dossier megakernel/megakernel/. En fait, le dossier megakernel peut-être utilisé comme app     dans le cas où on sait que de toutes façons, on ne fera pas d'autres apps. 
"""

# megakernel/apps.py

from django.apps import AppConfig


class MegaKernelConfig(AppConfig):
    name = 'megakernel'

"""
    C'est cool, notre dossier est déjà considéré comme une app. Maintenant on va éditer le settings.py qui est contenu dans megakernel pour dire "Notre app existe,           ajoute-là."
"""

# megakernel/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'megakernel.apps.MegaKernelConfig',
]

"""
    Bon pour expliquer ce qu'on ajouter dans les "Installed apps", c'est la classe de config qu'on a faite (MegaKernelConfig). Décortiquons:
    
    'megakernel.apps.MegaKernelConfig'
    
    On dit à Django de chercher dans le dossier megakernel, puis dans apps (en fait, Python teste d'abord si c'est un fichier, ensuite il teste si c'est un dossier).
    Une fois qu'il a trouvé apps, il va prendre MegaKernelConfig.
    
    C'est les imports normaux en python, disons qu'on fait une classe dans un fichier a dans un dossier b. Pour l'importer, on fait:
    
    from b.a import c
    
    -------------------------------------------------------------------------------
    
    Bref, maintenant que notre dossier est compté comme une app grâce à nos éditions dans le fichier settings.py et l'ajout du apps.py, il faut faire en sorte à ce       que notre app affiche quelque chose. On va donc faire notre page d'accueil.
    
    On va créer un fichier views.py
"""

# megakernel/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse('Bienvenue sur Mega Kernel !')

"""
    Bon arrête ton shit, on a fait quoi là ?
    
    Déjà la première ligne nous permet d'importer la fonction HttpResponse, une fonction qui renvoie une réponse HTTP. (en fait, tout les serveurs font ça:
    
    Le client envoie une requête (GET ou POST ou d'autres plus compliquées) -> Le serveur traite -> Le serveur renvoie une réponse
    
    C'est le fonctionnement normal d'un serveur web).
    
    Quand on va dans une page pour y accéder simplement, on fait un GET. On demande l'accès à une page. Quand on envoie des données en serveur pour qu'elles soient
    traitées, c'est POST.
    
    Django fait pareil dans sa vue. Une vue prends une requête (le request en paramètre dans index), et renvoie une réponse. Si on enlève le return d'ailleurs et         qu'elle retourne rien, Django soulèvera une erreur "Response awaited but got NoneType instead" (j'voulais un pain au chocolat, j'ai payé, mais j'ai rien eu).
    
    Notre vue est correcte, maintenant on va router notre vue pour qu'elle aie une URL.
"""

# megakernel/urls.py (Avant)

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# megakernel/urls.py (Après)

from django.conf.urls import url
from django.contrib import admin
from . import views  # Ici, on importe d'abord la vue, le . signifie le dossier actuel, sachant que urls.py et views.py sont dans le même dossier.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]

"""
    Maintenant, si on démarre notre serveur à l'aide de la commande
    
    > python manage.py runserver
    
    Si on accède à localhost:8000 sur notre navigateur, on aura une page blanche avec texte noir: "Bienvenue sur Mega Kernel !".
    
    Vous l'aurez sûrement remarqué mais le fichier manage.py est plus ou moins la CLI pour le serveur.
    
    
    Bref c'est bien beau mais on est encore loin de notre but, vous trouvez pas ?
    On va commencer à réaliser le vrai shit. Déjà ajouter des modèles.
    
    Le modèle ici n'est pas le M de MVC. Ici, c'est dans l'idéologie de l'ORM (Object-relational Mapping). Une ORM consiste à prendre une table SQL et à la rapprocher     à une classe en Python.
    
    L'avantage ? PLEIN. Django est le framework web qui dispose de la meilleure ORM et permet d'éviter à 98% de taper une commande SQL directement pour simplifier         notre approche.
    
    Comme un exemple parle mieux qu'un long paragraphe ou une image, commencons:
"""

# megakernel/models.py

from django.db import models

class Uploader(models.Model):
    """
    Classe pour un gars qui envoie un fichier.
    """
    ip = models.CharField(max_length=15) #  Un CharField doit TOUJOURS contenir une valeur max_length (nombre max de caractères).
    
    def __str__(self):
        return self.ip

class Fichier(models.Model):
    """
    Classe pour un Fichier à contenir.
    """
    uploader = models.ForeignKey(Uploader, on_delete=models.CASCADE) #  On ajoute pas de propriété verbose_name car ce champ sera automatiquement rempli.
    name = models.CharField(max_length=80, verbose_name = 'Titre')
    desc = models.TextField(verbose_name = 'Description') #  TextField = CharField sans limite de caractères
    file = models.FileField(verbose_name = 'Fichier')
    date_of_upload = models.DateTimeField(auto_now=True) #  Pareil que pour le champ uploader
    #  ^ auto_now (si il est vrai) fera en sorte que la date à garder dans ce modèle sera automatiquement ajoutée à la création d'un objet.
    
    def __str__(self):
        return self.name
    
"""
    Bon. On a déjà fait quelque chose de pas mal non ? Ici chaque classe peut-être apparentée à une table SQL. Si vous avez déjà fait du SQL, vous devez sûrement d'ailleurs reconnaître le format des fields. CharField, TextField, FileField, ...
    
    Des explications s'imposent.
    
    Déjà, un champ ForeignKey n'est pas un champ mais une relation. C'est à dire qu'on l'associe à un autre modèle. Ici Uploader (premier paramètre du field).
    
    Maintenant, pourquoi une fonction __str__ ? C'est une spécificité à Python.
    
    Lorsqu'on fait par exemple:
    
    unfichier = Fichier(name='blabla')
    print(unfichier)

    Python affichera : "<Object Fichier at reference 0x4e894>". La fonction __str__ est une fonction qui dira quoi afficher lorsqu'on demandera de la représenter dans une chaîne de caractères comme ici. Maintenant, son utilité sur Django sera au moment de représenter le fichier dans l'espace admin (quand le FBI nous demandera de supprimer deux trois fichiers).
    
    Comme Naoki précise, il y a la Primary Key. Où est elle ?
    
    Sur un champ au hasard, on peut ajouter un paramètre "primary_key=True". Sinon qu'en est-il quand aucun n'en a comme maintenant ?
    
    Reprenons l'exemple d'au-dessus.
    
    print(unfichier.name) <-- Affiche "blabla"
    print(unfichier.id) <-- Affiche "0"
    
    Et voilà. Expliquons ça dans la définition de notre classe:
    
    class Fichier(models.Model) <-- Elle hérite de la classe Model !
    
    En héritant de Model, elle hérite de ses méthodes (Fonctions) et variables. Une variable est créée d'office en Clé primaire qui est ID. Elle existera toujours         même si vous choisissez un autre champ en primary_key (mais elle ne sera plus la clé primaire).
    
    Bref, maintenant mettons à jour notre base de données.
    
    Django a des migrations (des manifestes de changements par apps, en gros). Faisons celui de notre app.
    
    > python manage.py makemigrations megakernel
    
    Ici il va mentionner les changements fait. Maintenant qu'on a le manifeste, il faut créer la base de données.
    
    > python manage.py migrate
    
    Et voilà. Django est configuré de base pour utiliser SQLite3 donc aucun problème ça ira.
    
    > python manage.py createsuperuser
    
    On crée un super utilisateur. Pour l'espace admin. C'est tout, ne faites rien d'autre.
    
    Bref, maintenant il faudrait des vues qui fassent quelque chose non ? On va donc commencer les TEMPLATES.
    
    Un Template est un modèle de page (cette fois-ci, Modèle pour le MVC, HEIN QL) à la façon de Ruby on Rails. On va commencer ça par un formulaire.
    
    En effet, il nous faut bien un formulaire d'envoi de fichier, non ? Faisons un fichier forms.py
"""

# megakernel/forms.py

from django import forms

class FichierForm(forms.Form):
    name = forms.CharField(verbose_name = Titre)
    desc = forms.TextField(verbose_name = 'Description') #  TextField = CharField sans limite de caractères
    file = forms.FileField(verbose_name = 'Fichier')

"""
    'tin je me surprends à donner des cours comme ça /PAN
    
    Ici, un Form se rapproche d'un model. Sauf qu'on inclut pas les fields (champs) qui seront automatiquement gérés une fois dans le model.
    
    Maintenant qu'on a le formulaire, écrivons la vue.
"""

# megakernel/views.py (Avant)

from django.http import HttpResponse

def index(request):
    return HttpResponse('Bienvenue sur Mega Kernel !')

# megakernel/views.py (Après)

from django.shortcuts import render
from .forms import FichierForm

def index(request):
    form = FichierForm() #  On instancie le formulaire.
    return render(request, 'index.html', context={
        'form': form,
    }

"""
    Si ici on lance à nouveau le serveur, on aura une erreur à l'affichage de l'accueil.
    
    Le deuxième argument de return indique le template à charger (index.html), et il n'existe pas. Créons-le.
"""

# megakernel/settings.py

...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/' #  On a ajouté cette ligne.
        ],
...

# templates/index.html

<html>
    <body style="min-width: 100vw; min-height: 100vh;">
                
        <h1 style="text-align: center">MEGAKERNEL</h1>
        <h2 style="text-align: center">Envoyez un fichier sans avoir peur de Marine le Pen (ou de la CIA, surtout).</h2>
        {{ form }}
    </body>
</html>

"""
    Ce qu'on a fait là, c'est un template. Un fichier HTML avec un gabarit de Django. Vous ne reconnaissez pas le gabarit ? Je vais vous aider:
    
    {{ form }}
    
    Ce gabarit sert à afficher une variable traitée par Django. Ici, notre formulaire qu'on a définit dans la vue. Comment elle est passée de la vue au template ? Il     y a un paramètre context dans la fonction render que vous pouvez voir plus haut dans le fichier views.py.
    
    Bon plot twist, ça va pas trop marcher comme ça. Voilà la version entière du template:
"""

# templates/index.html

<html>
    <body style="min-width: 100vw; min-height: 100vh;">
                
        <h1 style="text-align: center">MEGAKERNEL</h1>
        <h2 style="text-align: center">Envoyez un fichier sans avoir peur de Marine le Pen (ou de la CIA, surtout).</h2>
        <form action="#" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Envoyer le fichier" />
        </form>
    </body>
</html>
                
"""
    Faites pas attention au csrf_token, c'est une balise (gabarit) à intégrer de force dans un formulaire pour empêcher le Cross-site Request Forgery (une attaque).       Django va vous taper sur les doigts si vous le faites pas donc donnez-vous la peine. ;)
    
    Bon. Pour l'instant notre fichier ne fait pas grand chose. Déjà, si le fichier est en ligne, on ne peut pas y accéder (car on ne connaît pas l'URL). Maintenant, il faut aussi que le formulaire fasse quelque chose, parce que rien ne se passera.
    
    Comme vous pouvez le voir, ici le formulaire enverra les données par POST. On va donc devoir changer notre vue pour qu'il prenne les données envoyées par le formulaire, mais comment ?
    
    Changeons le views.py
"""
                
# megakernel/views.py (Avant)

from django.shortcuts import render
from .forms import FichierForm

def index(request):
    form = FichierForm() #  On instancie le formulaire.
    return render(request, 'index.html', context={
        'form': form,
    }
                  
# megakernel/views.py (Après)

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FichierForm
from . import models

def index(request):
    if request.method == 'POST':
        form = FichierForm(request.POST)
        if form.is_valid():  # On vérifie si le formulaire est valide ou non.
            uder = models.Uploader()
            uder.ip = une_methode_au_hasard_pour_avoir_lip()
            uder.save()  # On sauvegarde l'uploader.
            fichier = models.Fichier()
            fichier.uploader = uder  # On lie le fichier à l'uploader.
            # Si le form est valide, un dictionnaire Python appelé cleaned_data contient les valeurs du formulaire.
            fichier.name = form.cleaned_data['name']
            fichier.desc = form.cleaned_data['desc']
            fichier.file = form.cleaned_data['file']
            fichier.save()
            return HttpResponseRedirect('/{}/'.format(fichier.id))  # Si l'upload est fait, on le redirige vers la page du fichier
    form = FichierForm()  # On instancie le formulaire.
    return render(request, 'index.html', context={
        'form': form,
    }

"""
    Une fois que tout ça est fait, il nous reste plus qu'à faire une page pour le fichier en question !
"""

# megakernel/views.py


from django.shortcuts import render, get_object_or_404
from .forms import FichierForm
from . import models

...

def fichier(request, id_du_fichier):
    file = get_object_or_404(models.Fichier, pk=id_du_fichier)  # Trouve le Fichier dans la base de données, sinon retourne une page 404.
    return render(request, 'fichier.html', context={
        'fichier': file,
    }

# megakernel/urls.py (Avant)

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]

# megakernel/urls.py (Après)

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'?P<id_du_fichier>[0-9]+)/', views.fichier, name='fichier'),
    url(r'^$', views.index, name='index'),
]

"""
    L'ordre ici compte beaucoup dans les urls, comme un programme lit de haut en bas, c'est pareil pour les URLs. Les URLs sont d'ailleurs des regex (Regular Expressions).

    Supposons l'adresse "megakernel.fr/059984651/".

    Ici on voudrait que ce soit la vue "fichier" qui soit appelée. Mais si la vue index était avant, elle serait appelée, pourquoi ?

    Parce que son URL convient, en effet, la regular expression stipule juste qu'il faut ^$, donc tout passe, également rien. C'est pour ça qu'on la met après la vue fichier. Parce que si elle est traitée dans l'ordre correct, alors l'adresse s'arrêtera à la vue fichier vu qu'elle correspond (il y a en effet un ID donné). Si rien n'est donné, on passe et donc, tombe sur l'index.

    Maintenant, on écrit simplement le template pour le fichier. Mais en mieux.
"""

# templates/base.html

<html>
    <body style="min-width: 100vw; min-height: 100vh;">
        {% block 'content' %}
        {% endblock %}
    </body>
</html>

# templates/fichier.html

{% extends 'base.html' %}

{% block 'content' %}
    Voilà le fichier numéro {{ fichier.id }}.

    <a href="{{ fichier.url }}">Télécharger</a>

    <a href="{% url 'index' %}">Retour au menu</a>
{% endblock %}

"""
    J'espère que je n'ai pas besoin d'explique ce que extends, block et endblock signifient. Concrètement, ces balises nous permettent d'hériter d'un fichier (et que d'un fichier, on ne peut pas faire en sorte qu'un template héritent de plusieurs fichiers, mais on peut faire en sorte que plusieurs templates s'héritent à la chaîne (genre base -> page_basique -> fichier). Pour le reste, on joue aux LEGO.

    Quant à la balise url, c'est Django qui se chargera de mettre l'URL correcte selon le nom qu'on a donné à l'URL dans notre fichier urls.py.

    VOILA. Nous avons fait un Megaupload like rapidement (en 442 lignes exactement). J'enregistre ça à côté si nécessaire. Mais maintenant vous avez une bonne idée de la simplicité de Django. Je vous invite à le découvrir par vous-même plus intensément et si vous avez besoin d'un très bon exemple d'utilisation de production de Django, regardez le projet Mangaki, c'est un projet auquel j'ai contribué. :p

https://github.com/mangaki/mangaki
"""