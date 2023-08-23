from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep((id + 1)*0.1)
        # add to the queue
        await queue.put(value)
    # send an all done signal

    print(f'{time.ctime()} Producer {id}: Done')


async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create a shared queue
    queue = asyncio.Queue(2)
    # start consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # run the producer and consumer
    await queue.join()


# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:16:10 2023 Consumer: Running
# Wed Aug 23 15:16:10 2023 Producer: Running
# Wed Aug 23 15:16:10 2023 Producer: Running
# Wed Aug 23 15:16:10 2023 Producer: Running
# Wed Aug 23 15:16:10 2023 Producer: Running
# Wed Aug 23 15:16:10 2023 Producer: Running
# Wed Aug 23 15:16:11 2023 > got 0.14675463796399846
# Wed Aug 23 15:16:11 2023 > got 0.3979498662079691
# Wed Aug 23 15:16:11 2023 > got 0.7389706331202228
# Wed Aug 23 15:16:12 2023 > got 0.30552365720686736
# Wed Aug 23 15:16:12 2023 > got 0.812317185111225
# Wed Aug 23 15:16:13 2023 > got 0.3122261068855071
# Wed Aug 23 15:16:13 2023 > got 0.8801480745405877
# Wed Aug 23 15:16:14 2023 > got 0.10436473097559984
# Wed Aug 23 15:16:14 2023 > got 0.07829337670361947
# Wed Aug 23 15:16:14 2023 > got 0.2787294667669826
# Wed Aug 23 15:16:15 2023 > got 0.9089279530779593
# Wed Aug 23 15:16:16 2023 > got 0.41972359687145
# Wed Aug 23 15:16:16 2023 > got 0.9539330166179875
# Wed Aug 23 15:16:17 2023 > got 0.9005662795013692
# Wed Aug 23 15:16:18 2023 > got 0.4764087342858422
# Wed Aug 23 15:16:18 2023 > got 0.7605060921134578
# Wed Aug 23 15:16:19 2023 > got 0.9546876151347929
# Wed Aug 23 15:16:20 2023 > got 0.27165254954354945
# Wed Aug 23 15:16:20 2023 > got 0.0370651036675006
# Wed Aug 23 15:16:20 2023 > got 0.6654957844142799
# Wed Aug 23 15:16:21 2023 > got 0.8085173789089005
# Wed Aug 23 15:16:22 2023 > got 0.05113637209385613
# Wed Aug 23 15:16:22 2023 > got 0.5689738733558471
# Wed Aug 23 15:16:23 2023 > got 0.10517204788861145
# Wed Aug 23 15:16:23 2023 > got 0.08897215267267877
# Wed Aug 23 15:16:23 2023 > got 0.6706518125569516
# Wed Aug 23 15:16:23 2023 > got 0.2740908443868094
# Wed Aug 23 15:16:24 2023 > got 0.7269305494356353
# Wed Aug 23 15:16:24 2023 > got 0.8949685026888465
# Wed Aug 23 15:16:25 2023 > got 0.057227687978718245
# Wed Aug 23 15:16:25 2023 > got 0.8666469277467894
# Wed Aug 23 15:16:26 2023 > got 0.16580325371797
# Wed Aug 23 15:16:26 2023 > got 0.38500661324621677
# Wed Aug 23 15:16:27 2023 > got 0.3998709904436435
# Wed Aug 23 15:16:27 2023 > got 0.4507676326212655
# Wed Aug 23 15:16:28 2023 > got 0.8725050818723924
# Wed Aug 23 15:16:29 2023 > got 0.4308696506444496
# Wed Aug 23 15:16:29 2023 Producer 0: Done
# Wed Aug 23 15:16:29 2023 > got 0.0710061636914544
# Wed Aug 23 15:16:29 2023 > got 0.7331124723208313
# Wed Aug 23 15:16:30 2023 > got 0.028085858303726896
# Wed Aug 23 15:16:30 2023 Producer 1: Done
# Wed Aug 23 15:16:30 2023 > got 0.4893533084515189
# Wed Aug 23 15:16:30 2023 > got 0.9490586607532269
# Wed Aug 23 15:16:31 2023 > got 0.7187387878676837
# Wed Aug 23 15:16:32 2023 > got 0.3875972903376952
# Wed Aug 23 15:16:33 2023 > got 0.42214629818971094
# Wed Aug 23 15:16:33 2023 Producer 3: Done
# Wed Aug 23 15:16:33 2023 > got 0.571313085489165
# Wed Aug 23 15:16:34 2023 > got 0.6344970340456884
# Wed Aug 23 15:16:34 2023 Producer 2: Done
# Wed Aug 23 15:16:34 2023 > got 0.42532581899499067
# Wed Aug 23 15:16:34 2023 Producer 4: Done
# Wed Aug 23 15:16:35 2023 > got 0.9886223792631345
# Wed Aug 23 15:16:36 2023 > got 0.7425115443041651