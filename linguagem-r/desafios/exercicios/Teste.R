# Função para calcular a média móvel e gerar sinais de compra/venda
  media_movel_cross <- function (precos,janela) {
    # Calcular a média móvel 
    media_movel <- apply (embed(precos,janelas), 1, mean)
    # Gerar sinais de compra/venda
    sinais <- ifelse (precos[janela:length(precos)]) > media_movel, 1,
                ifelse(precos[janela:length(precos)]) < media_movel, -1,
                            res=data.frame(precos,
                                           media_mov=c(rep(NA,janela - 1), media_movel),
                                           sinais=c(rep(NA,janela - 1),sinais))
  
                          return(res) #retorna
                         }
  # Exemplos de uso                          
    precos <- c(10, 12, 15, 13, 11, 14, 18, 16)
    janela <- 3
    df <- media_movel_cross(precos,janela)
    print(df)
    
  