from datetime import datetime
import boto3

client = boto3.client('iam')
sns = boto3.client('sns')

response = client.list_users(PathPrefix='/', #specify the users list path so that it iwll display all the users in that path
                            #Marker='100',
                            MaxItems=500 #default 100 users list will provide
                             )


for userslist in response["Users"]:
    out_user_list = userslist

    get_create_date = datetime.date(userslist['CreateDate'])
    current_day = datetime.today()
    expire_days = current_day.date()- get_create_date
    out_user_list+=1
    if expire_days.days==1:
    send_msg = sns.publish(
            TopicArn='arn:aws:sns:ap-south-1:988892460704:getting_password_age_user',
            Subject='IAM users creation date details',
            Message= str(userslist)
            )





#print("userlist['UserName', 'UserId', 'CreateDate'] --> : ", userslist['UserName'], ',', userslist['UserId'],
           #   ',', userslist['CreateDate'])
