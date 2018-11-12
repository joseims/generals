library(tidyverse)
library(plyr)
data <- read_csv("./workspace/vis/lab2/enade_2017_ufcg.csv")
result <-
  data %>% 
  mutate(nota = as.integer(NT_GER/20), afirmativa = if_else(QE_I15 != 'A',"Sim","Não") )%>%
    select(nota,QE_I08,QE_I04,QE_I05,QE_I02,afirmativa)

#QE_I04/05
cat0405 <- c('A','B','C','D','E','F')
val0405 <- c('Nenhuma','Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série)','Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série)','Ensino Médio','Ensino Superior - Graduação','Pós-graduação')
frame0405 <- data.frame("Categoria" = cat0405,"Value" = val0405)
result$QE_I04 = mapvalues(result$QE_I05,from=cat0405,to=val0405)
result$QE_I05 = mapvalues(result$QE_I05,from=cat0405,to=val0405)

#QE_I08
cat08 <- c('A','B','C','D','E','F','G')
val08 <- c('Até 1,5 salário mínimo (até R$ 1.405,50)','De 1,5 a 3 salários mínimos (R$ 1.405,51 a R$ 2.811,00)', 'De 3 a 4,5 salários mínimos (R$ 2.811,01 a R$ 4.216,50)','De 4,5 a 6 salários mínimos (R$ 4.216,51 a R$ 5.622,00)','De 6 a 10 salários mínimos (R$ 5. 622,01 a R$ 9.370,00)','De 10 a 30 salários mínimos (R$ 9.370,01 a R$ 28.110,00)','Acima de 30 salários mínimos (mais de R$ 28.110,00)')
frame08 <- data.frame("Categoria" = cat08,"Value" = val08)
result$QE_I08 = mapvalues(result$QE_I08,from=cat,to=val)

#QE_I02
cat02 <- cat0405
val02 <- c('Branca','Preta','Amarela','Parda','Indígena','Não quero declarar')
frame02 <- data.frame("Categoria" = cat02,"Value" = val02)
result$QE_I02 = mapvalues(result$QE_I02,from=cat02,to=val02)

write_csv(result,"./show.csv")

