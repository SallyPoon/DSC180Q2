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

#     bag_path = os.path.join(indir, '2021-01-25-00-01-16.bag')
#     b = bagreader(bag_path)

#     imu_data = b.message_by_topic('/imu')
#     df_imu = pd.read_csv(imu_data)
#     df_imu.to_csv(os.path.join(outdir,'imu_data_test.csv'))


#     yaw_data = b.message_by_topic('/yaw')
#     df_yaw = pd.read_csv(yaw_data)
#     df_yaw.to_csv(os.path.join(outdir,'yaw_data_test.csv'))
    
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


    print('Extracted .bag data and written to destination successfully')
    
    return

def plotter(odom_data,imu_data, yaw_data, outdir):

    os.mkdir(outdir)
    
    # IMU topic data plots first
    plt.plot(df_odom_3412['pose.pose.position.x'], [0] * len(df_odom_3412))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 3412")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_3412.png'))
    print('ERPM_Gain 3412 success!')
               
    plt.plot(df_odom_3912['pose.pose.position.x'], [0] * len(df_odom_3912))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 3912")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_3912.png'))
    print('ERPM_Gain 3912 success!')

    plt.plot(df_odom_4112['pose.pose.position.x'], [0] * len(df_odom_4112))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 4112")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_4112.png'))
    print('ERPM_Gain 4112 success!')
               
    plt.plot(df_odom_4612['pose.pose.position.x'], [0] * len(df_odom_4612))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 4612")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_4612.png'))
    print('ERPM_Gain 4612 success!')
               
    plt.plot(df_odom_5112['pose.pose.position.x'], [0] * len(df_odom_5112))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 5112")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_5112.png'))
    print('ERPM_Gain 5112 success!')
               
    plt.plot(df_odom_5612['pose.pose.position.x'], [0] * len(df_odom_5612))
    plt.xlabel('Distance in meters')
    plt.title("ERPM_Gain 5612")
    plt.xticks(np.arange(0, 2.5 ,0.2))
    plt.savefig(os.path.join(outdir, 'ERPM_Gain_5612.png'))
    print('ERPM_Gain 5612 success!')
               
    
#     # Yaw topic data plots
#     df_yaw = pd.read_csv(yaw_data)
#     df_yaw['Time'] - df_yaw['Time'].min()
    
#     plt.plot(df_yaw['Time'], df_yaw['data'])
#     plt.title('Yaw (Degrees)')
#     plt.xlabel('Time')
#     plt.ylabel('Degrees')
#     plt.savefig(os.path.join(outdir, 'yaw_plot.png'))
#     print('yaw plot success!')
    
#     df_odom = pd.read_csv(odom_data)
#     df_odom['secs'] = df_odom['Time'] - 1606874987
#     s = pd.Series(df_odom['pose.pose.position.x'])
#     df_odom['delta_x'] = (s.diff() * df_odom['secs'])
#     s = pd.Series(df_odom['pose.pose.position.y'])
#     df_odom['delta_y'] = (s.diff() * df_odom['secs'])
#     delta_x = [j-i for i, j in zip(df_odom['pose.pose.position.x'][:-1], df_odom['pose.pose.position.x'][1:])]
#     delta_y = [j-i for i, j in zip(df_odom['pose.pose.position.y'][:-1], df_odom['pose.pose.position.y'][1:])]
#     delta_x.insert(0,0)
#     delta_y.insert(0,0)

#     df_odom['delta_x'] = delta_x
#     df_odom['delta_y'] = delta_y
#     pos_x = []
#     pos_y = []
#     def convert(data):
#         delta_x = ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])) - 
#                    ((data['delta_y'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
#         delta_y = ((data['delta_x'] * math.sin(data['pose.pose.orientation.w'] * data['secs'])) - 
#                ((data['delta_x'] * math.cos(data['pose.pose.orientation.w'] * data['secs'])))) * data['secs']
#         #print(delta_y)
#         pos_x.append(delta_x)
#         pos_y.append(delta_y)
#     df_odom.apply(convert,axis = 1)
#     #print(pos_x)
#     df_odom['pos_x'] = pos_x
#     df_odom['pos_y'] = pos_y
#     plt.plot(pos_x, pos_y,'b')
#     plt.xlabel('X in meters')
#     plt.ylabel('Y in meters')
#     plt.savefig(os.path.join(outdir, 'odom_plot.png'))
#     print('odom plot success!')
#     print("Successfully written all plots to destination")
    
#     erpm = [2.418573, 2.72192, 3.0153, 2.1984, 2.0407]
#     tuning = pd.DataFrame(data = erpm, index = ['4412','4912','5412','3912','3412'], columns =  ['distance'])
#     tuning['off_by'] = tuning['distance'] - 2.0
#     tuning.to_csv(os.path.join(outdir, 'tuning.csv'),index = False)
    
if __name__ == '__main__':
    main()
