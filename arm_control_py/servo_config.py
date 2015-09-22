import math
 
servo_param = {
    # Upper Arm Servo
    1: { 
        'home_encoder': 0,
        'max_ang': math.radians( 120 ),
        'min_ang': math.radians( 0 )
#       'max_speed': math.radians(50)
#		'rad_per_enc': math.radians(300.0) / 1024.0,
#		'flipped': False,
       },

    # Grasper Servo
    2: {
        'home_encoder': 0,
        'max_ang': math.radians( 110 ),
        'min_ang': math.radians( -110 )
    }
}

# CW negative, CCW positive from face
