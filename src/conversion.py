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

    bag_path = os.path.join(indir, '2020-12-10-00-01-16.bag')
    b = bagreader(bag_path)

    imu_data = b.message_by_topic('/imu')
    df_imu = pd.read_csv(imu_data)
    df_imu.to_csv(os.path.join(outdir,'imu_data_test.csv'))


    yaw_data = b.message_by_topic('/yaw')
    df_yaw = pd.read_csv(yaw_data)
    df_yaw.to_csv(os.path.join(outdir,'yaw_data_test.csv'))
    
    odometry_path = os.path.join(indir, '2020-12-01-18-09-47.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'odom_data_test.csv'))

    print('Extracted .bag data and written to destination successfully')
    
    return


if __name__ == '__main__':
    main()
