# Fake Data Generator - GitHub Copilot Tutorial

This project demonstrates how to use GitHub Copilot for Python development, including project setup, code scaffolding, and external API integration.

## Project Overview

This application showcases:
- **Project Scaffolding**: Using GitHub Copilot to set up a Python project structure
- **Code Organization**: Following Python best practices with modular design
- **External API Integration**: Connecting to Ollama (local LLM) for AI-generated data
- **Development Workflow**: Virtual environments, dependencies, and Git setup

## Files Structure

- `main.py` - Entry point that demonstrates the FakeDataGenerator class
- `fake_data_generator.py` - Core class for generating structured fake data
- `create_fake_data.py` - Script that uses Ollama AI to generate CSV data
- `requirements.txt` - Python dependencies
- `.copilot-instructions.md` - GitHub Copilot configuration for this project

## Setup Instructions

### 1. Clone and Setup Virtual Environment

```bash
# Clone the repository
git clone <repository-url>
cd copilot-experimenation

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Basic Application

```bash
python main.py
```

This will demonstrate the basic fake data generator functionality.

### 3. AI-Generated Data (Optional)

To use the AI-powered data generation with Ollama:

1. **Install Ollama** (if not already installed):
   - Visit [ollama.ai](https://ollama.ai) for installation instructions

2. **Start Ollama server**:
   ```bash
   ollama serve
   ```

3. **Pull the required model**:
   ```bash
   ollama pull phi3.5:latest
   ```

4. **Run the AI data generator**:
   ```bash
   python create_fake_data.py
   ```

This will generate a `fake_data.csv` file with AI-generated sample data.

## Features Demonstrated

### GitHub Copilot Capabilities
- **Project Setup**: Scaffolding Python applications
- **Code Organization**: Extracting classes into separate files
- **API Integration**: Connecting to external services (Ollama)
- **Best Practices**: Python coding standards and project structure
- **Documentation**: Generating docstrings and comments

### Python Development
- Virtual environment management
- Module imports and organization
- Error handling for external APIs
- CSV file generation and handling
- Requirements management with pip

## Tutorial Reference

This project is based on a GitHub Copilot tutorial that shows how AI can assist with:
- Setting up Python projects from scratch
- Scaffolding code structure
- Integrating with external APIs
- Following development best practices
- Managing dependencies and environments

The tutorial demonstrates that GitHub Copilot can help not just with writing code, but with entire project setup and development workflows.

## Extending the Project

You can extend this project by:
- Adding more data types to the FakeDataGenerator
- Implementing different AI models or APIs
- Adding data validation and formatting
- Creating a web interface
- Adding database integration
- Implementing data export in different formats

## Dependencies

- `requests` - For HTTP API calls to Ollama
- Python 3.7+ - Core language requirement

## Notes

- The Ollama integration requires a local Ollama server running
- The basic FakeDataGenerator works without any external dependencies
- Virtual environment setup is recommended for dependency isolation
- The `.gitignore` is configured to exclude virtual environments and common Python artifacts