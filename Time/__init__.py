import check50
import check50.c

@check50.check()
def exists():
    """time.py"""
    check50.exists("time.py")

@check50.check(exists)
def compiles():
    """time.py compiles"""
    check50.c.compile("time.py", lcs50=True)

@check50.check(compiles)
def check():
    """time.py does what it is supposed to do"""
    t_format = "%d/%m/%Y, %H:%M:%S"
    now = datetime.now()
    now = now.replace(tzinfo=pytz.utc)
    local = 'Local : '+(now.strftime(t_format))
    Berlin = 'Europe/Berlin : '+now.astimezone(pytz.timezone('Europe/Berlin')).strftime(t_format)
    New_York = 'America/New_York : '+now.astimezone(pytz.timezone('America/New_York')).strftime(t_format)
    London = 'Europe/London : '+now.astimezone(pytz.timezone('Europe/London')).strftime(t_format)
    Shanghai = 'Asia/Shanghai : '+now.astimezone(pytz.timezone('Asia/Shanghai')).strftime(t_format)
    Accra = 'Africa/Accra : '+now.astimezone(pytz.timezone('Africa/Accra')).strftime(t_format)
    check50.run("python time.py").stdout(local).stdout(Berlin).stdout(New_York).stdout(London).stdout(Shanghai).stdout(Accra)
