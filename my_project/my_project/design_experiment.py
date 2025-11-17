from my_project.pydantic_models import ExperimentConfig



def setup_experiment(config: ExperimentConfig):

    return {'param1': config.param1, 'param2': config.param2}
