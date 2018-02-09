from moviepy.editor import *

clip = VideoFileClip("here input video .mp4").subclip(000000,000003)

clip=clip.set_pos('center')
imag=ImageSequenceClip(['f.jpg',], fps=24)

video = CompositeVideoClip([imag,clip])
#video.preview(fps=25, audio=False)
video.write_videofile("here you output video.mp4",fps=24)
