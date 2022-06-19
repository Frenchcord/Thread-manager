from asyncio import run
from threading import Thread
def async_thread(func, args = None):
  if args is None: 
    thread = Thread(target=function)
  else:
    thread = Thread(target=function, args=args)
  thread.start()
  thread.join()
