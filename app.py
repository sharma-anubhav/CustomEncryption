from __future__ import unicode_literals
from flask import Flask,render_template,url_for,request

from encryption import encrypt1,encrypt2, decrypt1, decrypt2
import time
import spacy

nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

# Web Scraping Pkg
# from urllib.request import urlopen
from urllib.request import urlopen


# Reading Time
def readingTime(mytext):
	total_words = len([ token.text for token in nlp(mytext)])
	estimatedTime = total_words/200.0
	return estimatedTime

# Fetch Text From Url
def get_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

def remove_emptychar(line):
    for alpha in line:
        if alpha == chr(0):
            line = line.replace(chr(0), '')
    line = line.rstrip(" ")
    return line

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Decrypt')
def Decrypt():
	return render_template('Decrypt.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		final_reading_time = readingTime(rawtext)
		e1 = encrypt1(rawtext)
		e1 = e1.rstrip(" ")
		final_encrypt = encrypt2(e1)
		#d1 = decrypt1(e2)
		#final_decrypt = decrypt2(d1)

		summary_reading_time = readingTime(final_encrypt)
		end = time.time()
		final_time = end-start
	return render_template('index.html',ctext=rawtext,final_cipher=final_encrypt,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time)


@app.route('/Decrypt_analysis',methods=['GET','POST'])
def Decrypt_analysis():
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext2']
		final_reading_time = readingTime(rawtext)
		d1 = decrypt2(rawtext)
		d1 = remove_emptychar(d1)
		final_decrypt = decrypt1(d1)
		summary_reading_time = readingTime(final_decrypt)
		end = time.time()
		final_time = end-start
	return render_template('Decrypt.html',ctext=rawtext,final_message=final_decrypt,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time)

@app.route('/about')
def about():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

#python -m spacy download en
