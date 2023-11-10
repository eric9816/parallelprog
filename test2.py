import asyncio


#
# async def main():
#     print('Начинаем')
#     await asyncio.sleep(3)  # приостановка выполнения на 1 секунду
#     print('Закончили')
#
# # Запускаем асинхронную функцию
# asyncio.run(main())
# print('Осн')
#
def salt():
    print('посолили')

async def boil_water(sec: int = 5):
    print('Ставим воду чтоб закипела')
    await asyncio.sleep(sec)
    print('Вода вскипела')
    salt()


async def chop_vegs(sec: int = 3):
    print('Нарезаем овощи')
    await asyncio.sleep(sec)
    print('Нарезали')


async def main():
	await boil_water()
	await chop_vegs()
    # task1 = asyncio.create_task(boil_water())
    # task2 = asyncio.create_task(chop_vegs())
    # await task1
    # await task2
    # await asyncio.gather(task1, task2)
    #await asyncio.gather(boil_water(), chop_vegs())

import time
st = time.time()
asyncio.run(main())
et = time.time()
print(et - st)
