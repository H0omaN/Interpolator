import glob
import subprocess
import os

outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/Sample/IMERG-Comprehensive-V06/"
files=os.listdir(outputfolder)
files.sort()
outpufiles=glob.glob(outputfolder+"*.nc")
outpufiles.sort() 
i=0
for file in outpufiles:
    Script0='cdo remapcon2,/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/Sample/IMERG-Comprehensive-V06/grid '
    Script1=file+' /extracted/'+files[i]
    Script=Script0+Script1
    subprocess.getstatusoutput(Script)
    i=i+1