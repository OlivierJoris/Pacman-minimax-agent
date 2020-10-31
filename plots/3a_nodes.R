dumby_node <- c(log(1013), log(382), log(3122))
greedy_node <- c(log(30), log(422), log(1865))
smarty_node <- c(log(30), log(422), log(1865))

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_node, greedy_node, smarty_node), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,10), main = "Comparison of number of the expanded nodes of the different pairs", ylab = "Expanded nodes (logarithmic value)")
legend("topleft", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))
text(1.5,2,round(log(1013), digits=2), srt=90, col = "white")
text(2.5,2,round(log(382), digits=2), srt=90, col = "white")
text(3.5,2,round(log(3122), digits=2), srt=90,col = "white")

text(5.5,2,round(log(30), digits=2), srt=90, col = "white")
text(6.5,2,round(log(422), digits=2), srt=90, col = "white")
text(7.5,2,round(log(1865), digits=2), srt=90, col = "white")

text(9.5,2,round(log(30), digits=2), srt=90, col = "white")
text(10.5,2,round(log(422), digits=2), srt=90, col = "white")
text(11.5,2,round(log(1865), digits=2), srt=90, col = "white")


