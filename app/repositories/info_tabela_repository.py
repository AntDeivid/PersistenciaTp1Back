import pandas as pd

from app.models.info_tabela import InfoTabela


class InfoTabelaRepository:

    FILE_PATH = 'data/info_tabela.csv'

    def __init__(self):
        self._check_file()

    def _check_file(self):
        try:
            pd.read_csv(self.FILE_PATH)
        except FileNotFoundError:
            pd.DataFrame(columns=['id', 'pontos', 'jogos', 'vitorias', 'empates', 'derrotas']).to_csv(self.FILE_PATH, index=False)

    def save(self, info_tabela: InfoTabela) -> InfoTabela:
        df = pd.read_csv(self.FILE_PATH)
        info_tabela_dict = info_tabela.model_dump()
        df = pd.concat([df, pd.DataFrame([info_tabela_dict])], ignore_index=True)
        df.to_csv(self.FILE_PATH, index=False)

        return info_tabela

    def get_all(self) -> list[InfoTabela]:
        df = pd.read_csv(self.FILE_PATH)
        return [InfoTabela(**info_tabela) for info_tabela in df.to_dict(orient='records')]

    def get_by_id(self, id: int) -> InfoTabela | None:
        df = pd.read_csv(self.FILE_PATH)
        info_tabela = df.loc[df['id'] == id].to_dict(orient='records')
        if info_tabela:
            return InfoTabela(**info_tabela[0])
        return None

    def update(self, info_tabela: InfoTabela) -> InfoTabela:
        df = pd.read_csv(self.FILE_PATH)
        info_tabela_dict = info_tabela.model_dump()
        df.loc[df['id'] == info_tabela.id] = info_tabela_dict
        df.to_csv(self.FILE_PATH, index=False)

        return info_tabela

    def delete(self, id: int) -> None:
        df = pd.read_csv(self.FILE_PATH)
        df = df.loc[df['id'] != id]
        df.to_csv(self.FILE_PATH, index=False)

    def get_next_id(self) -> int:
        df = pd.read_csv(self.FILE_PATH)
        if df.empty:
            return 1
        return df['id'].max() + 1