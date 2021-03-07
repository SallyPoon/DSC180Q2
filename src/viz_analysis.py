import os
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import math
import numpy as np

# IMU Mount Analysis Plots

def mounting_imu_plot(filename, outdir):
    df_imu = pd.read_csv(filename)
    df_imu['Time'] - df_imu['Time'].min()

    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.x'], label='Lin. Accel X')
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.y'], label='Lin. Accel Y')
    plt.axhline(y=0, color='black', xmin=0.04, xmax=0.96, label= 'Zero Accel')
    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Linear Acceleration (m/$s^2$)', fontsize=20)
    plt.legend(fontsize=14)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Linear Acceleration', fontsize=20)

    name = filename.split("/")[-1]
    name = name.split(".")[0]

    plt.savefig(os.path.join(outdir, "Mounting_" + name + ".png"))
    print("Mounting " + name + ' plot success!')

# IMU Half Arc Analysis Plots

def half_arc_yaw_plot(filename, plot_range, outdir):
    df_imu = pd.read_csv(filename)
    df_imu['Time'] - df_imu['Time'].min()
    yaw_offset = [x + 360 if x < 0 else x for x in df_imu['data']]
    plt.figure(figsize=(10,8))
    plt.title('West to East Yaw', fontsize=20)
    plt.plot(df_imu['Time'][:plot_range], yaw_offset[:plot_range])
    plt.axhline(y=270, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    plt.axhline(y=90, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Yaw (deg)', fontsize=20)

    name = filename.split("/")[-1]
    name = name.split(".")[0]

    plt.savefig(os.path.join(outdir,  "Half_Arc_" + name + ".png"))
    print("Half Arc IMU " + name + ' plot success!')

# IMU topic data plots first
def report_plots(filename, outdir):
    df_imu = pd.read_csv(filename)
    df_imu['Time'] - df_imu['Time'].min()
    
    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.x'])
    plt.title('IMU X-Acceleration')
    plt.xlabel('Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.savefig(os.path.join(outdir, 'accel_x_plt.png'))
    print('x-acceleration plot success!')
    
    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.y'])
    plt.title('IMU Y-Acceleration')
    plt.xlabel('Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.savefig(os.path.join(outdir, 'accel_y_plot.png'))
    print('y-acceleration plot success!')
    
    plt.figure(figsize=(10,8))
    plt.scatter(df_imu['linear_acceleration.x'], df_imu['linear_acceleration.y'], alpha=0.5)
    plt.title('IMU Scatterplot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(os.path.join(outdir, 'accel_scatter_plot.png'))
    print('scatter-acceleration plot success!')
    
    plt.figure(figsize=(10,8))
    plt.hist(df_imu['linear_acceleration.x'], bins=None)
    plt.title('IMU X-Acceleration Distribution')
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(outdir, 'accel_x_hist.png'))
    print('x-acceleration hist plot written successfully!')
    
    plt.figure(figsize=(10,8))
    plt.hist(df_imu['linear_acceleration.y'], bins=None)
    plt.title('IMU X-Acceleration Distribution')
    plt.xlabel('y')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(outdir, 'accel_y_hist.png'))
    print('y-acceleration hist plot success!')

    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['orientation.x'])
    plt.title('Orientation X-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (X)')
    plt.savefig(os.path.join(outdir, 'orient_x_plot.png'))
    print('orientation x plot success!')
   
    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['orientation.y'])
    plt.title('Orientation Y-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (X)')
    plt.savefig(os.path.join(outdir, 'orient_y_plot.png'))
    print('orientation y plot success!')
    
    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['orientation.z'])
    plt.title('Orientation Z-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (Z)')
    plt.savefig(os.path.join(outdir, 'orient_z_plot.png'))
    print('orientation z plot success!')

    plt.figure(figsize=(10,8))
    plt.plot(df_imu['Time'], df_imu['orientation.z'])
    plt.title('Orientation W-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (W)')
    plt.savefig(os.path.join(outdir, 'orient_w_plot.png'))
    print('orientation w plot success!')

def odom_plots(filename, outdir):

    df_odom = pd.read_csv(filename)
    
    name = filename.split("/")[-1]
    name = name.split("_")[-1]
    name = name.split(".")[0]

    plt.figure(figsize=(10,8))
    plt.plot(df_odom['pose.pose.position.x'], [0] * len(df_odom))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain " + name)
    plt.xticks(np.arange(0, 2.5 ,0.2))

    plt.savefig(os.path.join(outdir, 'ERPM_Gain_' + name + '.png'))
    print('ERPM_Gain ' + name + ' plot success!')


def plot_all(outdir, IMU, Odom):

    # Reset outdir
    if (os.path.exists(outdir) and os.path.isdir(outdir)):
        shutil.rmtree(outdir)
    
    os.mkdir(outdir)

    #Plot IMU Mounting
    for filename in IMU['Mounting']:
        mounting_imu_plot(filename, outdir)

    #Plot IMU Half Arc
    for d in IMU['Half_Arc']:
        half_arc_yaw_plot(d["f"], d["r"], outdir)

    #Plot IMU Report
    report_plots(IMU['Report'], outdir)

    #Plot Odom Tuning
    for filename in Odom['Vesc']:
        odom_plots(filename, outdir)

    return

    # df_imu = pd.read_csv(mount_simple)
    # df_imu['Time'] - df_imu['Time'].min()
    
    # plt.figure(figsize=(10,8))
    # plt.plot(df_imu['Time'], df_imu['linear_acceleration.x'], label='Lin. Accel X')
    # plt.plot(df_imu['Time'], df_imu['linear_acceleration.y'], label='Lin. Accel Y')
    # plt.axhline(y=0, color='black', xmin=0.04, xmax=0.96, label= 'Zero Accel')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('Linear Acceleration (m/$s^2$)', fontsize=20)
    # plt.legend(fontsize=14)
    # plt.xticks(fontsize=16)
    # plt.yticks(fontsize=16)
    # plt.title('Linear Acceleration', fontsize=20)

    # df_imu = pd.read_csv(mount_sec)
    # df_imu['Time'] - df_imu['Time'].min()
    
    # plt.figure(figsize=(10,8))
    # plt.plot(df_imu['Time'], df_imu['linear_acceleration.x'], label='Lin. Accel X')
    # plt.plot(df_imu['Time'], df_imu['linear_acceleration.y'], label='Lin. Accel Y')
    # plt.axhline(y=0, color='black', xmin=0.04, xmax=0.96, label= 'Zero Accel')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('Linear Acceleration (m/$s^2$)', fontsize=20)
    # plt.legend(fontsize=14)
    # plt.xticks(fontsize=16)
    # plt.yticks(fontsize=16)
    # plt.title('Linear Acceleration', fontsize=20)

    





    # df_imu = pd.read_csv(yaw_hfg)
    # df_imu['Time'] - df_imu['Time'].min()
    # yaw_offset = [x + 360 if x < 0 else x for x in df_imu['data']]
    # plt.figure(figsize=(10,8))
    # plt.title('West to East Yaw', fontsize=20)
    # plt.plot(df_imu['Time'][:-100], yaw_offset[:-100])
    # plt.axhline(y=270, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.axhline(y=90, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('Yaw (deg)', fontsize=20)

    # df_imu = pd.read_csv(yaw_hfo)
    # df_imu['Time'] - df_imu['Time'].min()
    # yaw_offset = [x + 360 if x < 0 else x for x in df_imu['data']]
    # plt.figure(figsize=(10,8))
    # plt.title('West to East Yaw', fontsize=20)
    # plt.plot(df_imu['Time'], yaw_offset)
    # plt.axhline(y=270, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.axhline(y=90, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('Yaw (deg)', fontsize=20)

    # df_imu = pd.read_csv(yaw_hfu)
    # df_imu['Time'] - df_imu['Time'].min()
    # yaw_offset = [x + 360 if x < 0 else x for x in df_imu['data']]
    # plt.figure(figsize=(10,8))
    # plt.title('West to East Yaw', fontsize=20)
    # plt.plot(df_imu['Time'][:-350], yaw_offset[:-350])
    # plt.axhline(y=270, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.axhline(y=90, color='red', xmin=0.04, xmax=0.96, label= 'Zero Accel', linestyle='dashed')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('Yaw (deg)', fontsize=20)


    
    
    # plt.plot(df_imu['Time'], df_imu['orientation.x'])
    # plt.title('Orientation X-Value')
    # plt.xlabel('Time')
    # plt.ylabel('Quaternion (X)')
    # plt.savefig(os.path.join(outdir, 'orient_x_plot.png'))
    # print('orientation x plot success!')
    
    # plt.plot(df_imu['Time'], df_imu['orientation.y'])
    # plt.title('Orientation Y-Value')
    # plt.xlabel('Time')
    # plt.ylabel('Quaternion (X)')
    # plt.savefig(os.path.join(outdir, 'orient_y_plot.png'))
    # print('orientation y plot success!')
    
    # plt.plot(df_imu['Time'], df_imu['orientation.z'])
    # plt.title('Orientation Z-Value')
    # plt.xlabel('Time')
    # plt.ylabel('Quaternion (Z)')
    # plt.savefig(os.path.join(outdir, 'orient_z_plot.png'))
    # print('orientation z plot success!')

    # plt.plot(df_imu['Time'], df_imu['orientation.z'])
    # plt.title('Orientation W-Value')
    # plt.xlabel('Time')
    # plt.ylabel('Quaternion (W)')
    # plt.savefig(os.path.join(outdir, 'orient_w_plot.png'))
    # print('orientation w plot success!')
    
    # Yaw topic data plots
    # df_yaw = pd.read_csv(yaw_data)
    # df_yaw['Time'] - df_yaw['Time'].min()
    
    # plt.plot(df_yaw['Time'], df_yaw['data'])
    # plt.title('Yaw (Degrees)')
    # plt.xlabel('Time')
    # plt.ylabel('Degrees')
    # plt.savefig(os.path.join(outdir, 'yaw_plot.png'))
    # print('yaw plot success!')
    
    # df_odom = pd.read_csv(odom_data)
    # df_odom['secs'] = df_odom['Time'] - 1606874987
    # s = pd.Series(df_odom['pose.pose.position.x'])
    # df_odom['delta_x'] = (s.diff() * df_odom['secs'])
    # s = pd.Series(df_odom['pose.pose.position.y'])
    # df_odom['delta_y'] = (s.diff() * df_odom['secs'])
    # delta_x = [j-i for i, j in zip(df_odom['pose.pose.position.x'][:-1], df_odom['pose.pose.position.x'][1:])]
    # delta_y = [j-i for i, j in zip(df_odom['pose.pose.position.y'][:-1], df_odom['pose.pose.position.y'][1:])]
    # delta_x.insert(0,0)
    # delta_y.insert(0,0)

    # df_odom['delta_x'] = delta_x
    # df_odom['delta_y'] = delta_y
    # pos_x = []
    # pos_y = []
    # def convert(data):
    #     delta_x = ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])) - 
    #                ((data['delta_y'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
    #     delta_y = ((data['delta_x'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])) - 
    #            ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
    #     #print(delta_y)
    #     pos_x.append(delta_x)
    #     pos_y.append(delta_y)
    # df_odom.apply(convert,axis = 1)
    # #print(pos_x)
    # df_odom['pos_x'] = pos_x
    # df_odom['pos_y'] = pos_y
    # plt.plot(pos_x, pos_y,'b')
    # plt.xlabel('X in meters')
    # plt.ylabel('Y in meters')
    # plt.show()
    # plt.savefig(os.path.join(outdir, 'odom_plot.png'))
    # print('odom plot success!')
    # print("Successfully written all plots to destination")


if __name__ == '__main__':
    main()

