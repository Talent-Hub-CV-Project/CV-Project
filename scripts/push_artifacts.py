import wandb
import os

wandb.login(key=os.environ.get("WANDB_KEY"))
run = wandb.init(project="animal_species_classification", job_type="add-dataset")
artifact = wandb.Artifact(name="animal_species_data", type="dataset")
artifact.add_dir(local_path="./artifacts")
run.log_artifact(artifact)
