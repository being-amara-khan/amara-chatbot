# Amara's AI Assistant Chatbot 🤖

A modern, containerized chatbot application built with Streamlit and Docker, ready for deployment to AWS ECR and EC2.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

## 🌟 Features

- 💬 Clean, modern UI with message bubbles
- 🤖 Simple rule-based responses with emoji support
- 📝 Message history tracking
- 🐳 Docker containerization
- ☁️ AWS ECR deployment ready
- 🔄 Real-time chat interface
- 🎨 Custom styling and animations

## 📋 Prerequisites

- Python 3.10 or higher
- Docker installed on your system
- Git for version control
- AWS CLI configured with appropriate credentials
- An AWS ECR repository created

## 🚀 Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/amara-chatbot.git
cd amara-chatbot
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

5. Open your browser and navigate to:
```
http://localhost:8501
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t amara-chatbot .
```

2. Run the container:
```bash
docker run -p 8501:8501 amara-chatbot
```

## ☁️ AWS Deployment

### 1. Login to AWS ECR
```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
```

### 2. Tag the Docker image
```bash
docker tag amara-chatbot:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/amara-chatbot:latest
```

### 3. Push to ECR
```bash
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/amara-chatbot:latest
```

### Running on EC2

1. Launch an EC2 instance with Docker installed
2. Login to ECR on the EC2 instance:
```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
```

3. Pull and run the container:
```bash
docker pull <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/amara-chatbot:latest
docker run -d -p 8501:8501 <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/amara-chatbot:latest
```

4. Access the application at:
```
http://<ec2-instance-public-ip>:8501
```

## 📁 Project Structure

```
amara-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── .dockerignore      # Docker build context exclusions
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 🔧 Customization

### Adding New Responses

You can customize the chatbot's responses by modifying the `RESPONSES` dictionary in `app.py`:

```python
RESPONSES = {
    "hello": "Hi there! 👋 How can I help you today?",
    "how are you": "I'm doing great, thanks for asking! How about you? 😊",
    # Add your custom responses here
}
```

### Styling

The application uses custom CSS for styling. You can modify the styles in the `st.markdown()` section of `app.py`.

## 🔒 Security Notes

- Ensure your EC2 security group allows inbound traffic on port 8501
- Consider using AWS Secrets Manager for any sensitive configuration
- Use IAM roles for EC2 instances to access ECR
- Never commit sensitive information or API keys to the repository

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👩‍💻 Author

Amara Khan

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Docker for containerization
- AWS for cloud infrastructure 