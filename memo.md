# memo

- public IP
    - 52.193.209.186
- user name
    - ec2-user

scp -i "techacademy-mentor.pem" requirements.txt ec2-user@52.193.209.186:/home/ec2-user/
scp -i "techacademy-mentor.pem" todo_app_front/index.html ec2-user@52.193.209.186:/home/ec2-user/todo_app_front/
scp -i "techacademy-mentor.pem" todo_app_front/style.css ec2-user@52.193.209.186:/home/ec2-user/todo_app_front/
scp -i "techacademy-mentor.pem" todo_app_front/main.js ec2-user@52.193.209.186:/home/ec2-user/todo_app_front/
scp -i "techacademy-mentor.pem" todo_app_back/app.py ec2-user@52.193.209.186:/home/ec2-user/todo_app_back/