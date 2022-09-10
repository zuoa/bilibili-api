# bilibili_api.session

from bilibili_api import session
from .common import get_credential


async def test_a_fetch_session_msgs():
    return await session.fetch_session_msgs(12076317, get_credential())


async def test_b_get_sessions():
    return await session.get_sessions(get_credential())


async def test_c_get_new_sessions():
    return await session.new_sessions(get_credential())


async def test_d_send_msg():
    await session.send_msg(get_credential(), 660303135, "THIS IS A TEST MSG. ")
