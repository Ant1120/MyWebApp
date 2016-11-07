import random, datetime


def readlog(logfile):
        try:
                log = open(logfile, 'r')
                records = log.read()
        except:
                log = open(logfile, 'w')
                records = ""
        finally:
                log.close()
        return records


def writelog(logfile, line):
        log = open(logfile, 'a')
        log.write(line)
        log.close()


def timestamp():
        stamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        return stamp


def randomstr(len=64):
        randomstr = ""
        for n in range(0, len):
                randomstr = randomstr + random.choice(r"01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-.+")
        return randomstr