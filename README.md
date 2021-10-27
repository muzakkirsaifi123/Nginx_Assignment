# Ngnix Assignment

Implementing load balancer and reverse proxy using nginx

### Steps

#### Step-1. Install `Nginx` in your system using this command.

```bash

sudo apt-get update

sudo apt-get install nginx
```

#### Step-2.  We have two options like Delete or move `defualt` file in `/etc/nginx/sites_enabled`

```bash
cd /etc/nginx/sites_enabled
ls
sudo rm default
```


#### Step-3. Create a `.conf` file in `/etc/nginx/conf.d/`
   
   > lb.conf
```text
  upstream python {
        server localhost:5001;
        server localhost:5002;
        server localhost:5003;
    }
    # This server accepts all traffic to port 80 and passes it to the upstream. 
    # Notice that the upstream name and the proxy_pass need to match.


    server {
        listen 80;
        server_name localhost;
        location / {
            proxy_pass http://python;
        }
        location /server1 {
            proxy_pass http://127.0.0.1:5001;
        }
        location /server2 {
            proxy_pass http://127.0.0.1:5002;
        }
        location /server3 {
            proxy_pass http://127.0.0.1:5003;
        }
    }

```

#### Step-4. Restart nginx server using this command.


> Restart and status check respectively 

```bash
systemctl restart nginx.service

systemctl status nginx.service   

```
#### Step-5. Create python apps  and run using these commands.

```bash
python3 server1.py
python3 server2.py
python3 server3.py
```
