clc;
clear;
close all
x = 0;
y = 0;
q = 0;
out = 0.0;
n = 10000000.0;

for i = 1:n
    x = rand;
    y = rand;
    if (sqrt(x*x+y*y))<1.00000
        q = q + 1;
    end
end
out = q*4.0/n;
