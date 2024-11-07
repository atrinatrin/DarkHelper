#--------------------------------------------------------------------------|Variebels For Api
api_id =11057906                                                          #-|
api_hash = 'b7f975dcdf30c826b3e6178ff3f72356'                            #-|
bot_id= 1658760514                                                       #-|
bot_username='@managemntapuBot'#@darkhelperrobot'                        #-|
#--------------------------------------------------------------------------| » Creating Client & Import Pyrogram
from pyrogram import Client                                              #-|                          
bot = Client('amirairj-helper', api_id, api_hash                         #-|  
,workers=300,workdir =r'/root/helper/crused/V2/Config/Info/bot')         #-| YOUR PATH 
del  api_hash , api_id                                                   #-|
#--------------------------------------------------------------------------|
