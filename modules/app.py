import packages.shipping_ecommerce  # importing another package, then a file
from packages.shipping_ecommerce import calc_shipping
from packages import shipping_ecommerce


import converters  # importing another file
from converters import kg_to_lbs  # this is only for one function, instead of the full module

print(converters.lbs_to_kg(160))
print(kg_to_lbs(80))

# calling
packages.shipping_ecommerce.calc_shipping()
print(calc_shipping())
print(shipping_ecommerce.calc_shipping())
