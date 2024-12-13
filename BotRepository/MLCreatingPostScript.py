from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from huggingface_hub import login

class GeneratePost:

    def __init__(self, post_description, language, max_length):
        self.post_description = post_description,
        self.language = language
        self.max_length = max_length
    
    def create_post(self):
        try:

            login("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")

            hf_llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B-Preview")

            post_description = self.post_description
            language = self.language
            max_length = self.max_length

            template = """Question: {question}
                        
                        Answer:"""

            question = f"""You are a creative writer specializing in {post_description} in {language}. Please write a post that contains {max_length} words.

                            Make sure your text is:
                            1. Engaging for the audience.
                            2. Relevant to the topic of {post_description}.
                            3. Clear and easy to read.
                            4. Contains key points or information useful to the target audience.

                            Write a post in {language}, limited to no more than {max_length} words."""
            
            prompt = PromptTemplate(template=template, input_variables=["question"])
            
            llm_chain = prompt | hf_llm
        except:
            return "Произошла ошибка. Повторите попытку"
        finally:
            return llm_chain.invoke(input=question)