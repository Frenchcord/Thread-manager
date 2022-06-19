from threading import Thread
def protr(func, args):
  if args is None: 
    thread = Thread(target=func)
  else:
    thread = Thread(target=func, args=args)
  thread.start()
  thread.join()
