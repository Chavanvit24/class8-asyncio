from random import random
import asyncio 
import time

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waitting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
    # report
    print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queqe
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())



# Producer: Running
# Consumer: Running
# Wed Aug 23 14:16:19 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:19 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:20 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:20 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:21 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:21 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:22 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:22 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:23 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:23 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:24 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:24 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:16:24 2023 Producer: Done
# Wed Aug 23 14:16:25 2023 >got None
# Wed Aug 23 14:16:25 2023 Consumer: Done
    