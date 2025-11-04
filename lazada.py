def Lazada_get_jfy( driver ) :

    webautomatic.goto_web( driver , 'https://www.lazada.co.th' , clear_ctrl_f5=True , wait_to_load=3 )
    webautomatic.scroll_max( driver )
    time.sleep( 5 )

    element_data = webautomatic.find_custom_xpath_muti ( driver , xpath ='//div[@class="card-jfy-wrapper"]//img[@class="image" and contains( @src , ".webp") ]' , timeout =0.5 )
    tools.print_attribute ( element_data , 'src' , print_all=False )
    src_img = tools.convert_attribute_to_list ( element_data , 'src'  )

    element_data =webautomatic.find_custom_xpath_muti ( driver , xpath ='//div[@class="card-jfy-wrapper"]//span[@class="title"]' , timeout =0.5 )
    tools.print_text ( element_data , print_all=False )
    title = tools.convert_text_to_list ( element_data  )

    element_data =webautomatic.find_custom_xpath_muti ( driver , xpath ='//div[@class="card-jfy-wrapper"]//div[@class="hp-mod-price-first-line"]//span[@class="price"]' , timeout =0.5 )
    tools.print_text ( element_data , print_all=False )
    price = tools.convert_text_to_list ( element_data  )

    element_data = webautomatic.find_custom_xpath_muti ( driver , xpath ='//div[@class="card-jfy-wrapper"]//a[contains( @href , "//www.lazada.co.th/products/" ) ]' , timeout =0.5 )
    tools.print_attribute ( element_data , 'href' , print_all=False )
    href = tools.convert_attribute_to_list ( element_data , 'href'  )

    element_data =webautomatic.find_custom_xpath_muti ( driver , xpath ='//div[@class="card-jfy-wrapper"]//div[@class="card-jfy-ratings-comment"]' , timeout =0.5 )
    tools.print_text ( element_data , print_all=False )
    review = tools.convert_text_to_list ( element_data  )

    if len( src_img ) == len( title ) == len( price ) == len( href ) == len( review ) :

        data = {

            'รูปสินค้า' : src_img , 
            'ชื่อสินค้า' : title , 
            'ราคาสินค้า' : price , 
            'ลิงค์สินค้า' : href , 
            'รีวิวสินค้า' : review 

        }

        df = pd.DataFrame( data )

        file_save_name = 'Lazada-Dataset.xlsx'

        df.to_excel(  file_save_name , index=False )

        print( 'สำเร็จ' )

    else :

        print( 'ไม่สำเร็จ' )