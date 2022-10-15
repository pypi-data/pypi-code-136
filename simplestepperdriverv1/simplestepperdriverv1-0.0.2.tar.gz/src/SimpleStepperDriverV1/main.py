# from SimpleStepperDriverV1 import SimpleStepperDriverV1
# import time



# ssd = SimpleStepperDriverV1(method='rtu',serialPort = '/dev/ttyACM0')

# ssd.writeD0(True)
# print(ssd.readA5(),ssd.readA4())
# ssd.on()
# ssd.off()
# ssd.go_forward(steps_per_second=20,steps=200)


# while(1):
#     ssd.go_forward(steps_per_second=200,steps=200)
#     time.sleep(1)
#     ssd.go_backward(steps_per_second=200,steps=200)
#     time.sleep(1)
#     print(ssd.get_steps_from_start())
  # print(ssd.readMap())
    # ssd.stop()