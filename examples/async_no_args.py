from Thread_manager import async_thread
async def funct():
  print('hello world!')

async_thread(funct)
