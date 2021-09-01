//d 1step: 0.24mm
//r&l 1step: 0.32mm

#include<ctype.h>
#include<stdlib.h>
#define SOLENOID_PIN 8
#define X_DIR_PIN 7
#define X_STEP_PIN 6
#define Y_DIR_PIN1 5
#define Y_STEP_PIN1 4
#define Y_DIR_PIN2 3
#define Y_STEP_PIN2 2

#define MAX_REPOS 7

char num_repos[MAX_REPOS];
int num_repos_iter = 0;
char dir_flag = '\0';

const int MOTOR_DELAY = 500;

String ser_data = "";

void setup()
{
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    while(Serial.available() > 0)
    {
        char rec = Serial.read();
        ser_data += rec;
        
        //실행 영역

        if (rec == 'p')
        {
            Serial.println(ser_data);
            digitalWrite(SOLENOID_PIN, HIGH);
            delay(70);
        }
        else if (rec == 'P')
        {
            Serial.println(ser_data);
            digitalWrite(SOLENOID_PIN, LOW);
            delay(70);
        }
        else if (rec == 'd')
        {
            Serial.println(ser_data);
            dir_flag = 'd';
        }
        else if (rec == 'r')
        {
            Serial.println(ser_data);
            dir_flag = 'r';
        }
        else if (rec == 'l')
        {
            Serial.println(ser_data);
            dir_flag = 'l';
        }
        else if (isdigit(rec) != 0)
        {
            Serial.println(ser_data);
            num_repos[num_repos_iter] = rec;
            num_repos_iter += 1;
        }
        else if (rec == '`')
        {
            int tmp = atoi(num_repos);
            
            if (dir_flag == 'd')
            {
                ctrl_Y_motor(Y_DIR_PIN1, Y_DIR_PIN2, Y_STEP_PIN1, Y_STEP_PIN2, tmp);
            }
            else if (dir_flag == 'r')
            {
                ctrl_motor(X_DIR_PIN, X_STEP_PIN, HIGH, tmp);
            }
            else if (dir_flag == 'l')
            {
                ctrl_motor(X_DIR_PIN, X_STEP_PIN, LOW, tmp);
            }

            Serial.println(tmp);
            
            for(int i = 0; i < MAX_REPOS; ++i)
            {
                num_repos[i] = '\0';
            }
            dir_flag = '\0';
            num_repos_iter = 0;
        }
        else
        {
            Serial.println("U");
        }
        ser_data = "";
        delay(1);
    }
}


void ctrl_motor(int motor_dir_pin, int motor_step_pin, int motor_dir, int motor_step)
{
    if(motor_dir == HIGH)
    {
        digitalWrite(motor_dir_pin, HIGH);
    }
    else
    {
        digitalWrite(motor_dir_pin, LOW);
    }
    for(int i = 0; i < motor_step * 2; ++i)
    {
        digitalWrite(motor_step_pin, HIGH);
        delayMicroseconds(MOTOR_DELAY);
        digitalWrite(motor_step_pin, LOW);
        delayMicroseconds(MOTOR_DELAY);
    }
}

void ctrl_Y_motor(int motor_dir_pin1, int motor_dir_pin2, int motor_step_pin1, int motor_step_pin2, int motor_step)
{
    digitalWrite(motor_dir_pin1, HIGH);
    digitalWrite(motor_dir_pin2, LOW);
    for(int i = 0; i < motor_step; ++i)
    {
        digitalWrite(motor_step_pin1, HIGH);
        digitalWrite(motor_step_pin2, HIGH);
        delayMicroseconds(MOTOR_DELAY * 2);
        digitalWrite(motor_step_pin1, LOW);
        digitalWrite(motor_step_pin2, LOW);
        delayMicroseconds(MOTOR_DELAY * 2);
    }
}