import yaml

class CodeAnalyzer:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def load_prompt(self, mode):
        with open("prompts/templates.yaml", "r") as f:
            templates = yaml.safe_load(f)
        return templates[mode]["description"]

    def analyze(self, file_path, mode):
        with open(file_path, "r") as f:
            code = f.read()
        prompt = self.load_prompt(mode)
        return self.llm_client.run(prompt, code)