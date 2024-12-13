from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from huggingface_hub import login

class GeneratePost:

    def __init__(self, post_description, language, max_length):
        self.post_description = post_description,
        self.language = language
        self.max_length = max_length
    
    def create_post(self):
        login("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")

        hf_llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B-Preview")

        post_description = self.post_description
        language = "Russian" if self.language == "Русский" else "English"
        max_length = self.max_length

        template = """
                        Context: {context}
                        
                        Answer:
                    """

        context = f"""
                        You are a creative writer specializing in {post_description} in {language}. Please write a post that contains {max_length} words.

                        Make sure your text is:
                        1. Engaging for the audience.
                        2. Relevant to the topic of {post_description}.
                        3. Clear and easy to read.
                        4. Contains key points or information useful to the target audience.
                    """
        
        prompt = PromptTemplate(template=template, input_variables=["context"])
        
        llm_chain = prompt | hf_llm
        try:
            answer = llm_chain.invoke(input=context)
        except:
            answer = "Ошибка. Попробуйте переписать пост"
        finally:
            return answer