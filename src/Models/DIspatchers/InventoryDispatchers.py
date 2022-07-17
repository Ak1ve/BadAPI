import asyncio
import math
from typing import Coroutine, Callable, Optional, Literal

from src.Models.abc.APIDispatcher import *
from src.Models.objects import *
from src.Models.objects.Filter import Filter


class InventoryDispatcher(APIDispatcher):
    def __init__(self):
        super().__init__()

    async def fetch_inventory(self, filter_: Optional[Filter] = None) -> list[InventoryPage]:
        tasks: list[Coroutine[InventoryPage]] = []
        for x in range(1, math.ceil((await self.total_amount()).total / 60 + 1)):
            tasks.append(self.fetch_page(x, filter_))

        gathered = await asyncio.gather(*tasks)
        return list(gathered)

    async def fetch_page(self, page_num: int, filter_: Optional[Filter] = None) -> InventoryPage:
        url = filter_.assemble("inventory", page=page_num)\
            if filter_ is not None else Filter().assemble("inventory", page=page_num)
        return await self.fetch_json(url, InventoryPage)

    async def total_amount(self, filter_: Optional[Filter] = None) -> InventoryToyTotal:
        url = filter_.assemble("total") if filter_ is not None else Filter().assemble("total")
        return await self.fetch_json(url, InventoryToyTotal)

