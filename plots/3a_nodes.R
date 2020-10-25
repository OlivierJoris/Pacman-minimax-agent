dumby_node <- c(log(1013), log(382), Inf)
greedy_node <- c(log(30), log(422), log(7553))
smarty_node <- c(log(30), log(422), log(7553))

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_node, greedy_node, smarty_node), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,10), main = "Comparison of number of the expanded nodes of the different pairs", ylab = "Expanded nodes (logarithmic value)")
legend("topleft", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

