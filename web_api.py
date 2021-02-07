import requests 
from bs4 import BeautifulSoup as bs 

kullanici_bilgi = {
    'UserName' : 'kazimhas96',
    'Password' : 'hXbtvxUNVOs',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
} 
def oturum():
    with requests.session() as s1 :

        url = 'https://www.itemsatis.com/index.php'
        
        r = s1.get(url ,headers = headers)
        
        soup = bs(r.content ,'html5lib')
        
        kullanici_bilgi['csrf_token'] = soup.find("input" , attrs={'name' :  'csrf_token'})['value']
        
        url = 'https://www.itemsatis.com/api/login.html'
        
        giris = s1.post(url,data=kullanici_bilgi,headers=headers)
        
        #print(giris.text)
        
        url = 'https://www.itemsatis.com/favori-ilanlarim.html'
        
        r = s1.get(url , headers = headers)
        
        return r.status_code

print(oturum())
