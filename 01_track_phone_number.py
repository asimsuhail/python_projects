import phonenumbers
from phonenumbers import timezone, carrier, geocoder

target_number = input("enter phone number with country code")
number        = phonenumbers.parse(target_number)
target_timezone = timezone.time_zones_for_number(number)
target_carrier  = carrier.name_for_number(number,'en')
target_reg      = geocoder.description_for_number(number, 'en')

print(number, target_timezone, target_reg, target_carrier)