   #importing Python module to control GPIO pins and sleep module to allow for delays
    import RPi.GPIO as GPIO

    #Assigning each input from the L298N motor-board to RPi GPIO pins
    in1 = 7
    in2 = 8
    enA = 20
    in3 = 9
    in4 = 10
    enB = 21
    temp1 = 1

    #For GPIO numbering
    GPIO.setmode(GPIO.BCM)


    #setting GPIO pins as outputs
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    #setting enabler pins as output
    GPIO.setup(enA,GPIO.OUT)
    GPIO.setup(enB,GPIO.OUT)

    #setting default output to low
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    #Assigning PWM frequency [p = GPIO.PWM(channel, frequency)]
    pA = GPIO.PWM(enA,100)
    pB = GPIO.PWM(enB,100)

    #p.start(DutyCycle)
    pA.start(25)
    pB.start(25)
    print('\n')
    print('Default speed and direction is LOW and FORWARD')
    print('r-run, s-stop, f-forward, b-backward, l-low, m-medium, h-high, e-exit, right- Turn right, left- Turn left')
    print('\n')

    while(1):
    
    x = input()
    
    if x=='r':
        print('Run')
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print('Forward')
            x='z'
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print('Backward')
            x='z'
            
    elif x=='right':
        print('Turn right')
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        x='z'
    
    elif x=='left':
        print('Turn left')
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        x='z'
        
    elif x=='s':
        print('Stop')
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'
            
    elif x=='f':
        print('Forward')
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'
            
    elif x=='b':
        print('Backward')
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=1
        x='z'
            
    elif x=='l':
        print('Low')
        pA.ChangeDutyCycle(45)
        pB.ChangeDutyCycle(45)
        x='z'
            
    elif x=='m':
        print('Medium')
        pA.ChangeDutyCycle(75)
        pB.ChangeDutyCycle(75)
        x='z'
            
    elif x=='h':
        print('High')
        pA.ChangeDutyCycle(100)
        pB.ChangeDutyCycle(100)
        x='z'  
        
    elif x=='e':
        print('Exit')
        GPIO.cleanup()
        print('GPIO cleanup')
        break
        
    else:
        print('--- Wrong data ---')
        print('--- Please enter defined data to continue ---')