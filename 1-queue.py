# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
        #print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queue.get()
        # check for stop signal
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



# Wed Aug 23 13:59:55 2023 Producer: Running
# Wed Aug 23 13:59:55 2023 Consumer: Running
# Wed Aug 23 13:59:55 2023 >got 0.4005375647306254
# Wed Aug 23 13:59:56 2023 >got 0.6049312098164017
# Wed Aug 23 13:59:57 2023 >got 0.8519853400885906
# Wed Aug 23 13:59:58 2023 >got 0.8822785598597811
# Wed Aug 23 13:59:58 2023 >got 0.6129830881599454
# Wed Aug 23 13:59:58 2023 >got 0.08126665977096692
# Wed Aug 23 13:59:59 2023 >got 0.2748567187469343
# Wed Aug 23 13:59:59 2023 >got 0.6163500699362253
# Wed Aug 23 14:00:00 2023 >got 0.5277776507771988
# Wed Aug 23 14:00:00 2023 Producer: Done
# Wed Aug 23 14:00:00 2023 >got 0.033609054155467
# Wed Aug 23 14:00:00 2023 Consumer: Done