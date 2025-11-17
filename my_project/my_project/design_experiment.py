import os
from my_project.pydantic_models import EchoReport  # assuming this is defined in your Pydantic module

# Dictionary of experimental configurations for testing
experiments_dic = {
    'GPT4o_t03_promptSimple': {
        "model_engine": "AzureOpenAI_Async",
        "total_async_n": 3,  # number of requests to be sent in parallel
        "pre_prompt": (
            "You possess knowledge of medical terminologies, especially that of a "
            "cardiologist with experience reading and interpreting echocardiographic reports "
            "with knowledge of structural heart findings. Follow the Pydantic structure to "
            "extract structured data from the echo report. Provide the structured data in "
            "clean JSON format. Only extract values explicitly stated in the report. If a "
            "field is not mentioned or cannot be confidently extracted, do not impute data. "
            "Never assume “normal” unless explicitly documented."
        ),
        "temperature": 0,
        "model": 'gpt-4o-2024-11-20',
        "experiment_aRGB_cellcolor": "8f4e0d",  # used for highlighting 
        'max_tokens': 2048,
        "timeout": 60,
        'max_retries': 2,
        "seed": None,
        "logprobs": False,
        'open_at_end': False,
        'excel_file_path': r"Syngo 5 sample.xlsx",  # could also be a .csv
        "Pydantic_Objects_List": [EchoReport],
        "parser_error_handling": "llm_to_correct",
        "openai_api_key": "",
        "runpod_base_url": "",
        "runpod_api": "",
        "azure_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "azure_api_version": "2024-08-01-preview",
        "text_column": "Report",  # either textPath_column OR text_column
        "textPath_column": None,
    },
}

def get_experiment_config(name: str):
    """Return a copy of the experiment config by name."""
    config = experiments_dic.get(name)
    if config is None:
        raise ValueError(f"Experiment '{name}' not found in experiments_dic.")
    return config.copy()
