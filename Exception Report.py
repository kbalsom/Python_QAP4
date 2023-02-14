def vision_recognize_people(msg)
    global person found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    person_found = True

def scan_for_person_and_play_sound():
    global person found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    person_found == False:
    While person_found == False:
        gimbal_ctrl.rotate_with_degree(rm_define.clockwise, -250)
        gimbal_ctrl.rotate_with_degree(rm_define.clockwise, 250)

def start():
    room_one_type = 1 # Fire
    room_two_type = 2 # Skip
    room_three_type = 1 # Fire
    room_four_type = 3 # Person

    # Robot Settings
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.5)
    chassis_ctrl.set_rotate_speed(30)
    gimbal_ctrl.set_rotate_speed(30)
    # Move from starting point to Room #1 (718 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,2.18)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    gimbal_ctrl.recenter()
    # Move to door, Scan Room #1,
    if(room_one_type == 1):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_fire()
    elif(room_one_type == 2):
        # Turn to face the hallway to prepare to move towards the door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    elif (room_one_type == 3):
        # Drive through the door
        chassis_ctrl.move_with_distance(0, 1)
        scan_for_person_and_play_sound()
        # Rotate towards door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        # Exit through the door
        chassis_ctrl.move_with_distance(0, 1)
        return_to_start_of_course(1)
        move_to_room_from_start(1)
    # Return to Hallway
    # Move to Turning Point (760 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,2.60)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90) # This might not be 90 degrees, have to angle to Reset Point
    gimbal_ctrl.recenter()
    # Move to Reset Point (274 cm)
    chassis_ctrl.move_with_distance(0,2.74)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90) # This might not be 90 degrees, have to angle down hallway
    # Reset point
    # Move to Room #2 (502 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,0.02)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90) # This might not be 90 degrees, have to angle to Reset Point
    gimbal_ctrl.recenter()
    # Move to door, Scan Room # 2
     if(room_two_type == 1):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_fire()
    elif(room_two_type == 2):
        # Turn to face the hallway to prepare to move towards the door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    elif (room_two_type == 3):
        # Drive through the door
        chassis_ctrl.move_with_distance(0, 1)
        scan_for_person_and_play_sound()
        # Rotate towards door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        # Exit through the door
        chassis_ctrl.move_with_distance(0, 1)
        return_to_start_of_course(1)
        move_to_room_from_start(1)
    # Return to Hallway
    # Move to Room # 3 (890 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,3.90)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90) # This might not be 90 degrees, have to angle to Reset Point
    gimbal_ctrl.recenter()
    # Move to door, Scan Room # 3
     if(room_three_type == 1):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_fire()
    elif(room_three_type == 2):
        # Turn to face the hallway to prepare to move towards the door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    elif (room_three_type == 3):
        # Drive through the door
        chassis_ctrl.move_with_distance(0, 1)
        scan_for_person_and_play_sound()
        # Rotate towards door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        # Exit through the door
        chassis_ctrl.move_with_distance(0, 1)
        return_to_start_of_course(1)
        move_to_room_from_start(1)
    # Return to hallway
    # Move to Room # 4 (1052 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,0.52)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    gimbal_ctrl.recenter()
    # Move to door, Scan Room #4
     if(room_four_type == 1):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_fire()
    elif(room_four_type == 2):
        # Turn to face the hallway to prepare to move towards the door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    elif (room_four_type == 3):
        # Drive through the door
        chassis_ctrl.move_with_distance(0, 1)
        scan_for_person_and_play_sound()
        # Rotate towards door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        # Exit through the door
        chassis_ctrl.move_with_distance(0, 1)
        return_to_start_of_course(1)
        move_to_room_from_start(1)
    # Return to hallway
    # Return to Reset Point (2417 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,4.17)
    # Move from Reset Point to Turning Point (274 cm)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90) # This might not be 90 degrees.
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0,2.74)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90) # This might not be 90 degrees.
    gimbal_ctrl.recenter()
    # Move from Turning Point to Starting Point (1478 cm)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,5.0)
    chassis_ctrl.move_with_distance(0,4.78)
    # Arrived at Starting Point, End of Program
