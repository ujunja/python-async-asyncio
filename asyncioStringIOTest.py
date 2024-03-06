import asyncio
import time
import io

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def string_IO_test():
    message = 'This is a test line'
    print("hello2")
    file = io.StringIO()
    
    def loopCount():
        count = 0
        while count < 50:
            file.write(message)
            count = count + 1
    
    def getFile():
        return file
    
async def string_IO_print(f: io.StringIO):
    print(f.read())
        
        
async def main():
    file = string_IO_test()

    task2 = asyncio.create_task(
        string_IO_test())

    task3 = asyncio.create_task(
        string_IO_print(file)
    )

    print(f"started at {time.strftime('%X')}")

    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())