from django.contrib.auth.models import User
from django.db import models


class Recherche(models.Model):
    first_name = models.CharField("Prénom", max_length=50)
    last_name = models.CharField("Nom", max_length=50)
    description = models.TextField("Description")
    is_valid = models.BooleanField("Validation", default=False)
    linked_id_user = models.PositiveIntegerField("linked_id_user", default=0)

    # gestionnaire sollicité
    CHOICES = [
        ('CHU Limoges - 2 avenue Martin Luther King, 87042 Limoges Cedex', 'CHU Limoges - 2 avenue Martin Luther '
                                                                           'King, 87042 Limoges Cedex'),
    ]
    gest_soll = models.CharField(
        "Gestionaire sollicité",
        max_length=70,
        choices=CHOICES,
        default='CHU Limoges - 2 avenue Martin Luther King, 87042 Limoges Cedex',
    )

    # phase1 : initialisation
    proj_name = models.CharField("Titre complet du projet", max_length=50)  # projet titre complet
    proj_acronym = models.CharField("Accronyme du projet", max_length=10)
    proj_public_title = models.CharField("Titre grand public du projet", max_length=50)  # projet titre grand public

    but_proj = models.BooleanField(
        "Etude réalisée dans le cadre du parcours de formation (étudiant, thèse, mémoire, etc) ?",
        default=False,
    )
    date_but_proj = models.DateField("Date de soutenance")

    publ_proj = models.BooleanField(
        "Publication prévue ?",
        default=False,
    )
    date_publ_proj = models.DateField("Date de publication")

    etu_proj_choice = [
        ('Etude mono-service', 'Etude mono-service'),
        ('Etude multi-service', 'Etude multi-service'),
        ('Etude multicentrique', 'Etude multicentrique'),
    ]
    etu_proj = models.CharField("Type d'Etudes", choices=etu_proj_choice, max_length=70)

    finality_search_choice = [
        ('Biologie', 'Biologie'),
        ('Medecine', 'Medecine'),
        ('Santé publique', 'Santé publique'),
        ('Sciences humaines', 'Sciences humaines'),
        ('Sciences sociales', 'Sciences sociales'),
        ('Autres (A preciser)', 'Autres (A preciser)'),
    ]
    finality_search = models.CharField("Finalité de la recherche", choices=finality_search_choice, max_length=70)

    other_finality_search = models.CharField("Autres finalités de la recherche", blank=True, max_length=50)

    type_search_choice = [
        ('Cohorte Fixe', 'Cohorte Fixe'),
        ('Cohorte Dynamique', 'Cohorte Dynamique'),
        ('Cohorte prospective', 'Cohorte prospective'),
        ('Cohorte rétrospective', 'Cohorte rétrospective'),
        ('Contrôle de cas', 'Contrôle de cas'),
        ('Cas seul', 'Cas seul'),
        ('Crossover de cas', 'Crossover de cas'),
        ('Études écologiques ou communautaires', 'Études écologiques ou communautaires'),
        ('Basée sur la famille', 'Basée sur la famille'),
        ('Autres (A preciser)', 'Autres (A preciser)'),
    ]
    type_search = models.CharField("Type de recherche/Objectif/Intérêt pour la santé publique",
                                   choices=type_search_choice, max_length=70)

    other_type_search = models.TextField("Autres type de recherche", blank=True)

    # TRAITEMENTS – STRATEGIES – PROCEDURES – SCHEMA DE LA RECHERCHE
    description_treatment1 = models.TextField("Description briève de la démarche prévue")

    description_treatment2 = models.TextField(
        "Description des principales caractéristiques de la recherche (étude comparative, descriptive, etc)")

    def __str__(self):
        return self.last_name + " " + self.first_name + " - " + self.description

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name == "linked_id_user":
                pass
            else:
                yield field.verbose_name.title(), field.value_to_string(self)


class Comment(models.Model):
    id_recherche = models.IntegerField()
    username_writer = models.CharField(max_length=30)
    role_writer = models.CharField(max_length=50)
    message = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username_writer + "[" + self.role_writer + "] : " + self.message
