#%%  Imports
import os.path as osp
from skimage import io
from skimage.transform import resize
import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont
from random import shuffle, seed

#%%  Calculate sizes and resolutions

path = r'c:\dev\a2_contact'
images_grid = ( 4, 8 )
seeds = ( 448, 444 )
im_dim = ( 420, 320 )
border_ratio = ( .8, .5 )

a4_mm = ( 210, 297 )
full_image_pixels = tuple( 10 * x for x in a4_mm )

im_diff = ( 40, 40 )
im_border = [0,0]

for i in [0,1]:
    im_border[i] = int( border_ratio[i] * (full_image_pixels[i] - ( im_dim[i] * images_grid[i] + im_diff[i] * (images_grid[i] - 1) ))  )

#%%  Some font issues calculations
chars = 1488 + np.arange( 27 )
char_length = ( 20, 50, 90, 50, 20, 100, 80, 20, 20, 100, 50, 50, 60, 10, 20, 100, 100, 20, 60, 50, 60, 60, 40, 20, 50, 10, 20 )
clm = dict( zip( chars, map( lambda x:(190 - x)/10, char_length )) )
chars = ord( '0' ) + np.arange( 10 )
clm.update( zip( chars, 10 * [ 13 ] ) )
clm[ ord( ' ' ) ] = 7
clm[ ord( '.' ) ] = 7
clm[ ord( '-' ) ] = 10


#%%  Read from excel
df = pd.ExcelFile( osp.join( path, r'contacts.xlsx' ) ).parse( 'Sheet2' )
contacts = []
contact_items = ( 'image', 'name', 'date', 'ima_name', 'ima_num', 'aba_name', 'aba_num' )
for i, row in df.iterrows():
    contacts.append( dict( zip( contact_items, [ row[ x ] for x in contact_items ] ) ) )

#%%  Reading contact images
for c in tqdm( contacts ):
    c[ 'im_data' ] = resize( io.imread( osp.join( path, c['image'] ) ), ( im_dim[1], im_dim[1] ) )

#%%  shuffle contacts
for s in seeds:
    seed( s )
    shuffle( contacts )

#%%  generating text image
def GetTxtAndMaxLength( c ):
    lines = [ c['date'] + ' ' + c['name'][-1::-1], 
              c['ima_num'] + ' ' + c['ima_name'][-1::-1] ]
    if isinstance( c['aba_name'], str ):
        lines.append( c['aba_num'] + ' ' + c['aba_name'][-1::-1] )
    max_length = np.max( [ sum( [ clm[ord(x)] for x in txt ] ) for txt in lines ] )
    return '\n'.join( lines ), max_length

def EmbedTxtToImg( im, c ):
    pil_im = Image.fromarray( ( 255 * im ).astype( np.uint8 ) )
    fnt = ImageFont.truetype( font='david.ttf', size=30, index=0, encoding='unic', layout_engine=ImageFont.LAYOUT_RAQM )
    txt, max_length = GetTxtAndMaxLength( c )
    draw = ImageDraw.Draw( pil_im )
    draw.multiline_text( ( im.shape[1] - max_length - 4, 4 ), txt, fill=(255,255,0), font=fnt, spacing=4, align="right" )
    return np.array( pil_im ).astype( np.float ) / 255

#%% create the final image
full_im = resize( io.imread( osp.join( path, r'school-rocket-ship.jpeg' )), ( full_image_pixels[0], full_image_pixels[1] ) )
for (y,x), c in tqdm( zip( np.ndindex( images_grid ), contacts ) ):
    y_start = y * (im_dim[0] + im_diff[0]) + im_border[0]
    y_end = y_start + im_dim[1]
    x_start = x * (im_dim[1] + im_diff[1]) + im_border[1]
    x_end = x_start + im_dim[1]
    full_im[ y_start : y_end, x_start : x_end ] = contacts[ y * images_grid[1] + x ][ 'im_data' ]
    y_text_start = y_end
    y_text_end = y_text_start + im_dim[0] - im_dim[1]
    full_im[ y_text_start : y_text_end, x_start : x_end ] = EmbedTxtToImg( .4 * full_im[ y_text_start : y_text_end, x_start : x_end ], c )

#%% save to file
io.imsave( osp.join( path, 'contacts.png' ), full_im )
