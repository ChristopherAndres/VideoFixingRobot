#Video Fixing Robot
#By Chris Andres
#Requires Ubuntu, Python3, ffmpeg and MediaInfo

#Importing required libs
import os
import argparse
import subprocess
import sys
from datetime import datetime
import shutil

#Passing Arguments from the command line
parser = argparse.ArgumentParser(description='A Tortual of Argparse')
parser.add_argument("-i", required=True, type=str, help="Imput file name")
parser.add_argument("-o", required=True, type=str, help="output File Name")
args = parser.parse_args()

#Basic deffinations
inputFile = args.i
outputFile = args.o

#Starting Folder
startingFolder = os.getcwd()
print("Working on: " +inputFile)

#Creating A working folder
workingFolder = inputFile + "_Working"
os.mkdir(workingFolder)
shutil.copy(inputFile, workingFolder)

#Moving to the working folder
os.chdir(workingFolder)

#Script used to rip frames from the video, and re render it
ffmpegInput = "ffmpeg -i " + str(inputFile) + " -r 1/1 " + "$filename%03d.tiff"

#running the ffmpeg script
os.system(ffmpegInput)

print("done")

#ffmpeg rendering script
ffmpegOutput = "ffmpeg -r 4 -i %03d.tiff -c:v libx264 -vf fps=30 -pix_fmt yuv420p " + outputFile

#running the output script
os.system(ffmpegOutput)

#copying the output file back to the starting dir, and cleaning up the workspace
shutil.move(outputFile, startingFolder)
os.chdir(startingFolder)
shutil.rmtree(workingFolder)

print("Done")