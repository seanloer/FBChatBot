import fbchat,requests

def getW():
    #url='http://opendata2.epa.gov.tw/AQX.json'
    #raw=requests.get(url)
    #data=raw.json()
    msg=''
    #for x in data:
        #if x[u'County']=='臺中市':
            #print('PM2.5: '+x['PM2.5'])
            #msg+=x['SiteName']+'的PM2.5: '+x['PM2.5']+'\n'
    #subclass fbchat.Client and override required methods
    appid='&appid=f0053f6b5de58103d6f23aff3bafb101'
    #API DOC=>http://openweathermap.org/current
    url='http://api.openweathermap.org/data/2.5/weather?q='
    city='taichung'
    raw=requests.get(url+city+appid)
    data=raw.json()

    print('城市: '+str(data['name']))
    print('濕度: '+str(data['main']['humidity']))
    #溫度轉換:https://zh.wikipedia.org/wiki/%E6%91%84%E6%B0%8F%E6%B8%A9%E6%A0%87
    print('溫度: '+str(int(data['main']['temp'])-273.0))
    print()
    Wtotal='城市: '+str(data['name'])+'\n濕度: '+str(data['main']['humidity'])+'\n溫度: '+str(int(data['main']['temp'])-273.0)

    msg+=Wtotal
    return msg


def getNO2():
    url='http://opendata2.epa.gov.tw/AQX.json'
    raw=requests.get(url)
    data=raw.json()
    msg=''
    
    for x in data:   
        if x[u'County']=='臺中市':
            print('NO2: '+x['NO2'])
            Ntotal=x['SiteName']+': '+x['NO2']+'\n'
            
    msg+='台中市的NO2:\n'+Ntotal
    return msg

def getPM():
    url='http://opendata2.epa.gov.tw/AQX.json'
    raw=requests.get(url)
    data=raw.json()
    msg=''
    
    for x in data:
        if x[u'County']=='臺中市':
            print('PM2.5: '+x['PM2.5'])
            Ptotal=x['SiteName']+': '+x['PM2.5']+'\n'
            
    msg+='台中市的PM2.5:\n'+Ptotal
    return msg

def getP():
    #url='http://opendata2.epa.gov.tw/AQX.json'
    #raw=requests.get(url)
    #data=raw.json()
    msg=''
    #for x in data:
        #if x[u'County']=='臺中市':
            #print('PM2.5: '+x['PM2.5'])
            #msg+=x['SiteName']+'的PM2.5: '+x['PM2.5']+'\n'
    #subclass fbchat.Client and override required methods
    appid='&appid=f0053f6b5de58103d6f23aff3bafb101'
    #API DOC=>http://openweathermap.org/current
    url='http://api.openweathermap.org/data/2.5/weather?q='
    city='taichung'
    raw=requests.get(url+city+appid)
    data=raw.json()

    print('城市: '+str(data['name']))
    print('經度: '+str(data['coord']['lon']))
    #溫度轉換:https://zh.wikipedia.org/wiki/%E6%91%84%E6%B0%8F%E6%B8%A9%E6%A0%87
    print('緯度: '+str(data['coord']['lat']))
    Ptotal='經度: '+str(data['coord']['lon'])+'\n緯度: '+str(data['coord']['lat'])

    msg+=Ptotal
    return msg

class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read

        print("%s said: %s"%(author_id, message))

        #if you are not the author, echo
        if str(author_id) != str(self.uid):
            if message.upper()=='天氣':
                self.send(author_id,getW())
            if message.upper()=='NO2':
                self.send(author_id,getNO2())
            if message.upper()=='PM2.5':
                self.send(author_id,getPM())
            if message.upper()=='位置':
                self.send(author_id,getP())                    
            else:
                self.send(author_id,'聽不懂你的意思，請重新輸入')

bot = EchoBot("seanloerwei@gmail.com", "seanloerwei3")
bot.listen()
