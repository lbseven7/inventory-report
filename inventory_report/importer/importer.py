# Esse requisito, por mais que a descrição tenha te assustado um pouco,
# não é um bicho de 7 cabeças não, fica tranquilo!
# Nele, precisamos reorganizar parte do código que já escrevemos dentro do
# arquivo inventory.py em 4 novos arquivos:
# Um com a classe abstrata Importer, que será a interface da estratégia
# Três arquivos, cada um com uma das três classes de estratégias herdeiras:
# CsvImporter, JsonImporter e XmlImporter.
# Essas três classes herdeiras você já implementou dentro do inventory.py
# então agora só é necessário organizá-las!

from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self):
        pass
