dumby_score <- c(546, 544, 542)
greedy_score <- c(560, 560, 558)
smarty_score <- c(560, 560, 558)

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_score, greedy_score, smarty_score), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,600), main = "Comparison of the scores of the different pairs", ylab = "Score")
legend("bottomright", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

text(1.5,300,546, srt=90, col = "white")
text(2.5,300,544, srt=90, col = "white")
text(3.5,300,542, srt=90,col = "white")

text(5.5,300,560, srt=90, col = "white")
text(6.5,300,560, srt=90, col = "white")
text(7.5,300,558, srt=90, col = "white")

text(9.5,300,560, srt=90, col = "white")
text(10.5,300,560, srt=90, col = "white")
text(11.5,300,558, srt=90, col = "white")