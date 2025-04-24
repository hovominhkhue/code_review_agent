import argparse
import yaml
from agent.analyzer import CodeAnalyzer
from agent.llm_interface import LLMClient

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--mode", choices=["strict", "mentor", "test_focus"], default="mentor")
    parser.add_argument("--provider", choices=["openai", "ollama", "anthropic"], required=True)
    args = parser.parse_args()

    config = load_config()
    llm = LLMClient(args.provider, config[f"{args.provider}_model"], config)
    analyzer = CodeAnalyzer(llm)
    review = analyzer.analyze(args.file, args.mode)

    with open("reviews/review_output.md", "w") as f:
        f.write(review)
    print("✅ Revue générée dans reviews/review_output.md")

if __name__ == "__main__":
    main()