#!/usr/bin/env python
import sys
import json
#sys.path.insert(0, 'src')
from src.test import tester, plotter
from src.conversion import convert
from src.eda import plots
from src.viz_analysis import plot_all

def main(targets):
    data_cfg = json.load(open('config/conversion.json'))
    eda_cfg = json.load(open('config/eda-params.json'))
    viz_cfg = json.load(open('config/viz-params.json'))
    test_cfg = json.load(open('config/test-params.json'))
    test_vis_cfg = json.load(open('config/test-vis-params.json'))
    
    if 'test' in targets:
        imu_data = tester(**test_cfg)
        vis = plotter(**test_vis_cfg)
        print('Completed. Plots are saved.')
    if 'conversion' in targets:
        convert(**data_cfg)
        print('Raw Data Bags converted to csv')
    if 'eda' in targets:
        data = plots(**eda_cfg)
        print('Data plotted')
    if 'viz_analysis' in targets:
        plot_all(**viz_cfg)
        print('Data plotted')
    return





if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


