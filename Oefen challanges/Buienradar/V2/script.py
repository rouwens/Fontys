from buienradar.buienradar import (get_data, parse_data)
from buienradar.constants import (CONTENT, RAINCONTENT, SUCCESS)
import configparser
import discord
client = discord.Client()

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


                # Vanaf hier begint het Discord gedeelte
                client = discord.Client()

                # De uitkomsten van Buienradar worden omgezet naar strings die door de bot worden uitgelezen.
                locatie = "Weeroverzicht van " + locatie
                voorspellingstijd = "Voorspellingstijd " + tijd + " minuten" 
                tempratuur = "Tempratuur: " + tempindex + " °C"
                gevoelstempratuur = "Gevoelstempratuur: " + gevoelindex + " °C" 
                windkracht = "Windkracht: " + windkrachindex
                windrichting = "Windrichting: " + windrichtingindex
                luchtvochtigheid = "Luchtvochtigheid: " + vochtigindex + " %"
                weerstation = "Weerstation: " + stationindex 
                meettijd = "Meettijd: " +meetindex

                channel = client.get_channel(785889829522243617)

                await channel.send(locatie)
                await channel.send(voorspellingstijd)
                await channel.send("-----------------")
                await channel.send(tempratuur)
                await channel.send(gevoelstempratuur)
                await channel.send(windkracht)
                await channel.send(windrichting)
                await channel.send(luchtvochtigheid)
                await channel.send(weerstation)
                await channel.send(meettijd)

                return

@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('weer venray'):
        start(lati = "51.525287", longi = "5.973349", tijd = tijd, locatie = "Venray")
        await message.channel.send("weer venray"

    if message.content.startswith('weer eindhoven'):
        await message.channel.send("weer eindhoven"

    if message.content.startswith('weer hunsel'):
        await message.channel.send("weer hunsel"

client.run(TOKEN)
