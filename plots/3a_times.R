dumby_time <- c(1.2418715953826904, 1.2615628242492676, 0.1945199966430664)
greedy_time <- c(0.7822279930114746, 0.7808997631072998, 0.20549941062927246)
smarty_time<- c(0.8416516780853271, 0.8425991535186768, 0.2897369861602783)

colors <- c("blue", "green", "red", "blue", "green", "red", "blue", "green", "red")

barplot(cbind(dumby_time, greedy_time, smarty_time), beside = TRUE, names.arg = c("dumby", "greedy", "smarty"), col = colors, ylim = c(0,1.5), main = "Comparison of the computation times of the different pairs", ylab = "Computation time")
legend("topright", legend = c("hminimax0.py", "hminimax1.py", "hminimax2.py"), col=c("blue", "green", "red"), pch = c(15,15))

text(1.5,0.5,round(1.2418715953826904, digits=2), srt=0, col = "black")
text(2.5,0.5,round(1.2615628242492676, digits=2), srt=0, col = "black")
text(3.5,0.5,round(0.1945199966430664, digits=2), srt=0,col = "black")

text(5.5,0.5,round(0.7822279930114746, digits=2), srt=0, col = "black")
text(6.5,0.5,round(0.7808997631072998, digits=2), srt=0, col = "black")
text(7.5,0.5,round(0.20549941062927246, digits=2), srt=0, col = "black")

text(9.5,0.5,round(0.8416516780853271, digits=2), srt=0, col = "black")
text(10.5,0.5,round(0.8425991535186768, digits=2), srt=0, col = "black")
text(11.5,0.5,round(0.2897369861602783, digits=2), srt=0, col = "black")