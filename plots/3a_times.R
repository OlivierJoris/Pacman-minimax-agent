dumby_time <- c(0.43427276611328125, 0.18589186668395996, 1.2429444789886475)
greedy_time <- c(0.020479202270507812, 0.19808149337768555, 0.7558848857879639)
smarty_time<- c(0.10458183288574219, 0.2829768657684326, 0.8371939659118652)

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_time, greedy_time, smarty_time), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,1.5), main = "Comparison of the computation times of the different pairs", ylab = "Computation time")
legend("topleft", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

text(1.5,0.5,round(0.43427276611328125, digits=2), srt=0, col = "black")
text(2.5,0.5,round(0.18589186668395996, digits=2), srt=0, col = "black")
text(3.5,0.5,round(1.2429444789886475, digits=2), srt=0,col = "black")

text(5.5,0.5,round(0.020479202270507812, digits=2), srt=0, col = "black")
text(6.5,0.5,round(0.19808149337768555, digits=2), srt=0, col = "black")
text(7.5,0.5,round(0.7558848857879639, digits=2), srt=0, col = "black")

text(9.5,0.5,round(0.10458183288574219, digits=2), srt=0, col = "black")
text(10.5,0.5,round(0.2829768657684326, digits=2), srt=0, col = "black")
text(11.5,0.5,round(0.8371939659118652, digits=2), srt=0, col = "black")