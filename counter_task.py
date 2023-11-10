# put your python code here
import asyncio as io

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}


async def counter(name: str, count: int):
    await io.sleep(count)
    print(f"{name}: {count}")


async def main():

    lst = []
    for i in range(1, 14):
        if i <= 7:
            c1 = io.create_task(counter(name="Counter 1", count=i))
            c2 = io.create_task(counter(name="Counter 2", count=i))
            lst.append(c1)
            lst.append(c2)

        else:
            c1 = io.create_task(counter(name="Counter 1", count=i))
            lst.append(c1)

    await io.gather(*lst)

io.run(main())
    # c1 = "Counter 1"
    # c2 = "Counter 2"
    # for i in range(1, max_counts[c1] + 1):
    #     if i
    #     c1 = io.create_task(counter(name="Counter 1", count=))


