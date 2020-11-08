dumby_node <- c(log(3122), log(3122), log(382))
greedy_node <- c(log(1865), log(1865), log(422))
smarty_node <- c(log(1865), log(1865), log(422))

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_node, greedy_node, smarty_node), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,10), main = "Comparison of number of the expanded nodes of the different pairs", ylab = "Expanded nodes (logarithmic value)")
legend("topright", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))
text(1.5,3,round(log(3122), digits=2), srt=90, col = "black")
text(2.5,3,round(log(3122), digits=2), srt=90, col = "black")
text(3.5,3,round(log(382), digits=2), srt=90,col = "black")

text(5.5,3,round(log(1865), digits=2), srt=90, col = "black")
text(6.5,3,round(log(1865), digits=2), srt=90, col = "black")
text(7.5,3,round(log(422), digits=2), srt=90, col = "black")

text(9.5,3,round(log(1865), digits=2), srt=90, col = "black")
text(10.5,3,round(log(1865), digits=2), srt=90, col = "black")
text(11.5,3,round(log(422), digits=2), srt=90, col = "black")


