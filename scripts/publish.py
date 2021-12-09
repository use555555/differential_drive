#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import speech_recognition as sr
import rospkg
import sys, os


# ROS Image message
from sensor_msgs.msg import Image
from std_msgs.msg import Float64
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

def movebase_client(px,py,oz,w):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = px
    goal.target_pose.pose.position.y = py
    goal.target_pose.pose.orientation.z = oz
    goal.target_pose.pose.orientation.w = w

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def image_callback(msg):
    # Convert your ROS Image message to OpenCV2
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    # Save your OpenCV2 image as a jpeg 
    cv2.imwrite(path+f'/Picture/{command}_{pic}.jpg', cv2_img)

if __name__ == '__main__':
    rospack = rospkg.RosPack()
    path = rospack.get_path('differential_drive')
    r = sr.Recognizer()
    bridge = CvBridge()
    rospy.init_node('movebase_client_py')
    head_topic = "/head_position_controller/command"
    cam_topic = "/camera_position_controller/command"
    head = rospy.Publisher(head_topic, Float64, queue_size=1)
    cam = rospy.Publisher(cam_topic, Float64, queue_size=1)
    head.publish(0)
    rospy.sleep(0.5)
    cam.publish(0)
    rospy.sleep(0.5)


# Reading Microphone as source
# listening the speech and store in audio_text variable
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        with sr.Microphone() as source:
            print("Reducing the noise")
            r.adjust_for_ambient_noise(source, duration=5)
            print("Command please")
            audio_text = r.listen(source, phrase_time_limit=2)
            print("Command received")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            
            try:
                # using google speech recognition
                command = ''
                command = r.recognize_google(audio_text)
                if command == 'exit':
                    break
                if command == 'kitchen':
                    print(f'The command is: {command}')
                    result = movebase_client(4.3,0.3,-0.69,0.725)
                    if result:
                        print("Goal reached!!!")
                        head.publish(0)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 1
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0.785)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 2
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.785)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 3
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.047)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 4
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                    result = movebase_client(4.3,0.3,0.69,0.725)


                elif command == 'bathroom':
                    print(f'The command is: {command}')
                    result = movebase_client(6,0.6,0,1)
                    if result:
                        print("Goal reached!!!")
                        head.publish(0.5)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 1
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.6)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 2
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.6)
                        rospy.sleep(0.5)
                        cam.publish(0.25)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 3
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-2)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 4
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)
                    
                    result = movebase_client(6,0.6,-1,0)


                elif command == 'living room':
                    print(f'The command is: {command}')
                    result = movebase_client(5.3,4.5,0,1)
                    if result:
                        print("Goal reached!!!")
                        head.publish(0)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 1
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.25)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 2
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(1.45)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 3
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(2.5)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 4
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                    result = movebase_client(5.3,4.5,-1,0)


                elif command == 'bedroom':
                    print(f'The command is: {command}')
                    result = movebase_client(1.7,3.6,-1,0)
                    if result:
                        print("Goal reached!!!")
                        head.publish(1.047)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 1
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(1.65)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 2
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.35)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 3
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-2)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 4
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)
                    
                    result = movebase_client(1.7,3.6,0,1)

                elif command == 'all':
                    print(f'The command is: {command}')
                    result = movebase_client(4.3,0.3,-0.69,0.725)
                    if result:
                        print("Goal 1 reached!!!")
                        head.publish(0)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 1
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0.785)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 2
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.785)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 3
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.047)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 4
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                        result = movebase_client(4.3,0.3,0.69,0.725)


                    result = movebase_client(6,0.6,0,1)
                    if result:
                        print("Goal 2 reached!!!")
                        head.publish(0.5)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 5
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.6)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 6
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-0.6)
                        rospy.sleep(0.5)
                        cam.publish(0.25)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 7
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-2)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 8
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                        result = movebase_client(6,0.6,-1,0)


                    result = movebase_client(5.3,4.5,0,1)
                    if result:
                        print("Goal 3 reached!!!")
                        head.publish(0)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 9
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.25)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 10
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(1.45)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 11
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(2.5)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 12
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                    result = movebase_client(5.3,4.5,-1,0)


                    result = movebase_client(1.7,3.6,-1,0)
                    if result:
                        print("Goal 4 reached!!!")
                        head.publish(1.047)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 13
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(1.65)
                        rospy.sleep(0.5)
                        cam.publish(0)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 14
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-1.35)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 15
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(-2)
                        rospy.sleep(0.5)
                        cam.publish(-0.224)
                        rospy.sleep(0.5)
                        image_topic = "/robot/camera1/image_raw"
                        pic = 16
                        sub = rospy.Subscriber(image_topic, Image, image_callback)
                        rospy.sleep(0.5)
                        sub.unregister()

                        head.publish(0)
                        rospy.sleep(2)
                        cam.publish(0)
                        rospy.sleep(2)

                        result = movebase_client(1.7,3.6,0,1)

                result = movebase_client(0.5,0,0,1)
                if result:
                    print("Execution done!")
                    rospy.sleep(5)
            except:
                print("Sorry, Please say the command again")
                rospy.sleep(3)