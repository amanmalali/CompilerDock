import pytest

from application import app


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "inp, out",
    [
        (  # successful compilation
            {"lang": "python3", "code": "print('Hello World')", "stdin": "", "id": 1},
            (
                {
                    "output": "Hello World\n",
                    "error": "",
                    "fail": False,
                    "timeout": False,
                    "id": 1,
                },
                200,
            ),
        ),
        (  # unsupported language input
            {"lang": "pytho", "code": "print('Hello World')", "stdin": "", "id": 1},
            ({"error": "Unknown or unsupported language pytho"}, 400,),
        ),
    ],
)
async def test_compiler(inp, out):
    test_client = app.test_client()
    reponse = await test_client.post("/", json=inp)
    result = await reponse.get_json()
    assert reponse.status_code == out[1]
    assert result == out[0]
