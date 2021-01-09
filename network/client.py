from network.server import ServerConnect
import asyncio


class User(ServerConnect):
    def __init__(self):
        super(User, self).__init__()
        self.socket.setblocking(False)

    async def listen_socket(self, user_sock):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)

    async def send_data(self, data):
        while True:
            await self.main_loop.run_in_executor()

    async def main(self):
        task_1 = self.main_loop.create_task(self.listen_socket)
        task_2 = self.main_loop.create_task(self.send_data)

        await asyncio.gather((task_1, task_2))