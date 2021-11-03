#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import subprocess
import matplotlib.pyplot as plt 
 
fio_size="1m" 
fio_runtime="60" 
fio_rwmixwrite="33" 
fio_filesize="1g" 
fio_readwrite="randrw" 
fio_direct="0" 
numjobs="1"
device = 'nvme0n1'
fio_slat_pos_start=9
fio_clat_pos_start=13
fio_lat_pos_start=37
blocksize = "256k"


slat_tab = []
clat_tab = []
lat_tab = []

for blocksize in ('1k', '2k', '4k', '16k', '256k', '1m'):
  command = "sudo fio --minimal -name=temp-fio --bs="+str(blocksize)+" --ioengine=libaio --iodepth=1"+" --size="+fio_size+" --direct=0 --rw=randrw"+" --filename=/dev/"+str(device)+" --numjobs="+str(numjobs)+" --time_based --runtime="+fio_runtime+" --group_reporting"
  os.system (command)

  os.system("sleep 2") #Give time to finish inflight IOs
  try:
    output = subprocess.check_output(command, shell=True)
  except subprocess.CalledProcessError, e:
    print e.output

  fio_type_offset=41

  # slat
  slat = float(output.split(";")[fio_type_offset+fio_slat_pos_start])
  print(slat)
  slat_tab.append(slat)

  # clat
  clat = float(output.split(";")[fio_type_offset+fio_clat_pos_start])
  print(clat)
  clat_tab.append(clat)

  # lat
  lat = float(output.split(";")[fio_type_offset+fio_lat_pos_start])
  print(lat)
  lat_tab.append(lat)

lw = 2

plt.plot(size, slat_tab, color='yellow', linewidth=lw, label='slat')
plt.legend(loc='upper right')
plt.show()
plt.plot(size, lat_tab, color='red', linewidth=lw, label='lat')
plt.legend(loc='upper right')
plt.show()
plt.plot(size, clat_tab, color='black', linewidth=lw, label='clat')
plt.legend(loc='upper right')
plt.show()
