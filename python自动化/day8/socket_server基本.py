#encoding:utf-8

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try: #使用try except捕捉客户端连接断开异常
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("error:" ,e)
                break

if __name__ == "__main__":
    HOST,PORT = "localhost",9999

    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()