import MyCode, flask, re


app = flask.Flask(__name__)
logfile = "ip.log"


@app.route('/myip')
def myip():
        output = flask.request.remote_addr
	return output


@app.route('/version')
def version():
	output = "Hi there! This is version 0.5b."
	return output


@app.route('/updateip/<host>')
def updateip(host):
	MyCode.writelog(logfile, MyCode.timestamp()+','+host+','+flask.request.remote_addr+'\n')
	return "200"


@app.route('/queryip/<host>')
def queryip(host):
        records = MyCode.readlog(logfile)
        matches = re.findall(r'([0-9]{14}),'+host+',([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', records)
	if matches:
                output = sorted(matches,reverse=True)[0][1]
        else: output = "404"
	return output


@app.route('/iphistory/<host>')
def iphistory(host):
        output = ""
        records = MyCode.readlog(logfile)
        matches = re.findall(r'([0-9]{14}),'+host+',([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', records)
	if matches:
                history = sorted(matches,reverse=True)
                for item in history:
                        output = output + "<p>{0:^16s} | {1:^15s}</p>".format(item[0], item[1])
        else: output = "404"
	return output


@app.route('/randomstr')
@app.route('/randomstr/<int:len>')
def randomstr(len=1024):
        output = MyCode.randomstr(len)
        return output


@app.route('/loolooloo')
def loolooloo():
        return flask.redirect("https://www.amazon.com/photos/share/pTFyId1C2YdCq9OCQykZFhuKe0UGjjov5oRRIIAyVZs")


@app.route('/')
@app.route('/<anyone>')
def index(anyone="John Dow"):
        output = "Hi there, " + anyone + "! Your answer to the life, universe and everything is " + MyCode.randomstr()
        return output


