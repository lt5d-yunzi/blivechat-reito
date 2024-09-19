# -*- coding: utf-8 -*-
import asyncio

import aiohttp

import utils.request

VERSION = 'v1.8.3'


def check_update():
    asyncio.get_running_loop().create_task(_do_check_update())


async def _do_check_update():
    try:
        async with utils.request.http_session.get(
            'https://github.com/lt5d-yunzi/blivechat-reito/releases/latest'
        ) as r:
            data = await r.json()
            if data['name'] != VERSION:
                print('---------------------------------------------')
                print('New version available:', data['name'])
                print(data['body'])
                print('Download:', data['html_url'])
                print('---------------------------------------------')
    except aiohttp.ClientConnectionError:
        print('Failed to check update: connection failed')
    except asyncio.TimeoutError:
        print('Failed to check update: timeout')
