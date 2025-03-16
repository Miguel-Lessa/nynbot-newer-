from abc import ABC, abstractmethod
from discord import Message

class Command(ABC):
    @abstractmethod
    async def execute(self, message: Message):
        pass