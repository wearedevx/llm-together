import llm
import together
from pydantic import Field
from typing import Optional

@llm.hookimpl
def register_models(register):

    together_instance = Together()
    model_list = together_instance.get_models()

    for model in model_list:
        if 'isFeaturedModel' in model and model['isFeaturedModel']:
            register(Together(model)) 

def not_nulls(data) -> dict:
    return {key: value for key, value in data if value is not None}

class Together(llm.Model):
    model_id = "llm-together"
    needs_key = "together"
    key_env_var = "TOGETHER_API_KEY"
    default_stop = "<human>"

    def get_models(self):
        together.api_key = self.get_key()
        return together.Models.list()
    
    def __init__(self, model=None):
        together.api_key = self.get_key()

        if (model is not None):
            self.model_id = model["name"]
            self.model = model

    class Options(llm.Options):
        temperature: Optional[float] = Field(
            description=(
                "What sampling temperature to use, between 0 and 2. Higher values like "
                "0.8 will make the output more random, while lower values like 0.2 will "
                "make it more focused and deterministic."
            ),
            ge=0,
            le=2,
            default=None,
        )
        max_tokens: Optional[int] = Field(
            description="Maximum number of tokens to generate.", default=256
        )
        top_p: Optional[float] = Field(
            description=(
                "An alternative to sampling with temperature, called nucleus sampling, "
                "where the model considers the results of the tokens with top_p "
                "probability mass. So 0.1 means only the tokens comprising the top "
                "10% probability mass are considered. Recommended to use top_p or "
                "temperature but not both."
            ),
            ge=0,
            le=1,
            default=None,
        )
        repetition_penalty: Optional[float] = Field(
            description=(
                "A number that controls the diversity of generated text by "
                "reducing the likelihood of repeated sequences. Higher values "
                "decrease repetition."
            ),
            ge=-2,
            le=2,
            default=None,
        )

    def execute(self, prompt, stream, response, conversation):
        kwargs = dict(not_nulls(prompt.options))

        user_prompt = "{}\n\n{}".format(prompt.system or "", prompt.prompt)
        history = ""
        stop = self.default_stop

        if 'config' in self.model:
            if conversation is not None:
                for message in conversation.responses:
                    if 'prompt_format' in self.model["config"] and self.model["config"]['prompt_format']:
                        history += self.model["config"]["prompt_format"].format(prompt = message.prompt) + " " + message.text() + "\n"
                    else:
                        history += "{}\n\n{}".format(message.prompt, message.text())+ "\n"

            if 'prompt_format' in self.model["config"] and self.model["config"]['prompt_format']:
                user_prompt = self.model["config"]["prompt_format"].format(prompt = user_prompt)


            if 'stop' in self.model["config"]:
                stop = self.model["config"]["stop"]

        output = together.Complete.create(
            prompt =  history + "\n" + user_prompt,
            model = self.model_id, 
            stop = stop,
            **kwargs,
        )

        return [output['output']['choices'][0]['text']]
