################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys
from evdev import UInput, ecodes as e

class TestListener(Leap.Listener):
    hand_id = 0
    spread_win = False
    curtime = 0
    ui = None
    
    def on_init(self, controller):
        self.ui = UInput()
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame() 

        if not frame.hands.is_empty:
            hand = frame.hands[0]

            fingers = hand.fingers
            if not fingers.is_empty:
                if hand.id == self.hand_id and not self.spread_win and len(fingers) >= 4 and (frame.timestamp - self.curtime) <= 1000000:
                    #print "(Spread) Old timestamp is %d, current is %d (%d)" % (self.curtime, frame.timestamp, (frame.timestamp - self.curtime))
                    self.spread_windows()
                    print "Spread windows"
                    self.spread_win = True
                    self.curtime = frame.timestamp
                    print "Hand open timestamp is %d" % self.curtime
            else:
                if hand.id == self.hand_id and self.spread_win and (frame.timestamp - self.curtime) <= 1000000:
                    #print "(Unspread) Old timestamp is %d, current is %d (%d)" % (self.curtime, frame.timestamp, (frame.timestamp - self.curtime))
                    self.spread_windows()
                    print "Unspread windows"
                    self.spread_win = False
                else:
                    self.hand_id = hand.id
                    self.curtime = frame.timestamp
                    #print "Fist timestamp is %d" % self.curtime

    def spread_windows(self):
        self.ui.write(e.EV_KEY, e.KEY_LEFTMETA, 1) # <super> key down
        self.ui.write(e.EV_KEY, e.KEY_W, 1) # 'W' key down
        self.ui.write(e.EV_KEY, e.KEY_W, 0) # 'W' key up
        self.ui.write(e.EV_KEY, e.KEY_LEFTMETA, 0) # <super> key up
        self.ui.syn()

def main():
    listener = TestListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press Enter to quit..."
    sys.stdin.readline()

    controller.remove_listener(listener)

if __name__ == "__main__":
    main()