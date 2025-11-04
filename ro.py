# ลิงค์ดาวน์โหลด Diagram : https://app.code2flow.com/dZXeutE7It7w

import random
handle = tool_v2.get_handle_id( 'Ragnarok Landverse' )[0]

obj_autoclick =autoclick_v2( 
  
  mode_pic =2 ,
  mode_click =5 ,

  add_x =0 ,
  delete_x =9 ,
  add_y =0 ,
  delete_y =32 
  
)

class move_pos_func :

  def move_pos( handle , obj_autoclick : autoclick_v2 ) :

    move_set = [  
      
      [651, 240], 
      [658, 563], 
      [457, 397], 
      [826, 393], 
      [552, 288], 
      [813, 505], 
      [787, 292], 
      [483, 516], 
                    
    ]

    random.shuffle( move_set )

    _ , _ , ( x,y ) = win32gui.GetCursorInfo()

    move_last = move_set[0]

    obj_autoclick.move_mouse( handle_id=handle  , first=[x,y] , last=[move_last[0],move_last[1]] , delay=0.5 , showdb=True   )

    while True :

      if obj_autoclick.find_img ( handle_id=handle , pic_local='no-move.png' , threshold_set=0.85 , showimg=False , modecoler=False , rectangle_show=0  , showdb= False , timeout=1 , region=None ) != False :
        
        print( 'ไม่สามารถคลิกได้' )

        random.shuffle( move_set )

        move_last = move_set[0]

        obj_autoclick.move_mouse( handle_id=handle  , first=[x,y] , last=[move_last[0],move_last[1]] , delay=0.5 , showdb=False   )

      else :
        
        print( 'สามารถคลิกได้' )

        for x in range( 3 ) :

          obj_autoclick.click(  handle_id=handle  , local=move_last , lv_click=5 , showdb= True )
          time.sleep( 1 )

        break

      time.sleep(1.5)

class att_mon :

  def att( handle_id ) :
        
    obj_poling_1 =func_bot_coler_process_v2( 
      
      lower_coler =[12 ,88 ,229 ],
      hi_coler =[16 ,109 ,239 ],

      w_set =[30 ,40 ],
      h_set =[20 ,35 ],
    
      mode_pic =2 ,
      mode_click =5 ,

      add_x =0 ,
      delete_x =9 ,
      add_y =0 ,
      delete_y =32 
      
    )

    obj_poling_2 =func_bot_coler_process_v2( 
      
      lower_coler =[0 ,113 ,238 ],
      hi_coler =[2 ,127 ,255 ],

      w_set =[30 ,40 ],
      h_set =[20 ,35 ],
    
      mode_pic =2 ,
      mode_click =5 ,

      add_x =0 ,
      delete_x =9 ,
      add_y =0 ,
      delete_y =32 
      
    )

    obj_farbre =func_bot_coler_process_v2( 
      
      lower_coler =[43 ,57 ,217 ],
      hi_coler =[58 ,75 ,253 ],

      w_set =[15 ,30 ],
      h_set =[15 ,30 ],
    
      mode_pic =2 ,
      mode_click =5 ,

      add_x =0 ,
      delete_x =9 ,
      add_y =0 ,
      delete_y =32 
      
    )

    obj_rabbit =func_bot_coler_process_v2( 
      
      lower_coler =[118 ,0 ,243 ],
      hi_coler =[124 ,31 ,255 ],

      w_set =[20 ,30 ],
      h_set =[20 ,30 ],
    
      mode_pic =2 ,
      mode_click =5 ,

      add_x =0 ,
      delete_x =9 ,
      add_y =0 ,
      delete_y =32 
      
    )

    mon_all = []
    
    mon1 = obj_poling_1.find_process_coler_muti (  handle_id =handle_id ,showdb =False ,timeout =0  ,region =None )

    mon2 = obj_poling_2.find_process_coler_muti (  handle_id =handle_id ,showdb =False ,timeout =0  ,region =None )

    mon3 = obj_farbre.find_process_coler_muti (  handle_id =handle_id ,showdb =False ,timeout =0  ,region =None )

    mon4 = obj_rabbit.find_process_coler_muti (  handle_id =handle_id ,showdb =False ,timeout =0  ,region =None )

    if mon1 != False :
      mon_all = mon_all + mon1

    if mon2 != False :
      mon_all = mon_all + mon2

    if mon3 != False :
      mon_all = mon_all + mon3

    if mon4 != False :
      mon_all = mon_all + mon4

    if len( mon_all ) > 0 :
      
      target_x = 645
      target_y = 361

      pos_attt = min(mon_all, key=lambda point: ((point[0] - target_x) ** 2 + (point[1] - target_y) ** 2) ** 0.5)
      
      return pos_attt

    else :

      return False


while True:
  
  mon_pos = att_mon.att( handle )
  if mon_pos != False :
    print( 'เจอมอนส์เตอร์' )
    
    print( 'คลิกตีมอนเตอร์' )
    obj_autoclick.click(  handle_id=handle  , local=mon_pos , lv_click=5 , showdb= False )

    time.sleep(5)

    while True :

      if obj_autoclick.find_img (  handle_id=handle , pic_local='mon-check.png' , threshold_set=0.75 , showimg=False , modecoler=True , rectangle_show=0 , showdb= False , timeout=0 , region=None ) != False :
        print( 'มอนสเตอร์ยังไม่ตาย' )
        time.sleep(0.5)

      else :
        print( 'มอนสเตอร์ตายแล้ว' )
        break

  else :

    print( 'ไม่เจอมอนส์เตอร์' )
    move_pos_func.move_pos( handle , obj_autoclick ) 

  print( 'รอบอททำงานใหม่' )
  time.sleep( 1 )