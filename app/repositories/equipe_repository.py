import logging

import pandas as pd

from app.models.equipe import Equipe


class EquipeRepository:

    FILE_PATH = 'data/equipes.csv'

    def __init__(self):
        self.logger = logging.getLogger("app.EquipeRepository")
        self.logger.debug("Inicializando EquipeRepository")
        self._check_file()

    def _check_file(self):
        try:
            pd.read_csv(self.FILE_PATH)
            self.logger.debug("Arquivo de equipes encontrado")
        except FileNotFoundError:
            pd.DataFrame(columns=['id', 'nome', 'estadio', 'apelido', 'jogadores_registrados','info_tabela_id']).to_csv(self.FILE_PATH, index=False)
            self.logger.debug("Arquivo de equipes não encontrado, criando novo arquivo")

    def save(self, equipe: Equipe) -> Equipe:
        df = pd.read_csv(self.FILE_PATH)
        equipe_dict = equipe.model_dump()
        df = pd.concat([df, pd.DataFrame([equipe_dict])], ignore_index=True)
        df.to_csv(self.FILE_PATH, index=False)

        self.logger.info(f"Nova equipe salva: {equipe}")

        return equipe

    def get_all(self) -> list[Equipe]:
        df = pd.read_csv(self.FILE_PATH)
        self.logger.info("Listando todas as equipes")
        return [Equipe(**equipe) for equipe in df.to_dict(orient='records')]

    def get_by_id(self, id: int) -> Equipe | None:
        df = pd.read_csv(self.FILE_PATH)
        equipe = df.loc[df['id'] == id].to_dict(orient='records')
        if equipe:
            self.logger.info(f"Equipe encontrada: {equipe[0]}")
            return Equipe(**equipe[0])

        self.logger.info(f"Equipe com id {id} não encontrada")
        return None

    def get_with_search(self, search: str) -> list[Equipe]:
        df = pd.read_csv(self.FILE_PATH)
        filtered_equipes = df[(df['nome'].str.contains(search, case=False)) | (df['apelido'].str.contains(search, case=False))]
        self.logger.info(f"Listando equipes com a busca: {search}")
        return [Equipe(**equipe) for equipe in filtered_equipes.to_dict(orient='records')]

    def update(self, equipe_id: int, equipe: Equipe) -> Equipe:
        df = pd.read_csv(self.FILE_PATH)
        index_to_update = df.loc[df['id'] == equipe_id].index[0]
        df.loc[index_to_update] = equipe.model_dump()
        df.to_csv(self.FILE_PATH, index=False)

        self.logger.info(f"Equipe atualizada: {equipe}")
        return equipe

    def delete(self, id: int) -> None:
        df = pd.read_csv(self.FILE_PATH)
        df = df.loc[df['id'] != id]
        df.to_csv(self.FILE_PATH, index=False)
        self.logger.info(f"Equipe com id {id} deletada")

    def get_next_id(self) -> int:
        df = pd.read_csv(self.FILE_PATH)
        self.logger.info("Buscando próximo id")
        if df.empty:
            return 1
        return df['id'].max() + 1
    
    def count_lines(self) -> int:
        df = pd.read_csv(self.FILE_PATH)
        self.logger.info("Contando linhas do arquivo de equipes")
        return df.shape[0] - 1

    def get_file_path(self) -> str:
        self.logger.info("Retornando caminho do arquivo de equipes")
        return self.FILE_PATH