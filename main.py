import sim
import numpy as np
import struct
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID !=-1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')
sim.simxGetPingTime(clientID)
# sim.simxFinish(clientID)
ret, targetObj = sim.simxGetObjectHandle(clientID, 'qd_target', 
                  sim.simx_opmode_blocking)
ret_qd, qd = sim.simxGetObjectHandle(clientID, 'Quadcopter_1', 
                  sim.simx_opmode_blocking)
ret, arr = sim.simxGetObjectPosition(clientID, targetObj, -1, sim.simx_opmode_blocking)
# reto, arro = sim.simxGetOb
print(ret)
print(sim.simx_return_ok)
if ret==sim.simx_return_ok:
    print (type(arr))
# thrust = [0,0,10]  # Force in the x direction
# torque = [0,0,5]  # Torque around the z axis
# sim.simxSetObjectPosition(clientID, targetObj,-1,(arr[0],arr[1] + 1,arr[2]), 
#                   sim.simx_opmode_blocking)
# 示例：传递参数到CoppeliaSim中的一个信号 
# thrust = 1.0 # 推力值，可以根据需要修改 
# torque = 4.0 # 目标位置的Z值，可以根据需要修改 # 发送信号到CoppeliaSim
torque_array = np.array([1.1, 2.2, 3.3], dtype=np.float32)

    # 将数组转换为字符串
torque = struct.pack('f' * len(torque_array), *torque_array)
thrust_array = np.array([1.1, 2.2, 3.3], dtype=np.float32)

    # 将数组转换为字符串
thrust = struct.pack('f' * len(torque_array), *torque_array)
# # 传入数组到CoppeliaSim
# torque = 'abcd'
i = 0
sim.simxSetStringSignal(clientID, 'start', 's', sim.simx_opmode_oneshot_wait)
while i<10: 
    result = sim.simxSetStringSignal(clientID,'torque_1', torque, sim.simx_opmode_oneshot_wait)
    sim.simxSetStringSignal(clientID,'thrust_1', thrust, sim.simx_opmode_oneshot_wait)
    # if result == sim.simx_return_ok:
    #     print(torque)
    # else:
    #     print('Failed to send string signal')
    # result = sim.simxSetFloatSignal(clientID, 'thrust_x', thrust, sim.simx_opmode_oneshot_wait) 
    # sim.simxSetFloatSignal(clientID, 'torque_x', torque, sim.simx_opmode_oneshot_wait)
    # sim.simxSetFloatSignal(clientID, 'thrust_y', thrust, sim.simx_opmode_oneshot_wait) 
    # sim.simxSetFloatSignal(clientID, 'torque_y', torque, sim.simx_opmode_oneshot_wait)
    # sim.simxSetFloatSignal(clientID, 'thrust_z', thrust, sim.simx_opmode_oneshot_wait) 
    # sim.simxSetFloatSignal(clientID, 'torque_z', torque, sim.simx_opmode_oneshot_wait)
    i = i + 1
    if result == sim.simx_return_ok:
        print('sucess')
    else:
        print('Failed to send string signal')
sim.simxSetStringSignal(clientID, 'start', 'e', sim.simx_opmode_oneshot_wait)
# sim.addForceAndTorque(clientID, qd, force, torque, sim.simx_opmode_blocking)
sim.simxFinish(clientID)
# import sim

# # Connect to the remote API server
# clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
# if clientID != -1:
#     print('Connected to remote API server')

#     # Get the handle of the object
#     returnCode, objectHandle = sim.simxGetObjectHandle(clientID, 'Quadcopter_1', sim.simx_opmode_blocking)

#     if returnCode == sim.simx_return_ok:
#         print(f'Object handle: {objectHandle}')
        
#         # Define the force and torque to be applied
#         force = [10, 0, 0]  # Force in the x direction
#         torque = [1, 0, 5]  # Torque around the z axis

#         # Apply the force and torque
#         returnCode = sim.simxCallScriptFunction(clientID, 'remoteApiCommandServer',
#                                         sim.sim_scripttype_childscript,
#                                         'sim.addForceAndTorque',
#                                         [objectHandle], force + torque,
#                                         [], bytearray(), sim.simx_opmode_blocking)
#     else:
#         print('Failed to get object handle')

#     # Close the connection to the server
#     sim.simxFinish(clientID)
# else:
#     print('Failed connecting to remote API server')
