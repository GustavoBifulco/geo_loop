import os

def executar_geo_ai():
    print("Lendo GEOLOOP_BOOT.txt...")
    with open("GEOLOOP_BOOT.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    if "época_atual = 13" in conteudo and "guerra" in conteudo:
        print("Executando época 13: Criando sistema de guerra...")
        with open("LOG.txt", "a", encoding="utf-8") as log:
            log.write("\nIA Builder: Criado sistema inicial de guerra.")
        with open("RELATORIO_GERAL.txt", "a", encoding="utf-8") as rel:
            rel.write("\nSistema militar adicionado.")
    else:
        print("Nenhuma tarefa encontrada.")

if __name__ == "__main__":
    executar_geo_ai()