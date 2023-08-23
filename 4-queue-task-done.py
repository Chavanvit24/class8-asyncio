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
        # add to the queqe
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
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

 # entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:36:10 2023 Consumer: Running
# Wed Aug 23 14:36:10 2023 Producer: Running
# Wed Aug 23 14:36:11 2023 >got 0.6047311911155581
# Wed Aug 23 14:36:12 2023 >got 0.473692949473994
# Wed Aug 23 14:36:12 2023 >got 0.6970755927096884
# Wed Aug 23 14:36:13 2023 >got 0.046128418538340155
# Wed Aug 23 14:36:13 2023 >got 0.799310941162372
# Wed Aug 23 14:36:14 2023 >got 0.9622150113242969
# Wed Aug 23 14:36:15 2023 >got 0.52075340716108
# Wed Aug 23 14:36:15 2023 >got 0.7477549839837873
# Wed Aug 23 14:36:16 2023 >got 0.3236137690447043
# Wed Aug 23 14:36:16 2023 Producer: Done
# Wed Aug 23 14:36:17 2023 >got 0.6804837869197412
# Wed Aug 23 14:36:17 2023 >got None