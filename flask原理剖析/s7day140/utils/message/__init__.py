import settings
import importlib

def send_msgs(msg):

    for path in settings.MSG_LIST:
        m,c = path.rsplit('.',maxsplit=1)
        md = importlib.import_module(m)
        obj = getattr(md,c)()
        obj.send(msg)
