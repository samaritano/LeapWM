# LeapWM - Events sender
#
# Author: Paolo Aldovini
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from evdev import UInput, ecodes as e
import time

# Get input device
ui = UInput()

# Send <super> + 'W' keyboard combination (Spread all windows)
ui.write(e.EV_KEY, e.KEY_LEFTMETA, 1) # <super> key down
ui.write(e.EV_KEY, e.KEY_W, 1) # 'W' key down
ui.write(e.EV_KEY, e.KEY_W, 0) # 'W' key up
ui.write(e.EV_KEY, e.KEY_LEFTMETA, 0) # <super> key up
ui.syn()

time.sleep(2)

ui.write(e.EV_KEY, e.KEY_LEFTMETA, 1) # <super> key down
ui.write(e.EV_KEY, e.KEY_W, 1) # 'W' key down
ui.write(e.EV_KEY, e.KEY_W, 0) # 'W' key up
ui.write(e.EV_KEY, e.KEY_LEFTMETA, 0) # <super> key up
ui.syn()

time.sleep(2)

# Simulate Alt + Tab keyboard combination
ui.write(e.EV_KEY, e.KEY_LEFTALT, 1) # Alt key down
ui.write(e.EV_KEY, e.KEY_TAB, 1) # Tab key down
ui.write(e.EV_KEY, e.KEY_TAB, 0) # Tab key up
ui.write(e.EV_KEY, e.KEY_TAB, 1) # Tab key down
ui.write(e.EV_KEY, e.KEY_TAB, 0) # Tab key up
ui.write(e.EV_KEY, e.KEY_LEFTALT, 0) # Alt key up
ui.syn()

time.sleep(2)

ui.write(e.EV_KEY, e.KEY_LEFTALT, 1) # Alt key down
ui.write(e.EV_KEY, e.KEY_TAB, 1) # Tab key down
ui.write(e.EV_KEY, e.KEY_TAB, 0) # Tab key up
ui.write(e.EV_KEY, e.KEY_LEFTALT, 0) # Alt key up
ui.syn()

# Close input device
ui.close()