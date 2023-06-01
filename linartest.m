global f m1 m2 s;
s=1; m1=2; m2=2; f=1;
x0=[0,0,1,1,0,0.4,0,-0.2];% начальные условия
t0=[0:.001:60];%шкала времени
opts= odeset('RelTol',1e-8,'AbsTol',1e-8);
[t,x]=ode45(@linar,t0,x0,opts);
figure(1);
plot(x(:,1),x(:,2));
hold on
grid on
grid minor
axis equal %симметричные оси
plot(x0(1),x0(2),'bo',x0(3),x0(4),'r*');
plot(x(:,3),x(:,4));