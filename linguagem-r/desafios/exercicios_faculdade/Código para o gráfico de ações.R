# Função para calcular a média móvel e gerar sinais de compra/venda
library(zoo)
media_movel_cross <- function(precos, janela) {
  # Calcular a média móvel 
  media_movel <- c(rep(NA, janela - 1), 
                   rollapply(precos, width = janela, FUN = mean, align = "right"))
  
  # Gerar sinais de compra/venda
  sinais <- ifelse(precos[janela:length(precos)] > media_movel[janela:length(precos)], 1,
                   ifelse(precos[janela:length(precos)] < media_movel[janela:length(precos)], -1, NA))
  
  # Construir dataframe
  res <- data.frame(precos = precos,
                    media_mov = media_movel,
                    sinais = c(rep(NA, janela - 1), sinais))
  
  return(res) #retorna
}

  # Exemplos de uso                          
precos <- c(10, 12, 15, 13, 11, 14, 18, 16)
janela <- 3
df <- media_movel_cross(precos, janela)
print(df)


