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

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            # retrieve the get() awaitable
            get_await = queue.get()
            # await the awaitable with a timeout
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print('Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queqe
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())


# Producer: Running
# Wed Aug 23 14:30:00 2023 Consumer: Running
# Wed Aug 23 14:30:01 2023 >got 0.19230134303439872
# Wed Aug 23 14:30:01 2023 Consumer: gave up waiting...
# Wed Aug 23 14:30:01 2023 >got 0.5752745710022692
# Wed Aug 23 14:30:02 2023 Consumer: gave up waiting...
# Wed Aug 23 14:30:02 2023 >got 0.6200209423261206
# Wed Aug 23 14:30:02 2023 Consumer: gave up waiting...
# Wed Aug 23 14:30:02 2023 >got 0.6296264466537967
# Wed Aug 23 14:30:03 2023 >got 0.2491206640446798
# Wed Aug 23 14:30:03 2023 Consumer: gave up waiting...
# Wed Aug 23 14:30:03 2023 >got 0.550146944041507
# Wed Aug 23 14:30:04 2023 Consumer: gave up waiting...
# Wed Aug 23 14:30:04 2023 >got 0.8018792684115492
# Wed Aug 23 14:30:04 2023 >got 0.4188357211245384
# Wed Aug 23 14:30:05 2023 >got 0.15501382751356874
# Wed Aug 23 14:30:05 2023 Producer: Done
# Wed Aug 23 14:30:05 2023 >got 0.3171833152437087
# Consumer: Done