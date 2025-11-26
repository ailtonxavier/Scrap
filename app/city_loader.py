import yaml


class CityLoader:
    """Classe responsável por carregar a lista de cidades de um arquivo YAML."""

    def load(self, path: str = "cities.yml"):
        """
        Carrega e parseia o arquivo YAML contendo a lista de cidades.

        Args:
            path (str): O caminho para o arquivo YAML. O padrão é "cities.yml".

        Returns:
            list: Uma lista de dicionários, onde cada dicionário representa uma cidade.
                  Retorna uma lista vazia se o arquivo não for encontrado ou
                  se ocorrer um erro na leitura.
        """
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
