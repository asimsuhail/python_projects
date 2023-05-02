import phonenumbers
from phonenumbers import timezone, carrier, geocoder

target_number   = input("enter phone number with country code")   # input the target number
number          = phonenumbers.parse(target_number)               # parse the number in specific format
target_timezone = timezone.time_zones_for_number(number)          # gets the timezon of number
target_carrier  = carrier.name_for_number(number,'en')            # network of number
target_reg      = geocoder.description_for_number(number, 'en')   # description of number region

print(number, target_timezone, target_reg, target_carrier)
