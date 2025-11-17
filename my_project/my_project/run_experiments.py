from my_project.functions import example_function

from my_project.pydantic_models import ExperimentConfig

from my_project.design_experiment import setup_experiment



if __name__ == '__main__':

    config = ExperimentConfig(param1=5, param2=0.1)

    experiment = setup_experiment(config)

    result = example_function(experiment['param1'])

    print('Experiment result:', result)
