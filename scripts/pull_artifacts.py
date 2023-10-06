import wandb
import os

wandb.login(key=os.environ.get("WANDB_KEY"))
run = wandb.init(project="animal_species_classification", job_type="get-dataset")
artifact = run.use_artifact("animal_species_data:latest")
datadir = artifact.download()

os.symlink("animal_species_data:v0", "artifacts/animal_species_data")
