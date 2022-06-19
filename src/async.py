import asyncio
from threading import Thread
def async_thread(func, args = None):
  def he(arg):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(func(arg))
    loop.close()
  if args is None: 
    thread = Thread(target=he)
  else:
    thread = Thread(target=he, args=args)
  thread.start()
  thread.join()
