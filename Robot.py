#Video Fixing Robot
#By Chris Andres
#Requires Python3, and MediaInfo

#Importing required libarys
import os
import argparse
import subprocess

#Passing Arguments from the command line
parser = argparse.ArgumentParser(description='A Tortual of Argparse')
parser.add_argument("-i", required=True, type=str, help="Imput file name")
parser.add_argument("-o", type=str, help="output File Name")
args = parser.parse_args()

#Basic deffinations
inputFile = args.i
outputFile = args.o

print("Working on: " +inputFile)

widthComand ="mediainfo --inform=" + "'" + "Video" +";" + "%Width%" + "'" + " " + inputFile
heightCommand ="mediainfo --inform=" + "'" + "Video" +";" + "%Height%" + "'" + " " + inputFile


width = os.popen(widthComand).read()
height = os.popen(heightCommand).read()

print("The Width is: " + width)
print("The Height is: " + height)


#Used to test syscall
#call(["ls", "-l"])

