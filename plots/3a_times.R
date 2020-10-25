dumby_time <- c(0.6751060485839844, 0.3033175468444824, Inf)
greedy_time <- c(0.05023622512817383, 0.3528401851654053, 2.678455352783203)
smarty_time<- c(0.2405099868774414, 0.48928165435791016, 2.790019989013672)

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_time, greedy_time, smarty_time), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,3), main = "Comparison of the computation times of the different pairs", ylab = "Computation time")
legend("topleft", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

