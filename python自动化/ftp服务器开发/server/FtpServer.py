#encoding:utf-8

import os ,socketserver
import json

class FtpServer(socketserver.BaseRequestHandler):

    def authenticate(self): #客户端认证
        pass

    def cmd_put(self,*args): #上传文件方法
        cmd_dict = args[0]
        filename = cmd_dict['filename']
        filesize = cmd_dict['filesize']
        if os.path.isfile(filename):
            filename = filename+'.new'
        recv_size = 0
        f = open(filename, 'wb')
        while recv_size < filesize:
            data = self.request.recv(1024)
            recv_size += 1024
            f.write(data)
        else:
            f.close()
            print("Received successfully !")


    def cmd_get(self): #下载文件方法
        pass


    def handle(self):
        print("客户端IP：{}，端口:{} 连接成功".format(self.client_address[0], self.client_address[1]))
        while True:
            try:  # 使用try except捕捉客户端连接断开异常
                self.msg_dict = json.loads(self.request.recv(1024).strip().decode())
                print("{} 端口wrote: {}".format(self.client_address[1],self.msg_dict))
                cmd_str = self.msg_dict['action']
                if hasattr(self, "cmd_%s" % cmd_str):  # 使用hasattr检测类是否有这个方法
                    self.request.send(b"ok !")
                    func = getattr(self, "cmd_%s" % cmd_str)  # 使用getattr反射到相应的方法
                    func(self.msg_dict)  # 调用对应的方法
                else:
                    self.request.send("error !")
            except ConnectionResetError as e:
                print("error:", e, "客户端IP：{}，端口:{} 连接断开".format(self.client_address[0], self.client_address[1]))
                break


if __name__ == "__main__":
    HOST,PORT = "localhost",9999

    # server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)  #只支持单个客户端连接
    server = socketserver.ThreadingTCPServer((HOST,PORT),FtpServer) #多并发连接支持
    server.serve_forever()