from django.db import models
from cart.models import Cart
from payment.models import Payment
from django.conf import settings


class State(object):
    CHOICES = [("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
               ("Andhra Pradesh", "Andhra Pradesh"),
               ("Arunachal Pradesh", "Arunachal Pradesh"),
               ("Assam", "Assam"),
               ("Bihar", "Bihar"),
               ("Chandigarh", "Chandigarh"),
               ("Chattisgarh", "Chattisgarh"),
               ("Dadra & Nagar Haveli", "Dadra & Nagar Haveli"),
               ("Daman and Diu", "Daman and Diu"),
               ("Delhi", "Delhi"),
               ("Goa", "Goa"),
               ("Gujarat", "Gujarat"),
               ("Haryana", "Haryana"),
               ("Himachal Pradesh", "Himachal Pradesh"),
               ("Jammu & Kashmir", "Jammu & Kashmir"),
               ("Jharkhand", "Jharkhand"),
               ("Karnataka", "Karnataka"),
               ("Kerala", "Kerala"),
               ("Lakshadweep", "Lakshadweep"),
               ("Madhya Pradesh", "Madhya Pradesh"),
               ("Maharashtra", "Maharashtra"),
               ("Manipur", "Manipur"),
               ("Meghalaya", "Meghalaya"),
               ("Mizoram", "Mizoram"),
               ("Nagaland", "Nagaland"),
               ("Odisha", "Odisha"),
               ("Pondicherry", "Pondicherry"),
               ("Punjab", "Punjab"),
               ("Rajasthan", "Rajasthan"),
               ("Sikkim", "Sikkim"),
               ("Tamilnadu", "Tamilnadu"),
               ("Telangana", "Telangana"),
               ("Tripura", "Tripura"),
               ("Uttar Pradesh", "Uttar Pradesh"),
               ("Uttarakhand", "Uttarakhand"),
               ("West Bengal", "West Bengal"),
               ]


class ResidenceType:
    RENTED = "RENTED_SELF"
    RENTED_FAMILY = "RENTED_FAMILY"
    OWNED_BY_SELF = "OWNED_BY_SELF"
    OWNED_BY_SPOUSE = "OWNED_BY_SPOUSE"
    OWNED_BY_PARENTS = "OWNED_BY_PARENTS"
    OWNED_BY_RELATIVES = "OWNED_BY_RELATIVES"

    CHOICES = (
        (RENTED, "Rented/Leased-Self"),
        (RENTED_FAMILY, "Rented/Leased by Family"),
        (OWNED_BY_SELF, "Owned by self"),
        (OWNED_BY_SPOUSE, "Owned by Spouse"),
        (OWNED_BY_PARENTS, "Owned by Parents"),
        (OWNED_BY_RELATIVES, "Owned by Relative")
    )


class City(models.Model):
    name = models.SlugField(max_length=50, null=True, blank=True)
    display_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    state = models.CharField(max_length=200, choices=State.CHOICES, null=True)
    related_city = models.ManyToManyField("self", blank=True)
    parent_city = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name='child_cities',
                                    help_text="website will show parent city's cars too in listing page")
    exchange_serviceable = models.BooleanField(default=False, null=True)
    lead_tat = models.IntegerField(default=120, null=True, help_text="Threshold in days for HIGH TAT flag")


class Locality(models.Model):
    city = models.ForeignKey(City, blank=True, on_delete=models.CASCADE)
    name = models.SlugField(max_length=50, null=True)
    display_name = models.CharField(max_length=50)


class ContactDetails(models.Model):
    RELATIONCHOICES = (
        ('work', 'Work'),
        ('home', 'Home'),
        ('random', 'Random'))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=True, blank=True)
    address_line_1 = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    contact_number = models.CharField(max_length=13, null=True, blank=True, db_index=True)
    alternate_contact_number = models.CharField(
        max_length=13, null=True, blank=True, db_index=True)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50, null=True)
    locality = models.ForeignKey(Locality, null=True, blank=True, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    relation = models.CharField(max_length=30, default='work')
    start_of_living_year = models.PositiveIntegerField(null=True)
    residence_type = models.CharField(max_length=100, choices=ResidenceType.CHOICES, null=True, blank=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    active = models.BooleanField(default=True)


class Order(models.Model):
    contact_details = models.ForeignKey(ContactDetails, null=True, on_delete=models.PROTECT)
    models.DateTimeField(auto_now_add=True, db_index=True)
    cart = models.OneToOneField(Cart, null=True, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True, db_index=True)