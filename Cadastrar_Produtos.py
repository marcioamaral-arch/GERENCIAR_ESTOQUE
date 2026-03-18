from datetime import datetime

class ItemNotaFiscal:
    def __init__(self, cod_material, descricao, unid_medida, quantidade, 
                 val_precounit, val_icms, cfop_cod, ncm, 
                 cst_origem, cst_tributacao, cod_fornecedor, 
                 uf_orig, dtemis, dtentr):
        
        # Identificação
        self.COD_MATERIAL = cod_material
        self.DESCRIÇÃO_PRODUTO = descricao
        self.UNID_MEDIDA = unid_medida
        self.COD_FORNECEDOR = cod_fornecedor
        
        # Quantidade e Valores
        self.quantidade = float(quantidade)
        self.VAL_PRECOUNIT = float(val_precounit)
        self.VAL_ICMS = float(val_icms)
        self.VAL_TOTAL = self.quantidade * self.VAL_PRECOUNIT
        
        # Tributação e Fiscal
        self.CFOP_COD = cfop_cod
        self.NCM = ncm
        self.CST_ORIGEM = cst_origem
        self.CST_TRIBUTAÇÃO = cst_tributacao
        self.UF_ORIG = uf_orig
        
        # Datas
        self.DTEMIS = dtemis
        self.DTENTR = dtentr

    def __str__(self):
        return f"[{self.COD_MATERIAL}] {self.DESCRIÇÃO_PRODUTO} - Qtd: {self.quantidade} - Total: R${self.VAL_TOTAL:.2f}"

def cadastrar_novo_item():
    print("\n--- Cadastro de Novo Item ---")
    try:
        cod_material = input("Código do Material: ")
        descricao = input("Descrição do Produto: ")
        unid_medida = input("Unidade de Medida: ")
        quantidade = input("Quantidade: ")
        val_precounit = input("Valor Unitário: ")
        val_icms = input("Valor ICMS: ")
        cfop_cod = input("CFOP: ")
        ncm = input("NCM: ")
        cst_origem = input("CST Origem: ")
        cst_tributacao = input("CST Tributação: ")
        cod_fornecedor = input("Código Fornecedor: ")
        uf_orig = input("UF Origem: ")
        dtemis = input("Data Emissão (dd/mm/aaaa): ")
        dtentr = input("Data Entrada (dd/mm/aaaa): ")

        # Cria a instância
        item = ItemNotaFiscal(cod_material, descricao, unid_medida, quantidade,
                              val_precounit, val_icms, cfop_cod, ncm,
                              cst_origem, cst_tributacao, cod_fornecedor,
                              uf_orig, dtemis, dtentr)
        return item
    except ValueError as e:
        print(f"Erro na conversão de dados: {e}")
        return None

# --- Exemplo de Uso ---
lista_itens = []

# Adicionar um item via terminal
novo_item = cadastrar_novo_item()
if novo_item:
    lista_itens.append(novo_item)

# Exibir os itens cadastrados
print("\n--- Itens na Lista ---")
for item in lista_itens:
    print(item)
    # Exemplo de acesso a atributo específico
    print(f"   (ICMS: {item.VAL_ICMS}, CFOP: {item.CFOP_COD})")