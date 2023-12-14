import re

search = "Mini"
product = "Apple iPad Mini 6 2021 256 GB Cellular"

# One way is to check if the search string is a sub string of the product
if search in product:
    print("Product found")
else:
    print("Product not found")

# The other way is to use regex Expressions to check if the string exists
if re.match(search, product) is None:
    print("Product not found")
else:
    print("Product found")

# However if the case of the search string doesn't matter
# We can always change it all to lower case and check
if search.lower() in product.lower():
    print("Product found")
else:
    print("Product not found")
# Or even Upper Case too
if search.upper() in product.upper():
    print("Product found")
else:
    print("Product not found")
