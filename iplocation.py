import turtle

ip=turtle.getIP()
print(ip)

country=turtle.getCountry(ip,'plain')
print(country)

country=turtle.getCountry(ip,'json')
print(country)

geodata=turtle.getGeoData(ip)
print(geoData)

ptrData=turtle.getPTR(ip)
print(ptrData)

turtle.showipDetails('216.239.32.0')

.showCountryDetails('216.239.32.0')
