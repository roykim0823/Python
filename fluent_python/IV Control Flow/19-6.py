import asyncio
import itertools
import time

# Example 19-5. spinner_async.py: the spin and slow coroutines
async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow() -> int:
    # await asyncio.sleep(3)
    time.sleep(3)
    return 42

# Example 19-4. spinner_async.py: the main function and supervisor coroutine
async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()  # raise CancelledError
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()