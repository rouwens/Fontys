from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import discord
import os
client = discord.Client()

inputlat = "leeg"
inputlong = "leeg"
inputlocatie = "leeg"


@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('weer venray'):
        inputlat = float(51.525287)
        inputlong = float(5.973349)
        inputlocatie = "Venray"

        timeframe = int(5)

        latitude = float(inputlat)
        longitude = float(inputlong) 

        result = get_data(latitude=latitude,
                         longitude=longitude,
                                )

        if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)
                
        locatie = inputlocatie
                
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

        locatie = "Weeroverzicht van " + locatie
        voorspellingstijd = "Voorspellingstijd 5 minuten" 
        tempratuur = "Tempratuur: " + tempindex + " °C"
        gevoelstempratuur = "Gevoelstempratuur: " + gevoelindex + " °C" 
        windkracht = "Windkracht: " + windkrachindex
        windrichting = "Windrichting: " + windrichtingindex
        luchtvochtigheid = "Luchtvochtigheid: " + vochtigindex + " %"
        weerstation = "Weerstation: " + stationindex 
        meettijd = "Meettijd: " +meetindex

        await message.channel.send(locatie)
        await message.channel.send(voorspellingstijd)
        await message.channel.send("-----------------")
        await message.channel.send(tempratuur)
        await message.channel.send(gevoelstempratuur)
        await message.channel.send(windkracht)
        await message.channel.send(windrichting)
        await message.channel.send(luchtvochtigheid)
        await message.channel.send(weerstation)
        await message.channel.send(meettijd)
    
    if message.content.startswith('weer eindhoven'):
        inputlat = float(51.450967)
        inputlong = float(5.479683)
        inputlocatie = "Eindhoven"

        timeframe = int(5)

        latitude = float(inputlat)
        longitude = float(inputlong) 

        result = get_data(latitude=latitude,
                         longitude=longitude,
                                )

        if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)
                
        locatie = inputlocatie
                
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

        locatie = "Weeroverzicht van " + locatie
        voorspellingstijd = "Voorspellingstijd 5 minuten" 
        tempratuur = "Tempratuur: " + tempindex + " °C"
        gevoelstempratuur = "Gevoelstempratuur: " + gevoelindex + " °C" 
        windkracht = "Windkracht: " + windkrachindex
        windrichting = "Windrichting: " + windrichtingindex
        luchtvochtigheid = "Luchtvochtigheid: " + vochtigindex + " %"
        weerstation = "Weerstation: " + stationindex 
        meettijd = "Meettijd: " +meetindex

        await message.channel.send(locatie)
        await message.channel.send(voorspellingstijd)
        await message.channel.send("-----------------")
        await message.channel.send(tempratuur)
        await message.channel.send(gevoelstempratuur)
        await message.channel.send(windkracht)
        await message.channel.send(windrichting)
        await message.channel.send(luchtvochtigheid)
        await message.channel.send(weerstation)
        await message.channel.send(meettijd)
    
    if message.content.startswith('weer hunsel'):
        inputlat = float(51.188768)
        inputlong = float(5.813526)
        inputlocatie = "Hunsel"

        timeframe = int(5)

        latitude = float(inputlat)
        longitude = float(inputlong) 

        result = get_data(latitude=latitude,
                         longitude=longitude,
                                )

        if result.get(SUCCESS):
                    data = result[CONTENT]
                    raindata = result[RAINCONTENT]

                    result = parse_data(data, raindata, latitude, longitude, timeframe)
                
        locatie = inputlocatie
                
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

        locatie = "Weeroverzicht van " + locatie
        voorspellingstijd = "Voorspellingstijd 5 minuten" 
        tempratuur = "Tempratuur: " + tempindex + " °C"
        gevoelstempratuur = "Gevoelstempratuur: " + gevoelindex + " °C" 
        windkracht = "Windkracht: " + windkrachindex
        windrichting = "Windrichting: " + windrichtingindex
        luchtvochtigheid = "Luchtvochtigheid: " + vochtigindex + " %"
        weerstation = "Weerstation: " + stationindex 
        meettijd = "Meettijd: " +meetindex

        await message.channel.send(locatie)
        await message.channel.send(voorspellingstijd)
        await message.channel.send("-----------------")
        await message.channel.send(tempratuur)
        await message.channel.send(gevoelstempratuur)
        await message.channel.send(windkracht)
        await message.channel.send(windrichting)
        await message.channel.send(luchtvochtigheid)
        await message.channel.send(weerstation)
        await message.channel.send(meettijd)

client.run(TOKEN)

print (inputlocatie)
