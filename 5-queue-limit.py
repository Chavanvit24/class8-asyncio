from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queqe):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
    print(f'{time.ctime()} Producer: Done')


async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queqe.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create the shared queqe
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many product
    product = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:38:03 2023 Consumer: Running
# Wed Aug 23 14:38:03 2023 Producer: Running
# Wed Aug 23 14:38:03 2023 Producer: Running
# Wed Aug 23 14:38:03 2023 Producer: Running
# Wed Aug 23 14:38:03 2023 Producer: Running
# Wed Aug 23 14:38:03 2023 Producer: Running
# Wed Aug 23 14:38:03 2023 >got 0.061669762608179024
# Wed Aug 23 14:38:03 2023 >got 0.29187310708620495
# Wed Aug 23 14:38:04 2023 >got 0.10091515725135347
# Wed Aug 23 14:38:04 2023 >got 0.5129086347964157
# Wed Aug 23 14:38:04 2023 >got 0.5385972968890629
# Wed Aug 23 14:38:05 2023 >got 0.7024823325702738
# Wed Aug 23 14:38:06 2023 >got 0.1466917569147831
# Wed Aug 23 14:38:06 2023 >got 0.6768521252534866
# Wed Aug 23 14:38:06 2023 >got 0.49259713923287485
# Wed Aug 23 14:38:07 2023 >got 0.9687807542192975
# Wed Aug 23 14:38:08 2023 >got 0.353653556903905
# Wed Aug 23 14:38:08 2023 >got 0.963571843761843
# Wed Aug 23 14:38:09 2023 >got 0.6012307505935006
# Wed Aug 23 14:38:10 2023 >got 0.1333881537307593
# Wed Aug 23 14:38:10 2023 >got 0.10351875307075054
# Wed Aug 23 14:38:10 2023 >got 0.08507163995483236
# Wed Aug 23 14:38:10 2023 >got 0.7547131070441372
# Wed Aug 23 14:38:11 2023 >got 0.5770608272080934
# Wed Aug 23 14:38:12 2023 >got 0.21678420289434663
# Wed Aug 23 14:38:12 2023 >got 0.03608463478716384
# Wed Aug 23 14:38:12 2023 >got 0.4490546793306718
# Wed Aug 23 14:38:12 2023 >got 0.2196565228733105
# Wed Aug 23 14:38:12 2023 >got 0.9838206933294457
# Wed Aug 23 14:38:13 2023 >got 0.8067606937856804
# Wed Aug 23 14:38:14 2023 >got 0.06217006993334995
# Wed Aug 23 14:38:14 2023 >got 0.1204594461931372
# Wed Aug 23 14:38:14 2023 >got 0.2373952906380905
# Wed Aug 23 14:38:15 2023 >got 0.7723844340281704
# Wed Aug 23 14:38:16 2023 >got 0.16004540024558211
# Wed Aug 23 14:38:16 2023 >got 0.14841411138244764
# Wed Aug 23 14:38:16 2023 >got 0.39237065927526504
# Wed Aug 23 14:38:16 2023 >got 0.3408478956590305
# Wed Aug 23 14:38:17 2023 >got 0.4704055041080204
# Wed Aug 23 14:38:17 2023 >got 0.5114732030394137
# Wed Aug 23 14:38:18 2023 >got 0.7276906019050613
# Wed Aug 23 14:38:18 2023 >got 0.6267874424011657
# Wed Aug 23 14:38:19 2023 >got 0.04727946151066664
# Wed Aug 23 14:38:19 2023 >got 0.6291829578974156
# Wed Aug 23 14:38:20 2023 >got 0.5025081048842173
# Wed Aug 23 14:38:20 2023 Producer: Done
# Wed Aug 23 14:38:20 2023 >got 0.6797982717087191
# Wed Aug 23 14:38:21 2023 >got 0.3675335978587879
# Wed Aug 23 14:38:21 2023 >got 0.5157547410950781
# Wed Aug 23 14:38:22 2023 >got 0.06600657363055851
# Wed Aug 23 14:38:22 2023 >got 0.2029991546670451
# Wed Aug 23 14:38:22 2023 Producer: Done
# Wed Aug 23 14:38:22 2023 >got 0.9066222381083012
# Wed Aug 23 14:38:22 2023 Producer: Done
# Wed Aug 23 14:38:23 2023 >got 0.38106391889266356
# Wed Aug 23 14:38:23 2023 >got 0.416409975057319
# Wed Aug 23 14:38:23 2023 Producer: Done
# Wed Aug 23 14:38:24 2023 >got 0.25933258024567585
# Wed Aug 23 14:38:24 2023 Producer: Done
# Wed Aug 23 14:38:24 2023 >got 0.06593292355998626
# Wed Aug 23 14:38:24 2023 >got 0.9908742247564428