clear all
close all
clc

T890822ASC = fun_import(".\DATA\T890822_ASC.TAB", [1, Inf]);

j = 1;
for i = 1:length(T890822ASC)
    seq(i) = j;
    j = j+1;
end

plot(seq(1:1000),T890822ASC(1:1000,6))