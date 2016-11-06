import web, socket, random, re, datetime

urls = (
                '/myip', 'myip',
                '/version', 'version',
                '/updateip/(.*)', 'updateip',
                '/queryip/(.*)', 'queryip',
                '/(.*)', 'index'
        )

logfile = "ip.log"


render = web.template.render('Templates/')

class index:
	def GET(self, arg1):
		name = arg1
		ID = int(random.random()*random.random()*random.random()*random.random()*random.random()*10**10)
		return render.index(name, ID)

class myip:
	def GET(self):
                output = socket.gethostbyname(socket.gethostname())
		return output

class version:
	def GET(self):
		output = "Hi there! This is version 0.1."
		return output

class updateip:
	def GET(self, arg1):
		writelog(timestamp()+','+arg1+','+socket.gethostbyname(socket.gethostname())+'\n')
		return "200"

class queryip:
	def GET(self, arg1):
                records = openlog()
                matches = re.findall(r'([0-9]{14}),'+arg1+',([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', records)
		if matches:
                        output = sorted(matches,reverse=True)[0][1]
                else: output = "404"
		return output


if __name__ == "__main__":
        app = web.application(urls, globals())
	app.run()


# This function allows azure to hook up the correct URLs to the correct functions
def wsgiHandler():
    return web.application(urls, globals(), autoreload=False).wsgifunc()



def openlog():
        try:
                log = open(logfile, 'r')
                records = log.read()
        except:
                log = open(logfile, 'w')
                records = ""
        finally:
                log.close()
        return records


def writelog(arg1):
        log = open(logfile, 'a')
        log.write(arg1)
        log.close()


def timestamp():
        stamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        return stamp
