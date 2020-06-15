from datetime import datetime
import pytz

A = ['Europe/Berlin', 'America/New_York', 'Europe/London', 'Asia/Shanghai', "Africa/Accra"]


def main():
    t_format = "%d/%m/%Y, %H:%M:%S"
    now = datetime.now()
    now = now.replace(tzinfo=pytz.utc)

    local = datetime.now()
    print("Local:", local.strftime(t_format))

    for cities in A:
        t = now.astimezone(pytz.timezone(cities))
        print(cities, ":", t.strftime(t_format))


if __name__ == "__main__":
    main()