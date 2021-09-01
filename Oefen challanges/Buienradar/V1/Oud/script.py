from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import configparser

# Hierin moet het volledige pad van het config bestand staan.
vollpad_conf = '/home/daan/Bureaublad/School/Github/fontys/Buienradar/config.ini'

config = configparser.ConfigParser()
config.read(vollpad_conf)

tijd = config['settings']['tijd']
locatie = config['settings']['locatie']

def start(lati, longi, tijd, locatie):

                timeframe = int(tijd)

                latitude = float(lati)
                longitude = float(longi) 

                result = get_data(latitude=latitude,
                                longitude=longitude,
                                )

                if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)
                
                locatie = locatie
                
                stringresult = str(result)
                
                # Tempratuur uit de string filteren.
                strtemp  = stringresult[3500:]
                tempvoor = strtemp.index("temperature': ") + 14
                tempachter = strtemp.index(" 'feeltemperature': ") - 1
                tempindex = strtemp[tempvoor:tempachter]

                # Gevoelstempratuur uit de string filteren.
                strgevoel  = stringresult[3500:]
                gevoelvoor = strgevoel.index("feeltemperature': ") + 18
                gevoelachter = strgevoel.index(" 'visibility': ") - 1
                gevoelindex = strgevoel[gevoelvoor:gevoelachter]

                # Windkracht uit de string filteren.
                strwindkracht = stringresult[3500:]
                windkrachtvoor = strwindkracht.index("windforce': ") + 12
                windkrachtachter = strwindkracht.index(" 'winddirection': ") - 1
                windkrachindex = strwindkracht[windkrachtvoor:windkrachtachter]

                # Windrichting uit de string filteren.
                strwindrichting = stringresult[3500:]
                windrichtingvoor = strwindrichting.index("winddirection': ") + 17
                windrichtingachter = strwindrichting.index(" 'windazimuth': ") - 2
                windrichtingindex = strwindrichting[windrichtingvoor:windrichtingachter]

                # Weerstation uit de string filteren.
                strstation = stringresult[3500:]
                stationvoor = strstation.index("stationname': ") + 15
                stationachter = strstation.index(" 'condition': ") - 9
                stationindex = strstation[stationvoor:stationachter]

                # Luchtvochtigheid uit de string filteren
                strvochtig = stringresult[3200:]
                vochtigvoor = strvochtig.index("humidity") + 11
                vochtigachter = strvochtig.index("groundtemperature") - 3
                vochtigindex = strvochtig[vochtigvoor:vochtigachter]
                
                # Meet tijd uit de string filteren
                strmeet = stringresult[3200:]
                meetvoor = strmeet.index("measured") + 42
                meetachter = strmeet.index("tzinfo") - 2
                meetindex = strmeet[meetvoor:meetachter]

                print()
                print ("Weeroverzicht van", locatie)
                print ("Voorspellingstijd", tijd, "minuten")
                print ()
                print ("Tempratuur:        ", tempindex)
                print ("Gevoelstempratuur: ", gevoelindex)
                print ("Windkracht:        ", windkrachindex)
                print ("Winrichting:       ", windrichtingindex)
                print ("Luchtvochtigheid:  ", vochtigindex,"%")
                print ("Weerstation:       ", stationindex)
                print ("Meet tijd:         ", meetindex)

                print ()
           

if locatie == "venray" or locatie == "Venray":
    start(lati = "51.525287", longi = "5.973349", tijd = tijd, locatie = "Venray")

elif locatie == "eindhoven" or locatie == "Eindhoven":
    start(lati = "51.450967", longi = "5.479683", tijd = tijd, locatie = "Eindhoven")

elif locatie == "hunsel" or locatie == "Hunsel":
    start(lati = "51.188768", longi = "5.813526", tijd = tijd, locatie = "Hunsel")

else: 
    print ("Locatie niet herkend/ondersteund")

    