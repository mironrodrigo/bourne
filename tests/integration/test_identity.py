import pytest

@pytest.mark.asyncio
async def test_health_check():
    assert 1 + 1 == 2