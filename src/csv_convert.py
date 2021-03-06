import os
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import math

def convert(indir, outdir):
    dir = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, dir)
    
    #reset if needed
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)
    
    print(path)
    print(indir)
    print(outdir)

    os.mkdir(path)
    os.mkdir(outdir)

    print('Output directory created successfully')
    
    odometry_path = os.path.join(indir, '2021-01-25-18-09-47.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'odom_data_test.csv'))
    
    
    odometry_path = os.path.join(indir, 'straight_3412.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_3412 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_3412.csv'))

    odometry_path = os.path.join(indir, 'straight_3912.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_3912 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_3412.csv'))

    odometry_path = os.path.join(indir, 'straight_4112.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_4112 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_4112.csv'))

    odometry_path = os.path.join(indir, 'straight_3912.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_3912 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_3912.csv'))

    odometry_path = os.path.join(indir, 'straight_4612.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_4612 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_4612.csv'))

    odometry_path = os.path.join(indir, 'straight_5112.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_5112 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_5112.csv'))

    odometry_path = os.path.join(indir, 'straight_5612.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom_5612 = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'df_odom_5612.csv'))