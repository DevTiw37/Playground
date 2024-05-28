# A kilometer is equal to `0.621371` miles
# A mile is equal to `1.60934` kilometers

# Example output:
# 3 miles are equal to 4.8289 kilometers

# Type your code here:
def converMi2Km(miles):
  meters = miles * 1609.344
  kilometers = meters/1000
  return kilometers

miles_to_convert = 3
print(f"{miles_to_convert} miles is = {converMi2Km(miles_to_convert)} kilometers")

