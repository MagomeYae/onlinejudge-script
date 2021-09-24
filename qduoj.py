# -*- coding: utf-8 -*-
# Copyright (C) 2021 MagomeYae
#
# This module is part of onlinejudge-script and is released under
# the AGPL v3 License: https://www.gnu.org/licenses/agpl-3.0.txt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations
import asyncio
import logging
import os
import sys


import aiohttp


class QduOJ:
    def __init__(self, url: str, user: str, password: str, session: aiohttp.ClientSession):
        self.url = url
        self.user = user
        self.password = password
        self.session = session
        self.logger = logging.getLogger(f'QduOJ_{user}')
        self.logger.setLevel(logging.DEBUG)

    @classmethod
    async def create(cls, url: str, user: str, password: str) -> QduOJ:
        return cls(url, user, password, aiohttp.ClientSession(raise_for_status=True))

    async def login(self) -> None:
        pass

    async def logout(self) -> None:
        pass

    async def upload_file(self, path: str, spj: bool = False) -> dict[str, str]:
        data = aiohttp.FormData()
        data.add_field('spj', spj)
        data.add_field('file', open(path, 'rb'),
                       filename=os.path.basename(path),
                       # content_type='multipart/form-data'
                       )
        async with self.session.post(f'{self.url}/api/admin/test_case', data=data) as resp:
            return await resp.json()

    async def cleanup(self) -> None:
        if self.session is not None:
            await self.session.close()
            self.session = None


async def main() -> None:
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s')
    asyncio.get_event_loop().run_until_complete(main())
