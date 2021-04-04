from datetime import date
from flask import Flask, redirect, request, url_for, render_template, session
from bs4 import BeautifulSoup
import requests

import sqlite3

import sys


app = Flask(__name__)       # our Flask app

app.secret_key= "super secret key" #For accessing session

DB_FILE = 'mydb'            # file for our Database


#inserting content in the databases


class insertTable:

    def insertingTable(var1, var2, var3, var4, var5, var6):

        connection= sqlite3.connect(DB_FILE)

        cursor=connection.cursor()

        cursor.execute("insert into stocks VALUES (?, ?, ?, ?, ?, ?)", (var1, var2, var3, var4, var5, var6))

        connection.commit()

        cursor.close()


def _insert(name, email, comment ):


    """

    put a new entry in the database

    """

    params = {'name':name, 'email':email, 'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()  
    cursor.execute("insert into guestbook wVALUES (:name, :email, :comment)",params)
    connection.commit()
    cursor.close()


def _insertuser(name, email, username, password ):

    """

    put a new entry in the database

    """

    params = {'name':name, 'email':email, 'username':username, 'password':password}

    connection = sqlite3.connect(DB_FILE)

    cursor = connection.cursor()  

    cursor.execute("insert into account VALUES (:name, :email, :username, :password)",params)
    connection.commit()
    cursor.close()

#routing a specific url


@app.route('/')

def index():

  return render_template('index.html')


@app.route('/registration')


def registration():

    return render_template('registration.html')


@app.route('/aboutUs')

def aboutUs():

    aboutUspage=requests.get("https://www.emirates.com/ae/english/?page=/ae/english/")
    aboutsoup = BeautifulSoup(aboutUspage.content, 'html.parser')
    mainHeading=aboutsoup.find(class_={'hero__title'})
    textContent1=mainHeading.find(class_={'hero__subheading'})
    text1=textContent1.get_text()
    textContent2=mainHeading.find(class_={'hero__heading'})
    text2=textContent2.get_text()
    textContent3=mainHeading.find(class_={'hero__description'})
    text3=textContent3.get_text()

    return render_template('aboutUs.html', text1=text1, text2=text2,text3=text3)


@app.route('/contact')

def contact():


    return render_template('contact.html')



@app.route('/information')

def information():


    return render_template('information.html')


@app.route('/fsa')


def fsa():


   return render_template('fsa.html')



"""Posting content in the etihad database"""

@app.route('/etihadAir', methods=['POST','GET'])

def etihadAir():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from etihad")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('etihadAir.html', comments=rv)

"""Mehtod for posting comment and redirecting to the template"""

@app.route('/etihadc', methods=['POST'])

def etihadc():

    _newetihadc(session['username'], request.form['comment'])

    return redirect(url_for('etihadAir'))


"""Filling the username and their comments in the database"""

def _newetihadc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into etihad values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/turkishAir', methods=['POST','GET'])

def turkishAir():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from turkish")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('turkishAir.html', comments=rv)


@app.route('/turkishc', methods=['POST'])

def turkishc():

    _newturkishc(session['username'], request.form['comment'])

    return redirect(url_for('turkishAir'))


def _newturkishc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into turkish values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/emiratesAir', methods=['POST','GET'])

def emiratesAir():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from emirates")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('emiratesAir.html', comments=rv)


@app.route('/emiratesc', methods=['POST'])

def emiratesc():

    _newemiratesc(session['username'], request.form['comment'])

    return redirect(url_for('emiratesAir'))

def _newemiratesc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into emirates values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/swissAir', methods=['POST','GET'])
def swissAir():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from swiss")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('swissAir.html', comments=rv)


@app.route('/swissc', methods=['POST'])

def swissc():

    _newswissc(session['username'], request.form['comment'])

    return redirect(url_for('swissAir'))

def _newswissc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into swiss values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/lca')

def lca():

    return render_template('lca.html')


@app.route('/indigo', methods=['POST','GET'])

def indigo():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from indigo")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('indigo.html', comments=rv)


@app.route('/indigoc', methods=['POST'])

def indigoc():

    _newindigoc(session['username'], request.form['comment'])

    return redirect(url_for('indigo'))


def _newindigoc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into indigo values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/flyDubai', methods=['POST','GET'])

def flyDubai():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from flyDubai")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('flyDubai.html', comments=rv)

@app.route('/flyDubaic', methods=['POST'])

def flyDubaic():

    _newflyDubaic(session['username'], request.form['comment'])

    return redirect(url_for('flyDubai'))


def _newflyDubaic(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into flyDubai values(:username, :comment)", params)
    connection.commit()
    cursor.close()

@app.route('/airArabia', methods=['POST','GET'])

def airArabia():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from airarabia")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('airArabia.html', comments=rv)

@app.route('/airArabiac', methods=['POST'])

def airArabiac():

    _newairArabiac(session['username'], request.form['comment'])

    return redirect(url_for('airArabia'))

def _newairArabiac(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into airarabia values(:username, :comment)", params)
    connection.commit()
    cursor.close()


@app.route('/virginAtlantic', methods=['POST','GET'])

def virginAtlantic():

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * from virginAtlantic")
    rv=cursor.fetchall()
    cursor.close()

    return render_template('virginAtlantic.html', comments=rv)

@app.route('/virginAtlanticc', methods=['POST'])

def virginAtlanticc():

    _newvirginAtlanticc(session['username'], request.form['comment'])

    return redirect(url_for('virginAtlantic'))


def _newvirginAtlanticc(username, comment):

    params = {'username':username,'comment':comment}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("insert into virginAtlantic values(:username, :comment)", params)
    connection.commit()
    cursor.close()

"""Making a logout method in which it populates the session with the value none"""

@app.route('/logout', methods=['GET', 'POST'])

def logout():

    session.pop("logged in",None)
    session.pop("username",None)

    return redirect("/")


#nserting values into guestbook

@app.route('/hello', methods=['POST'])

def hello():

    _insert(request.form['name'], request.form['email'], request.form['comment'])

    return redirect(url_for('contact'))

#Inserting Values in for signing in 

@app.route('/sign', methods=['POST'])

def sign():

    _insertuser(request.form['name'], request.form['email'], request.form['username'], request.form['password'])

    return redirect(url_for('login'))

#Viewing the guestbook

@app.route('/view', methods=['POST','GET'])

def view():

    """

    Accepts POST requests, and processes the form;

    Redirect to view when completed.

    """

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM guestbook")
    rv = cursor.fetchall()
    cursor.close()

    return render_template("view.html",entries=rv)

#Verifying if the user is a registered and loggin in

@app.route('/login', methods=['POST', 'GET'])

def login():

    try:

        if request.method == 'POST':

            query = "select * from account where username = '" + request.form['username']
            query = query + "' and password = '" + request.form['password'] + "';"
            connection = sqlite3.connect(DB_FILE)
            cur = connection.execute(query)
            rv = cur.fetchall()
            cur.close()

            if len(rv) == 1:

                session['username'] = request.form['username']
                session['logged in'] = True
                return redirect("information")

            else:

                return render_template('login.html', msg="Username/Password Incorrect!")

        else:

            return render_template('login.html')

    except:

        return render_template('login.html', message="Error Taken Place!")


@app.route('/weather')

def weather():

    try:

        conn= sqlite3.connect('mydb')
        cur = conn.cursor()
        page1=requests.get('https://www.bbc.com/weather/292223')
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        dubaicurrentDay = soup1.find(class_="wr-day__body")
        dubaioneDay_items= dubaicurrentDay.find_all(class_="wr-day__details")
        dubaitonight = dubaioneDay_items[0]
        dubaitempC = dubaitonight.find(class_="wr-value--temperature--c").get_text()
        dubailowestDay_items= dubaicurrentDay.find_all(class_="wr-day-temperature__low-value")
        dubailow = dubailowestDay_items[0]
        dubaitemplowC = dubailow.find(class_="wr-value--temperature--c").get_text()
        dubaistatus = dubaitonight.find(class_="wr-day__details__weather-type-description").get_text()
        cur.execute("insert into dubaiWeather values (?, ?, ?)", (dubaitempC, dubaitemplowC, dubaistatus))

    except:

        return render_template('weather.html', message="Error Taken Place!")

    try:

        page2=requests.get('https://www.bbc.com/weather/2147714')
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        sydneycurrentDay = soup2.find(class_="wr-day__body")
        sydneyoneDay_items= sydneycurrentDay.find_all(class_="wr-day__details")
        sydneytonight = sydneyoneDay_items[0]
        sydneytempC = sydneytonight.find(class_="wr-value--temperature--c").get_text()
        sydneylowestDay_items= sydneycurrentDay.find_all(class_="wr-day-temperature__low-value")
        sydneylow = sydneylowestDay_items[0]
        sydneytemplowC = sydneylow.find(class_="wr-value--temperature--c").get_text()
        sydneystatus = sydneytonight.find(class_="wr-day__details__weather-type-description").get_text()
        cur.execute("insert into sydneyWeather values (?, ?, ?)", (sydneytempC, sydneytemplowC, sydneystatus))

    except:

        return render_template('weather.html', message="Error Taken Place!")

    try:

        page3=requests.get('https://www.bbc.com/weather/5128581')
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        newYorkcurrentDay = soup3.find(class_="wr-day__body")
        newYorkoneDay_items= newYorkcurrentDay.find_all(class_="wr-day__details")
        newYorktonight = newYorkoneDay_items[0]
        newYorktempC = newYorktonight.find(class_="wr-value--temperature--c").get_text()
        newYorklowestDay_items= newYorkcurrentDay.find_all(class_="wr-day-temperature__low-value")
        newYorklow = newYorklowestDay_items[0]
        newYorktemplowC = newYorklow.find(class_="wr-value--temperature--c").get_text()
        newYorkstatus = newYorktonight.find(class_="wr-day__details__weather-type-description").get_text()
        cur.execute("insert into newYorkWeather values (?, ?, ?)", (newYorktempC, newYorktemplowC, newYorkstatus))

    except:

        return render_template('weather.html', message="Error Taken Place!")

    try:

        page4=requests.get('https://www.bbc.com/weather/1261481')
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        newDelhicurrentDay = soup4.find(class_="wr-day__body")
        newDelhioneDay_items= newDelhicurrentDay.find_all(class_="wr-day__details")
        newDelhitonight = newDelhioneDay_items[0]
        newDelhitempC = newDelhitonight.find(class_="wr-value--temperature--c").get_text()
        newDelhilowestDay_items= newDelhicurrentDay.find_all(class_="wr-day-temperature__low-value")
        newDelhilow = newDelhilowestDay_items[0]
        newDelhitemplowC = newDelhilow.find(class_="wr-value--temperature--c").get_text()
        newDelhistatus = newDelhitonight.find(class_="wr-day__details__weather-type-description").get_text()
        cur.execute("insert into newDelhiWeather values (?, ?, ?)", (newDelhitempC, newDelhitemplowC, newDelhistatus))

    except:

        return render_template('weather.html', message="Error Taken Place!")

    try:

        page5=requests.get('https://www.bbc.com/weather/1850147')
        soup5 = BeautifulSoup(page5.content, 'html.parser')
        tokyocurrentDay = soup5.find(class_="wr-day__body")
        tokyooneDay_items= tokyocurrentDay.find_all(class_="wr-day__details")
        tokyotonight = tokyooneDay_items[0]
        tokyotempC = tokyotonight.find(class_="wr-value--temperature--c").get_text()
        tokyolowestDay_items= tokyocurrentDay.find_all(class_="wr-day-temperature__low-value")
        tokyolow = tokyolowestDay_items[0]
        tokyotemplowC = tokyolow.find(class_="wr-value--temperature--c").get_text()
        tokyostatus = tokyotonight.find(class_="wr-day__details__weather-type-description").get_text()
        cur.execute("insert into tokyoWeather values (?, ?, ?)", (tokyotempC, tokyotemplowC, tokyostatus))

    except:

        return render_template('weather.html', message="Error Taken Place!")


    #commit the changes to db

    conn.commit()

    #close the connection

    conn.close()

    return render_template ('weather.html', dubaitempC=dubaitempC,dubaitemplowC=dubaitemplowC, dubaistatus=dubaistatus,
    sydneytempC=sydneytempC,sydneytemplowC=sydneytemplowC, sydneystatus=sydneystatus,
    newYorktempC=newYorktempC,newYorktemplowC=newYorktemplowC, newYorkstatus=newYorkstatus, 
    newDelhitempC=newDelhitempC,newDelhitemplowC=newDelhitemplowC, newDelhistatus=newDelhistatus,
    tokyotempC=tokyotempC,tokyotemplowC=tokyotemplowC, tokyostatus=tokyostatus)


@app.route('/ekFlightSchedule')

def FlightSchedule():
    flightS  = requests.get("https://flightaware.com/live/fleet/UAE")
    soup = BeautifulSoup(flightS.content, 'html.parser')
    scheduleTable = soup.find("div", class_="pageContainer")
    contents = scheduleTable.find("table", class_="prettyTable fullWidth")
    tabledata = contents.find_all("tr")
    for x in range(2,4):  
        arrayTable = tabledata[x]
        table = arrayTable.find_all("td")
        identification = table[0].get_text()
        genre = table[1].get_text()
        origin = table[2].get_text()
        destination = table[3].get_text()
        departureTime = table[4].get_text()
        arrivalTime = table[5].get_text()
        #This code is for connection to DB.
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("select identification from flightSchedule")
        result = cursor.fetchall()
    try:
        if(identification,) in result:
            print("exists")
        else:
            cursor.execute("insert into flightSchedule values (:identification, :genre, :origin, :destination, :departureTime, :arrivalTime)", (identification, genre, origin, destination, departureTime, arrivalTime))
            connection.commit()
            cursor.close()
    except:
        return render_template('ekFlightSchedule.html', message="Error Taken Place!")   

 
    return redirect(url_for('flightSchedule'))
#This code is for displaying it to the page.
@app.route('/flightSchedule',methods=['POST','GET'])
def flightSchedule():
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flightSchedule")
        rv = cursor.fetchall()
        cursor.close()
        return render_template('ekFlightSchedule.html',flightTable=rv)


@app.route('/airlineStocks')

def airlineStocks():

    page=requests.get("https://markets.businessinsider.com/stocks/spicejet-stock")
    soup = BeautifulSoup(page.content, 'html.parser')
    stockMainPrice=soup.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    stock=stockMainPrice.get_text()
    currency=soup.find(class_={'currency-iso warmGrey'})
    currencyText=currency.get_text()

    page2=requests.get("https://markets.businessinsider.com/stocks/dal-stock")
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    stockMainPrice2=soup2.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    stock2=stockMainPrice2.get_text()

    singpage=requests.get("https://markets.businessinsider.com/stocks/singapore_airlines_1-stock")
    singsoup = BeautifulSoup(singpage.content, 'html.parser')
    singstockMainPrice=singsoup.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    singstock=singstockMainPrice.get_text()
    singcurrency=singsoup.find(class_={'currency-iso warmGrey'})
    singcurrencyText=singcurrency.get_text()

    cathpage=requests.get("https://markets.businessinsider.com/stocks/cathay_pacific_airways-stock")
    cathsoup = BeautifulSoup(cathpage.content, 'html.parser')
    cathstockMainPrice=cathsoup.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    cathstock=cathstockMainPrice.get_text()
    cathcurrency=cathsoup.find(class_={'currency-iso warmGrey'})
    cathcurrencyText=cathcurrency.get_text()

    aalpage=requests.get("https://markets.businessinsider.com/stocks/aal-stock")
    aalsoup = BeautifulSoup(aalpage.content, 'html.parser')
    aalstockMainPrice=aalsoup.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    aalstock=aalstockMainPrice.get_text()

    asiapage=requests.get("https://markets.businessinsider.com/stocks/asiana_airlines-stock")
    asiasoup = BeautifulSoup(asiapage.content, 'html.parser')
    asiastockMainPrice=asiasoup.find(class_={'push-data aktien-big-font text-nowrap no-padding-at-all'})
    asiastock=asiastockMainPrice.get_text()
    asiacurrency=asiasoup.find(class_={'currency-iso warmGrey'})
    asiacurrencyText=asiacurrency.get_text()

    a=insertTable

    a.insertingTable(stock, stock2, singstock, cathstock, aalstock, asiastock)  

    return render_template ('airlineStocks.html', stock=stock, currencyText=currencyText, 

    stock2=stock2,  singstock=singstock, singcurrencyText=singcurrencyText, 

    cathstock=cathstock, cathcurrencyText=cathcurrencyText, aalstock=aalstock, asiastock=asiastock, asiacurrencyText=asiacurrencyText)


#Condition for running the python file

if __name__ == '__main__':          

    app.run(debug = True)

