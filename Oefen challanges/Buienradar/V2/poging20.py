from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import discord
import os
import configparser
client = discord.Client()

def buienradar(inputlocatie, testmeet):
        templatitude = 0
        templongitude = 0

        locatie = inputlocatie
        print (locatie)

        if locatie == "Venray":
            templatitude = 51.525444
            templongitude = 5.972049
        
        if locatie == "Eindhoven":
            templatitude = 51.450967
            templongitude = 5.479683    

        timeframe = int(5)

        latitude = 51.525444
        longitude = 5.972049

        print (latitude, longitude)

        result = get_data(latitude=latitude,
                         longitude=longitude,
                                )

        if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)
                

                
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
        strstation = stringresult[3200:]
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

        locatieplaats = "Weeroverzicht van " + locatie
        voorspellingstijd = "Voorspellingstijd 5 minuten" 
        tempratuur = "Tempratuur: " + tempindex + " °C"
        gevoelstempratuur = "Gevoelstempratuur: " + gevoelindex + " °C" 
        windkracht = "Windkracht: " + windkrachindex
        windrichting = "Windrichting: " + windrichtingindex
        luchtvochtigheid = "Luchtvochtigheid: " + vochtigindex + " %"
        weerstation = "Weerstation: " + stationindex 
        meettijd = "Meettijd: " +meetindex

        testmeet = meettijd
        testlocatie = weerstation

        return (testlocatie, testmeet)

        #return (returnlocatieplaats, returnvoorspellingstijd, returntempratuur, returngevoelstempratuur, returnwindkracht, returnwindrichting, returnluchtvochtigheid, returnweerstation, returnmeettijd)

testlocatie = ""
testmeet = ""
reslocatie, testmeet = buienradar(testlocatie, testmeet)

@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('weer venray'):
        inputlocatie = "Venray"

        buienradar (inputlocatie, testmeet)

        await message.channel.send(reslocatie)
        await message.channel.send(testmeet)

client.run(token)
