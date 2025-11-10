import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

hf_token = os.getenv("HF_TOKEN")

class JobGenieAgent:
    def __init__(self, hf_token: str = None):
        self.hf_token = hf_token or os.environ.get("HF_TOKEN")
        if not self.hf_token:
            raise ValueError("HF_TOKEN not set. Please provide a Hugging Face API token.")

        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=self.hf_token
        )
    def generate_cover_letter(self, job_description: str, cv_text: str) -> str:
        prompt = (
            f"Write a concise, professional cover letter for this job description:\n"
            f"{job_description}\n\n"
            f"Use this CV information to highlight relevant experience:\n"
            f"{cv_text}\n\n"
            f"Return only the final cover letter text — do not include reasoning or explanations."
        )

        response = self.client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3:novita",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=700
        )

        content = response.choices[0].message.content.strip()
        content = content.replace("**", "")
        import re
        content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        print(f"✅ Generated cover letter:\n{content}\n")
        return content
   