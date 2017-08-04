# Rotate a gif
# depend on PIL, imageio

import PIL.Image
import imageio
import os.path
import shutil

def extractGIF( gif_file, output_path, output_format = "{0}.png" ):
    frame = PIL.Image.open( gif_file )
    frame_index = 0
    frame_names = []
    while frame:
        frame_name = os.path.join( output_path, output_format.format( frame_index ) )
        frame_names.append( frame_name )
        frame.save( frame_name, 'PNG' )
        frame_index += 1
        try:
            frame.seek( frame_index )
        except EOFError:
            break

    return frame_names

def rotateFrames( frames, angle ):
    for frame_name in frames:
        frame = PIL.Image.open( frame_name )
        frame = frame.rotate( angle )
        frame.save( frame_name )

def makeGIF( frames, output_file ):
    gif_frames = []
    for frame_name in frames:
        gif_frames.append( imageio.imread( frame_name ) )

    if os.path.exists( output_file ):
        os.remove( output_file )

    imageio.mimsave( output_file, gif_frames )

if __name__ == "__main__":
    root = r"D:\test\python"
    gif_file = r"88.gif"
    output_gif = r"88_rotate90.gif"
    temp_folder = "temp_gif"

    os.chdir( root )
    if not os.path.exists( temp_folder ):
        os.makedirs( temp_folder )

    frames = extractGIF( gif_file, temp_folder )
    rotateFrames( frames, 360 )
    makeGIF( frames, output_gif )

##    shutil.rmtree( temp_folder )
    