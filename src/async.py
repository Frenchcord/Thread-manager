from asyncio import run
from threading import Thread
def async_thread(func, args = None):
  def he(arg = None):
    if arg is None:
      run(func())
      return
    run(func(args))
  if args is None:
    thread = Thread(target=he)
  else:
    thread = Thread(target=he, args=args)
  thread.start()
  thread.join()
