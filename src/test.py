import os
import shutil
import bagpy
import rosbag
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import math

def tester(indir, outdir):
    dir = "test"
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

    bag_path = os.path.join(indir, '2021-01-25-00-01-16.bag')
    b = bagreader(bag_path)

    imu_data = b.message_by_topic('/imu')
    df_imu = pd.read_csv(imu_data)
    df_imu.to_csv(os.path.join(outdir,'imu_data_test.csv'))


    yaw_data = b.message_by_topic('/yaw')
    df_yaw = pd.read_csv(yaw_data)
    df_yaw.to_csv(os.path.join(outdir,'yaw_data_test.csv'))
    
    odometry_path = os.path.join(indir, '2021-01-25-18-09-47.bag')
    bag = bagreader(odometry_path)
    odom_data = bag.message_by_topic('/vesc/odom')
    df_odom = pd.read_csv(odom_data)
    df_odom.to_csv(os.path.join(outdir,'odom_data_test.csv'))

    print('Extracted .bag data and written to destination successfully')
    
    return

def plotter(odom_data,imu_data, yaw_data, outdir):

    os.mkdir(outdir)
    
    # IMU topic data plots first
    df_imu = pd.read_csv(imu_data)
    df_imu['Time'] - df_imu['Time'].min()
    
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.x'])
    plt.title('IMU X-Acceleration')
    plt.xlabel('Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.savefig(os.path.join(outdir, 'accel_x_plt.png'))
    print('x-acceleration plot success!')
    
    plt.plot(df_imu['Time'], df_imu['linear_acceleration.y'])
    plt.title('IMU Y-Acceleration')
    plt.xlabel('Time')
    plt.ylabel('Acceleration (m/s^2)')
    plt.savefig(os.path.join(outdir, 'accel_y_plot.png'))
    print('y-acceleration plot success!')
    
    plt.scatter(df_imu['linear_acceleration.x'], df_imu['linear_acceleration.y'], alpha=0.5)
    plt.title('IMU Scatterplot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(os.path.join(outdir, 'accel_scatter_plot.png'))
    print('scatter-acceleration plot success!')
    
    plt.hist(df_imu['linear_acceleration.x'], bins=None)
    plt.title('IMU X-Acceleration Distribution')
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(outdir, 'accel_x_hist.png'))
    print('x-acceleration hist plot written successfully!')
    
    plt.hist(df_imu['linear_acceleration.y'], bins=None)
    plt.title('IMU X-Acceleration Distribution')
    plt.xlabel('y')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(outdir, 'accel_y_hist.png'))
    print('y-acceleration hist plot success!')
    
    plt.plot(df_imu['Time'], df_imu['orientation.x'])
    plt.title('Orientation X-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (X)')
    plt.savefig(os.path.join(outdir, 'orient_x_plot.png'))
    print('orientation x plot success!')
    
    plt.plot(df_imu['Time'], df_imu['orientation.y'])
    plt.title('Orientation Y-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (X)')
    plt.savefig(os.path.join(outdir, 'orient_y_plot.png'))
    print('orientation y plot success!')
    
    plt.plot(df_imu['Time'], df_imu['orientation.z'])
    plt.title('Orientation Z-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (Z)')
    plt.savefig(os.path.join(outdir, 'orient_z_plot.png'))
    print('orientation z plot success!')

    plt.plot(df_imu['Time'], df_imu['orientation.z'])
    plt.title('Orientation W-Value')
    plt.xlabel('Time')
    plt.ylabel('Quaternion (W)')
    plt.savefig(os.path.join(outdir, 'orient_w_plot.png'))
    print('orientation w plot success!')
    
    # Yaw topic data plots
    df_yaw = pd.read_csv(yaw_data)
    df_yaw['Time'] - df_yaw['Time'].min()
    
    plt.plot(df_yaw['Time'], df_yaw['data'])
    plt.title('Yaw (Degrees)')
    plt.xlabel('Time')
    plt.ylabel('Degrees')
    plt.savefig(os.path.join(outdir, 'yaw_plot.png'))
    print('yaw plot success!')
    
    df_odom = pd.read_csv(odom_data)
    df_odom['secs'] = df_odom['Time'] - 1606874987
    s = pd.Series(df_odom['pose.pose.position.x'])
    df_odom['delta_x'] = (s.diff() * df_odom['secs'])
    s = pd.Series(df_odom['pose.pose.position.y'])
    df_odom['delta_y'] = (s.diff() * df_odom['secs'])
    delta_x = [j-i for i, j in zip(df_odom['pose.pose.position.x'][:-1], df_odom['pose.pose.position.x'][1:])]
    delta_y = [j-i for i, j in zip(df_odom['pose.pose.position.y'][:-1], df_odom['pose.pose.position.y'][1:])]
    delta_x.insert(0,0)
    delta_y.insert(0,0)

    df_odom['delta_x'] = delta_x
    df_odom['delta_y'] = delta_y
    pos_x = []
    pos_y = []
    def convert(data):
        delta_x = ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])) - 
                   ((data['delta_y'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
        delta_y = ((data['delta_x'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])) - 
               ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
        #print(delta_y)
        pos_x.append(delta_x)
        pos_y.append(delta_y)
    df_odom.apply(convert,axis = 1)
    #print(pos_x)
    df_odom['pos_x'] = pos_x
    df_odom['pos_y'] = pos_y
    plt.plot(pos_x, pos_y,'b')
    plt.xlabel('X in meters')
    plt.ylabel('Y in meters')
    plt.savefig(os.path.join(outdir, 'odom_plot.png'))
    print('odom plot success!')
    print("Successfully written all plots to destination")
    
    erpm = [2.418573, 2.72192, 3.0153, 2.1984, 2.0407]
    tuning = pd.DataFrame(data = erpm, index = ['4412','4912','5412','3912','3412'], columns =  ['distance'])
    tuning['off_by'] = tuning['distance'] - 2.0
    tuning.to_csv(os.path.join(outdir, 'tuning.csv'),index = False)
    
if __name__ == '__main__':
    main()
