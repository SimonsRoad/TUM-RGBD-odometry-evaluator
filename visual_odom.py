import sys
import configparser
from gui.GUI import MainWindow
from gui.threadGUI import ThreadGUI
from MyAlgorithm import MyAlgorithm
from PyQt5.QtWidgets import QApplication
from read_rosbag import Read_Rosbag
from pose import Pose

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('visual_odometry.cfg')
    bag_file = config['FILE']['rosbag_file_dir']
    #bag_file = 
    pose_obj = Pose()
    bag = Read_Rosbag(pose_obj ,bag_file)
    
    algorithm = MyAlgorithm(bag , pose_obj)
    app = QApplication(sys.argv)
    myGUI = MainWindow()
    myGUI.set_bag(bag)
    myGUI.set_pose(pose_obj)
    myGUI.setAlgorithm(algorithm)
    myGUI.show()


    t2 = ThreadGUI(myGUI)
    t2.daemon=True
    t2.start()


    sys.exit(app.exec_())
