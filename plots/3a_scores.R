dumby_score <- c(546, 544, -Inf)
greedy_score <- c(560, 560, 551)
smarty_score <- c(560, 560, 551)

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_score, greedy_score, smarty_score), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,600), main = "Comparison of the scores of the different pairs", ylab = "Score")
legend("bottomright", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

