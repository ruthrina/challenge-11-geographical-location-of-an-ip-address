import geocoder

def get_ip_location(ip_address):

    location = geocoder.ip(ip_address)
    return location

ip_address ='1.1.1.1'

ip_location = get_ip_location(ip_address)

print(f"IP ADDRESS: {ip_address}")
print(f"LOCATION: {ip_location.latlng}")
print(f"CITY: {ip_location.city}")
print(f"COUNTRY: {ip_location.country}")