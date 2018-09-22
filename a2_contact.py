#%%  Imports
import os.path as osp
from skimage import io
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
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

im_diff = ( 50, 50 )
im_border = [0,0]

for i in [0,1]:
    im_border[i] = int( border_ratio[i] * (full_image_pixels[i] - ( im_dim[i] * images_grid[i] + im_diff[i] * (images_grid[i] - 1) ))  )

#%%  Some font issues calculations
chars = 1488 + np.arange( 27 )
char_length = ( 20, 50, 90, 50, 20, 100, 80, 20, 20, 100, 50, 50, 60, 10, 20, 100, 100, 20, 60, 50, 60, 60, 40, 20, 50, 10, 20 )
clm = dict( zip( chars, map( lambda x:(190 - x)/10, char_length )) )
clm[ ord( ' ' ) ] = 7


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

#%%  Create the image
full_im = np.ones( ( full_image_pixels[0], full_image_pixels[1], 3 ) )
for y in range( images_grid[0] ):
    y_start = y * (im_dim[0] + im_diff[0]) + im_border[0]
    y_end = y_start + im_dim[1]
    for x in range( images_grid[ 1 ] ):
        x_start = x * (im_dim[1] + im_diff[1]) + im_border[1]
        x_end = x_start + im_dim[1]
        full_im[ y_start : y_end, x_start : x_end ] = contacts[ y * images_grid[1] + x ][ 'im_data' ]

#%%
r'test_font.jpg'
r'school-rocket-ship.jpeg'


        if isinstance( c['aba_name'], str ):
            txt += '\n' + c['aba_num'] + ' ' + c['aba_name'][-1::-1]

c['ima_num'] + ' ' + c['ima_name'][-1::-1]
c['date'] + ' ' + c['name'][-1::-1]

chars = 1488 + np.arange( 27 )
char_length = ( 20, 50, 90, 50, 20, 100, 80, 20, 20, 100, 50, 50, 60, 10, 20, 100, 100, 20, 60, 50, 60, 60, 40, 20, 50, 10, 20 )
clm = dict( zip( chars, map( lambda x:(190 - x)/10, char_length )) )
clm[ ord( ' ' ) ] = 7

[ clm[ord[x]] for x in txt ]
io.imsave( r'c:\Users\ajax\Desktop\a2_contact\full_images\test1.jpg', np.uint8( 255 * full_im ) )
fnt = ImageFont.truetype(font='arial.ttf', size=30, index=0, encoding='unic')
x_start : x_end
full_im[ y_start_t : y_end_t, x_start : x_end ]
pil_im = Image.fromarray( ( 255 * im ).astype( np.uint8 ) )

y * im_dim[0] + max(0, im_dim[0] - 1 ) * im_diff[0] + im_border[0]
y_start = y * im_dim[0] + max(0, im_dim[0] - 1 ) * im_diff[0] + im_border[0]
y_end = y_start + im_dim[0]

border_ratio
return [' '.join(t) for t in topic_words]

chars = 1488 + np.arange( 27 )
char_length = ( 20, 50, 90, 50, 20, 100, 80, 20, 20, 100, 50, 50, 60, 10, 20, 100, 100, 20, 60, 50, 60, 60, 40, 20, 50, 10, 20 )
clm = dict( zip( chars, map( lambda x:(190 - x)/10, char_length )) )
clm[ ord( ' ' ) ] = 7

[ clm[ord[x]] for x in txt ]

y * im_dim[0] + max(0, im_dim[0] - 1 ) * im_diff[0] + im_border[0]
        y_start = y * im_dim[0] + max(0, im_dim[0] - 1 ) * im_diff[0] + im_border[0]
        y_end = y_start + im_dim[0]
