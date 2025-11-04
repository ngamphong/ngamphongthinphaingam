handle = tool_v2.get_handle_id( '05.mp4' )

obj = autoclick_v2(  mode_pic =2 ,mode_click =1 ,add_x =0 ,delete_x =0 ,add_y =0 ,delete_y =0 )

kb = keyboard_custom( keyboard_mode=2 , handle=handle[0] , showdb=True , safemode=False )

while True :

  if obj.find_pixel_box( handle_id=handle[0]  , local_box=[463, 351, 215, 18] , hex_coler_list=['0xBA1104'] , shade=5  , showdb= False , timeout=60 , step=1  ) != False :

    kb.Keydown_Keyup( keytarget='e' , delay=0.1  , presses=1 , active_windows=True , delay_active_window=0  )
    print( 'กดปุ่ม : e สำเร็จ !' )
