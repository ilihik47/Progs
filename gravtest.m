global G m1 m2;
G=1; m1=250; m2=500;
x0=[0,0,10,0,0,-3,0,6];% начальные условия
t0=[0:.001:170];%шкала времени
opts= odeset('RelTol',1e-8,'AbsTol',1e-8);
[t,x]=ode45(@gravity,t0,x0,opts);
figure(1);
plot(x(:,1),x(:,2));
hold on
grid on
grid minor
axis equal %симметричные оси
plot(0,0,'bo',10,0,'r*');
plot(x(:,3),x(:,4));
