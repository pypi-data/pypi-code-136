import win32api
import win32gui
import win32con

from common import _Listener

class Listener(_Listener):

    def _callback_filtered(self, _hwnd, msg, wparam, _lparam):
        if msg == win32con.WM_POWERBROADCAST \
            and wparam  == win32con.PBT_APMSUSPEND:
            self.on_sleep() 
        elif msg == win32con.WM_QUERYENDSESSION:
            self.on_shutdown()

    def _event_thread(self):
        self.hwind = self._mk_hwnd()
        events = True
        while events: # poll for new events
            events, msg = win32gui.GetMessage(None, 0, 0) # type: ignore
            win32gui.DispatchMessage(msg) # type: ignore
            
    def _mk_hwnd(self):
        wndclass = win32gui.WNDCLASS()
        wndclass.hInstance = win32api.GetModuleHandle(None) # type: ignore
        wndclass.lpszClassName = "bedtime"
        wndclass.lpfnWndProc = { 
            win32con.WM_QUERYENDSESSION: self._callback_filtered,
            win32con.WM_POWERBROADCAST : self._callback_filtered }
        myWindowClass = win32gui.RegisterClass(wndclass) # type: ignore
        hwnd = win32gui.CreateWindowEx(win32con.WS_EX_LEFT, # type: ignore
                                        myWindowClass, 
                                        "", 
                                        0, 0, 0, 
                                        win32con.CW_USEDEFAULT, 
                                        win32con.CW_USEDEFAULT, 
                                        0, 0, 
                                        wndclass.hInstance, 
                                        None)
        return hwnd

    def __del__(self):
        win32gui.DestroyWindow(self.hwnd) # type: ignore