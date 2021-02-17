from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sqlite3

my_url = 'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=48d86383-47fc-48fb-a7a3-e9aecf885f73&as-searchtext=mobile'

#initilize data base
conn = sqlite3.connect('Flipkart.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Flipkart')
cur.execute('''CREATE TABLE Flipkart(
	"Name"	TEXT,
	"Rating"	INTEGER,
	"RAM"	TEXT,
	"ROM"	TEXT,
	"Storage Exp"	TEXT,
	"Display"	TEXT,
	"Rear Camera"	TEXT,
	"Front Camera"	TEXT,
	"Battery"	TEXT,
	"Processor"	INTEGER
);''')
#Request to url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#initilize soup
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class":"col col-7-12"})

product = 0
data = list
for container in containers:
    print(product)
    n = container.find("div", {"class": "_3wU53n"})
    name = n.text
    print(name)

    ratings = container.find("div", {"class": "niH0FQ"})
    ratings = ratings.text
    ratings = ratings.split(',')
    retings = ratings[0]
    print(retings)

    details = container.find("div", {"class": "_3ULzGw"})
    x = details.find("ul", {"class": "vFw0gD"})
    y = x.findAll("li",{"class":"tVe95H"})
    storage = y[0].text
    abc = storage.split('|')
    Ram = abc[0]
    Rom = abc[1]
    Exp = abc[2]

    Display = y[1].text

    Camera = y[2].text
    cam = Camera.split('|')
    rear = cam[0]
    front = cam[1]

    Battery = y[3].text

    Processor = y[4].text

    print("Ram = ",Ram)
    print("Rom = ",Rom)
    print("Expandable = ",Exp)
    print("Display = ",Display)
    print("Camera = ",Camera)
    print("Battery = ",Battery)
    print("Processor = ",Processor)
    cur.execute('INSERT INTO Flipkart VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(name, retings, Ram, Rom, Exp, Display, rear, front, Battery, Processor))
    conn.commit()
    print("===================================================================")
    product = product+1

cur.close()