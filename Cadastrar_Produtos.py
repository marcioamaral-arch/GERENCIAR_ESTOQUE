def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    
    # Pede os dados para o usuário
    try:

        cod = input("COD_MATERIAL: ")
        desc = input("DESCRIÇÃO_PRODUTO: ")
        unid = input("UNID_MEDIDA: ")
        qtd = float(input("Quantidade: "))
        preco = float(input("VAL_PRECOUNIT: "))
        icms = float(input("VAL_ICMS: "))
        cfop = input("CFOP_COD: ")
        ncm = input("NCM: ")
        cst = input("CST_ORIGEM: ")
        cst_trib = input("CST_TRIBURACAO: ")
        cod_fornecedor = input("COD_FORNECEDOR: ")
        uf_origem = input("UF ORIGEM: ")
        data_nf = input("DATA_NF: ")
        data_entrada_nf = input("DATA_ENTRADA_NF: ")


        
        # dicionário para o produto
        produto = {
            "COD_MATERIAL": cod,
            "DESCRIÇÃO_PRODUTO": desc,
            "UNID_MEDIDA": unid,
            "quantidade": qtd,
            "VAL_PRECOUNIT": preco,
            "VAL_ICMS": icms,
            "CFOP_COD": cfop,
            "NCM": ncm,
            "CST_ORIGEM": cst,
            "CST_TRIBURACAO": cst_trib,
            "COD_FORNECEDOR": cod_fornecedor,
            "UF ORIGEM": uf_origem,
            "DATA_NF": data_nf,
            "DATA_ENTRADA_NF": data_entrada_nf

        }
        return produto
    except ValueError:
        print("Erro: Entrada de valor inválida (quantidade/preço devem ser números).")
        return None

def exibir_produtos(lista_produtos):
    print("\n" + "="*80)
    print(f"{'COD':<10} | {'DESCRIÇÃO':<20} | {'UNID':<5} | {'QTD':<8} | {'PREÇO':<10} | {'ICMS':<8}")
    print("-" * 80)
    for p in lista_produtos:
        print(f"{p['COD_MATERIAL']:<10} | {p['DESCRIÇÃO_PRODUTO']:<20} | {p['UNID_MEDIDA']:<5} | "
              f"{p['quantidade']:<8.2f} | {p['VAL_PRECOUNIT']:<10.2f} | {p['VAL_ICMS']:<8.2f}")
    print("="*80 + "\n")

# Fluxo Principal
produtos = []
while True:
    novo_prod = cadastrar_produto()
    if novo_prod:
        produtos.append(novo_prod)
    
    cont = input("Cadastrar novo produto? (s/n): ").lower()
    if cont != 's':
        break

# Exibe o relatório final
if produtos:
    exibir_produtos(produtos)
