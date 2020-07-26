import pytest

from application import app


data = {
        "lang": "python3",
        "code": "print('Hello World')",
        "stdin": "",
        "id": 1
    }
expected = {
    "output": "Hello World\n",
    "error": "",
    "fail": 0,
    "timeout": 0,
    "id": 1
}


@pytest.mark.asyncio
async def test_compiler():
    test_client = app.test_client()
    reponse = await test_client.post("/", json=data)
    result = await reponse.get_json()
    assert reponse.status_code == 200
    assert result == expected
