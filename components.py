import streamlit as st
from pytube import YouTube
import os

def init():
    st.set_page_config(page_title="My YouTube Video Downloader",layout="wide")
    st.title('My yt video downloader')
    
def _link_input():
    link = st.text_input(label=" ",label_visibility='collapsed',placeholder="Enter Link")
    st.session_state.link = link
    
def _load_video_btn():
    if st.button("Load Video"):
        load_video()

def link_bar_container():
    col1,col2 = st.columns([5,1])
    with col1:
        _link_input()
    with col2:
        _load_video_btn()

def load_video():
    pass

def video_title(yt_vid_title="Empty"):
    st.write(yt_vid_title)
    
def video_info_container():
    if 'link' in st.session_state and st.session_state.link:
        col_left,col_right = st.columns([1,1])
        with col_left:
            _video_player()
        with col_right:
            vid_description()
            col_prop,col_download = st.columns([4,1])
            with col_prop:
                _video_properties()
            with col_download:
                mp4download_btn(st.session_state.link)
                mp3download_btn(st.session_state.link)
    
def _video_player():
    try:
        st.video(st.session_state.link)
    except:
        st.error("Video link is not valid")


def mp4download_btn(link):
    quality_choice = ("144p","480p","720p","1080p")
    if st.button("MP4 Download"):
        st.selectbox("quality", options = quality_choice)
        downloadmp4(link)
        
def downloadmp4(link):
    path = os.path.join(os.path.expanduser("~"), "Desktop/Visual Studio Code/Downloaded/Video")
    # YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download(path)
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download(path)
    
        
def mp3download_btn(link):
    if st.button("MP3 Download"):
        downloadmp3(link)
        
def downloadmp3(link):
    path = os.path.join(os.path.expanduser("~"), "Desktop/Visual Studio Code/Downloaded/Sound")
    yt = YouTube(link)
    streams = yt.streams.filter(only_audio=True)
    stream = streams.first()
    stream.download(path)

        
def yt_vid_quality():
    st.selectbox("Video quality")
    
def _video_properties():
    
    st.write("**Autor:** EricVanWilderman")
    st.write("**Date:** 23 sie 2023")
    st.write("**Likes:** 17k")
    st.write("**Views:** 872 062")
    
    
def vid_description():
    st.text_area("Description", disabled=True, value="""
             Is it possible to do the Geometry Dash RobTop main levels but only using the SHIP? Instead of taking the normal path I did with the wave, I just wanted to see if it was possible at all completing these levels in any way using the ship.  I did try to take the normal path when possible though.

MERCH STORE
https://streamlabs.com/ericvanwilderm...

BECOME A MEMBER TO JOIN MY PRIVATE DISCORD
 

 / discord  

MY OTHER CHANNEL
  

 / @vanwildermangame  

FOLLOW ME
Instagram ►  

 / eric_vanwilderman  
Twitter ►  

 / vanwilderman  

#geometrydash #gd #ship
             """, height=275)    