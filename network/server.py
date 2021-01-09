import socket
import asyncio
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')


class ServerConnect(ABC):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_loop = asyncio.get_event_loop()

    @abstractmethod
    async def listen_socket(self, data):
        raise NotImplementedError()

    @abstractmethod
    async def send_data(self, data):
        raise NotImplementedError()

    @abstractmethod
    async def main(self):
        raise NotImplementedError()

    def start_all(self):
        self.main_loop.run_until_complete(self.main())


class MainServer(ServerConnect):
    def __init__(self):
        super(ServerConnect, self).__init__()
        self.socket.bind(("127.0.0.1", 1234))
        self.socket.setblocking(False)
        self.users = []
        logging.info('Start working')

    async def accept_sockets(self):
        while True:
            user, address = await self.main_loop.sock_accept(self.socket)
            logging.info('Connect: ', address[0])
            self.users.append(user)
            self.main_loop.create_task(self.listen_socket(user))

    async def send_data(self, data):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    async def listen_socket(self, user_sock):
        logging.info('Listen user: ', user_sock)
        while True:
            data = self.main_loop.sock_recv(user_sock, 2048)
            await self.send_data(data)

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())


if __name__ == '__main__':
    server = MainServer()
    server.start_all()