import pandas as pd

from app.models.equipe import Equipe


class EquipeRepository:

    FILE_PATH = 'data/equipes.csv'

    def __init__(self):
        self._check_file()

    def _check_file(self):
        try:
            pd.read_csv(self.FILE_PATH)
        except FileNotFoundError:
            pd.DataFrame(columns=['id', 'nome', 'estadio', 'apelido', 'jogadores_registrados','info_tabela_id']).to_csv(self.FILE_PATH, index=False)

    def save(self, equipe: Equipe) -> Equipe:
        df = pd.read_csv(self.FILE_PATH)
        equipe_dict = equipe.model_dump()
        df = pd.concat([df, pd.DataFrame([equipe_dict])], ignore_index=True)
        df.to_csv(self.FILE_PATH, index=False)

        return equipe

    def get_all(self) -> list[Equipe]:
        df = pd.read_csv(self.FILE_PATH)
        return [Equipe(**equipe) for equipe in df.to_dict(orient='records')]

    def get_by_id(self, id: int) -> Equipe | None:
        df = pd.read_csv(self.FILE_PATH)
        equipe = df.loc[df['id'] == id].to_dict(orient='records')
        if equipe:
            return Equipe(**equipe[0])
        return None

    def update(self, equipe_id: int, equipe: Equipe) -> Equipe:
        df = pd.read_csv(self.FILE_PATH)
        index_to_update = df.loc[df['id'] == equipe_id].index[0]
        df.loc[index_to_update] = equipe.model_dump()
        df.to_csv(self.FILE_PATH, index=False)
        return equipe

    def delete(self, id: int) -> None:
        df = pd.read_csv(self.FILE_PATH)
        df = df.loc[df['id'] != id]
        df.to_csv(self.FILE_PATH, index=False)

    def get_next_id(self) -> int:
        df = pd.read_csv(self.FILE_PATH)
        if df.empty:
            return 1
        return df['id'].max() + 1