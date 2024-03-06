import asyncio
import time
import io

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def string_IO_test(file, queue):
    message = 'This is a test line'
    
    count = 0
    while count < 50:
        file.write(message)
        count += 1
        file.seek(0)  # 파일 포인터를 처음으로 이동
        data = file.getvalue()
        # 데이터를 큐에 넣음
        await queue.put(data)
        print("count : ", count)
        await asyncio.sleep(0)  # 이벤트 루프에 제어 양보

    # 더 이상 데이터가 없음을 알리는 특별한 신호를 보냄
    await queue.put(None)

async def string_IO_print(queue):
    while True:
        # 큐에서 데이터를 꺼내옴
        data = await queue.get()

        if data is None:
            break  # 종료 신호를 받으면 루프를 종료

        print(data)

async def main():
    file = io.StringIO()
    queue = asyncio.Queue()

    task1 = asyncio.create_task(
        string_IO_test(file, queue)
    )

    task2 = asyncio.create_task(
        string_IO_print(queue)
    )

    print(f"started at {time.strftime('%X')}")

    # 두 태스크가 동시에 실행되도록 합니다.
    await asyncio.gather(task1, task2)

    print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())
