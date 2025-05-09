# code_review_agent

## Objective

The goal of this project is to build a local or prompt-based AI agent capable of analyzing Python code. The agent can:

- Detect potential issues in the code.
- Suggest improvements based on best practices.
- Act as a code reviewer in different modes, such as strict, mentor, or test-focused.

This tool is designed to assist developers in improving code quality and adhering to Python standards.

## Features

- **Multiple Review Modes**: Choose between strict, mentor, or test-focused modes to tailor the review process.
- **LLM Integration**: Supports multiple LLM providers like OpenAI, Ollama, and Anthropic for generating code reviews.
- **Customizable Prompts**: Modify review templates to suit your specific needs.
- **Output Reports**: Generates detailed review reports in Markdown format.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/code_review_agent.git
   cd code_review_agent