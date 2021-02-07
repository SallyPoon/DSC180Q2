# Inside explore.ipynb / script.py
...
import code
params = json.load(open('config.txt'))

code.run_process(**params)

