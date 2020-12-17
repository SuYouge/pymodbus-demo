#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# PORT = 1
PORT = '/dev/ttyS1'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")

        # try except
        try:
            # 站号 功能码 起始地址 数量
            # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4)) # log
            # res = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1) # 
            # logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=1))
            # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 1))
            # logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 1, 1, 1, 1, 1]))
            logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0, output_value=2048))
            # print(res)
        except Exception as exc:
            alarm = (str(exc))
        #send some queries
        #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
        master.close()

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()
