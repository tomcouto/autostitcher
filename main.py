import os, random, sys

from moviepy.editor import *


clips_directory = os.getcwd() + '/clips/'
intro_dir = os.getcwd() + '/intro/'
outro_dir = os.getcwd() + '/outro/'


def build_video(clips_directory):
    # create a list of clips from clip folder

    clips_from_directory = os.listdir(clips_directory)
    intros = os.listdir(intro_dir)
    outros = os.listdir(outro_dir)

    clips = []

    # add intro to list first
    for mp4s in intros:
        clips.append(VideoFileClip(intro_dir + mp4s))

    # iterate through folder of clips adding them as VideoFileClip type to a list
    for mp4_file in clips_from_directory:
        mp4_file_to_append_to_list = clips_directory + mp4_file

        clips.append(VideoFileClip(mp4_file_to_append_to_list))

    # add outro to clips list
    for outs in outros:
        clips.append(VideoFileClip(outro_dir + outs))

    # append all videofileclips together
    video = concatenate_videoclips(clips, method='compose')

    # set the path to full videos for writing out
    full_videos_directory = os.getcwd() + '/full_videos/render.mp4'

    # write out video file with audio in 30 fps
    video.write_videofile(
        full_videos_directory,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        bitrate=None,
        audio=True,
        audio_fps=44100,
        preset='medium',
        audio_nbytes=4,
        audio_bitrate=None,
        audio_bufsize=2000,
        rewrite_audio=True,
        verbose=True,
        threads=None,
        ffmpeg_params=None)


build_video(clips_directory)
