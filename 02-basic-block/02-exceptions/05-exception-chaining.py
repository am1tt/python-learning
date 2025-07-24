
try:
    open("db.sqlite")
except OSError as exc:
    raise RuntimeError("unable to handle the error") from exc


## states the OsError , along with directory error 


def func():
    raise ConnectionError

try: 
    func()
    except ConnectionError as e:
        raise RuntimeError("failed to connect") from e