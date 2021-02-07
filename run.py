#!/usr/bin/env python
import sys
import json
sys.path.insert(0, 'src')
from test import tester, plotter
from conversion import convert
from eda import plots

def main(targets):
    data_cfg = json.load(open('config/conversion.json'))
    eda_cfg = json.load(open('config/eda-params.json'))
    test_cfg = json.load(open('config/test-params.json'))
    test_vis_cfg = json.load(open('config/test-vis-params.json'))
    
    if 'test' in targets:
        imu_data = tester(**test_cfg)
        vis = plotter(**test_vis_cfg)
        print('Completed. Plots are saved.')
    if 'conversion' in targets:
        data = tester(**data_cfg)
        print('Data converted to csv')
    if 'eda' in targets:
        data = plots(**eda_cfg)
        print('Data plotted')
    return





if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)


