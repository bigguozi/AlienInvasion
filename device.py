import pygame
import math
import serial
import serial.tools.list_ports
class Device():
    def __init__(self):
        """初始化程序完成打开串口与串口的初始化"""
        self.port     = 'COM3'
        self.baudrate = 115200
        self.bytesize = 8
        self.parity   = 'N'
        self.stopbits = 1 
        self.timeout  = 2
        self.ax_start = 2
        self.ax_end   = 7
        self.ay_start = 10
        self.ay_end   = 15
        self.btn_start= 19
        self.ax       = 0.0
        self.ay       = 0.0
        self.a        = 0.0
        self.angle    = 0.0
        self.btn      = 0
        self.dataReceived = False
        self.status   = len(list(serial.tools.list_ports.comports())) != 0
        #self.port     = serial.Serial(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
        if self.status == True :
            self.port     = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize, parity=self.parity, stopbits=self.stopbits, timeout=self.timeout)
        
        
        
        
        
        #
    def startConvert(self):
        """该函数向设备发送字符启动设备单次传感器数据采集"""
        self.port.write(('s').encode())
        
    def getSensorData(self):
        # 只有初始话成功才会进行传感器读取
        if self.status :    
            line=self.port.readline();
            #print((line));
            # 只有当接受到的数据帧长度满足要求才认为接受到了正确数据
            if len(line) == 22 :
                self.btn = bool(line[self.btn_start]==49)
                #print(self.btn)
                self.ax = float(line[self.ax_start:self.ax_end])
                self.ay = float(line[self.ay_start:self.ay_end])
                self.a  = math.sqrt(self.ax**2 + self.ay**2)
                if self.ax == 0 :
                    if self.ay >=0 :
                        self.angle = math.pi/2
                    else :
                        self.angle = -math.pi/2
                else :
                    self.angle = math.atan(self.ay / self.ax)
                if self.ax <0 :
                    self.angle += math.pi
                if self.angle < 0 :
                    self.angle += 2* math.pi
    
                self.dataReceived = True
            else :
                self.dataReceived = False
        sensorData = {'a':self.a,'ax':self.ax,'ay':self.ay,'angle':self.angle,'status':self.dataReceived,'btn':self.btn}
        return sensorData