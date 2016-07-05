from django.db import models
from django.core import validators
from photologue.models import Gallery


class Actor(models.Model):
    about = models.TextField(default="")
    full_name = models.CharField(max_length=128)
    feet_format = validators.RegexValidator('^[0-9\']*$', "Format must be e.g. 6'01")
    height_feet = models.CharField(max_length=4, help_text="Format: F'II e.g. 6'01 or 5'11", validators=[feet_format])
    height_meters = models.DecimalField(max_digits=3, decimal_places=2, help_text="Format: e.g. 1.83")
    HAIR_TYPES = [
        ('auburn',      "Auburn"),
        ('black',       "Black"),
        ('blond',       "Blond(e)"),
        ('darkbrown',   "Dark Brown"),
        ('fair',        "Fair"),
        ('grey',        "Grey"),
        ('greying',     "Greying"),
        ('lightbrown',  "Light/Mid Brown"),
        ('red',         "Red/Titian"),
        ('salt',        "Salt & Pepper"),
        ('sandy',       "Sandy"),
        ('silver',      "Silver"),
        ('strawblond', "Strawberry Blonde"),
        ('white',       "White"),
    ]
    hair_colour = models.CharField(max_length=10, choices=HAIR_TYPES, default='strawblonde')
    EYE_TYPES = [
        ('black',       "Black"),
        ('blue',        "Blue"),
        ('bluegreen',   "Blue-Green"),
        ('bluegrey',    "Blue-Grey"),
        ('brown',       "Brown"),
        ('green',       "Green"),
        ('grey',        "Grey"),
        ('greygreen',   "Grey-Green"),
        ('hazel',       "Hazel"),
        ('hbluebrown',  "Heterochromia - blue/brown"),
        ('hgreenblue',  "Heterochromia - green/blue"),
        ('hgreenbrown', "Heterochromia - green/brown"),
        ('hbluehazel',  "Heterochromia - blue/blue-hazel"),
        ('hcgreen',     "Heterochromia - Central Green"),
        ('hspecial',    "Heterochromia - distinct green and brown areas in both eyes"),
        ('lightblue',   "Light Blue"),
    ]
    eye_colour = models.CharField(max_length=10, choices=EYE_TYPES, default='brown')
    playing_age_min = models.IntegerField()
    playing_age_max = models.IntegerField()
    location = models.CharField(max_length=128)

    def __str__(self):
        return "{}".format(self.full_name)


class TheatreCredit(models.Model):
    first = models.DateField(help_text="Date of first performance.")
    final = models.DateField(help_text="Date of final performance.")
    performance = models.CharField(max_length=64)
    role = models.CharField(max_length=32)
    director = models.CharField(max_length=32, blank=True)
    venue = models.CharField(max_length=64, blank=True)
    location = models.CharField(max_length=32, blank=True)
    hidden = models.BooleanField(default=False)
    gallery = models.OneToOneField(Gallery, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.performance, self.final.year)


class Skill(models.Model):
    name = models.CharField(max_length=32, help_text="E.g. Piano")
    detail = models.TextField(help_text="E.g. Grade 5", blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    class Meta:
        verbose_name_plural = "education"
    institution = models.CharField(max_length=64, help_text="E.g. University of Bristol")
    start_date = models.DateField(blank=True)
    end_date = models.DateField()
    qualification = models.CharField(max_length=64, help_text="E.g. BA Media Studies")

    def start_year(self):
        return self.start_date.year

    def end_year(self):
        return self.end_date.year

    def __str__(self):
        return "{}, {}-{}".format(self.institution, self.start_date.year, self.end_date.year)


class ContactDetails(models.Model):
    class Meta:
        verbose_name_plural = "contact details"

    email = models.EmailField(max_length=128, help_text="E.g. sherlock_holmes@gmail.com", blank=True)
    phone = models.CharField(max_length=18, help_text="E.g. '07987 654 321' or '0041 234 56 78 90'", blank=True)
    address_line_1 = models.CharField(max_length=64, help_text="E.g. 221b Baker Street", blank=True)
    address_line_2 = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=32, help_text="E.g. London", blank=True)
    postcode = models.CharField(max_length=8, help_text="E.g. CL12 321", blank=True)
    spotlight = models.URLField(help_text="Link to your Spotlight profile", blank=True)

    def __str__(self):
        s = "Contact details"
        if len(self.email) > 0:
            s += ": {}".format(self.email)
        return s

