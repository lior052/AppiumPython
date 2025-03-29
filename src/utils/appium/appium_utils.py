import yaml
import os


class AppiumUtils:

    @staticmethod
    def load_yaml_file(file_name):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
        config_path = os.path.join(project_root, f"src/main/resources/{file_name}.yaml")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"YAML file not found at {config_path}")

        with open(config_path, "r") as file:
            return yaml.safe_load(file)


    @staticmethod
    def load_ios_device_config():
        config = AppiumUtils.load_yaml_file("device_config")  # Default file: "data.yaml"
        return config.get("ios", {})


    @staticmethod
    def load_test_data():
        config = AppiumUtils.load_yaml_file("data")  # Default file: "data.yaml"
        return config.get("test_data", {})
