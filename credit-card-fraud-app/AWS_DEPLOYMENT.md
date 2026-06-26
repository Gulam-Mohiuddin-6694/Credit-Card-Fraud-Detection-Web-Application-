# 🚀 AWS EC2 Deployment Guide

Complete step-by-step guide to deploy the Credit Card Fraud Detection application on AWS EC2.

## Prerequisites

- AWS Account
- Basic knowledge of AWS EC2
- SSH client (Terminal/PuTTY)
- Your dataset file (creditcard.csv)

## Step 1: Launch EC2 Instance

### 1.1 Login to AWS Console
- Go to AWS Console: https://console.aws.amazon.com
- Navigate to EC2 Dashboard

### 1.2 Launch Instance
1. Click **"Launch Instance"**
2. **Name**: fraud-detection-app
3. **AMI**: Ubuntu Server 20.04 LTS (Free tier eligible)
4. **Instance Type**: t2.medium (recommended) or t2.small (minimum)
5. **Key Pair**: Create new or use existing
   - Download and save the `.pem` file securely
6. **Network Settings**:
   - Create security group or use existing
   - Allow SSH (port 22) from your IP
   - Add rule: Custom TCP, Port 5000, Source: 0.0.0.0/0
7. **Storage**: 20 GB (minimum)
8. Click **"Launch Instance"**

### 1.3 Wait for Instance to Start
- Status should be "Running"
- Note the **Public IPv4 address**

## Step 2: Connect to EC2 Instance

### For Linux/Mac:
```bash
# Set permissions for key file
chmod 400 your-key.pem

# Connect via SSH
ssh -i your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
```

### For Windows:
Use PuTTY or Windows Terminal with the same SSH command.

## Step 3: Install System Dependencies

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip python3-venv -y

# Install Git
sudo apt install git -y

# Verify installations
python3 --version
pip3 --version
git --version
```

## Step 4: Setup Application

### 4.1 Clone Repository
```bash
# If using Git
git clone YOUR_REPOSITORY_URL
cd credit-card-fraud-app

# OR upload files manually using SCP
```

### 4.2 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

## Step 5: Upload Dataset

### Option 1: Using SCP (from your local machine)
```bash
# Open new terminal on your local machine
scp -i your-key.pem creditcard.csv ubuntu@YOUR_EC2_PUBLIC_IP:~/credit-card-fraud-app/dataset/
```

### Option 2: Using wget (if dataset is hosted)
```bash
cd dataset
wget YOUR_DATASET_URL
cd ..
```

### Option 3: Using FileZilla or WinSCP
- Connect to your EC2 instance
- Upload creditcard.csv to dataset/ folder

## Step 6: Train Models

```bash
cd model
python train_model.py
cd ..
```

**Note**: This will take 5-15 minutes. You'll see training progress in the terminal.

## Step 7: Run Application

### For Testing:
```bash
python app.py
```

### For Production (Background Process):
```bash
nohup python app.py > app.log 2>&1 &
```

To check if it's running:
```bash
ps aux | grep app.py
```

To view logs:
```bash
tail -f app.log
```

## Step 8: Access Application

Open your browser and navigate to:
```
http://YOUR_EC2_PUBLIC_IP:5000
```

## Step 9: Production Setup (Optional but Recommended)

### Install Gunicorn
```bash
pip install gunicorn
```

### Run with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Run in Background
```bash
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &
```

### Install and Configure Nginx (Optional)
```bash
# Install Nginx
sudo apt install nginx -y

# Create Nginx configuration
sudo nano /etc/nginx/sites-available/fraud-detection

# Add configuration:
server {
    listen 80;
    server_name YOUR_EC2_PUBLIC_IP;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# Enable site
sudo ln -s /etc/nginx/sites-available/fraud-detection /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Now access via: `http://YOUR_EC2_PUBLIC_IP` (port 80)

## Step 10: Setup Auto-Start (Optional)

### Create systemd service
```bash
sudo nano /etc/systemd/system/fraud-detection.service
```

Add:
```ini
[Unit]
Description=Credit Card Fraud Detection App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/credit-card-fraud-app
Environment="PATH=/home/ubuntu/credit-card-fraud-app/venv/bin"
ExecStart=/home/ubuntu/credit-card-fraud-app/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable fraud-detection
sudo systemctl start fraud-detection
sudo systemctl status fraud-detection
```

## Troubleshooting

### Application not accessible?
```bash
# Check if app is running
ps aux | grep app.py

# Check security group
# Ensure port 5000 is open in AWS Console

# Check firewall
sudo ufw status
sudo ufw allow 5000
```

### Models not loading?
```bash
# Verify models exist
ls -la model/*.pkl

# Retrain if needed
cd model
python train_model.py
cd ..
```

### Out of memory?
```bash
# Check memory usage
free -h

# Use t2.medium or larger instance
# Or add swap space:
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Port already in use?
```bash
# Find process using port 5000
sudo lsof -i :5000

# Kill process
sudo kill -9 PROCESS_ID
```

## Security Best Practices

1. **Restrict SSH Access**
   - Only allow your IP in security group
   - Use key-based authentication only

2. **Use HTTPS**
   - Get SSL certificate (Let's Encrypt)
   - Configure Nginx with SSL

3. **Regular Updates**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

4. **Firewall Configuration**
   ```bash
   sudo ufw enable
   sudo ufw allow 22
   sudo ufw allow 80
   sudo ufw allow 443
   sudo ufw allow 5000
   ```

5. **Backup Models**
   - Regularly backup trained models
   - Use S3 for storage

## Cost Optimization

- **Use t2.micro** for testing (free tier)
- **Use t2.medium** for production
- **Stop instance** when not in use
- **Use Reserved Instances** for long-term deployment
- **Monitor costs** in AWS Billing Dashboard

## Monitoring

### Check Application Status
```bash
curl http://localhost:5000
```

### View Logs
```bash
tail -f app.log
tail -f gunicorn.log
```

### Monitor Resources
```bash
htop
df -h
free -h
```

## Stopping the Application

```bash
# Find process
ps aux | grep app.py

# Kill process
kill PROCESS_ID

# Or if using systemd
sudo systemctl stop fraud-detection
```

## Updating the Application

```bash
# Pull latest changes
git pull origin main

# Restart application
sudo systemctl restart fraud-detection
```

## Cleanup

To remove everything:
```bash
# Stop application
sudo systemctl stop fraud-detection

# Remove files
cd ~
rm -rf credit-card-fraud-app

# Terminate EC2 instance from AWS Console
```

## Support

For issues:
- Check logs: `tail -f app.log`
- Verify security groups in AWS Console
- Ensure all dependencies are installed
- Check EC2 instance status

---

**🎉 Congratulations! Your application is now deployed on AWS EC2!**

Access it at: `http://YOUR_EC2_PUBLIC_IP:5000`
