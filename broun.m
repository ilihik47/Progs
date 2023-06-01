function f=broun(n,k)
global n k
n = 2;
k = 10;
x = 2*rand(1,n)-1;
y = 2*rand(1,n)-1;
for i = 2:k
    x(i,:) = x(i-1,:) + 2*rand(1,n)-1;
    y(i,:) = x(i-1,:) + 2*rand(1,n)-1;
end
figure(1);
plot(x,y)
grid on
grid minor
figure(2);
histogram(x(k,:),50)% гистограма последнего k-ого слоя%
figure(3);
histogram(y(k,:),50)
end

