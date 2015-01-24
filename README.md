# minibox
3D mini-itx box Python modelization

## Installing OCE, PythonOCC and CCAD on Ubuntu 14.10

### Required packages
```
$ sudo apt-get install cmake build-essential python3-dev libxmu-dev libxi-dev tcl-dev tk tk-dev swig git ftgl-dev libtbb2 libtbb2-dev python3-pyqt4.qtopengl ipython3
```
The libtbb2 and libtbb-dev packages are required for multithreading in OCE.

### Source code
Opencascade Community Edition (OCE) 0.16.1 et PythonOCC 0.16.0
```
$ cd ~
$ mkdir gitroot && cd gitroot
$ git clone git://github.com/tpaviot/oce.git
$ git clone git://github.com/tpaviot/pythonocc-core.git
$ git clone git://github.com/charles-sharman/ccad.git
$ cd ~/gitroot/oce
$ git checkout OCE-0.16.1
$ cd ~/gitroot/pythonocc-core
$ git checkout 0.16.0
$ cd ~/gitroot/ccad
$ git checkout tp/py3-port
$ git branch
```
OCE and PythonOCC need to be of together compatible versions.

### OCE build
```
$ cd ~/gitroot
$ mkdir oceBuild && cd oceBuild
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr/local/ -DOCE_INSTALL_PREFIX:PATH=/usr/local/ -DOCE_WITH_FREEIMAGE=OFF -DOCE_WITH_GL2PS=OFF -DOCE_VISUALISATION=ON -DOCE_DATAEXCHANGE=ON -DOCE_MULTITHREAD_LIBRARY=TBB -DCMAKE_BUILD_TYPE=Release -DOCE_TESTING:BOOL=ON ../oce
$ nproc
$ make -j<result of nproc command on your machine>
$ sudo make install
$ make test
```
### PythonOCC-core build
```
$ cd ~/gitroot
$ mkdir pythonocc-coreBuild && cd pythonocc-coreBuild
$ cmake -DOCE_INCLUDE_PATH=/usr/local/include/oce -DOCE_LIB_PATH=/usr/local/include/lib -DPYTHONOCC_INSTALL_DIRECTORY=/usr/local/lib/python3.4/dist-packages/OCC -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 ../pythonocc-core
$ make -j<result of nproc command on your machine>
$ sudo make install
```
Library cache reload:
```
$ sudo ldconfig
$ ldd /usr/local/lib/python3.4/dist-packages/OCC/_Standard.so
```
Testing:
```
$ cd ../pythonocc-core/test
$ python3 run_tests.py
$ cd ../examples
$ python3 core_helloworld.py
$ python3 core_animation.py
$ python3 core_dimensions.py
```
### CCAD installation
```
$ sudo python3 setup.py install --prefix=/usr/local
```
Only the ccad.model module is running well with the PythonOCC version used here.

Testing:
```
$ ipython3
: import ccad.model as cm
: import OCC.Display.SimpleGui as SimpleGui
: s1 = cm.sphere(1.0)
: display, start_display, add_menu, add_function_to_menu = SimpleGui.init_display()
: display.DisplayShape(s1.shape, update = True)
: start_display()
```
