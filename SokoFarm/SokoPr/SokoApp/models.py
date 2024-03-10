from django.db import models
from django.utils import timezone
from django import forms



class MyModel(models.Model):
    image = models.ImageField(upload_to='img/')

class Category(models.Model):
     CATEGORY_CHOICES = [
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Potatoes', 'Potatoes'),
        ('Cereals', 'Cereals'),
        ('Onions', 'Onions'),
        ('Spices', 'Spices'),
        ('Birds', 'Birds & Products'),
        ('Animals', 'Animals & Products'),
        ('Feeds', 'Feeds'),
        ('Seedlings', 'Seedlings'),
        ('Farm Inputs', 'Farm Inputs'),
        ('Farm Machinery', 'Farm Machinery'), 
    ]
     name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    

#class Subcategory(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #name = models.CharField(max_length=100)

class Product(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')    
    
   
    COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cabo Verde', 'Cabo Verde'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo (Congo-Brazzaville)', 'Congo (Congo-Brazzaville)'),
        ('Costa Rica', 'Costa Rica'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czechia (Czech Republic)', 'Czechia (Czech Republic)'),
        ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Eswatini (fmr. "Swaziland")', 'Eswatini (fmr. "Swaziland")'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Holy See', 'Holy See'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar (formerly Burma)', 'Myanmar (formerly Burma)'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('North Korea', 'North Korea'),
        ('North Macedonia', 'North Macedonia'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestine State', 'Palestine State'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Korea', 'South Korea'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Timor-Leste', 'Timor-Leste'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States of America', 'United States of America'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')
    ]
    
    
    COUNTY_CHOICES = [
        ('Baringo', 'Baringo'),
        ('Bomet', 'Bomet'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
        ('Embu', 'Embu'),
        ('Garissa', 'Garissa'),
        ('Homa Bay', 'Homa Bay'),
        ('Isiolo', 'Isiolo'),
        ('Kajiado', 'Kajiado'),
        ('Kakamega', 'Kakamega'),
        ('Kericho', 'Kericho'),
        ('Kiambu', 'Kiambu'),
        ('Kilifi', 'Kilifi'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Kisii', 'Kisii'),
        ('Kisumu', 'Kisumu'),
        ('Kitui', 'Kitui'),
        ('Kwale', 'Kwale'),
        ('Laikipia', 'Laikipia'),
        ('Lamu', 'Lamu'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Mandera', 'Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Meru', 'Meru'),
        ('Migori', 'Migori'),
        ('Mombasa', 'Mombasa'),
        ('Murang’a', 'Murang’a'),
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Nandi', 'Nandi'),
        ('Narok', 'Narok'),
        ('Nyamira', 'Nyamira'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Samburu', 'Samburu'),
        ('Siaya', 'Siaya'),
        ('Taita-Taveta', 'Taita-Taveta'),
        ('Tana River', 'Tana River'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Trans-Nzoia', 'Trans-Nzoia'),
        ('Turkana', 'Turkana'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Vihiga', 'Vihiga'),
        ('Wajir', 'Wajir'),
        ('West Pokot', 'West Pokot')
    ]

    # Override the category, subcategory, county, and country fields in the form
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    county = forms.ChoiceField(choices=COUNTY_CHOICES)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)

    name = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    description = models.TextField(default='')
    additional_info = models.TextField(default='')
    subcategory = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    county = forms.ChoiceField(choices=COUNTY_CHOICES)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)
    price = models.CharField(max_length=15)
    quantity = models.CharField(max_length=20)
    ready_for_purchase = models.BooleanField()
    purchase_timeframe = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to the current date and time on creation
    contacts = models.CharField(max_length=15)

def __str__(self):
    return self.name




# Create your models here.
