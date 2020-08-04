import pytest

from src.utils.run import run_code


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "inp, out",
    [
        (  # successful compilation
            ("python3", "print('Hello World')"),
            ("Hello World\n", False, False),
        ),
        (("python3", "print('Hello World)"), ("", True, False),),  # error ouput
        (("python3", "while True: pass"), ("", False, True)),  # timeout
    ],
)
async def test_run(inp, out):
    stdin = ""
    output, _, fail, timeout = await run_code(*inp, stdin)
    assert output == out[0]
    assert fail == out[1]
    assert timeout == out[2]
