#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from win32api import *
from win32gui import *
import time
import win32con

# Class
class WindowsBalloonTip:
    def __init__( self, title, msg, t = 10 ):
        message_map = { win32con.WM_DESTROY: self.OnDestroy, }

        # Register the window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle( None )
        wc.lpszClassName = 'PythonTaskbar'
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass( wc )

        # Create the window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None )
        UpdateWindow( self.hwnd )

        # Icons managment
        iconPathName = "C:/Program Files/Common Files/TortoiseOverlays/icons/Blip/AddedIcon.ico"
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage( hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags )
        except:
            hicon = LoadIcon( 0, win32con.IDI_APPLICATION )
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = ( self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, 'Tooltip' )

        # Notify
        Shell_NotifyIcon( NIM_ADD, nid )
        Shell_NotifyIcon( NIM_MODIFY, ( self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, hicon, 'Balloon Tooltip', msg, 200, title ) )
        # self.show_balloon(title, msg)
        time.sleep( t )

        # Destroy
        DestroyWindow( self.hwnd )
        classAtom = UnregisterClass( classAtom, hinst )
        
    def OnDestroy( self, hwnd, msg, wparam, lparam ):
        nid = ( self.hwnd, 0 )
        Shell_NotifyIcon( NIM_DELETE, nid )
        PostQuitMessage( 0 )
