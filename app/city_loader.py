import yaml


class CityLoader:
    def load(self, path: str = "cities.yml"):
        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)
                return data.get("capitais", [])
        except FileNotFoundError:
            print("Erro: O arquivo cities.yml não foi encontrado.")
            return []
        except (yaml.YAMLError, KeyError) as e:
            print(f"Erro ao ler cities.yml: {e}")
            return []
